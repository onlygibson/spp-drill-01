"""files-api: a small internal service for the spp-drill-01 practice repo.

Lists stored files and reports image dimensions.
"""
import os

from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)

DATA_DIR = os.environ.get("DATA_DIR", "/app/data")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/files")
def file_info():
    """Shows details for one stored file, e.g. /files?name=report.txt"""
    name = request.args.get("name", "")
    base_dir = os.path.normpath(os.path.abspath(DATA_DIR))
    target_path = os.path.normpath(os.path.join(base_dir, name))

    # Only allow files inside DATA_DIR (blocks ../ and absolute paths)
    if not target_path.startswith(base_dir + os.sep):
        return jsonify(output="", error="invalid file path"), 400

    if not os.path.isfile(target_path):
        return jsonify(output="", error="file not found"), 404

    try:
        st = os.stat(target_path)
    except OSError:
        app.logger.exception("could not read file info")
        return jsonify(output="", error="could not read file"), 500

    return jsonify(
        output=f"{st.st_mode:o} {st.st_size} {os.path.basename(target_path)}",
        error="",
    )


@app.route("/image-size", methods=["POST"])
def image_size():
    """Returns the width and height of an uploaded image."""
    upload = request.files.get("file")
    if upload is None:
        return jsonify(error="send an image as form field 'file'"), 400
    img = Image.open(upload.stream)
    return jsonify(width=img.width, height=img.height)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))