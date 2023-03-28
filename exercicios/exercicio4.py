import json
import csv


def get_book_count_by_category(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
    return categories


def get_categories_percent(book_count_by_category, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count_by_category.items()
    ]


if __name__ == "__main__":
    with open("exercicios/data/books.json") as file:
        books = json.load(file)

    book_count_by_category = get_book_count_by_category(books)
    categories_percent = get_categories_percent(
        book_count_by_category, len(books)
    )

    with open("exercicios/data/report.csv", "w") as file:
        header = ["categoria", "porcentagem"]
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(categories_percent)
