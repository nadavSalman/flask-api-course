




'''
Search for value in a given dic in the follwing format :
{
    {key:k1,values:v1},
    {key:k2,values:v2},
    {key:k3,values:v3}
}
Return: Tuple - (Search result {empty} / {Searched data},bollean expression :  find true else fale)
'''
def find_by_name(collection,name):
    search = {item['name']:item['price']  for item in collection if item['name'] == name}
    return (search, len(search) != 0)



    