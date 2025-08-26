from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GEMINI_API"))

class GeminiConfig:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API"))
        self.model_name = os.getenv("MODEL_ID")

    def generate_response(self, prompt):
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response
        except Exception as e:
            return e
        
class PromptEngine:

    @staticmethod
    def crop_recommendation(crop):
        return f"""

        You're an Farmer, you have provide the good feritilizer for the given crop:{crop}
        provide fetrilizer and the details in a valid json format, don't any markdown like ```json strictly, don't provide a string provide only json.
        STRICTLY don't any markdown like ```json, provide only json.

        output: 
        {{
        "fertilizer_name": <name of the fertilizer>,
        "description": <name of the description"
        }}

        """
    
    @staticmethod
    def yield_prediction(soil, nitrogen, phosphorus, potassium, crop):
        return f"""

        You're an Farmer, you have provide the yield_prediction for the given 
        soil:{soil}, 
        nitrogen value: {nitrogen},
        phosphorus value: {phosphorus},
        potassium value: {potassium},
        crop:{crop}
        provide fetrilizer and the details in a valid json format, don't any markdown like ```json strictly, don't provide a string provide only json.

        output: 
        {{
        "fertilizer_name": <provide one fertilizer for the crop and soil>,
        "description": <provide the description for the fertilizer.>"
        }}

        """