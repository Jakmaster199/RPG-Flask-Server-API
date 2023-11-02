from flask import Blueprint, send_from_directory

from app import myDb
BP = Blueprint("default", __name__)


@BP.route(rule='/')
def index():
    return 'Uhm... Something is wrong here....'


@BP.route(rule='/install/<install_code>')
def install_db(install_code: str):

    if install_code == "1nst4ll4ti0n_f0r_g4m3":
        from app.models.accounts import Account
        myDb.create_all()
        return "Database Installed!"
    else:
        return "Database not installed..."


@BP.route(rule='/favicon.ico', methods=["GET"])
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
