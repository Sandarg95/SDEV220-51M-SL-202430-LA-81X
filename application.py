from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class BOOK(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.year} - {self.description}"


@app.route('/')
def index():
    return 'Welcome to our Library!'


@app.route('/books')
def get_books():
    books = BOOK.query.all()

    output = []
    for book in books:
        book_data = {'title': book.title, 'author': book.author, 'year': book.year, 'description': book.description}
        output.append(book_data)

    return {"books": output}


@app.route('/books/<id>')
def get_book(id):
    book = BOOK.query.get_or_404(id)
    return {"title": book.title, "author": book.author, "year": book.year, "description": book.description}


@app.route('/books', methods=['POST'])
def add_book():
    book = BOOK(title=request.json['title'],
                author=request.json['author'],
                year=request.json['year'],
                description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_books(id):
    books = BOOK.query.get(id)
    if books is None:
        return {"error": "not found"}
    db.session.delete(books)
    db.session.commit()
    return {"message": "Yeeeee, book deleted !@"}