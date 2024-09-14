from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory storage for books
books = [
    {"id": "1", "title": "1984", "author": "George Orwell", "price": "9.99", "category": "Dystopian"},
    {"id": "2", "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": "7.99", "category": "Classic Fiction"}
]

# GET /books - Retrieve all books
@app.route('/api/bookstore/books', methods=['GET'])
def get_books():
    return jsonify({'books': books}), 200

# GET /books/<id> - Retrieve a book by its ID
@app.route('/api/bookstore/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({'book': book}), 200
    return jsonify({'message': 'Book not found'}), 404

# POST /books - Add a new book
@app.route('/api/bookstore/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': data['id'],
        'title': data['title'],
        'author': data['author'],
        'price': data['price'],
        'category': data['category']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added successfully!', 'book': new_book}), 201

# PUT /books/<id> - Update a book by its ID
@app.route('/api/bookstore/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book['title'] = data.get('title', book['title'])
        book['author'] = data.get('author', book['author'])
        book['price'] = data.get('price', book['price'])
        book['category'] = data.get('category', book['category'])
        return jsonify({'message': 'Book updated successfully!', 'book': book}), 200
    return jsonify({'message': 'Book not found'}), 404

# DELETE /books/<id> - Delete a book by its ID
@app.route('/api/bookstore/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
