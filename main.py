from flask import Flask, render_template, redirect, url_for, request
from data import db_session
from data.congratulation import Congratulation


app = Flask(__name__)


@app.route('/')
def congratulation():
    imgs = []
    db_sess = db_session.create_session()
    congs = []
    for cong in db_sess.query(Congratulation).all():
        congs.append(cong.text)
    for i in range(len(congs)):
        imgs.append(f"{1 + i % 8}.png")
    return render_template("congratulation_form.html", title="С 8 МАРТА ДЕВУШКИ", images=imgs, congs=congs)


@app.route('/add_a_greeting', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        text = request.form["idea_text"]
        db_sess = db_session.create_session()
        cong = Congratulation(text=text)
        db_sess.add(cong)
        db_sess.commit()
        return redirect('/')
    else:
        return render_template("add_a_greeting.html", title="ПАРНИ ПОЗДРАВЬТЕ ВСЕХ ДЕВУШЕ С 8 МАРТА")


if __name__ == '__main__':
    db_session.global_init("db/congratulation.db")
    app.run()