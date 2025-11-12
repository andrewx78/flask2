from api import app, db
from flask import request, abort, jsonify
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from sqlalchemy.exc import SQLAlchemyError
from api.schemas.author import author_schema, authors_schema, change_author_schema
from marshmallow import ValidationError, EXCLUDE

@app.post("/authors")
def create_author():
    # add_to_db(AuthorModel, author_data)  # Variant 2
    try:
        # 1 Get raw bites
        #print(request.data)
        # 2 Load bytes to dict
        #author_data = author_schema.loads(request.data)
        # 3 Create new AuthorModel instance via dict
        #author = AuthorModel(**author_data)
        author = author_schema.loads(request.data) # get_data() return raw bytes

        db.session.add(author)
        db.session.commit()
    except ValidationError as ve:
        abort(400, f"Validation error: {str(ve)}")
    except Exception as e:  
        abort(503, f"Database error: {str(e)}")
    return jsonify(author_schema.dump(author)), 201


# URL: "/authors/<int:author_id>/quotes"
@app.route("/authors/<int:author_id>/quotes", methods=["GET", "POST"])
def author_quotes(author_id: int):
    author = db.get_or_404(AuthorModel, author_id, description=f"Author with id={author_id} not found")

    if request.method == "GET":
        quotes = [quote.to_dict() for quote in author.quotes]
        return jsonify({"author": author.name} | {"quotes": quotes}), 200

    elif request.method == "POST":
        data = request.json
        new_quote = QuoteModel(author, **data)
        db.session.add(new_quote)
        db.session.commit()
        return jsonify(new_quote.to_dict() | { "author_id" : author.id}), 201
    else:
        abort(405)


@app.get("/get_authors")
def get_authors():
    authors_db = db.session.scalars(db.select(AuthorModel)).all()
    return authors_schema.dump(authors_db), 200


@app.get("/authors/<int:author_id>")
def get_author_by_id(author_id: int):
    author = db.get_or_404(AuthorModel, author_id, description=f'Author with id={author_id} not found')
    # instance -> dict -> json
    #return jsonify(author.to_dict()), 200
    return jsonify(author_schema.dump(author)), 200


#TODO

@app.route("/authors/<int:author_id>", methods=['DELETE'])
def delete_author(author_id):
    author = db.get_or_404(entity=AuthorModel, ident=author_id, description=f"Author with id={author_id} not found")
    db.session.delete(author)
    try:
        db.session.commit()
        return jsonify({"message": f"Author with id {author_id} has deleted."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(503, f"Database error: {str(e)}")




@app.route("/authors/<int:author_id>", methods=['PUT'])
def update_author_name_surname(author_id):
    try:
        new_data = change_author_schema.load(request.json, unknown=EXCLUDE)
    except ValidationError as ve:
        return abort(400, f"No valid data to update: {str(ve)}")

    if not new_data:
        return abort(400, "Invalid data")
    
    author = db.get_or_404(entity=AuthorModel,ident=author_id, description=f"Author with id={author_id} not found")

    try:
        for key_as_attr, value in new_data.items():
            setattr(author, key_as_attr, value)

        db.session.commit()
        return jsonify(author.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        abort (503, f"Database error: {str(e)}")
    

