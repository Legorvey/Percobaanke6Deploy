from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience/committee')
def committee():
    return render_template('committee.html')

@app.route('/experience/organizational')
def organizational():
    return render_template('organizational.html')

@app.route('/experience/academic')
def academic():
    return render_template('academic.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Pesan baru dari {name} ({email}): {message}")
        return redirect(url_for('contacts'))
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
