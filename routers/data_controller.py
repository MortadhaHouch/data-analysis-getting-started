from flask import request, jsonify, Blueprint, render_template
data_controller = Blueprint("data", __name__)
import  pandas as pd
# Route for uploading files and reading them
@data_controller.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file:
        if file.content_type == "application/json":
            data_frame = pd.read_json(file)
            return data_frame.to_html()
        elif file.content_type == "text/plain":
            data_frame = pd.read_csv(file)
            return data_frame.to_html()
        elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            data_frame = pd.read_excel(file)
            return data_frame.to_html()

# Route to render the HTML file upload page
@data_controller.route("/upload", methods=["GET"])
def render_file_upload():
    return render_template("index.html")
