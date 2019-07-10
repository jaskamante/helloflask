from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/jasmine")
def salvador():
    return "Hello, Jasmine"
if __name__ == "__main__":
    app.run(debug=True)