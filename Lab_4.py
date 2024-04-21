if __name__ == "__main__":
    # Write your solution here
    pass
class ConstructionElement:
    "Базовый класс - конструктивный элемент"
    def __init__(self, material: str, color: str):
        """

        :param material: Название материала
        :param color: Название цвета
        Пример
        >>> overlap = ConstructionElement('Бетон', 'Серый')
        """
        if isinstance(material, str):
            self.material = material
        else:
            raise TypeError("material должен быть типа str")

        if isinstance(color, str):
            self.color = color
        else:
            raise TypeError("color должен быть типа str")

    def __str__(self) -> str:
        return f"Конструктивный элемент сделан из материала: {self.material} и имеет {self.color} цвет."
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(material={self.material!r}, color={self.color!r})"

    def size(self, a: float, b: float) -> float:
        """
        Указываются размеры конструктивного элемента, в результате вычичсляется площадь элемента
        :param a: Длина, [м]
        :param b: Ширина, [м]
        """
        square = a*b
        return f"Площадь равна {square}"

class Wall(ConstructionElement):
    "Дочерний класс - стена"
    def __init__(self, material: str, color: str, wall_type: str):
        super().__init__(material, color)
        """

        :param material: Название материала
        :param color: Название цвета
        :param wall_type: Тип стены
        Пример:
        >>> wall1 = Wall('Дерево', 'Коричневый')
        """
        if isinstance(wall_type, str):
            self.wall_type = wall_type
        else:
            raise TypeError("wall_type должен быть типа str")

    def __str__(self) -> str:
        return f"Стена сделан из материала {self.material}, имеет цвет {self.color} и тип - {self.wall_type}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(material={self.material!r}, color={self.color!r}, wall_type={self.wall_type!r})"

    def size(self, a: float, b: float, c: float):
        """
        Выисление площади и объема стены
        :param c: высота
        """
        square = super().size(a, b)
        volume = a*b*c
        return f"{square}, объем равен {volume}"

    def bearing_capacity(self, bearing_capacity: float):
        """
        Параметр мощности прибора
        :bearing_capacity: Несущая способность, [МПа]
        Пример
         >>> wall1 = Wall('Кирпич', 'Красный', 'Несущая')
         >>> wall1.bearing_capacity(100)
        """
