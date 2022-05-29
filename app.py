from flask import Flask, render_template, request, abort
from random import choice

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/live/')
def live():
    return render_template('live.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
