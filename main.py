from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define models
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory storage for demonstration purposes
books = []

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    # Check if the book with the same ID already exists
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books.append(book)
    return book

@app.get("/books/", response_model=List[Book])
async def get_books():
    return books

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    for index, b in enumerate(books):
        if b.id == book_id:
            books[index] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

class Inventory(BaseModel):
    book_id: int
    quantity: int

inventories = []

@app.post("/inventories/", response_model=Inventory)
async def create_inventory(inventory: Inventory):
    inventories.append(inventory)
    return inventory

@app.get("/inventories/", response_model=List[Inventory])
async def get_inventories():
    return inventories




# from fastapi import FastAPI
# from book_catalog.app.main import app as book_catalog_app
# from inventory_management.app.main import app as inventory_management_app

# app = FastAPI()

# # Mounting each microservice's FastAPI app under different routes
# app.mount("/book_catalog", book_catalog_app)
# app.mount("/inventory_management", inventory_management_app)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

