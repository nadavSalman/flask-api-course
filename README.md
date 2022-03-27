








# $curl for query the rest api :

### POST with data from .json fiel:
use the data option :
```
    curl -d @payload.json  -v -H "Content-Type: application/json"   http://localhost:5000/store/kuku/item
```