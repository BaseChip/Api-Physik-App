import secrets

from flask_restful import Resource
from flask import request, make_response

from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString


class DeleteNote(Resource):
    @Checks.token_required
    def delete(email, id):
        note_id = SecureString.secureString(request.args.get("id"))
        if note_id == "":
            return make_response("Note ID missing", 500)
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM note WHERE id={note_id} AND usr_id = \"{id}\"")
        mydb.commit()
        return make_response("Deleted", 200)
