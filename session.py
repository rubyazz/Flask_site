from flask import Flask, render_template, url_for, request, make_response, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '37edd7d1307693b2658b6d5a84c10f321c6c616f'

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return f"<h1>Main page</h1><p>Число просмотров: {session['visits']}"


if __name__ == "__main__":
    app.run(debug=True)