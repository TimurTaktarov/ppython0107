import sqlite3

with sqlite3.connect('homework_db.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS books_shop(
    #         title TEXT NOT NULL,
    #         price INTEGER NOT NULL CHECK (price > 0),
    #         number_of_pages INTEGER NOT NULL CHECK (number_of_pages > 0)
    #     )
    # """
    # cursor.execute(query)

    # title = 'History'
    # price = '100'
    # number_of_pages = '241'
    # values = [title, price, number_of_pages]
    #
    # query = """
    #     INSERT INTO books_shop(title, price, number_of_pages)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # title = 'comic'
    # price = '95'
    # number_of_pages = '30'
    # values = [title, price, number_of_pages]
    #
    # query = """
    #     INSERT INTO books_shop(title, price, number_of_pages)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # values = (
    #     ('math', '50', '600'),
    #     ('History of Zelenskiy', '99', '50'),
    #     ('CR7', '250', '125'),
    # )
    #
    # query = """
    #     INSERT INTO books_shop(title, price, number_of_pages)
    #     VALUES (?, ?, ?)
    # """
    # cursor.executemany(query, values)

    # query = """
    #     SELECT title, price
    #     FROM books_shop
    #     WHERE price > 100
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=3))

    # query = """
    #     SELECT title, price
    #     FROM books_shop
    #     WHERE price
    #     ORDER BY price ASC
    #     LIMIT 3
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=10))

    # query = """
    #     SELECT title
    #     FROM books_shop
    #     WHERE title LIKE 'history%'
    #     LIMIT 2
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=10))

    # query = """
    #     ALTER TABLE books_shop
    #     ADD COLUMN barcode
    # """
    # cursor.execute(query)

    # query = """
    #     UPDATE books_shop
    #     SET
    #         barcode = :Barcode
    #     WHERE
    #         number_of_pages > 200
    # """
    # cursor.execute(query, {'Barcode': '0-00077'})
    #
    # query = """
    #     DELETE FROM books_shop
    #     WHERE price = 100
    # """
    # cursor.execute(query)
