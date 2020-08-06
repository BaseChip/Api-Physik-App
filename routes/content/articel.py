from flask import request
from flask_restful import Resource

from util.checks import Checks


class Articel(Resource):
    @Checks.getAppForDatabase
    def get(mydb):
        id = request.args.get("id", 0)
        if int(id):
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Eintraege WHERE id = {id}")
            x = mycursor.fetchone()
            articel = {
                "id": x[0],
                "thema_id": x[1],
                "autor": x[2],
                "titel": x[3],
                "typ": x[4],
                "content": x[5]
            }
            return articel
