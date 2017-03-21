# coding:utf-8
from flask import Flask, request


app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        video = request.files['video']
        video.save("/home/jagger/video.mov")
        return "Upload Successfully!"
    else:
        form_html = """
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="video">
            <input type="submit" value="Upload">
        </form>
        """
        return form_html

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7002)