# shown "pls work" in browser when run
from flask import Flask
app = Flask(__name__)       # define flask name

@app.route("/")
def index():
    return "pls work"           # content on the website

if __name__ == "__main__":          
    app.run(host='0.0.0.0' , port = 4000)       #localHost location





