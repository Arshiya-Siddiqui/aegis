from flask import Flask, request, jsonify
from aegis.core.sanitizer import PromptSanitizer

app = Flask(__name__)
sanitizer = PromptSanitizer()

@app.route("/api/prompt", methods=["POST"])
def handle_prompt():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' field"}), 400

    user_prompt = data["prompt"]
    sanitized_prompt = sanitizer.sanitize(user_prompt)

    return jsonify({
        "original_prompt": user_prompt,
        "sanitized_prompt": sanitized_prompt
    })

if __name__ == "__main__":
    app.run(debug=True)
