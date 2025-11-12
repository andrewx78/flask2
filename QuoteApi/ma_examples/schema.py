from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Integer(strict=True)
    name = fields.String(required=True, error_messages={"required": "field 'name' id required"})
    email = fields.Email()
    surname = fields.String()
