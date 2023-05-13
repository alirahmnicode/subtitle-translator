from flask import Blueprint, render_template, request 

from subtitle import translate_subtitle


bp = Blueprint("views", __name__)

@bp.get("/")
def index():
    return render_template("index.html")


@bp.route("/subtitle/translate/", methods=["GET", "POST"])
async def translate_view():
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            print("ali")
        file = request.files['file']
        subtitle_text = file.read().decode("utf-8")

        # translate subtitle
        new_file = await translate_subtitle(subtitle_text, "fa")
        # save file
        with open("a.srt", 'w') as f:
            f.write(new_file)

        return render_template("subtitle/translate.html")
    
    if request.method == "GET":
        return render_template("subtitle/translate.html")