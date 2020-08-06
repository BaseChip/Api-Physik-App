from flask import request, make_response
from flask_restful import Resource

import secrets
from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString


class AddNote(Resource):
    @Checks.token_required
    def post(email, id):
        note = SecureString.secureString(request.form.get("note", "None"))
        title = SecureString.secureString(request.form.get("title", "None"))
        app = SecureString.secureString(request.form.get("app", "None"))
        if note == "None" or app == "None" or title == "None":
            return make_response("Note / Title / App details missing", 500)
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO note (usr_id, note, app, title) VALUES (%s, %s, %s, %s)", (id, note, app, title))
        mydb.commit()
        return make_response("note added", 200)
