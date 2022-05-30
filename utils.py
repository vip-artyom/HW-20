import jwt
from flask import request, abort

from constants import SECRET_KEY, ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        print(request.headers)
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper