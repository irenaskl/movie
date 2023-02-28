from flask import Flask, request, jsonify

app = Flask(__name__)

movies = [{
    "id": 1,
    "title": "The Matrix",
    "description": "The Matrix is a computer-generated dream world...",
    "release_year": 1999,

},{
    "id": 2,
    "title": "The Matrix Reloaded",
    "description": "Continuation of the cult classic The Matrix...",
    "release_year": 2003,
}]

@app.route('/movies', methods=['GET'])
def hello():
    return jsonify(movies)

@app.route('/movies/<int:id>', methods=['GET'])
def search_movie(id):
    temp = ''
    return_code = 404
    for i in movies:
        # print(type(i["id"]))
        # print(type(id))
        if id is i["id"]:           
            temp = i
            return_code = 200 
    return temp, return_code

@app.route('/movies', methods=['POST'])
def add_movie():
    temp = request.get_json()
    try:
        title = temp["title"]
        release_year = temp["release_year"]
        movies.append(temp)
        return '', 200
    except KeyError:
        return '', 400
      
@app.route('/movies/<int:id>', methods=['PUT'])
def rename(id):
    temp = request.get_json()

    title = temp.get("title")
    release_year = temp.get("release_year")
    description = temp.get("description")


    for i in range(len(movies)):
        if movies[i]["id"] == id:
            if title:
                movies[i]["title"] = title
            if release_year:
                movies[i]["release_year"] = release_year
            if description:
                movies[i]["description"] = description        
            print(movies)
            return '', 204  
        return '', 404




if __name__=='__main__':
    app.run()    