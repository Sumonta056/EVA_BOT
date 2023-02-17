import webbrowser

import pyjokes
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

eva = pyttsx3.init()
# eva voice changing
voices: object = eva.getProperty('voices')
eva.setProperty('voice', voices[1].id)
listener = sr.Recognizer()


# take command from user voice function
def takeCommand():
    with sr.Microphone() as mic:
        print("Listening.....")
        voice = listener.listen(mic)
        command = listener.recognize_google(voice)
        command = command.lower()
        # if 'eva' in command:
        print(command)
    return command


# eva talk function
def evaTalk(text):
    eva.say(text)
    eva.runAndWait()


# eva initial talks
evaTalk('Hi , I am EVA . What\'s your name?')

# taking username from voice
# name = input("Your name : ")
name = takeCommand()
evaTalk('Hi ' + name + '! How can i help you?')

# take command of what to do
value = 1
while 1:
    if value > 1:
        evaTalk('Anything else ?' + name)

    todo = takeCommand()

    if 'goodbye' in todo:
        evaTalk("Goodbye" + name)
        exit()

    elif 'time' in todo:
        time = datetime.datetime.now().strftime('%I:%M %p')
        evaTalk("Time is " + time)
        value = value + 1

    elif 'play' in todo:
        todo = todo.replace('play', '')
        evaTalk('Playing Song')
        pywhatkit.playonyt(todo)
        evaTalk('Enjoy Music ! Goodbye')
        exit()

    elif 'tell me about' in todo:
        todo = todo.replace('tell me about', '')
        info = wikipedia.summary(todo, 3)
        evaTalk(info)
        value = value + 1

    elif 'search' in todo:
        todo = todo.replace('search', '')
        pywhatkit.search(todo)
        evaTalk('Enjoy Browsing ! Goodbye')
        exit()

    elif 'open facebook' in todo:
        url = 'https://www.facebook.com/'
        webbrowser.open_new_tab(url)
        evaTalk('Enjoy Browsing ! Goodbye')
        exit()

    elif 'date' in todo:
        evaTalk("Sorry" + name + "I am already booked")
        evaTalk("Don't Be Sad" + name + "You will get a better girl then me")
        value = value + 1

    elif 'joke' in todo:
        evaTalk(pyjokes.get_joke())
        value = value + 1

    elif 'weather' in todo:
        city = todo.replace('weather of', '')
        city = city + " weather"
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        evaTalk('Searching')
        soup = BeautifulSoup(res.text, 'html.parser')
        weather = soup.select('#wob_tm')[0].getText().strip()

        evaTalk(weather + "°C")
        value = value + 1
