from app.models.notes_models import Note
from app import response,app,db
from flask import request

def index():
    try :
        notes = Note.query.all()
        data = multiTransform(notes)

        return response.success_response(data,"success")
    
    except Exception as e:
        return response.bad_request_response([],str(e))
    
def show(id):
    try :
        note = Note.query.filter_by(id=id).first()
        if not note:
            return response.not_found_response([], 'note not found')

        data = transform(note)
        return response.success_response(data, "success")
    except Exception as e:
        return response.bad_request_response([], str(e))
    
def create(request):
    try :
        title = request.json['title']
        description = request.json['description']
        archived = request.json['archived']
        user_id = request.json['user_id']

        note = Note(title=title, description=description,archived=archived,user_id=user_id)
        db.session.add(note)
        db.session.commit()

        print("ini tuh jalan")
        return response.success_response(transform(note), "success")
    
    except Exception as e:
        print(str(e))
        return response.bad_request_response([], str(e))
    

def update(id):
    try :
        title = request.json['title']
        description = request.json['description']
        archived = request.json['archived']
        user_id = request.json['user_id']

        note = Note.query.filter_by(id=id).first()
        if not note:
            return response.not_found_response([], 'note not found')
        
        note.title = title
        note.description = description
        note.archived = archived
        note.user_id = user_id

        print("ini tuh jalan")
        db.session.commit()

        return response.success_response(transform(note), "success")
    
    except Exception as e:
        print(str(e))
        return response.bad_request_response([], str(e))
    

def delete(id):
    try :
        note = Note.query.filter_by(id=id).first()
        if not note:
            return response.not_found_response([], 'note not found')

        db.session.delete(note)
        db.session.commit()

        return response.success_response(None, "success")
    
    except Exception as e:
        return response.bad_request_response([], str(e))
    
def showByUserId(id):
    try :
        notes = Note.query.filter_by(user_id=id).all()
        if not notes:
            return response.not_found_response([], 'note not found')

        data = multiTransform(notes)
        return response.success_response(data, "success")
    except Exception as e:
        return response.bad_request_response([], str(e))


def transform(note):
    data = {
        "id" : note.id,
        "title" : note.title,
        "description" : note.description,
        "archived" : note.archived,
        "user_id" : note.user_id,
    }

    return data

def changeArchiveStatus(id):
    try :
        note = Note.query.filter_by(id=id).first()
        if not note:
            return response.not_found_response([], 'note not found')

        note.archived = not note.archived
        db.session.commit()

        return response.success_response(None, "success")
    except Exception as e:
        return response.bad_request_response([], str(e))

def multiTransform(notes):
    data = []
    for i in notes:
        data.append(transform(i))

    return data
