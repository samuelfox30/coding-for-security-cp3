from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=False)