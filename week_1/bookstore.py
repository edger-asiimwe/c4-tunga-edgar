from flask import Flask

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_all_books():
    return "All books are returned"


@app.route('/books/<int:book_id>', methods=['GET'])
def get_specific_book(book_id):
    return f"Book with id {book_id} is returned"


@app.route('/books/<int:book_id>', methods=['POST'])
def add_book(book_id):
    return f"Book with id {book_id} is added"


@app.route('/books', methods=['DELETE'])
def delete_all_books():
    return "All books are deleted"


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_specific_book(book_id):
    return f"Book with id {book_id} is deleted"


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    return f"Book with id {book_id} is updated"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
