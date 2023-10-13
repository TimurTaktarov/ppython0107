import pymongo
from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      f'@cluster1.ss7fmb4.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.homeworkDB
fantasy_books_coll = db.fantasy_books
school_books_coll = db.school_books

fantasy_books_coll.insert_one(
    {'title': 'Game of Thrones', 'price': 499, 'graduation year': 1996, 'pages': 864}
)

school_books_coll.insert_one(
    {'title': 'History', 'class': 2014, 'pages': 228}
)
school_books_coll.insert_one(
    {'title': 'Math', 'class': 2020, 'pages': 230}
)
school_books_coll.insert_one(
    {'title': 'Biologie', 'class': 2016, 'pages': 170}
)
school_books_coll.insert_one(
    {'title': 'Physik', 'class': 2022, 'pages': 218}
)
school_books_coll.insert_one(
    {'title': 'Geography', 'class': 2017, 'pages': 146}
)
school_books_coll.insert_one(
    {'title': 'Computer Science', 'class': 2019, 'pages': 300}
)

query = {'title': 'History'}
result = school_books_coll.find_one(query)
print(result)

query = {'title': 'Game of Thrones'}
operation = {'$inc': {'price': 56}}
result2 = fantasy_books_coll.update_one(query, operation)

query = {'title': 'Game of Thrones'}
fantasy_books_coll.delete_one(query)

query = {'class': {'$lt': 2020}}
school_books_coll.delete_many(query)

# fantasy_books_coll.drop()
# school_books_coll.drop()
