from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def form() :
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit() :
    name = request.form['name']
    email = request.form['email']

    session['name'] = name
    session['email'] = email

    return redirect(url_for('result'))

@app.route('/result')
def result() :
    name = session.get('name')
    email = session.get('email')

    if name and email :
        return render_template('result.html', name=name, email=email)
    else :
        return redirect(url_for('form'))

if __name__ == '__main__' :
    app.run(port = 5009, debug=True)