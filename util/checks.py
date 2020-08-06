from functools import wraps

from flask import request, make_response

import secrets
from util.mysql_connector import MySqlConnector
from util.secure_string import SecureString
from util.verify import Verify


class Checks:
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
             token = request.headers['x-access-token']
            except KeyError:
                return make_response("Token is missing", 401)
            mydb = MySqlConnector.connect(secrets.database_users)
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM user WHERE authkey = \"{token}\"")
            user = mycursor.fetchone()
            if user is None:
                return make_response("Invalid Token!", 401)
            return f(user[2], user[0])
        return decorated

    def validated_email_and_pw(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            email = SecureString.secureString(request.args.get("email", "muster"))
            password = SecureString.secureString(request.args.get("pw", "pw_muster"))
            if password == "pw_muster" or not Verify.email(email):
                return make_response("email / password not valid", 401)
            return f(email, password)
        return decorated

    def getAppForDatabase(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            app = SecureString.secureString(request.args.get("app", "None"))
            if app == "None":
                return make_response("App paramter is missing", 406)
            elif app.lower() == "mathe":
                return f(MySqlConnector.connect(secrets.database_mathe))
            elif app.lower() == "physik":
                return f(MySqlConnector.connect(secrets.database_physik))
            else:
                return make_response("App unknown", 406)
        return decorated
