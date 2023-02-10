import regex as regex
from getMorseCode import get_morse_code_ja
from export_csv import convert_dict_to_df, export_df_to_csv
import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from formClass import MorseCodeForm
import jaconv

filepath = "csv/morse_code_ja.csv"

#RUN ONCE FOR CSV MORSE CODE FILE
# get morse code dictionary
# morse_code_dict = get_morse_code_ja()
#
# # # export as csv
# col = ["code"]
# morse_code_df = convert_dict_to_df(morse_code_dict, col)
# export_df_to_csv(morse_code_df, filepath)
# #############

# open csv
morse_code_df = pd.read_csv(filepath)
morse_code_df = morse_code_df.rename(columns={"Unnamed: 0": "text"})

# Set Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

#Check if user entry is only hiragana and katakana, otherwise return false.
def check_hiragana_katakana_only(input_text):
    p = regex.compile(r'[\p{Script=Hiragana}\p{Script=Katakana}]+')
    return p.fullmatch(input_text)

## create one page
@app.route('/', methods=["GET","POST"])
def get_all_posts():
    morse_code = ""
    form = MorseCodeForm()
    if request.method == 'POST':
        input_text = request.form.get("input_text")
        if not check_hiragana_katakana_only(input_text):
            flash(f"Please enter 'Hiragana' or 'Katakana'.")
        else:
            for letter in input_text:
                # convert hiragana to katakana
                kana_letter = jaconv.hira2kata(letter)
                morse_code_letter = morse_code_df.loc[(morse_code_df['text'] == kana_letter)]["code"].values
                morse_code = morse_code + " " + morse_code_letter
            return render_template("index.html", form=form, morse_code=morse_code[0])
    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run()
