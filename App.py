from flask import Flask 

App=Flask(__name__)

@App.route("/")
def home():
    return "Hello world"

if __name__ =="__main__":
    App.run(debug=True)