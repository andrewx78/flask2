from author import Author
from schema import AuthorSchema
from marshmallow import ValidationError, RAISE, INCLUDE, EXCLUDE


json_data = """
{
    "id": 12,
    "name": "Ivan Petrov",
    "email": "ivan@mail.ru",
    "age": 34
}
"""
try:
    schema = AuthorSchema()
    # json string -> validated dict
    json_data_as_string = schema.loads(json_data, unknown=EXCLUDE)
    print(type(json_data_as_string), json_data_as_string)
except ValidationError as e:
    print(e)
    print(e.messages_dict)


result = schema.load(json_data_as_string, unknown=INCLUDE)
print(type(result), result)
print(Author(**result))
