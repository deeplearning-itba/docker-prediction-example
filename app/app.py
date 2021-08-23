from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
model = spacy.load('es_core_news_lg')

print('model loaded')

@app.route('/')
def health_check():
    return 'OK'

def get_vector(word):
    return [float(f) for f in model(word).vector]

@app.route('/api/v1/w2v', methods=['POST'])
def api_get_vectors():
    request_body = request.get_json(force=True)
    words = request_body['instances']
    predictions = {
        "predictions": [get_vector(word) for word in words]
    }
    return jsonify(predictions)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)