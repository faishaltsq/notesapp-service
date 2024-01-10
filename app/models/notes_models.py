from app import db 
from datetime import datetime

class Note (db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text, index=True, unique=True)
    archived = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Note {}>'.format(self.title)
    

