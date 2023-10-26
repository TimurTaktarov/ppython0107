import sqlite3
from pprint import pprint

with sqlite3.connect('hwssqqll_db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # query = """
    #     CREATE TABLE IF NOT EXISTS books(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     title TEXT NOT NULL,
    #     FOREIGN KEY (id) REFERENCES author(id)
    #     )
    # """
    # cursor.execute(query)
    #
    # query = """
    #     CREATE TABLE IF NOT EXISTS author(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     name TEXT NOT NULL
    #     )
    # """
    # cursor.execute(query)

    # values = [3, 'Amazon advices']
    # query = """
    #     INSERT INTO books(id, title)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)

    # query = """
    #     SELECT title, name
    #     FROM books
    #     LEFT JOIN author
    #     ON books.id = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    query = """
        SELECT 
        FROM books
        FULL JOIN author
        ON books.id = author.id    
    """
    result = cursor.execute(query)
    pprint(result.fetchall())
