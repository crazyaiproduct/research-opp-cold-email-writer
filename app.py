from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # if request.method == 'POST':
    input_dict = dict()
    input_dict['Professor_Name'] = request.form['professor'],
    input_dict['Opptunity_Type'] = request.form['main_opp'],
    input_dict['Semester'] = request.form['semester'],
    input_dict['Alternate_Opportunity_Type'] = request.form['second_opp'],
    input_dict['Your_Name'] = request.form['name'],
    input_dict['Education'] = request.form['education'],
    input_dict['Current_Work_Role'] = request.form['current-roles'],
    input_dict['Research_Interest'] = request.form['research-domain'],
    input_dict['Technical_Skills'] = request.form['skills'],
    input_dict['Personalities_Strength'] = request.form['strength'],
    input_dict['Related_Experiences'] = request.form['experience'],
    input_dict['Future_Resolution_Goal'] = request.form['goal'],
    input_dict['Professor_Website'] = request.form['professor'],
    input_dict['Professor_Research_Interest'] = request.form['professor'],
    input_dict['Interest_Paper_URL'] = request.form['professor'],
    input_dict['Paper_Abstract_CP'] = request.form['professor'],
    input_dict['Documents'] = request.form['professor']
    # Simple feedback response based on input
    response_message = f"Thank you, {name}! We've received your feedback."
    return render_template('feedback.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
