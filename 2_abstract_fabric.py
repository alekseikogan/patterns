# Абстрактная фабрика — это порождающий паттерн проектирования, который
# позволяет создавать семейства связанных объектов, не привязываясь к
# конкретным классам создаваемых объектов.

# Фишки:
# 1. Создает семейства объектов
# 2. Уносит логику создания объектов в отдельные классы
# 3. Заказчик выбирает лишь фабрику, а не объекты (взаимосвязанные или взаимозаменяемые)


from abc import ABC, abstractmethod


# Интерфейс для кнопок
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


# Кнопка для Windows
class WinButton(Button):
    def paint(self):
        print("Отрисовать кнопку в стиле Windows.")


# Кнопка для macOS
class MacButton(Button):
    def paint(self):
        print("Отрисовать кнопку в стиле macOS.")


# Интерфейс для чекбоксов
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Чекбокс для Windows
class WinCheckbox(Checkbox):
    def paint(self):
        print("Отрисовать чекбокс в стиле Windows.")


# Чекбокс для macOS
class MacCheckbox(Checkbox):
    def paint(self):
        print("Отрисовать чекбокс в стиле macOS.")


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Конкретная фабрика для Windows
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


# Конкретная фабрика для macOS
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Приложение, использующее фабрику
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None

    def create_ui(self):
        self.button = self.factory.create_button()

    def paint(self):
        self.button.paint()


# Конфигуратор приложения
class ApplicationConfigurator:
    @staticmethod
    def main():
        config = read_application_config_file()  # Предполагается, что эта функция определена

        if config['OS'] == "Windows":
            factory = WinFactory()
        elif config['OS'] == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
        app.create_ui()
        app.paint()


# Пример функции для чтения конфигурации (можно заменить реальной реализацией)
def read_application_config_file():
    return {'OS': 'Windows'}  # Пример возвращаемого значения


# Запуск конфигуратора
if __name__ == "__main__":
    ApplicationConfigurator.main()
