from flask import Flask, render_template, request, redirect, url_for
from email_model import EmailModel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    em = EmailModel()
    # if request.method == 'POST':
    input_dict = dict()
    input_dict['Professor_Name'] = request.form['professor'],
    input_dict['Opportunity_Type'] = request.form['main_opp'],
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
    input_dict['Professor_Website'] = request.form['pro_web'],
    input_dict['Professor_Research_Interest'] = request.form['pro-research-domain'],
    input_dict['Interest_Paper_URL'] = request.form['paper_url'],
    input_dict['Paper_Abstract_CP'] = request.form['paper_abstract'],
    input_dict['Documents'] = request.form['doc']

    # Get the email
    payload = em.process_input(input_dict=input_dict)
    response_message = em.call_llm(payload=payload)
    parsed_resp = em.parse_response(response_message)
    return render_template('feedback.html', response_message=parsed_resp)

if __name__ == '__main__':
    app.run(debug=True)
