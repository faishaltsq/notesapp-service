from app import app
from flask import request
from app.controllers import user_controllers , notes_controllers

@app.route('/api')
def index():
    return "this is api for Tugas Besar : Notes App"

@app.route('/api/v1/users',methods=['GET','POST'])
def user():
    if request.method != 'POST':
        return user_controllers.index()
    else :
        return user_controllers.create(request)
    
@app.route('/api/v1/users/<id>',methods=['PUT','GET','DELETE'])
def userById(id):

    if request.method == 'GET':
        return user_controllers.show(id)
    elif request.method == 'PUT':
        return user_controllers.update(id)
    elif request.method == 'DELETE':
        return user_controllers.delete(id)
    else:
        return user_controllers.index()
    

@app.route('/api/v1/notes',methods=['GET','POST'])
def note():
    if request.method != 'POST':
        return notes_controllers.index()
    else :
        return notes_controllers.create(request)
    
@app.route('/api/v1/notes/<id>',methods=['PUT','GET','DELETE'])
def noteById(id):

    if request.method == 'GET':
        return notes_controllers.show(id)
    elif request.method == 'PUT':
        return notes_controllers.update(id)
    elif request.method == 'DELETE':
        return notes_controllers.delete(id)
    else:
        return notes_controllers.index()
    

@app.route('/api/v1/notes/all/<id>',methods=['GET'])
def noteByUserId(id):
    return notes_controllers.showByUserId(id)