from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_image', methods=['POST'])
def receive_image():
    # Check if the request contains an image
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    # Process the image (optional)
    
    # Send a response to the app
    return jsonify({'message': 'Image received successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
