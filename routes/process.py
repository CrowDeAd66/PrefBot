from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to store uploaded PDFs
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """Endpoint to upload a PDF file."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 200
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/generate-html', methods=['POST'])
def generate_html():
    """Endpoint to generate HTML from uploaded PDF."""
    # Logic to convert PDF to HTML would go here (not implemented in this mockup)
    # Simulate HTML generation
    return jsonify({'message': 'HTML generated successfully'}), 200

@app.route('/status', methods=['GET'])
def check_status():
    """Endpoint to check the status of the processing."""
    # Status logic should be implemented here
    return jsonify({'status': 'Processing complete'}), 200

if __name__ == '__main__':
    app.run(debug=True)