from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def form():
    return render_template('survey.html')

@app.route('/dojo', methods=['Post'])
def dojo():
    print("it's here")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usertext'] = request.form['text_area']
    return redirect('/here')

@app.route('/here')
def here():
    print('last page!')
    return render_template('here.html')

if __name__ == "__main__":
    app.run(debug=True)