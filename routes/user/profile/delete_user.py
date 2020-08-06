import secrets

from flask import make_response
from flask_restful import Resource

from util.checks import Checks
from util.mysql_connector import MySqlConnector


class DeleteUser(Resource):
    @Checks.token_required
    def delete(email, id):
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM user WHERE email= \"{email}\"")
        mydb.commit()
        return make_response("user deleted", 200)
