from flask import Flask, render_template, request

#######################################
#######################################

import openai
import os

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except:
  print("OPENAI_API_KEY not found")


#######################################
#######################################

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
      prompt = request.form.get("prompt")
      
      response = openai.Completion.create(
        model="text-curie-001",
        prompt=prompt, 
        temperature=0, 
        max_tokens=20
        )

      print(response)

      return render_template('index.html', prompt=prompt, response=response["choices"][0]["text"])

    return render_template('index.html')