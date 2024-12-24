from flask import Flask, request, jsonify, render_template
from ocr import extract_text
from kie import extract_key_value_pairs
from utils import assign_confidence_score, flag_low_confidence

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    # Process the file
    text = extract_text(file_path)
    key_values = extract_key_value_pairs(file_path)
    confidence = assign_confidence_score(key_values)
    flagged = flag_low_confidence(confidence)

    #return jsonify({
    #    "text": text,
    #    "key_values": key_values,
    #    "confidence": confidence,
    #    "flagged": flagged
    #})
    return render_template('index.html', text=text, key_values=key_values, confidence=confidence, flagged=flagged)


if __name__ == '__main__':
    app.run(debug=True)