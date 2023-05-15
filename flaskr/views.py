from flask import Blueprint, render_template, request, send_file

from subtitle import translate_subtitle


bp = Blueprint("views", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.route("/subtitle/translate/", methods=["GET", "POST"])
async def translate_view():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            print("ali")
        file = request.files["file"]
        subtitle_text = file.read().decode("utf-8")

        # translate subtitle
        new_file = await translate_subtitle(subtitle_text, "fa")

        return send_file(
            new_file, download_name="ali.srt", mimetype="srt", as_attachment=True
        )

    if request.method == "GET":
        return render_template("subtitle/translate.html")
