from flask_restful import Resource, Api, reqparse
# flask_restful is an abstraction above flase to make the focouse of rest api more esyee.
from flask import Flask, request
from crud_auxiliary import find_by_name



app = Flask(__name__)
api = Api(app)

items = []
'''
End point implementation:
Header : {Content-Type: application/json}
GET   /items            Done
GET   /item/<name>      Done
POST  /item/<name>      Done
DEL   /item/<name>
PUT   /item/<name>
'''
class Item(Resource):
    def get(self,name):
        print(items)
        search = find_by_name(items,name)
        print(search)
        if search[1]:
            return search[0], 200
        return {'item':'Item not fount'},404
    
    def post(self, name):
        data = request.get_json()#if the request dose not attach a json pyload. Header : {Content-Type: application/json}
        item = {'name': name, "price": data['price']}
        items.append(item)
        return item, 201
    
    def delete(self,name):
        search = find_by_name(items,name)
        if search[1]:
            return search[0], 200
        return {'item':'Item not fount'},404
        
        
        
        
    
        
    
    
    
class ItemList(Resource):
    def get(self):
        return {'items': items}
    
    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')



app.run(port=5000,debug=True)

