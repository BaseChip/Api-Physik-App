import secrets
from flask import request, make_response, jsonify
from flask_restful import Resource

from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString


class GetNotes(Resource):
    @Checks.token_required
    def get(email, id):
        app_name = SecureString.secureString(request.args.get("app", ""))
        if app_name == "":
            return make_response("App paramter is missing", 406)
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM note WHERE usr_id = {id} AND app = \"{app_name}\"")
        notes = []
        for x in mycursor.fetchall():
            note = {
                "id": x[0],
                "title": x[2],
                "app": x[4]
            }
            notes.append(note)
        return jsonify(notes)
