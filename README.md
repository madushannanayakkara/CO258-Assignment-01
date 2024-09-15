# CO258-Assignment-01 (Flask Bookstore Service)

This is a simple RESTful service implemented in Flask for managing a bookstore. The service allows you to perform CRUD (Create, Read, Update, Delete) operations on books.

## Features

- **Get All Books**: Retrieve a list of all available books.
- **Get a Book by ID**: Retrieve details of a specific book by its ID.
- **Add a New Book**: Add a new book to the bookstore.
- **Update a Book**: Update the details of an existing book by its ID.
- **Delete a Book**: Delete a book from the bookstore by its ID.

## API Endpoints

- **GET /api/bookstore/books**: Retrieve all books.
- **GET /api/bookstore/books/{id}**: Retrieve a specific book by ID.
- **POST /api/bookstore/books**: Add a new book.
- **PUT /api/bookstore/books/{id}**: Update an existing book by ID.
- **DELETE /api/bookstore/books/{id}**: Delete a book by ID.

## Data Structure

Each book has the following attributes:

```json
{
    "id": "string",
    "title": "string",
    "author": "string",
    "price": "string",
    "category": "string"
}
```
