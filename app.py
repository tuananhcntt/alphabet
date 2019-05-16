# -*- coding: utf-8 -*-
import random

import romkan
from flask import Flask, render_template, redirect, request
from googletrans import Translator
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

alphabet = [u'あ', u'い', u'う', u'え', u'お',
            u'か', u'き', u'く', u'け', u'こ',
            u'さ', u'し', u'す', u'せ', u'そ',
            u'た', u'ち', u'つ', u'て', u'と',
            u'な', u'に', u'ぬ', u'ね', u'の',
            u'は', u'ひ', u'ふ', u'へ', u'ほ',
            u'ま', u'み', u'む', u'め', u'も',
            u'や', u' ', u'ゆ', u' ', u'よ',
            u'ら', u'り', u'る', u'れ', u'ろ',
            u'わ', u' ', u' ', u' ', u'を',
            u'ん', u' ', u' ', u' ', u' ']

communication = ['ohayoogozaimasu', 'konnichiwa', 'konbanwa', 'hajimemashite', 'oyasuminasai', 'sayoonara',
                 'jamataashita', 'mouichidoonegaishimasu', 'sumimasen', 'gomennasai',
                 'douzoyoroshikuonegaishimasu',
                 'arigatougozaimashita', 'osakinishitsureishimasu', 'otsukaresamadeshita', 'itadakimasu',
                 'gochisousamadeshita', 'ogenkidesuka', 'ogenkidesu', 'doitashimashite', 'yondekudasai',
                 'suwattekudasai', 'tattekudasai', 'kochira koso yoroshiku onegaishimasu',
                 'osokunattesumimasen',
                 'osokunatte', 'onegaishimasu', 'hajimemashou', 'ganbattekudasai', 'hai,ganbarimasu']

digit = {'rei': 0, 'ichi': 1, 'ni': 2, 'san': 3, 'yon': 4, 'shi': 4, 'go': 5, 'roku': 6, 'haha': 7, 'hachi': 8,
         'kyuu': 9, 'ku': 9, 'juu': 10}

digit_ro = ['rei', 'ichi', 'ni', 'san', 'yon', 'go', 'roku', 'haha', 'hachi', 'kyuu', 'ku', 'juu']


def get_katakana():
    katakana = []
    for i in alphabet:
        katakana.append(romkan.to_katakana(romkan.to_roma(unicode(i))))

    return katakana


@app.route('/')
def test():
    return redirect('/hiragana_alphabet')


@app.route('/katakana_alphabet', methods=['GET', 'POST'])
def l_katakana_alphabet():
    text_hi = random.choice(alphabet)
    text_ro = romkan.to_roma(text_hi)
    text_ka = romkan.to_katakana(text_ro)
    text = {
        'text_hi': text_ka,
        'text_ro': text_ro,
        'text_true': random.choice(
            ['nice, i like you', "standard, cheering", "You are very good", "Where are you falling, so good"]),
    }
    return render_template("index.html", text=text, alpha=get_katakana())


@app.route('/hiragana_alphabet', methods=['GET', 'POST'])
def l_hiragana_alphabet():
    text_hi = random.choice(alphabet)
    text_ro = romkan.to_roma(text_hi)
    text = {
        'text_hi': text_hi,
        'text_ro': text_ro,
        'text_true': random.choice(
            ['nice, i like you', "standard, cheering", "You are very good", "Where are you falling, so good"]),
    }
    return render_template("index.html", text=text, alpha=alphabet)


@app.route('/communication')
def l_communication():
    text_ro = random.choice(communication)
    text = {
        'text_hi': romkan.to_hiragana(text_ro),
        'text_ro': text_ro,
        'text_true': random.choice(
            ['nice, i like you', "standard, cheering", "You are very good", "Where are you falling, so good"]),
    }
    return render_template("index.html", text=text)


@app.route('/digit')
def l_digit():
    text_ro = random.choice(digit_ro)
    text = {
        'text_digit': digit[text_ro],
        'text_hi': romkan.to_hiragana(text_ro),
        'text_ro': text_ro,
        'text_true': random.choice(
            ['nice, i like you', "standard, cheering", "You are very good", "Where are you falling, so good"]),
    }
    return render_template("index.html", text=text)


@app.route('/translator')
def translator():
    return render_template("translator.html")


if __name__ == '__main__':
    app.run()
