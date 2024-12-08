from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Folder to store static files
STATIC_FOLDER = "static"
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/generate', methods=['POST'])
def generate_soundtrack():
    try:
        # Extract data from the POST request
        data = request.get_json()
        genre = data.get("genre", "Unknown")
        instruments = data.get("instruments", [])

        # Simulate generating audio data
        audio_data = b"FakeAudioData"  # Replace with actual audio generation logic

        # Save the generated audio file
        output_path = os.path.join(STATIC_FOLDER, "generated_audio.mp3")
        with open(output_path, "wb") as f:
            f.write(audio_data)

        # Return success response with the audio URL
        return jsonify({
            "status": "success",
            "audio_url": f"http://127.0.0.1:5000/static/generated_audio.mp3",
            "message": "Soundtrack generated successfully!"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
