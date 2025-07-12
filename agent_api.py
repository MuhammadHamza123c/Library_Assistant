from fastapi import FastAPI,File,UploadFile
import cv2
import main
from PIL import Image 
import pytesseract 
import numpy as np

id_list=[]
def extract_text(file_name):
    pil_image = Image.open(file_name)
    text = pytesseract.image_to_string(pil_image)
    cleaned = " ".join(text.split())
    return cleaned


app=FastAPI()

@app.get('/Library_Assistant')
def library_assistant(user:str=''):
    if user:
        return {'Response':main.Assistant(user)}
    elif user=='':
        return {'Response':"Welcome from Emerson University Library Assistant"}


@app.post('/image_upload')
def check(F1:UploadFile=File(...)):
    text=extract_text(F1.file)
    return {
        "body": {
            "data": {
                "body": text
            }
        }
    }


@app.get('/Store_number')
def store_data(number:str):
    if number in id_list:
        result="Done"
    else:
        id_list.append(number)
        result='''📚 Welcome to Emerson University Multan Library Assistant!

Assalamualaikum! 👋
I'm your digital library assistant, here to help you with:

🔍 Locating books in the library

✅ Checking availability of books

📖 Suggesting books based on your interests

📜 Providing library rules and regulations

Please use respectful language while chatting.
Note: For service improvement, your messages may be recorded.

How can I assist you today?'''

    return{
        'message':result
    }