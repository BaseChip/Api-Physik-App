from flask import jsonify
from flask_restful import Resource

from util.checks import Checks


class Topics(Resource):
    @Checks.getAppForDatabase
    def get(mydb):
        mycursor = mydb.cursor()
        mycursor.execute("Select * FROM Themen")
        topics = []
        for x in mycursor.fetchall():
            topic = {
                "id": x[0],
                "topic": x[1]
            }
            topics.append(topic)
        return jsonify(topics)
