from marshmallow import Schema, fields, validate

class PostAddEmailSchema(Schema):
    email = fields.Email(required=True)
    id = fields.UUID(required=True)
    reason = fields.String(required=True, validate=validate.Length(max=255))
    createdAt = fields.DateTime()