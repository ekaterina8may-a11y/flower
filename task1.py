import doctest
from typing import Union, Optional, List


class Dog:
    """
    Класс, описывающий собаку.

    Атрибуты:
        name (str): Кличка собаки.
        age (float): Возраст собаки в годах.
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: float, breed: str) -> None:
        """
        Инициализирует экземпляр класса Dog.

        Args:
            name: Кличка собаки (не может быть пустой строкой).
            age: Возраст собаки (должен быть положительным числом).
            breed: Порода собаки (не может быть пустой строкой).

        Raises:
            ValueError: Если name или breed - пустые строки, или age <= 0.

        >>> dog = Dog("Модя", 3.5, "Спаниель")
        >>> dog.name
        'Модя'
        >>> dog.age
        3.5
        >>> dog.breed
        'Спаниель'
        """
        if not name or not isinstance(name, str):
            raise ValueError("Кличка должна быть непустой строкой.")
        if not breed or not isinstance(breed, str):
            raise ValueError("Порода должна быть непустой строкой.")
        if not isinstance(age, (int, float)) or age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")

        self.name: str = name
        self.age: float = age
        self.breed: str = breed

    def bark(self) -> str:
        """
        Имитирует лай собаки.

        Returns:
            Строка с звуком лая.

        >>> dog = Dog("Бим", 2, "Дворняжка")
        >>> dog.bark()
        'Гав-гав!'
        """
        return "Гав-гав!"

    def eat(self, food_type: str) -> str:
        """
        Имитирует процесс еды.

        Args:
            food_type: Тип еды (корм, мясо, каша и т.д.).

        Returns:
            Реакция собаки на предложенную еду.

        >>> dog = Dog("Лаки", 1.5, "Такса")
        >>> dog.eat("кость")
        'Лаки с удовольствием ест кость'
        """
        return f"{self.name} с удовольствием ест {food_type}"

    def sleep(self, hours: float) -> str:
        """
        Имитирует сон собаки.

        Args:
            hours: Количество часов сна.

        Returns:
            Сообщение о том, сколько спала собака.

        >>> dog = Dog("Тузик", 3, "Овчарка")
        >>> dog.sleep(8)
        'Тузик спит 8 часов. Хороших снов!'
        """
        return f"{self.name} спит {hours} часов. Хороших снов!"


class Headphones:
    """
    Класс, описывающий наушники.

    Атрибуты:
        brand (str): Бренд наушников.
        is_wireless (bool): Беспроводные ли наушники.
        battery_level (Optional[int]): Уровень заряда батареи (для беспроводных) в процентах.
        volume (int): Текущий уровень громкости.
    """

    def __init__(self, brand: str, is_wireless: bool, battery_level: Optional[int] = None) -> None:
        """
        Инициализирует экземпляр класса Headphones.

        Args:
            brand: Бренд наушников (не может быть пустой строкой).
            is_wireless: True - беспроводные, False - проводные.
            battery_level: Уровень заряда (0-100). Обязателен, если is_wireless=True.

        Raises:
            ValueError: Если brand - пустая строка,
                       или battery_level вне диапазона [0, 100],
                       или battery_level не указан для беспроводных наушников.

        >>> hp = Headphones("Sony", True, 75)
        >>> hp.brand
        'Sony'
        >>> hp.is_wireless
        True
        >>> hp.battery_level
        75
        """
        if not brand or not isinstance(brand, str):
            raise ValueError("Бренд должен быть непустой строкой.")

        if is_wireless:
            if battery_level is None:
                raise ValueError("Для беспроводных наушников необходимо указать уровень заряда.")
            if not isinstance(battery_level, int) or not (0 <= battery_level <= 100):
                raise ValueError("Уровень заряда должен быть целым числом от 0 до 100.")
        else:
            battery_level = None

        self.brand: str = brand
        self.is_wireless: bool = is_wireless
        self.battery_level: Optional[int] = battery_level
        self.volume: int = 50  # начальная громкость

    def play_track(self, track_name: str) -> str:
        """
        Имитирует воспроизведение трека.

        Args:
            track_name: Название трека.

        Returns:
            Сообщение о воспроизведении.

        >>> hp = Headphones("JBL", True, 80)
        >>> hp.play_track("Bohemian Rhapsody")
        'Играет трек: Bohemian Rhapsody'
        """
        return f"Играет трек: {track_name}"

    def set_volume(self, level: int) -> str:
        """
        Устанавливает уровень громкости.

        Args:
            level: Уровень громкости (от 0 до 100).

        Returns:
            Сообщение об установленной громкости.

        Raises:
            ValueError: Если level вне диапазона [0, 100].

        >>> hp = Headphones("Sony", True, 60)
        >>> hp.set_volume(75)
        'Громкость установлена на 75'
        >>> hp.volume
        75
        """
        if not isinstance(level, int) or not (0 <= level <= 100):
            raise ValueError("Громкость должна быть целым числом от 0 до 100.")
        self.volume = level
        return f"Громкость установлена на {self.volume}"

    def check_battery(self) -> str:
        """
        Проверяет уровень заряда батареи.

        Returns:
            Сообщение о состоянии батареи.

        >>> hp_wireless = Headphones("Bose", True, 30)
        >>> hp_wireless.check_battery()
        'Уровень заряда: 30%'
        >>> hp_wired = Headphones("Audio-Technica", False)
        >>> hp_wired.check_battery()
        'Проводные наушники, заряд не требуется.'
        """
        if self.is_wireless and self.battery_level is not None:
            return f"Уровень заряда: {self.battery_level}%"
        return "Проводные наушники, заряд не требуется."


class Book:
    """
    Класс, описывающий книгу.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Общее количество страниц.
        current_page (int): Текущая открытая страница.
    """

    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Инициализирует экземпляр класса Book.

        Args:
            title: Название книги (не может быть пустой строкой).
            author: Автор книги (не может быть пустой строкой).
            pages: Количество страниц (должно быть положительным целым числом).

        Raises:
            ValueError: Если title или author - пустые строки,
                       или pages не является положительным целым числом.

        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        >>> book.title
        'Война и мир'
        >>> book.author
        'Лев Толстой'
        >>> book.pages
        1300
        """
        if not title or not isinstance(title, str):
            raise ValueError("Название должно быть непустой строкой.")
        if not author or not isinstance(author, str):
            raise ValueError("Автор должен быть непустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.current_page: int = 1  # начинаем с первой страницы

    def read_page(self, page_number: int) -> str:
        """
        Открывает указанную страницу.

        Args:
            page_number: Номер страницы для чтения (от 1 до pages).

        Returns:
            Сообщение о том, какая страница открыта.

        Raises:
            IndexError: Если page_number вне допустимого диапазона.

        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.read_page(42)
        'Читаем страницу №42'
        >>> book.current_page
        42
        """
        if not isinstance(page_number, int) or page_number < 1 or page_number > self.pages:
            raise IndexError(f"Страница должна быть от 1 до {self.pages}")
        self.current_page = page_number
        return f"Читаем страницу №{self.current_page}"

    def next_page(self) -> str:
        """
        Перелистывает на следующую страницу.

        Returns:
            Сообщение о новой текущей странице.

        Raises:
            IndexError: Если текущая страница последняя.

        >>> book = Book("Мастер и Маргарита", "Булгаков", 400)
        >>> book.read_page(5)
        'Читаем страницу №5'
        >>> book.next_page()
        'Теперь на странице 6'
        """
        if self.current_page >= self.pages:
            raise IndexError("Это последняя страница книги")
        self.current_page += 1
        return f"Теперь на странице {self.current_page}"

    def get_info(self) -> dict:
        """
        Возвращает информацию о книге.

        Returns:
            Словарь с названием, автором и количеством страниц.

        >>> book = Book("Преступление и наказание", "Ф.М. Достоевский", 400)
        >>> info = book.get_info()
        >>> info['author']
        'Ф.М. Достоевский'
        >>> info['current_page']
        1
        """
        return {
            'title': self.title,
            'author': self.author,
            'pages': self.pages,
            'current_page': self.current_page
        }


if __name__ == "__main__":
    # Запуск doctest для проверки примеров из документации
    doctest.testmod(verbose=True)

    # Демонстрация работы классов
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ")
    print("=" * 50)

    # Демонстрация Dog
    print("\n🐕 Класс Dog:")
    dog = Dog("Модя", 3.5, "Спаниель")
    print(dog.bark())
    print(dog.eat("мясо"))
    print(dog.sleep(8))

    # Демонстрация Headphones
    print("\n🎧 Класс Headphones:")
    hp = Headphones("Sony", True, 75)
    print(hp.play_track("Imagine"))
    print(hp.set_volume(60))
    print(hp.check_battery())

    # Демонстрация Book
    print("\n📚 Класс Book:")
    book = Book("Война и мир", "Лев Толстой", 1300)
    print(book.read_page(100))
    print(book.next_page())
    print(f"Информация о книге: {book.get_info()}")