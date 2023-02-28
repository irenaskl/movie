How to use

FLASK_APP=movies.py flask --debug run -h 0.0.0.0

curl localhost:5000/movies 

curl -X PUT -H "Content-Type: application/json" -d '{"title":"pes", "description":"o kockach"}' http://localhost:5000/movies/1

