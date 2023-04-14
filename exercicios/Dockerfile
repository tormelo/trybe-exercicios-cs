FROM mongo

COPY ./data/books.json /books.json

CMD mongoimport --host mongodb --db library --jsonArray --file /books.json
