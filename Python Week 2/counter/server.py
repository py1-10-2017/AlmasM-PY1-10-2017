from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "ThisisSecret"


@app.route('/index')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')


app.run(debug=True)
