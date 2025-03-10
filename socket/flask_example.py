"""flask"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """http://127.0.0.1:5000/에 접속하면 'index'를 반환"""
    return 'index'

@app.route('/hello')
def hello_world():
    """http://127.0.0.1:5000/hello에 접속하면 'Hello, World!'를 반환"""
    return 'Hello, World!'

@app.route('/user')
@app.route('/user/<username>')
def show_user_profile(username=None):
    """http://127.0.0.1:5000/user/xxx에 접속하면 'User xxx'를 반환"""
    return render_template('user_profile.html', username=username)

def main():
    app.debug = True
    app.run(host="", port=5000)


if __name__ == '__main__':
    main()
# Flask는 웹 서버를 내장하고 있어서 별도의 웹 서버를 설치하지 않아도 됨
