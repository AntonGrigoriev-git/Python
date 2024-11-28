from typing import Dict, List


class BookDetails():
    _list_object = {}

    def __new__(cls, title, author, genre, year, category):
        key = (title, author, genre, year, category)
        if key not in cls._list_object:
            cls._list_object[key] = super().__new__(cls)
            cls._list_object[key].title = title
            cls._list_object[key].author = author
            cls._list_object[key].genre = genre
            cls._list_object[key].year = year
            cls._list_object[key].category = category
        return cls._list_object[key]

    def __repr__(self):
        return f'{self.title} by {self.author} ({self.year}). [{self.genre}, {self.category}]'


class Book():
    def __init__(self, details: BookDetails, rating: float):
        self.details = details
        self.rating = rating

    def __repr__(self):
        return f'{self.details} (Rating: {self.rating})'


class BookSearch():
    def __init__(self, books: List[Book]):
        self.books = books

    def search_by_author(self, author:str)->List[Book]:
        return [book for book in self.books if book.details.author.strip().lower() == author.strip().lower()]

    def search_by_genre(self, genre:str)->List[Book]:
        return [book for book in self.books if book.details.genre.strip().lower() == genre.strip().lower()]

    def search_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if book.details.title.strip().lower() == title.strip().lower()]


class UserPreferences:
    def __init__(self):
        self.history = {}

    def add_to_history(self, user_id:int, genre:str):
        if user_id not in self.history:
            self.history[user_id] = []
        self.history[user_id].append(genre)

    def get_preferences(self, user_id: int)->List[str]:
        if user_id not in self.history:
            return []
        genre_count = {}
        for genre in self.history[user_id]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
        return sorted(genre_count, key=genre_count.get, reverse=True)


class Recommendate():
    def __init__(self, books: List[Book], u_p: UserPreferences):
        self.books = books
        self.u_p = u_p

    def recomendate(self, user_id, limit: int = 5)->List[Book]:
        prefer_genre = self.u_p.get_preferences(user_id)
        recommendations  = []
        for genre in prefer_genre:
            recommendations.extend(
              sorted(
                  [book for book in self.books if book.details.genre == genre],
                  key=lambda x: x.rating,
                  reverse=True,
            ))
        return recommendations[:limit]


class Facade():
    def __init__(self, books: List[Book]):
        self.book_search = BookSearch(books)
        self.u_p = UserPreferences()
        self.recomend = Recommendate(books, self.u_p)

    def add_user_history(self, user_id:int, genre:str):
        self.u_p.add_to_history(user_id, genre)

    def recommend_books(self, user_id:int, limit: int = 5)->List[Book]:
        return self.recomend.recomendate(user_id, limit )
    
    def get_all_books(self) -> List[Book]:
        return self.book_search.books
    
    def search_books_by_author(self, author: str) -> List[Book]:
        return self.book_search.search_by_author(author)
    
    def search_books_by_genre(self, genre: str) -> List[Book]:
        return self.book_search.search_by_genre(genre)
    
    def search_books_by_title(self, title: str) -> List[Book]:
        return self.book_search.search_by_title(title)


books = [
    Book(BookDetails('A', '1', 'Fantasy', 1999, 'Fiction'), 4.5),
    Book(BookDetails('B', '2', 'Sci-Fi', 1956, 'Fiction'), 4.8),
    Book(BookDetails('C', '1', 'Fantasy', 1999, 'Fiction'), 4.2),
    Book(BookDetails('D', '3', 'Horror', 1999, 'Fiction'), 4.0),
    Book(BookDetails('E', '2', 'Fantasy', 1999, 'Fiction'), 3.9)
]

facade = Facade(books)
facade.add_user_history(user_id=1, genre='Fantasy')
facade.add_user_history(user_id=1, genre='Fantasy')
facade.add_user_history(user_id=1, genre='Sci-Fi')
facade.add_user_history(user_id=2, genre='Horror')

print('User 1')
print(facade.recommend_books(user_id=1))
print('User 2')
print(facade.recommend_books(user_id=2))

print(facade.search_books_by_author(author='1'))
print(facade.search_books_by_genre(genre='Fantasy'))
print(facade.search_books_by_title(title='A'))

all_books = facade.get_all_books()

def display_books(books: List[Book]):
    if not books:
        print("Books not found")
    else:
        for num, book in enumerate(books, 1):
            print(f"{num}. {book}")

display_books(all_books)