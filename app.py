from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/verse/<int:page>')
def page(page):
    return render_template(f'./blog/{page}.html')


if __name__ == '__main__':
    app.run()
