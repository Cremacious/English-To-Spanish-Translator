import PySimpleGUI as sg
import requests
import os

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
MY_KEY = os.environ.get("KEY")

def translate(text):
    payload = {
        "q": f"{text}",
        "target": "es",
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": MY_KEY,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    translated_text = data['data']['translations'][0]['translatedText']
    return translated_text

# Define the layout for the window
layout = [
    [sg.Text('Enter text to translate:', size=(20, 1))],
    [sg.InputText('', size=(30, 1), key='-INPUT-')],
    [sg.Text('Translation:', size=(20, 1))],
    [sg.InputText('', size=(30, 1), key='-OUTPUT-')],
    [sg.Button('Translate')],
]

# Create the window
window = sg.Window('English to Spanish Translator', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Translate':
        input_text = values['-INPUT-']
        translated_text = translate(input_text)
        window['-OUTPUT-'].update(translated_text)

# Close the window
window.close()