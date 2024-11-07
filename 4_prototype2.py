# Паттерн проектирования "Прототип" (Prototype) используется для создания
# объектов на основе существующих объектов, а не через классическое создание
# новых экземпляров. Это # может быть полезно в ситуациях, когда создание
# нового объекта требует значительных затрат или сложных операций.

import copy


class HumanPrototype:
    """Базовый класс прототипа."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def clone(self):
        return copy.deepcopy(self)


class Men(HumanPrototype):
    def __init__(self, name, surname, attribute):
        super().__init__(name, surname)
        self.attribute = attribute

    def __str__(self):
        return f"Прототип Мужчины с атрибутом: {self.attribute}"


class Women(HumanPrototype):
    def __init__(self, name, surname, attribute):
        super().__init__(name, surname)
        self.attribute = attribute

    def __str__(self):
        return f"Прототип Женщины с атрибутом: {self.attribute}"


# Клиентский код
if __name__ == "__main__":
    # Создаем экземпляры прототипов
    man_proto = Men("Иван", "Иванов", "Сильный очень")
    women_proto = Women("Анна", "Петрова", "Красивая дама")

    # Клонируем объекты
    clone_a = man_proto.clone()
    clone_b = women_proto.clone()
    print(clone_a, clone_a.name, clone_a.surname)
    print(clone_b, clone_b.name, clone_b.surname)

    # Изменяем атрибут клона
    clone_a.attribute = "Мужчина стал слабый"
    clone_b.attribute = "И девушка некрасивой"
    print(clone_a)
    print(clone_b)
