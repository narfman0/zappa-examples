from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index(event=None, context=None):
    return render_template('index.html', time=datetime.now())


@app.route('/projects/')
def projects(event=None, context=None):
    return render_template('projects.html', projects=['dragula', 'wilhelm', 'concord'])


if __name__ == '__main__':
    app.run(debug=True)
