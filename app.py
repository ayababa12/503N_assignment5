from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/summarize", methods=["GET"])
def summarize():
    """
    Accepts a paragraph and returns a summary
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON payload."}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize the following:\n\n{data['text']}"}
            ],
            temperature=0.5,
            max_tokens=150
        )
        summary = response.choices[0].message.content.strip()
        return jsonify({"summary": summary})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route("/translate", methods=["GET"])
def translate():
    """
    Accepts a paragraph and returns a translation to Arabic
    """
    return "", 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000)