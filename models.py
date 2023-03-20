from datetime import datetime
from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    on_shelf = db.Column(db.Boolean, default=True)
    borrowed_by = db.Column(db.String(100))
    borrow_date = db.Column(db.DateTime)

    def borrow(self, user):
        self.on_shelf = False
        self.borrowed_by = user
        self.borrow_date = datetime.utcnow()

    def return_book(self):
        self.on_shelf = True
        self.borrowed_by = None
        self.borrow_date = None
