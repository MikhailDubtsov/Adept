from abc import ABC, abstractmethod

# TODO Написать 3 класса с документацией и аннотацией типов

class Furniture(ABC):
    """
    Абстрактный класс для описания мебели.

    Attributes:
        name (str): Название мебели.
        material (str): Материал, из которого изготовлена мебель.
        weight (float): Вес мебели в килограммах.

    Methods:
        get_description() -> str: Возвращает описание мебели.
        move(new_location: str) -> None: Перемещает мебель в новое место.
    """

    def __init__(self, name: str, material: str, weight: float):
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        self.name = name
        self.material = material
        self.weight = weight

    @abstractmethod
    def get_description(self) -> str:
        """Возвращает описание мебели."""
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Перемещает мебель в новое место.

        :param new_location: Новое местоположение.
        :return: None

        >>> chair = Chair("Стул", "Дерево", 5)
        >>> chair.move("Кухня")
        """
        ...

class Chair(Furniture):
    def get_description(self) -> str:
        """Возвращает описание стула."""
        return f"{self.name}, сделан из {self.material}, весит {self.weight} кг."

    def move(self, new_location: str) -> None:
        """Перемещает стул в новое местоположение."""
        print(f"{self.get_description()} перемещен в {new_location}.")

class Plant(ABC):
    """
    Абстрактный класс для описания растений.

    Attributes:
        species (str): Вид растения.
        height (float): Высота растения в сантиметрах.
        age (int): Возраст растения в годах.

    Methods:
        water(amount: float) -> None: Поливает растение.
        info() -> str: Возвращает информацию о растении.
    """

    def __init__(self, species: str, height: float, age: int):
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.height = height
        self.age = age

    @abstractmethod
    def water(self, amount: float) -> None:
        """
        Поливает растение.

        :param amount: Количество воды в миллилитрах.
        :return: None

        >>> succulent = Succulent("Кактус", 15, 2)
        >>> succulent.water(100)
        """
        ...

    @abstractmethod
    def info(self) -> str:
        """Возвращает информацию о растении."""
        ...

class Succulent(Plant):
    def water(self, amount: float) -> None:
        """Поливает суккулент."""
        print(f"{self.species} поливается {amount} мл воды.")

    def info(self) -> str:
        """Возвращает информацию о суккуленте."""
        return f"{self.species}, высота {self.height} см, возраст {self.age} лет."

class SocialMedia(ABC):
    """
    Абстрактный класс для описания социальных медиа.

    Attributes:
        name (str): Название платформы.
        age_limit (int): Возрастное ограничение.

    Methods:
        sign_up(user_age: int) -> bool: Регистрация пользователя.
        post(content: str) -> None: Размещение нового сообщения.
    """

    def __init__(self, name: str, age_limit: int):
        if age_limit < 0:
            raise ValueError("Возрастное ограничение должно быть неотрицательным.")
        self.name = name
        self.age_limit = age_limit

    @abstractmethod
    def sign_up(self, user_age: int) -> bool:
        """
        Регистрация пользователя.

        :param user_age: Возраст пользователя.
        :return: True если регистрация успешна, иначе False.

        >>> fb = Facebook("Facebook", 13)
        >>> fb.sign_up(15)  # Возраст пользователя подходит
        True
        >>> fb.sign_up(10)  # Возраст пользователя не подходит
        False
        """
        ...

    @abstractmethod
    def post(self, content: str) -> None:
        """Размещение нового сообщения."""
        ...

class Facebook(SocialMedia):
    def sign_up(self, user_age: int) -> bool:
        """Регистрация пользователя в Facebook."""
        return user_age >= self.age_limit

    def post(self, content: str) -> None:
        """Размещение нового сообщения на Facebook."""
        print(f"Сообщение опубликовано: {content}")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()