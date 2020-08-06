from flask import request, make_response
from flask_restful import Resource

import secrets
from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString


class ChangeNote(Resource):
    @Checks.token_required
    def post(email, id):
        note = SecureString.secureString(request.form.get("note"))
        note_id = SecureString.secureString(request.form.get("id"))
        if note_id == "" or note == "":
            return make_response("Note / ID details missing", 500)
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"UPDATE note SET note=\"{note}\" WHERE usr_id={id} AND id={note_id}")
        mydb.commit()
        return make_response("Changed", 200)
