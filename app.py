from flask import Flask, render_template
from flask_mail import Mail, Message

config = dict(
    MAIL_SERVER='smtp.ethereal.email',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_DEBUG=True,
    MAIL_USERNAME='liza.oconner@ethereal.email',
    MAIL_PASSWORD='by8xACmGhwzQwdBWRV',
    MAIL_DEFAULT_SENDER='Leonardo <leonardoferreiragraciano@gmail.com>',
)

app = Flask(__name__)
app.config.update(config)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<a href="/sendmail">SendEmail</a>'


@app.route('/sendmail', methods=['GET', 'POST'])
def sendmail():
    msg = Message(
        subject="Bem-Vindo",
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=['suporteban@gmail.com'],
        # body="Apenas mais um email enviado"
        html=render_template('mail/welcome.html', name="Leonardo")
    )
    mail.send(msg)
    return 'Email Enviando'


if __name__ == '__main__':
    app.run(debug=True)
