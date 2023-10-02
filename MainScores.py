"""This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.

1. score_server - This function will serve the score. It will read the score from the scores file
and will return an HTML that will be as follows:

<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{SCORE}</div></h1>
    </body>
</html>

If the function will have a problem showing the result of reading the error it will return the
following:

<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
    <body>
        <h1><div id="score" style="color:red">{ERROR}</div></h1>
    </body>
</html>
"""
from flask import Flask
from flask import render_template_string
import csv
import os

app = Flask(__name__)

def read_score_from_file():
    try:
        with open('score.txt', 'r') as file:
            return file.read().strip()
    except Exception as e:
        return f"ERROR: {str(e)}"

@app.route('/')
def score_server():
    score = read_score_from_file()
    if score.startswith("ERROR"):
        html = f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{score}</div></h1>
            </body>
        </html>
        '''
    else:
        html = f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
