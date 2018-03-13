from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Renders a very basic welcome page detailing where to find the game.

    :return: the rendered index.html page
    """
    return render_template('index.html')


@app.route('/match')
def match():
    """
    Renders the game page!!! Woohoo :)

    :return: the rendered match.html page
    """
    return render_template('match.html')


if __name__ == '__main__':
    app.run()
