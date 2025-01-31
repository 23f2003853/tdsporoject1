import json

import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Origin","*")        
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return
        
# Load student data from the JSON file
def load_student_data():
    with open('..\q-vercel-python.json', 'r') as file:
        return json.load(file)

def handler(request):
    # Load the student data
    students_data = load_student_data()

    # Get query parameters from the request
    query_params = request.query_params
    names = query_params.getlist('name')  # Get list of names from query

    # Find the marks for the requested names
    result = []
    for name in names:
        student = next((s for s in students_data if s['name'] == name), None)
        if student:
            result.append({"name": name, "marks": student["marks"]})
        else:
            result.append({"name": name, "marks": "Not Found"})
    
    # Return the result as a JSON response
    return json.dumps(result)
