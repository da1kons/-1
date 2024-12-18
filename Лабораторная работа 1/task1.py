import doctest

class Car:
    def __init__(self, brand: str, model: str, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param fuel_capacity: Объем топливного бака (литры)

        Примеры:
        >>> car = Car("Toyota", "Corolla", 50.0)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд автомобиля должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")

        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0.0

    def refuel(self, amount: float) -> None:
        """
        Заправить автомобиль.

        :param amount: Количество топлива для заправки (литры)

        :raise ValueError: Если количество топлива превышает объем бака

        Примеры:
        >>> car = Car("Toyota", "Corolla", 50.0)
        >>> car.refuel(20.0)
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Количество топлива должно быть положительным числом")
        if self.fuel_level + amount > self.fuel_capacity:
            raise ValueError("Нельзя заправить больше, чем объем бака")
        self.fuel_level += amount

    def drive(self, distance: float) -> None:
        """
        Ехать на автомобиле.

        :param distance: Расстояние для поездки (км)

        :raise ValueError: Если топлива недостаточно для поездки

        Примеры:
        >>> car = Car("Toyota", "Corolla", 50.0)
        >>> car.refuel(10.0)
        >>> car.drive(50.0)
        """
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        required_fuel = distance * 0.1  # Расход топлива: 10 км/литр
        if self.fuel_level < required_fuel:
            raise ValueError("Недостаточно топлива для поездки")
        self.fuel_level -= required_fuel

class Phone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param brand: Бренд телефона
        :param model: Модель телефона
        :param battery_capacity: Емкость аккумулятора (мАч)

        Примеры:
        >>> phone = Phone("Apple", "iPhone 13", 4000)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд телефона должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.battery_level = battery_capacity

    def charge(self, amount: int) -> None:
        """
        Зарядить телефон.

        :param amount: Количество заряда для добавления (мАч)

        :raise ValueError: Если количество заряда превышает емкость аккумулятора

        Примеры:
        >>> phone = Phone("Apple", "iPhone 13", 4000)
        >>> phone.charge(500)
        >>> phone.battery_level
        4000
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Количество заряда должно быть положительным числом")
        self.battery_level = min(self.battery_capacity, self.battery_level + amount)

    def make_call(self, duration: int) -> None:
        """
        Совершить звонок.

        :param duration: Продолжительность звонка (минуты)

        :raise ValueError: Если заряда недостаточно для звонка

        Примеры:
        >>> phone = Phone("Apple", "iPhone 13", 4000)
        >>> phone.make_call(10)
        """
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Продолжительность звонка должна быть положительным числом")
        required_battery = duration * 10  # Расход заряда: 10 мАч/минута
        if self.battery_level < required_battery:
            raise ValueError("Недостаточно заряда для звонка")
        self.battery_level -= required_battery

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read_pages(self, num_pages: int) -> None:
        """
        Читать страницы книги.

        :param num_pages: Количество читаемых страниц

        :raise ValueError: Если количество страниц превышает оставшееся число страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read_pages(50)
        """
        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        if self.current_page + num_pages > self.pages:
            raise ValueError("Нельзя прочитать больше, чем осталось страниц")
        self.current_page += num_pages

    def bookmark_page(self) -> int:
        """
        Установить закладку на текущую страницу.

        :return: Номер текущей страницы

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read_pages(100)
        >>> book.bookmark_page()
        100
        """
        return self.current_page

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
