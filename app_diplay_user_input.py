from flask import Flask, request, render_template, url_for

app_diplay_user_input = Flask(__name__)

@app_diplay_user_input.route('/')
def form() :
    return render_template('form.html')

@app_diplay_user_input.route('/submit', methods=['POST'])
def submit_form() :
    if request.method == 'POST' :
        name = request.form['name']
        email = request.form['email']
        return render_template('result.html', name=name, email=email)
    
if __name__ == '__main__' :
    app_diplay_user_input.run(port=5008, debug=True)
