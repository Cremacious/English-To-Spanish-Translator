import os

import requests

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
    result = response.json()
    new_text = result['data']['translations'][0]['translatedText']
    return new_text


running = True
while running:
    text = input("Text: ")
    result = translate(text)
    print(result)
