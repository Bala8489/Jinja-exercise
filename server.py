from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
  return "hello"


@app.route('/guess/<name>')
def guess_age(name):
  name_dict = {"name": name}

  response = requests.get("https://api.genderize.io?", params=name_dict)
  data = response.json()
  user_name = data["name"]
  user_age = data["age"]
  gender_response=requests.get(f"https://api.agify.io?name={name}")
  gender_data=gender_response.json()
  user_gender=gender_data["gender"]
  return render_template("index.html", name=user_name, age=user_age,gender=user_gender)


if __name__ == "__main__":
  app.run(debug=True)


