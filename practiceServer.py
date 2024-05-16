from flask import Flask,jsonify, request

app = Flask(__name__)
DATA = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Hello, world!"}

@app.route("/no_content")
def no_content():
    """return 'no content found' with a status of 204

    Returns:
        string: no content found with 204 status code
    """
    return ({"message":"No content found"}, 204)

@app.route("/exp")
def index_explicit():
    """return 'Hello World' message with a status code of 200

    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response({"message":"Hello World"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    """
    Retrieves data from a source and returns a response.

    Returns:
        A dictionary containing a message about the data retrieval status.
        If the data is found and not empty, the message will indicate the length of the data.
        If the data is empty, the message will indicate that the data is empty.
        If the data is not found, the message will indicate that the data is not found.
    


    Raises:
        None
    """
    
    try:
        if DATA and len(DATA) > 0:
            return {"message": f"Data of length {len(DATA)} found"}

        else:
            return {"message": "Data is empty"}, 500

    except NameError:
        return {"message": "Data not found"}, 404
    

@app.route("/name_search")
def name_search():
    """
    Searches the DATA for a dictionary with a matching "first_name" field based on the query parameter 'q'.

    Returns:
        A dictionary containing the matching dictionary if found, or a message indicating no match.
    
    CLI Example: url -X GET -i -w '\n' "localhost:5001/name_search?q=Ferdy" 

    Raises:
        None
    """
    query = request.args.get('q')
    if query:
        for item in DATA:
            if item.get('first_name') == query:
                return item
        return {"message": "No match found"}
    else:
        return {"message": "Query parameter 'q' is missing"}
    

@app.route("/count")
def count():
    """
    CLI : curl -X GET -i -w '\n' "localhost:5001/count"
    
    """
    try:
        return {"data count": len(DATA)}, 200

    except NameError:
        return {"message": "data not defined"}, 500
    
@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    """
    CLI (invalid ID): curl -X GET -i localhost:5001/person/11111111-589a-43b6-9a5d-d1601cf51111 
    (Valid ID): curl -X GET -i localhost:5001/person/66c09925-589a-43b6-9a5d-d1601cf53287 
    
        

    """
    for person in DATA:
        if person["id"] == str(id):
            return person
    return {"message": "person not found"}, 404

@app.route("/person/<uuid:id>", methods=['DELETE']) # by adding methods=['DELETE'] we are restricting the route to only accept DELETE requests
def delete_by_uuid(id):
    '''
    CLI: curl -X DELETE -i localhost:5001/person/66c09925-589a-43b6-9a5d-d1601cf53287 
    '''
    for person in DATA:
        if person["id"] == str(id):
            DATA.remove(person)
            return {"message":f"{id}"}, 200
    return {"message": "person not found"}, 404

@app.route("/person", methods=['POST'])
def add_by_uuid():
    '''
    CLI : curl -X POST -i -w '\n' \
  --url http://localhost:5001/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'
    '''
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
        
    # code to validate new_person ommited
    try:
        DATA.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

#error handling with json 
@app.errorhandler(404)
def api_not_found(e):
    return {"message": "API not found"}, 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
