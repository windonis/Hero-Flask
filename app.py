# We import Flask
from flask import Flask
import json
from flask import Response

    
# We create a Flask app
app = Flask(__name__)

# We establish a Flask route so that we can serve HTTP traffic on that route 
@app.route('/')
def index():
    with open('./data.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return Response(json.dumps(file_data), mimetype='application/json')
# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    app.run(debug=True)