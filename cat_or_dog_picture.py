from flask import Flask, send_file, request
import requests
import random

app = Flask(__name__)

@app.route('/image', methods=['GET'])
def get_random_image():
    animal = request.args.get('animal')
    if animal == 'cat':
        url = 'https://api.thecatapi.com/v1/images/search'
    elif animal == 'dog':
        url = 'https://api.thedogapi.com/v1/images/search'
    else:
        return jsonify({'error': 'Invalid animal type. Please specify "cat" or "dog".'}), 400

    response = requests.get(url).json()
    image_url = response[0]['url']

    # Send the image from the URL as a response
    return send_file(requests.get(image_url, stream=True).raw, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
