from flask import request, url_for
from flask_api import FlaskAPI
from flask import jsonify
from flask import json
from flask import Response
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)

@app.route('/name',methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    name = data['name']
    age = int(data['age'])
    
    print(name,age)

    if age >=18:
        response = str(name)+" :Allowed to Apply for Driving License"
    else:
        response = str(name)+" :minor, Not Allowed to Apply for Driving License"
    return jsonify({'Response':response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50010)
