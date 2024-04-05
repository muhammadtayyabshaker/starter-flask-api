from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/detect_human', methods=['POST'])
def detect_human():
    # Get image file from request
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({'error': 'No image provided'}), 400
    
    # Read the image
    nparr = np.fromstring(image_file.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Load pre-trained model for human detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Detect humans in the image
    humans, _ = hog.detectMultiScale(img, winStride=(8, 8), padding=(16, 16), scale=1.05)
    
    # Check if humans are detected
    if len(humans) > 0:
        response = {'human_detected': True}
    else:
        response = {'human_detected': False}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
