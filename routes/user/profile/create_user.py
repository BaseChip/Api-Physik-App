import secrets

from flask import make_response, jsonify
from flask_restful import Resource

from util.checks import Checks
from util.mysql_connector import MySqlConnector
from util.password import Password


class CreateUser(Resource):
    @Checks.validated_email_and_pw
    def get(email, password):
        mydb = MySqlConnector.connect(secrets.database_users)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM user WHERE email = \"{email}\"")
        has_entries = mycursor.fetchone()
        if has_entries is not None:
            return make_response("User already exists", 406)
        pw_hash = Password.get_hash(password)
        auth_key = Password.create_authkey()
        mycursor.execute("INSERT INTO user (email, password, authkey) VALUES (%s, %s, %s)", (email, pw_hash, auth_key))
        mydb.commit()
        return jsonify(Auth_Key=auth_key)