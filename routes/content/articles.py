from flask import request
from flask_restful import Resource

from util.checks import Checks


class Articels(Resource):
    @Checks.getAppForDatabase
    def get(mydb):
        id = request.args.get("id", 0)
        if int(id):
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Eintraege WHERE thema_id = {id}")
            articels = []
            for x in mycursor.fetchall():
                # hier werden nur die ID und der Titel zurück gegeben, da wir mehr details an der Stelle noch
                # nicht benötigen und für mehr informationen zu einem Artikel der /articel?id= link ist
                articel = {
                    "id": x[0],
                    "titel": x[3],
                }
                articels.append(articel)
            return articels
