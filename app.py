from flask import request

from config import app, create_table
from services.author import AuthorService


@app.route("/hello/", methods=["GET", "POST"])
def hello_world():
    data = {"message": "Hello World"}
    return data, 200


@app.route("/people/<name>", methods=["GET"])
def hello_name(name: str):
    firstname = request.args.get('firstname', "")
    age = request.args.get('age', "50")
    data = {"message": f"Hello {name} {firstname}, agé de {age}"}
    return data, 203


# Ressource Author
@app.route("/authors/", methods=["GET"])
def get_all_authors():
    authors = AuthorService.get_all()
    authors = [{"id": author.id, "firstname": author.firstname, "lastname": author.lastname} for author in authors]
    return authors, 200


@app.route("/authors/", methods=["POST"])
def save_author():
    body = request.json
    author = AuthorService.create(body)
    return {"id": author.id, "firstname": author.firstname, "lastname": author.lastname}, 201


if __name__ == "__main__":
    create_table()
    app.run(port=8000)
