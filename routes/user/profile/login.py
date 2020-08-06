from flask import make_response, jsonify
from flask_restful import Resource

import secrets
from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.password import Password


class UserLogin(Resource):
    @Checks.validated_email_and_pw
    def get(email, password):
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM user WHERE email = \"{email}\"")
        has_entries = mycursor.fetchone()
        if has_entries is None:
            return make_response("User dosnt exist", 409)
        mycursor.execute(f"SELECT password FROM user WHERE email = \"{email}\"")
        pw_hash = mycursor.fetchone()[0]
        if Password.validate(password, bytes(pw_hash, 'utf-8')):
            mycursor.execute(f"SELECT authkey FROM user WHERE email = \"{email}\"")
            return jsonify(Auth_Key=mycursor.fetchone()[0])
        else:
            return make_response("Wrong Password", 401)
