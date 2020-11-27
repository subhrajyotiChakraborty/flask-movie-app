import os
from flask import Flask
import requests
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# for dev
# load_dotenv(".env", verbose=True)
# app.config.from_object("default_config")
# app.config.from_envvar("APPLICATION_SETTINGS")

# for production
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTINGS")


@app.route("/movie")
@app.route("/movie/<string:movieName>")
def movies(movieName="Jurassic"):
    print(os.environ.get('API_KEY'))
    r = requests.get(f"http://www.omdbapi.com/?apikey={os.environ.get('API_KEY')}&s=/{movieName}")
    return r.json()


if __name__ == "__main__":
    app.run(debug=True)