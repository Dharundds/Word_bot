import PySimpleGUI as sg
from utils import get_meaning, get_antonyms, get_synonyms


def display_meaning():
    word = values['input']
    meaning = get_meaning(word)
    window['box'].print("\nWord: ", word)
    if meaning:
        window['box'].print("Meaning: ", meaning)


def display_synonyms():
    word = values['input']
    synonyms = get_synonyms(word)
    window['box'].print("\nWord: ", word)
    if synonyms:
        window['box'].print("Meaning:", synonyms)


def display_antonyms():
    word = values['input']
    antonyms = get_antonyms(word)
    window['box'].print("\nWord: ", word)
    if antonyms:
        window['box'].print("Antonyms: ", antonyms)


def clear_all():
    window.FindElement('box').Update(
        "Hi there... \nThis a Word bot\nType a word and click")
    window.FindElement('input').Update("")


layout = [
    [sg.Multiline("Hi there... \nThis a Word bot\nType a word and click", font=(
        'Arial', 16), size=(70, 15), key='box')],
    [sg.InputText('', font=('Arial', 16), size=(50, 1), key='input')],
    [sg.Button("Meaning", font=('Arial', 16), key='meaning'),
     sg.Button("Synonyms", font=('Arial', 16), key='synonyms'),
     sg.Button("Antonyms", font=('Arial', 16), key='antonyms'),
     sg.Button("Clear", font=('Arial', 16), key='clear')
     ]
]

if __name__ == "__main__":
    window = sg.Window("Word Bot", layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'meaning':
            display_meaning()
        elif event == 'synonyms':
            display_synonyms()
        elif event == 'antonyms':
            display_antonyms()
        elif event == 'clear':
            clear_all()
