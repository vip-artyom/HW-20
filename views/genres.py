from flask import jsonify, request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.get_json()
        genre_id = req_json["id"]
        genre_service.create(req_json)

        responce = jsonify()
        responce.status_code = 201
        responce.headers["Location"] = f"{genre_id}"
        return responce
    
    
@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, gid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def patch(self, gid):
        req_json = request.get_json()
        req_json["id"] = gid

        genre_service.update_partial(req_json)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
