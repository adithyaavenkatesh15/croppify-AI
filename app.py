from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
from ultralytics import YOLO
from google import genai
import json
import numpy as np
import cv2
from collections import Counter
import base64
from config import GeminiConfig, PromptEngine
import io
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load YOLO model
yolo_model = YOLO('./models/yolo-model.pt')
CONFIDENCE_THRESHOLD = 0.5

# Load RandomForest model for crop recommendation
RF_MODEL_PATH = os.path.join("models", "random_forest_model.pkl")
crop_model = joblib.load(RF_MODEL_PATH)

# Initialize Gemini
gemini = GeminiConfig()

# ------------------ ROUTES FOR HTML PAGES ------------------ #
@app.route('/')
def home():
    return render_template('plant.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizer.html')

@app.route('/yield')
def yield_prediction():
    return render_template('yield.html')

@app.route('/disease')
def disease():
    return render_template('disease.html')


# ------------------ CROP RECOMMENDATION API ------------------ #
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        print("Received data:", data)

        features = [
            data['nitrogen'],
            data['phosphorus'],
            data['potassium'],
            data['pH'],
            data['rainfall'],
            data['temperature'],
            data['humidity']
        ]

        prediction = crop_model.predict([features])[0]
        print("Prediction:", prediction)

        return jsonify({'recommendation': prediction})
    
    except Exception as e:
        print("Error occurred:", e)
        return jsonify({'error': str(e)})

# ------------------ DISEASE DETECTION WITH YOLO ------------------ #
@app.route('/detect-disease', methods=['POST'])
def yolo_result():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        detected_classes = []
        file = request.files['image']
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image_arr = np.array(image)

        results = yolo_model(image_arr)

        for r in results:
            boxes = r.boxes
            labels = r.names
            for box in boxes:
                if box.conf[0] < CONFIDENCE_THRESHOLD:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_id = int(box.cls[0])
                class_name = labels.get(class_id, "Unknown")
                detected_classes.append(class_name)

                cv2.rectangle(image_arr, (x1, y1), (x2, y2), (0, 0, 255), 2)
                text_position = (x2, max(y1 - 10, 0))
                cv2.putText(image_arr, class_name, text_position, cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (0, 255, 0), 2, cv2.LINE_AA)

        if not detected_classes:
            return jsonify({'error': 'No disease detected'}), 200

        pil_image = Image.fromarray(image_arr)
        image_stream = io.BytesIO()
        pil_image.save(image_stream, format='JPEG')
        image_stream.seek(0)
        image_base64 = base64.b64encode(image_stream.getvalue()).decode()

        class_counts = dict(Counter(detected_classes))

        return jsonify({
            'image': image_base64,
            'detected_classes': class_counts
        }), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


# ------------------ FERTILIZER RECOMMENDATION ------------------ #
@app.route('/fertilizer', methods=['POST'])
def fertilizer_recommendation():
    try:
        data = request.get_json()
        nitrogen = data.get('nitrogen')
        phosphorus = data.get('phosphorus')
        potassium = data.get('potassium')
        crop = data.get('crop')
        soil = data.get('soil')

        prompt = PromptEngine.yield_prediction(soil, nitrogen, phosphorus, potassium, crop)
        response = gemini.generate_response(prompt)

        cleaned_str = response.text.strip().split('```json')[-1].split('```')[0].strip()

        print(f"Received data: {json.loads(cleaned_str)}")

        return jsonify({'recommendation': json.loads(cleaned_str)}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


# ------------------ MAIN ------------------ #
if __name__ == '__main__':
    app.run(debug=True, port=5000)
