BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# Реализация класса Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Реализация класса Library
class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        Args:
            books: Список книг (по умолчанию None, создается пустой список)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        Returns:
            int: ID для новой книги
        """
        if not self.books:  # Если список книг пуст
            return 1
        else:
            # Получаем ID последней книги и увеличиваем на 1
            last_book = self.books[-1]
            return last_book.id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её ID.

        Args:
            book_id: Идентификатор книги

        Returns:
            int: Индекс книги в списке

        Raises:
            ValueError: Если книги с указанным ID не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        # Если книга не найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1