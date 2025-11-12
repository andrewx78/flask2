from author import Author
from schema import AuthorSchema
from marshmallow import ValidationError, RAISE, INCLUDE, EXCLUDE
from pprint import pprint


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


result = schema.load(json_data_as_string, unknown=EXCLUDE)
print(type(result), result)
#print(Author(**result))


json_data_list = """
[
{
"id": 1,
"name": "Alex",
"email": "alex@mail.ru"
},
{
"id": 2,
"name": "Ivan",
"email": "ivan@mail.ru"
},
{
"id": 4,
"name": "Tom",
"email": "tom@mail.ru"
}
]
"""

# При обработке списка необходимо указать параметр many=True
# Лиюо при создании экземпляра схемы при вызове методов load, loads
# Exmple 1
authors_schema = AuthorSchema(many=True)
result_one = authors_schema.loads(json_data_list)
pprint(result_one, sort_dicts=False)

#Example 2
result_two = schema.loads(json_data_list, many=True)
print('\n===========Repeat===========\n')
pprint(result_two, sort_dicts=False)