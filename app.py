from flask import Flask
from database.__init__ import database
from views.user_view import user
#pip install flask

app = Flask(__name__)

print(database)

app.register_blueprint(user)

@app.route("/")
def index():
    return "HOME"


if __name__ == "__main__":
    app.run()

#flask --app app run