from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline('summarization', model='Falconsai/text_summarization')

@app.route('/summarize', methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data["text"]
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return jsonify({"Summary": summary[0]['summary_text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
