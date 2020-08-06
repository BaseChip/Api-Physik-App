from flask import request, make_response, jsonify
from flask_restful import Resource

import secrets
from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString


class GetNote(Resource):
    @Checks.token_required
    def get(email, id):
        note_id = SecureString.secureString(request.args.get("id", ""))
        if note_id == "":
            return make_response("ID paramter is missing", 406)
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM note WHERE usr_id = {id} AND id = \"{note_id}\"")
        for x in mycursor.fetchall():
            note = {
                "id": x[0],
                "title": x[2],
                "note": x[3],
            }
        return jsonify(note)
