from flask import Flask, render_template, request, Markup
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
      if request.form.get("completion_prompt"):
        completion_prompt = request.form.get("completion_prompt")
        completion_model = request.form.get("completion_model")

        resp = None
        error = None

        try:
          response = openai.Completion.create(
            model=completion_model,
            prompt=completion_prompt, 
            temperature=0, 
            max_tokens=512
          )
          print(response)
          resp = response["choices"][0]["text"]
          resp = Markup(resp.lstrip("\n").replace('\n', '<br>'))

        except openai.error.OpenAIError as e:
          error = e

        return render_template('index.html', completion_prompt=completion_prompt, completion_response=resp, completion_error=error)


      if request.form.get("image_prompt"):
        image_prompt = request.form.get("image_prompt")
        
        resp = None
        error = None

        try:
          response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="512x512"
          )        
          resp = response['data'][0]['url']

        except openai.error.OpenAIError as e:
          error = e

        return render_template('index.html', image_prompt=image_prompt, image_url=resp, image_error=error)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))