from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/summarize", methods=["GET"])
def summarize():
    """
    Accepts a paragraph and returns a summary
    """
    return "", 200

@app.route("/translate", methods=["GET"])
def translate():
    """
    Accepts a paragraph and returns a translation to Arabic
    """
    return "", 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000)