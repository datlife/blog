"""Handle Exceptions. """
from flask import jsonify


def template(data, code=500):
    """Generic Template for generating  exception in JSON."""
    return {'message': {'errors': {'body': data}}, 'status_code': code}

UNKOWN_ERROR = template([], code=500)
POST_NOT_FOUND = template(['Post not found'], code=404)


class InvalidUsage(Exception):
    """InvalidUsage object for Blog App."""
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def unknown_error(cls):
        return cls(**UNKOWN_ERROR)

    @classmethod
    def article_not_found(cls):
        return cls(**POST_NOT_FOUND)
