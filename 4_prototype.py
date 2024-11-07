# Паттерн проектирования "Прототип" (Prototype) используется для создания
# объектов на основе существующих объектов, а не через классическое создание
# новых экземпляров. Это # может быть полезно в ситуациях, когда создание
# нового объекта требует значительных затрат или сложных операций.

import copy


class Prototype:
    """Базовый класс прототипа."""

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototypeA(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return f"ConcretePrototypeA with attribute: {self.attribute}"


class ConcretePrototypeB(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return f"ConcretePrototypeB with attribute: {self.attribute}"


# Клиентский код
if __name__ == "__main__":
    # Создаем экземпляры прототипов
    prototype_a = ConcretePrototypeA("A1")
    prototype_b = ConcretePrototypeB("B1")

    # Клонируем объекты
    clone_a = prototype_a.clone()
    clone_b = prototype_b.clone()
    print(clone_a)  # Вывод: ConcretePrototypeA with attribute: A1
    print(clone_b)  # Вывод: ConcretePrototypeB with attribute: B1

    # Изменяем атрибут клона
    clone_a.attribute = "A2"
    clone_b.attribute = "B2"
    print(clone_a)  # Вывод: ConcretePrototypeA with attribute: A2
    print(clone_b)  # Вывод: ConcretePrototypeB with attribute: B2
