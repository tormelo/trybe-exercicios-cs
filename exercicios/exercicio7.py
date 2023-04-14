from pymongo import MongoClient


with MongoClient() as client:
    db = client.library

    search_result = db.books.aggregate(
        [
            {"$match": {"status": "PUBLISH"}},
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
        ]
    )

    for category in search_result:
        print(category["_id"], category["count"], sep=": ")
