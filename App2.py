from flask import Flask

App2=Flask(__name__)

@App2.route("/")
def home():
    return "Hello world"

@App2.route("/Anjali")
def Minnu():
    return "Petname"

if(__name__=="__main__"):
    App2.run(debug=True)   