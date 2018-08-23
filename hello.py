import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    apikey_mailgun = os.environ.get("apikey_mailgun")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    requests.post(
        "https://api.mailgun.net/v3/mail.polinfo.fr/messages",
        auth=("api", apikey_mailgun_polinfo),
        data={
            "from": f"{name} <{email}>",
            "to": "xuan.polinfo@gmail.com",
            "subject": "Message à partir du site web de polinfo.fr",
            "text": f"Email: {email}\nPhone: {phone}\n{message}",
        },
    )

    # from flask_mail import Message
    # msg = Message("Message à partir du site web de 4-you.fr", recipients=['xuan.polinfo@gmail.com'])
    # msg.body = f"Email: {email}\nPhone: {phone}\n{message}"
    # mail.send(msg)

    return redirect(url_for("index"))
