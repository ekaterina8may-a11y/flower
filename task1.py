class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер для названия (только чтение)"""
        return self._name

    @property
    def author(self):
        """Геттер для автора (только чтение)"""
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги, наследуется от Book"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        """Геттер для количества страниц"""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Сеттер с проверкой количества страниц"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} ({self.pages} стр.)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """Геттер для длительности"""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Сеттер с проверкой длительности"""
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        """Форматируем длительность в часы и минуты"""
        hours = int(self.duration // 60)
        minutes = int(self.duration % 60)

        if hours > 0:
            time_str = f"{hours} ч {minutes} мин"
        else:
            time_str = f"{minutes} мин"

        return f"{super().__str__()} (длительность: {time_str})"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования с разными книгами
if __name__ == "__main__":
    # Бумажные книги
    paper_books = [
        PaperBook("Мастер и Маргарита", "Михаил Булгаков", 480),
        PaperBook("Преступление и наказание", "Федор Достоевский", 672),
        PaperBook("Сто лет одиночества", "Габриэль Гарсиа Маркес", 432),
        PaperBook("Над пропастью во ржи", "Джером Сэлинджер", 288),
        PaperBook("Портрет Дориана Грея", "Оскар Уайльд", 320)
    ]

    # Аудиокниги
    audio_books = [
        AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 510.5),
        AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 98.0),
        AudioBook("Три товарища", "Эрих Мария Ремарк", 720.0),
        AudioBook("Алхимик", "Пауло Коэльо", 240.5),
        AudioBook("Шантарам", "Грегори Дэвид Робертс", 1260.0)
    ]

    print("=" * 50)
    print("БУМАЖНЫЕ КНИГИ:")
    print("=" * 50)
    for book in paper_books:
        print(str(book))
        print(f"  repr: {repr(book)}")
        print()

    print("=" * 50)
    print("АУДИОКНИГИ:")
    print("=" * 50)
    for book in audio_books:
        print(str(book))
        print(f"  repr: {repr(book)}")
        print()

    # Демонстрация неизменяемости названия и автора
    print("=" * 50)
    print("ПРОВЕРКА НЕИЗМЕНЯЕМОСТИ:")
    print("=" * 50)

    book = paper_books[0]
    print(f"Пытаемся изменить название книги '{book.name}'...")
    try:
        book.name = "Новое название"
    except AttributeError as e:
        print(f"  Ошибка: {e}")

    # Демонстрация валидации
    print("\nПРОВЕРКА ВАЛИДАЦИИ:")
    print("-" * 30)

    print("Пытаемся установить отрицательное количество страниц...")
    try:
        book.pages = -100
    except ValueError as e:
        print(f"  Ошибка: {e}")

    print("\nПытаемся установить длительность строкой...")
    try:
        audio_books[0].duration = "два часа"
    except TypeError as e:
        print(f"  Ошибка: {e}")