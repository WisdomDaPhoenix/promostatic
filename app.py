from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/home")
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")



if __name__=="__main__":
    app.run(port=5700,debug=True,host='0.0.0.0')