__author__ = 'sulla'

from flask import Flask, session

app = Flask(__name__)


@app.route('/getstatus')
def get_status():
    if 'status' in session:
        print(session['status'])
        return session['status']
    else:
        return "No Value"


@app.route('/setstatus')
def set_status():
    session['status'] = "True"
    return "Action Set"


@app.route('/')
def root():
    return "Hello World !!!"


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
