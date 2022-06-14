from flask_restful import Resource, Api, reqparse
# flask_restful is an abstraction above flase to make the focouse of rest api more esyee.
from flask import Flask, request


app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        print(items)
        search = {item['name']:item['price']  for item in items if item['name'] == name }
        if len(search) != 0:
            return search
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item':'Item not fount'},404
    
    def post(self, name):
        data = request.get_json()#if the request dose not attach a json pyload. Header : {Content-Type: application/json}
        item = {'name': name, "price": data['price']}
        items.append(item)
        return item, 201
    
    
    
    # def delete(self,name):
        
        
    
        
    
    
    
class ItemList(Resource):
    def get(self):
        return {'items': items}
    
    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')



app.run(port=5000,debug=True)

