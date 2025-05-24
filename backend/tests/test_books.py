# backend/tests/test_books.py
def test_create_book(client, admin_token):
    response = client.post(
        "/api/books/",
        json={"title": "Test Book", "author": "Author", "year": 2023},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"