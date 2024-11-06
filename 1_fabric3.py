from abc import ABC, abstractmethod

# Продукт
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретные продукты
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Результат работы ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Результат работы ConcreteProductB"

# Фабрика
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: {product.operation()}"

# Конкретные фабрики
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Клиентский код
def client_code(creator: Creator) -> None:
    print(creator.some_operation())

if __name__ == "__main__":
    print("Клиент: Работа с ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print(ConcreteCreatorA.operation)

    print("\nКлиент: Работа с ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
