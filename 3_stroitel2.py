# Продукт
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def show(self) -> None:
        print("Продукт создан с частями:", ", ".join(self.parts))


# Строитель
class Builder:
    def build_part_a(self) -> None:
        pass

    def build_part_b(self) -> None:
        pass

    def get_product(self) -> Product:
        pass


# Конкретный строитель
class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self) -> None:
        self.product.add("Часть A")

    def build_part_b(self) -> None:
        self.product.add("Часть B")

    def get_product(self) -> Product:
        return self.product


# Директор
class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def construct_minimal_product(self) -> None:
        self.builder.build_part_a()

    def construct_full_product(self) -> None:
        self.builder.build_part_a()
        self.builder.build_part_b()


# Клиентский код
if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    print("Создание минимального продукта:")
    director.construct_minimal_product()
    product = builder.get_product()
    product.show()

    print("\nСоздание полного продукта:")
    builder = ConcreteBuilder()  # Создаем новый строитель
    director = Director(builder)
    director.construct_full_product()
    product = builder.get_product()
    product.show()
