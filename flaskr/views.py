from flask import Blueprint, render_template, request, send_file, flash, redirect

from subtitle import translate_subtitle
from .utilities import allowed_file


bp = Blueprint("views", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.route("/subtitle/translate/", methods=["GET", "POST"])
async def translate_view():
    if request.method == "POST":
        # check if the post request has the file part
        file_name = request.files["file"].filename

        if "file" not in request.files or file_name == "":
            flash("فایلی انتخاب نشده.", "warning")
            return redirect(request.url)

        file = request.files["file"]

        if allowed_file(file_name) and file:
            subtitle_text = file.read().decode("utf-8")
            # translate subtitle
            new_file = await translate_subtitle(subtitle_text, "fa")
            return send_file(
                new_file, download_name="ali.srt", mimetype="srt", as_attachment=True
            )
        else:
            flash("فایل انتخاب شده مجاز نیست", "danger")
            return redirect(request.url)

    if request.method == "GET":
        return render_template("subtitle/translate.html")
