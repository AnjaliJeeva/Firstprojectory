from flask import Flask,render_template

App3=Flask(__name__)

@App3.route("/")
def Index():
    return render_template("Index.html")

@App3.route("/About")
def About():
    return render_template("About.html")

@App3.route("/Home")
def Home():
    return render_template("Home.html")

if __name__=="__main__":
    App3.run(debug=True)
