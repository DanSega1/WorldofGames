from flask import Flask, render_template_string

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
                <title>World of Games</title>
                <style>
                    body {{
                        text-align: center;
                        background-color: #f0f0f0;
                        font-family: 'Poppins', sans-serif;
                    }}
                    .title {{
                        font-size: 48px;
                        font-weight: bold;
                        margin-top: 20px;
                    }}
                    h1 {{
                        font-family: 'Poppins', sans-serif;
                        font-size: 24px;
                        color: green;
                    }}
                </style>
            </head>
            <body>
                <h1>{score}</h1>
            </body>
        </html>
        '''
    else:
        html = f'''
        <html>
            <head>
                <title>World of Games</title>
                <style>
                    body {{
                        text-align: center;
                        background-color: #f0f0f0;
                        font-family: 'Poppins', sans-serif;
                    }}
                    .title {{
                        font-size: 64px;
                        font-weight: bold;
                        margin-top: 20px;
                    }}
                    h1 {{
                        font-family: 'Poppins', sans-serif;
                        font-size: 34px;
                        color: green;
                    }}
                </style>
            </head>
            <body>
                <h1 class="title">World of Games</h1>
                <h1>The global score is {score} pt</h1>
            </body>
        </html>
        '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
