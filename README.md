🌾 Croppify-AI: AI-Driven Crop Health Monitoring and Yield Prediction

## 📌 Overview

Agriculture faces persistent challenges such as **crop diseases, excessive fertilizer usage, and inaccurate yield predictions**, which lead to reduced productivity and environmental degradation.
**Croppify-AI** is an **AI-powered solution** that integrates **machine learning, deep learning, and large language models (LLMs)** to provide real-time insights for farmers.

This project is implemented as a **Flask-based web application** with an easy-to-use interface for farmers to:

* 📊 Recommend the best crop to cultivate
* 🦠 Detect crop diseases from leaf images
* 🌱 Suggest fertilizer usage
* 🌾 Predict crop yield

---

## 🚀 Features

* **Crop Recommendation**

  * Uses **Random Forest** to recommend crops based on soil nutrients (NPK), pH, temperature, humidity, and rainfall.
  * Achieved **99.54% accuracy**.

* **Disease Detection**

  * Employs **YOLOv8** for real-time detection of crop diseases from leaf images.
  * Achieved **91% accuracy**.

* **Fertilizer Recommendation**

  * Uses **LLMs** to analyze crop type, soil conditions, and deficiencies to recommend fertilizers.

* **Yield Prediction**

  * Utilizes **LLMs** to estimate yield per hectare based on environmental and crop parameters.

* **User Interface**

  * Built with **Flask + HTML/CSS** for a clean, mobile-friendly experience.
  * Supports both **text and image input**.

---

## 🖼️ System Architecture

```mermaid
graph TD
    A[Farmer Input: Soil Data, Crop Image, Queries] --> B[Backend - Flask API]
    B --> C[Crop Recommendation - Random Forest]
    B --> D[Disease Detection - YOLOv8]
    B --> E[Fertilizer Suggestion - LLM]
    B --> F[Yield Prediction - LLM]
    C --> G[Results Displayed on Web UI]
    D --> G
    E --> G
    F --> G


---

## ⚙️ Tech Stack

* **Programming Language**: Python 3.8+
* **ML/DL Libraries**: Scikit-learn, TensorFlow / PyTorch, OpenCV
* **Web Framework**: Flask, HTML, CSS, JavaScript
* **Development Tools**: Google Colab / Jupyter, VS Code, Git
* **Datasets**:

  * Crop Recommendation Dataset (Kaggle)
  * Plant Disease Dataset (Kaggle)

---

## 🖥️ Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/adithyaavenkatesh15/croppify-AI.git
   cd croppify-AI
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:

   ```bash
   python app.py
   ```

4. Open your browser at:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Results

* **Crop Recommendation Accuracy**: 99.54%
* **Disease Detection Accuracy (YOLOv8)**: 91%
* **Fertilizer & Yield Prediction**: Context-specific suggestions powered by LLMs.

---

## 🌍 Applications

* Smart disease detection & treatment recommendations
* Personalized fertilizer guidance
* Accurate yield estimation for financial planning
* Sustainable farming practices through optimized resource use
* Accessible to farmers via mobile-friendly web app

---

## 🔮 Future Enhancements

* 🌐 IoT sensor integration for real-time soil & weather monitoring
* 📱 Mobile app development (Android with Kotlin)
* 🗣️ Multilingual & voice support
* ⚡ AutoML for continuous model retraining
* 🔗 Blockchain for secure data ownership

---

## 🏆 Achievements

* Presented at **FORSCH’25 National-Level Techno-Cultural Fest**, Anna University, Coimbatore.

---

## 👨‍💻 Contributors

* **Adithyaa MV (2311004)**
* **Ramzan R (2311048)**
* **Thamarai Selvi O (2311061)**

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
