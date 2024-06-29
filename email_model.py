import requests
import json
import time
import re

class EmailModel():
    def __init__(self) -> None:
        self.url = "https://api.deepseek.com/chat/completions"
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer [API Key]' # Replace [API Key] with your own api key here
        }
    
    def process_input(self, input_dict):
        
        pay_load_string = '''
                    <Instructions>
                    You will be writing an email to a professor {Professor_Name} to express interest in research opportunities. I will
                    provide you with background context and specific instructions for what to include in each paragraph
                    of the email.

                    Here is the background context you should refer to when writing the email:
                    <context>
                    I am interested in the research of Professor {Professor_Name} and hope to work with him. 
                    I would like to write an email to reach out to Professor {Professor_Name} asking for {Opportunity_Type} opportunities starting in the {Semester}, and {Alternate_Opportunity_Type} opportunities starting as soon as possible.
                    Also, please explain why my past experience makes me a good fit for the opportunity in the email.

                    <student_info>
                    <name>
                    {Your_Name}
                    </name>
                    <education>
                    {Education}
                    </education>
                    <work>
                    {Current_Work_Role}
                    </work>
                    <research_interest>
                    {Research_Interest}
                    </research_interest>
                    <key_strengths>
                    ### Skills
                    {Technical_Skills}
                    ### Personalities
                    {Personalities_Strength}
                    </key_strengths>
                    <related_experience>
                    {Related_Experiences}
                    </related_experience>
                    <furture_plan>
                    {Future_Resolution_Goal}
                    </furture_plan>
                    </student_info>

                    <professor_info>
                    <professor_website>
                    {Professor_Website}
                    </professor_website>
                    <reserach_interest>
                    {Professor_Research_Interest}
                    </reserach_interset>
                    <interested_project>
                    <paper_url>
                    {Interest_Paper_URL}
                    </paper_url>
                    <paper_abstract>
                    {Paper_Abstract_CP}
                    </paper_abstract>
                    </interested_project>

                    </professor_info>

                    </context>


                    Your objective is to:
                    <objective>
                    Create an email for me, which is based on the [student_info] and [professor_info] provided in [context], and aims to express my interests in Professor {Professor_Name}'s research and ask for {Opportunity_Type} opportunities starting in the {Semester}, and {Alternate_Opportunity_Type} opportunities starting as soon as possible.
                    Also, please explain why my past experience makes me a good fit for the opportunity in the email.
                    </objective>


                    The writing style should be:
                    <style>
                    Follow the writing style of academic communications, be concise and straight to the point. Keep it simple.
                    </style>


                    The tone of the email should be:
                    <tone>
                    Passionate, professional, simple.
                    </tone>

                    The target audience is:
                    <audience>
                    Professor {Professor_Name}, who is hiring {Opportunity_Type}, {Alternate_Opportunity_Type}.
                    </audience>


                    Before you begin writing, think through a high-level outline of the email in a <scratchpad>. Then
                    write out each paragraph of the email as instructed below. Enclose each paragraph in <paragraph>
                    tags.
                    <response>
                    Please write one paragraph per interaction. I would provide specific requirements for each paragraph in the following inputs. Only write the one I require at a time.
                    <paragraph_1>
                    Introduce myself regarding education and work, and briefly mention I'm reaching out for potential {Opportunity_Type}, {Alternate_Opportunity_Type} opportunity for semester {Semester}.
                    </paragraph_1>
                    </response>

                    <paragraph_2>
                    <content>
                    Introduce my relevant research or work experience. Explain why I am interested in the professor's paper. Keep it simple.
                    </content>
                    <style>
                    Keep it simple.
                    </style>
                    </paragraph_2>

                    <paragraph_3>
                    <content>
                    Mention my strengths and skills. Keep it simple.
                    </content>
                    <style>
                    Keep it simple.
                    </style>
                    </paragraph_3>

                    <paragraph_4>
                    <content>
                    Express hope to work with the professor and ask if professor would love to have a short discussion regarding potential opportunities.
                    Remind the professor to check the attached {Documents}.
                    </content>
                    <style>
                    Keep it simple.
                    </style>
                    </paragraph_4>

                    Enclose the full email inside <email> tags. Remember to address the professor by name in the
                    salutation, and include a sign-off at the end.
                    '''.format(
                        Professor_Name=input_dict['Professor_Name'],
                        Opportunity_Type=input_dict['Opportunity_Type'],
                        Semester=input_dict['Semester'],
                        Alternate_Opportunity_Type=input_dict['Alternate_Opportunity_Type'],
                        Your_Name=input_dict['Your_Name'],
                        Education=input_dict['Education'],
                        Current_Work_Role=input_dict['Current_Work_Role'],
                        Research_Interest=input_dict['Research_Interest'],
                        Technical_Skills=input_dict['Technical_Skills'],
                        Personalities_Strength=input_dict['Personalities_Strength'],
                        Related_Experiences=input_dict['Related_Experiences'],
                        Future_Resolution_Goal=input_dict['Future_Resolution_Goal'],
                        Professor_Website=input_dict['Professor_Website'],
                        Professor_Research_Interest=input_dict['Professor_Research_Interest'],
                        Interest_Paper_URL=input_dict['Interest_Paper_URL'],
                        Paper_Abstract_CP=input_dict['Paper_Abstract_CP'],
                        Documents=input_dict['Documents']
                    )
        
        payload = json.dumps({
            "messages":[
                {
                    "role": "user",
                    'content': pay_load_string
                }
            ],
            "model": "deepseek-coder",
            "frequency_penalty": 0,
            "max_tokens": 1024,
            "presence_penalty": 0,
            "stop": None,
            "stream": False,
            "temperature": 0.2,
            "top_p": 1,
            "logprobs": False,
            "top_logprobs": None
                    })

        return payload



    def call_llm(self, payload):
        start = time.time()
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        print("Response: ", response.text)
        json_response = json.loads(response.text)
        
        end = time.time()
        print("Backend Response Time (s): ", end - start)
        return json_response["choices"][0]["message"]["content"]


    def parse_response(self, response):
        response = response.replace("<email>", "")
        response = response.replace("</email>", "")
        response_list =  re.split(r'<\/?paragraph>|\n', response)
        parsed_resp = "<br><br>".join([word for word in response_list if word])
        
        return parsed_resp

        