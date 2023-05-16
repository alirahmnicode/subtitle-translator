from flask import Blueprint, render_template, request, send_file, flash, redirect

from subtitle import translate_subtitle
from .utilities import allowed_file
from google_translate.constant import GOOGLE_LANGUAGES_TO_CODES


bp = Blueprint("views", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.route("/subtitle/translate/", methods=["GET", "POST"])
async def translate_view():
    if request.method == "POST":
        form = request.form

        file_name = request.files["file"].filename
        target_language = form.get("language")
        bilingual = form.get("bilingual") == "on"

        if "file" not in request.files or file_name == "":
            flash("فایلی انتخاب نشده.", "warning")
            return redirect(request.url)

        file = request.files["file"]

        if allowed_file(file_name) and file:
            subtitle_text = file.read().decode("utf-8")
            # translate subtitle
            new_file = await translate_subtitle(subtitle_text, target_language, bilingual)
            return send_file(
                new_file, download_name=file_name, mimetype="srt", as_attachment=True
            )
        else:
            flash("فایل انتخاب شده مجاز نیست", "danger")
            return redirect(request.url)

    if request.method == "GET":
        # languages suport
        languages = GOOGLE_LANGUAGES_TO_CODES
        return render_template("subtitle/translate.html", languages=languages)
