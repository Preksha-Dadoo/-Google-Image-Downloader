!pip install landingai
from PIL import Image
from landingai.predict import Predictor
# Enter your API Key
endpoint_id = "f9de813d-5199-4a00-85e7-1cbca222d7c8"
api_key = "land_sk_gLSv7QzM4AfQXd9ZK3vi7MraffcjScR7JV7k7simO9sSyGRfNH"
# Load your image
image = Image.open("face_position.zip")
# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)
