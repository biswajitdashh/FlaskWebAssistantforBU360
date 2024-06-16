from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
application = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@application.route('/', methods=['GET','POST'])
def index():
    res=""
    if request.method == 'POST':
            system_behavior=request.form["system_behavior"]
            data=request.form["data"]
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content":system_behavior},
                    {"role": "user", "content": data},
                    {"role": "assistant", "content":"Do a web search based on the context provided"},
                ])
            res=response.choices[0].message.content
    return render_template("index.html",result=res)
if __name__ == '__main__':
    application.run(debug=True) 
