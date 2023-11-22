import streamlit as st
from PIL import Image
import os

st.title("Model Building Pipeline")

# Get the absolute path to the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Specify the relative path from the current script to the file
file_path = os.path.join(current_dir, "resources/images", "ml_pipeline.jpg")


image = Image.open(file_path)
st.image(image, caption='Credits: M Ravi Teja')
