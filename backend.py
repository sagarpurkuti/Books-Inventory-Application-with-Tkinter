import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# def search(title="", author="", year="", isbn=""):
#     conn = sqlite3.connect("books.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
#     rows = cur.fetchall()
#     conn.close()
#     return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    query = "SELECT * FROM book WHERE 1=1"
    params = []

    if title:
        query += " AND title LIKE ?"
        params.append("%" + title + "%")
    if author:
        query += " AND author LIKE ?"
        params.append("%" + author + "%")
    if year:
        query += " AND year=?"
        params.append(year)
    if isbn:
        query += " AND isbn=?"
        params.append(isbn)

    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
# insert("the locals", "jhon", 19990, 123123456)
update(2,"The Moon","SAGAR",2002,132123)
# delete(3)
# print(view())
# print(search(author="SAGAR"))