import sentry_sdk
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from sentry_sdk.integrations.flask import FlaskIntegration

import secrets
from routes.content.articel import Articel
from routes.content.articles import Articels
from routes.content.topics import Topics
from routes.physik.beugungsmuster import Beugungsmuster
from routes.user.notes.add_note import AddNote
from routes.user.notes.change_note import ChangeNote
from routes.user.notes.delete_note import DeleteNote
from routes.user.notes.get_note import GetNote
from routes.user.notes.get_notes import GetNotes
from routes.user.profile.create_user import CreateUser
from routes.user.profile.delete_user import DeleteUser
from routes.user.profile.login import UserLogin

sentry_sdk.init(
    dsn=secrets.sentry_dns,
    integrations=[FlaskIntegration()]
)
app = Flask(__name__)
CORS(app)
api = Api(app)
CORS(app)

# User
api.add_resource(CreateUser, "/createuser")
api.add_resource(UserLogin, "/login")
api.add_resource(DeleteUser, "/delete")

#Notes
api.add_resource(GetNotes, "/notes") #GET
api.add_resource(AddNote, "/note") # POST
api.add_resource(ChangeNote, "/changenote")
api.add_resource(DeleteNote, "/note") # DELETE
api.add_resource(GetNote, "/note") #GET

# Content
api.add_resource(Articel, "/articel")
api.add_resource(Articels, "/articels")
api.add_resource(Topics, "/topics")
# Physik
api.add_resource(Beugungsmuster, "/plot/beugungsmuster")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
