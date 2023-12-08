import os.path

from flask import Flask
from flask import render_template, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_bootstrap import Bootstrap4

from utils.parse_midi import get_note_queue

"""
Author: Lns-XueFeng
Create Time: 2023.11.11
Python Version: 3.9
"""


__author__ = "Lns-XueFeng"
__version__ = "0.1"
__license__ = "MIT"


app = Flask(__name__)
app.secret_key = "123456789"
midi_dir_path = "static/midi/"

bootstrap4 = Bootstrap4(app)

class UploadForm(FlaskForm):
    file = FileField(
        "选择midi音乐文件",
        validators=[FileRequired(), FileAllowed(["mid"])]
    )
    submit = SubmitField("上传midi音乐")


@app.route("/")
@app.route("/upload")
def home():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        file_name = file.filename
        file.save("static/midi/", file_name)
        flash(f"上传{file_name}成功！")
        session["filenames"] = [file_name]
        return redirect(url_for("home"))

    midi_list = os.listdir(midi_dir_path)
    return render_template("piano.html", form=form, midi_list=midi_list)


@app.route("/api/midi/<filename>")
def get_mid_note(filename):
    """ py提供数据接口给js """
    note_order_dict = get_note_queue(midi_dir_path + filename)
    return jsonify(note_order_dict)


if __name__ == "__main__":
    app.run(debug=True)
