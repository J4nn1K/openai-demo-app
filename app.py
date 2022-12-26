from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
      prompt = request.form.get("prompt")
      print(prompt)

    return render_template('index.html')