from flask import Flask, render_template, url_for, request, abort, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUCCESS2025'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'centrepointhqspace@gmail.com'
app.config['MAIL_PASSWORD'] = 'atxf epfs kuho qwkn'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('CENTREPOINTHQ','centrepointhqspace@gmail.com')
mail = Mail(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    global name, email, country
    msgbodysub = f"Congratulations you've been subscribed by us - CENTREPOINTHQ, for webinars, discounted offers and more by this author"

    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        country = request.form.get('country')
        msgbodyauthor = f"""Dear Success, \n\n
        We’re pleased to inform you that a new reader has subscribed to your book, Do’s and Don’ts for SMEs. 
        Below are the subscriber’s details::
                    Name of Subscriber -  {name}
                    Email of Subscriber -  {email}
                    Country of Subscriber -  {country} \n\n
        You may wish to add this contact to your mailing list for updates, webinars, newsletters, or future engagements. If you'd like, we can assist you in organizing and managing your subscriber list as part of our client support.
        If you have any questions or would like to enable this service, feel free to reply to this email.\n\n
        Warm Regards,
        WISDOM ENEFIOK
        FOR: CENTREPOINTHQ
        centrepointhqspace@gmail.com
        """
        msgobjsub = Message(subject="Subscription successfully received to Success Ajilore e-content, webinars and more", recipients=[email])
        msgobjauth = Message(subject="New Subscriber to Your Book: Do's and Don'ts for SMEs", recipients=['ajiloresuccess@gmail.com','wisdom.enefiok@protonmail.com'])
        msgobjsub.body = msgbodysub
        msgobjauth.body = msgbodyauthor
        try:
            mail.send(msgobjsub)
            mail.send(msgobjauth)
            completemsg = "Thanks for your subscription to this author. You are eligible for webinar updates and offers."
            return render_template("success.html", completemsg=completemsg)
        except:
            redirect(url_for("/"))
    return render_template("/")

if __name__=="__main__":
    app.run(port=5700,debug=True,host='0.0.0.0')