import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load the data from q-vercel-python.json
with open('q-vercel-python.json') as f:
    data = json.load(f)

# Create a dictionary for faster lookups
data_dict = {entry['name']: entry['marks'] for entry in data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Retrieve 'name' query parameters
    marks = []
    
    for name in names:
        # Check if the name exists in the data_dict
        if name in data_dict:
            marks.append(data_dict[name])
        else:
            marks.append(None)  # Return None for unknown names

    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
