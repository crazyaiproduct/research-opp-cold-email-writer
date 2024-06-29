from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
        # Simple feedback response based on input
        response_message = f"Thank you, {name}! We've received your feedback."
        return render_template('feedback.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
