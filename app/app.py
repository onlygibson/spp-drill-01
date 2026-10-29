"""files-api: a small internal service for the spp-drill-01 practice repo.

Lists stored files and reports image dimensions. It is intentionally
vulnerable. Treat it as a service handed to you by a developer team.
"""
import os
import subprocess

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
    result = subprocess.run(
        f"ls -la {DATA_DIR}/{name}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return jsonify(output=result.stdout, error=result.stderr)


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
