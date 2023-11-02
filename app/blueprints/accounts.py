from flask import Blueprint, request, json
from flask_expects_json import expects_json
from app import myDb
from app.models.accounts import Account
from app.schemas import account_create_schema

BP = Blueprint("account", __name__)


@BP.route(rule='/', methods=['POST'])
@expects_json(account_create_schema)
def acc_create():
    input_body = json.loads(request.data)

    acc = input_body['username']
    pwd = input_body['password']
    mail = input_body['email']

    new_account = Account(username=acc, password=pwd, email=mail)

    myDb.session.add(new_account)
    myDb.session.commit()

    return 'Account [%s] created successfully!!' % acc


@BP.route(rule='/<acc_id>', methods=['GET'])
def acc_retrieve(acc_id):

    account = Account.query.get(acc_id)
    print('%r' % account)
    return ''
