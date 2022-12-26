from flask import Flask, render_template, request
import openai
import os

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except:
  print("OPENAI_API_KEY not found")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

      print(request.form.get("completion_prompt"))
      
      if request.form.get("completion_prompt"):
        completion_prompt = request.form.get("completion_prompt")
        completion_model = request.form.get("completion_model")

        response = openai.Completion.create(
          model=completion_model,
          prompt=completion_prompt, 
          temperature=0, 
          max_tokens=3
          )

        print(response)

        return render_template('index.html', completion_prompt=completion_prompt, completion_response=response["choices"][0]["text"])

      if request.form.get("image_prompt"):
        image_prompt = request.form.get("image_prompt")

        print(image_prompt)

        response = openai.Image.create(
          prompt=image_prompt,
          n=1,
          size="512x512"
        )

        print(response)

        return render_template('index.html', image_prompt=image_prompt, image_url=response['data'][0]['url'])
    
    return render_template('index.html')