from crypt import methods
from hashlib import new
from flask import Flask, jsonify ,request
from markupsafe import re






'''
__name__ a special python variable give each file is unic name.
create an flask object with unic name
'''
app = Flask(__name__)

stores = [
    {
        'name': 'My Wondeful store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.67
            }
        ]
    }
]

# POST /store data: {name}
@app.route('/srote',methods=['POST'])
def create_store():
    requst_data = request.get_json()
    new_store = {
        'name': 'My Wondeful store',
        'items': []
    } 
    stores.append(new_store)
    return jsonify(new_store)
    
# GET  /store/<string:name>    
@app.route('/store/<string:name>')
def get_strore(name):
    # iterate over stors.
    # if the store name matches, return it.
    # if none match, return error masssage.
    [targetstore for store in stores if store['name'] == name]
    for store in stores:
        if store['name'] == name:
            return  jsonify(store['name'])
    raise ReferenceError(f'No store fount under the name {name}.')
#GET  /store
@app.route('/store')
def get_strors():
    return jsonify({'stires':stores})

# POST /store/<string:name>/item data: {name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    print(f'name param : {name}')
    print(f'request.get_json() -> {request.get_json()}')
    req_data = request.get_json()
    req_data_name = req_data['name']
    print(f' req_data_name :  {  req_data_name }')
    return jsonify({'k':'v'}) 
 
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass    

@app.route("/")
def root_route():
    return "v1"

app.run(port=5000)
    