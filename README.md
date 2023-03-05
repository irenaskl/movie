## How to use

## Run
```bash
FLASK_APP=movies.py flask --debug run -h 0.0.0.0
```
## GET
```bash
curl localhost:5000/movies
```
## PUT
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title":"pes", "description":"o kockach"}' http://localhost:5000/movies/1
```
