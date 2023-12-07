from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods =['GET', 'POST'])
def messages():
    if request.method =='GET':
        messages = []

        for message in Message.query.all():
            messages.append(message.to_dict())

        response = make_response(jsonify(messages),200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    elif request.method =='POST':
        message = request.get_json()
        new_message = Message(
        body= message['body'],
        username =message['username']
        )

        db.session.add(new_message)
        db.session.commit()

        response = make_response(
                jsonify(new_message.to_dict()),
                201
            )
        return response



@app.route('/messages/<int:id>', methods =['PATCH', 'DELETE'])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()

    if request.method =='PATCH':
        update =request.get_json()
        for attr in update:
            setattr(message, attr, update[attr])


        db.session.add(message)
        db.session.commit()

        message_dict = message.to_dict()

        response = make_response(
            jsonify(message_dict),
            200
        )
        return response
    
    elif request.method == 'DELETE':
        message = Message.query.filter_by(id=id).first()

        db.session.delete(message)
        db.session.commit()

        response =make_response(
            jsonify({
                'message': 'message delated successfuly!'
            })
        ), 200
        return response



if __name__ == '__main__':
    app.run(port=5555)
