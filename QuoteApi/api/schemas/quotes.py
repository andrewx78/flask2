from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema
from marshmallow import EXCLUDE
from marshmallow.validate import Length, Range


#Example of custom validator
def rating_validate(value: int):
    # if return True -> validation success
    # if return False -> raise ValidatinError
    return value in range(1, 6)


class QuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteModel
        dump_only = ("id",)
        unknown = EXCLUDE


    id = ma.auto_field()
    text = ma.auto_field(required=True, validate=Length(min=3))
    author_id = ma.auto_field()
    author = ma.Nested(AuthorSchema(only=("id", "name", "surname")))
    rating = ma.Integer(strict=True, validate=Range(1, 6))


quote_schema = QuoteSchema(exclude=["author_id"])
quotes_schema = QuoteSchema(many=True, exclude=["author"])
change_quotes_schema = QuoteSchema(load_instance=False)
change_quotes_without_rating = QuoteSchema(exclude=["rating"], partial=True)
