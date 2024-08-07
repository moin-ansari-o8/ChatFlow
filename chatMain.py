import json
import random
import os
import datetime
import requests
from bs4 import BeautifulSoup


convo_file = os.path.join('GitProjects', 'ChatFlow', 'referenceConvo.json')

def load_intents(file_path):
    try:
        with open(file_path, 'r') as file:
            intents_data = json.load(file)
        return intents_data['intents']
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file could not be parsed.")
        return []

def match_pattern(sent, patterns):
    return sum(1 for pattern in patterns if pattern.lower() in sent.lower())

def get_response(tag, intents):
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent["responses"])
def get_response(tag, intents):
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent["responses"])


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_current_date():
    today = datetime.datetime.now()
    return today.strftime("%Y-%m-%d")

def get_weather(city="anand"):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")

def handle_intent(intent, sent):
    if intent == "time":
        return f"The current time is {get_current_time()}."
    elif intent == "date":
        return f"Today's date is {get_current_date()}."
    elif intent == "weather":
        # Assume the location is provided after the keyword in the sentence
        location = sent.split()[-1]
        return get_weather(location)
    else:
        return get_response(intent, intents)
    
def main(sent):
    found_response = None
    max_count = 0
    intents = load_intents(convo_file)
    
    if not intents:
        print("No intents loaded. Exiting.")
        return
    
    for intent in intents:
        count = match_pattern(sent, intent['patterns'])
        if count > max_count:
            max_count = count
            found_response = get_response(intent['tag'], intents)
    
    print(f"$ : {found_response}" if found_response else "$ : I don't understand that.")

if __name__ == "__main__":
    while True:
        sent = input("# : ").lower()
        main(sent)
