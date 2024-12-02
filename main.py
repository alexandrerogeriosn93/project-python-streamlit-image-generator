import os
import openai
import streamlit as st
import urllib.request
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
openai.api_key = os.getenv("API_KEY")
