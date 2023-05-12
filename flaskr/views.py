from flask import Blueprint, render_template, request
import srt

from google_translate import GoogleTranslate
from subtitle import translate_subtitle


bp = Blueprint("views", __name__)

@bp.get("/")
def index():
    return render_template("index.html")


@bp.route("/subtitle/translate/", methods=["GET", "POST"])
async def translate_view():
    # text, language, tow or one
    # get file -> done
    # parsr srt -> done
    # translate
    # return new file
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            print("ali")
        #     flash('No file part')
        #     return redirect(request.url)
        file = request.files['file']
        subtitle_text = file.read().decode("utf-8")

        # translate subtitle
        new_file = await translate_subtitle(subtitle_text, "fa")

        # # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('download_file', name=filename))
        return render_template("subtitle/translate.html")
    
    if request.method == "GET":
        return render_template("subtitle/translate.html")