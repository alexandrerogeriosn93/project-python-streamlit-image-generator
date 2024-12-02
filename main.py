import os
import openai
import streamlit as st
import urllib.request
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
openai.api_key = os.getenv("API_KEY")


def generate_image(description):
    image_response = openai.Image.create(prompt=description, n=1, size="512x512")
    image_url = image_response["data"][0]["url"]
    urllib.request.urlretrieve(image_url, "image.png")
    image = Image.open("image.png")
    return image
