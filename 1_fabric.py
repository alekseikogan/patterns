# Фабричный метод — это порождающий паттерн проектирования, который
# определяет общий интерфейс для создания объектов в суперклассе,
# позволяя подклассам изменять тип создаваемых объектов.

# Паттерн Фабричный метод предлагает создавать объекты не напрямую,
# используя оператор new, а через вызов особого фабричного метода.

# SOLID:
# S - логика создания в отдельном модуле
# D - метод и возвращаемый объект является абстрактными

# Когда мы используем:
# 1. Когда заранее неизвестно с каким объектом будем работать в классе,
# но знаем, что будет делать этот объект

# Фабричный метод отделяет код производства продуктов от остального
# кода, который эти продукты использует.
# Классы Абстрактной фабрики чаще всего реализуются с помощью Фабричного метода

from abc import ABC, abstractmethod


# Интерфейс для кнопок
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, f):
        pass


# Кнопка для Windows
class WindowsButton(Button):
    def render(self):
        print("Отрисовать кнопку в стиле Windows.")

    def on_click(self, f):
        print("Навесить на кнопку обработчик событий Windows.")


# Кнопка для HTML
class HTMLButton(Button):
    def render(self):
        print("Вернуть HTML-код кнопки.")

    def on_click(self, f):
        print("Навесить на кнопку обработчик события браузера.")


# Базовый класс диалога
class Dialog(ABC):
    def render(self):
        # Используем фабричный метод для создания кнопки
        ok_button = self.create_button()
        ok_button.on_click(self.close_dialog)
        ok_button.render()

    # ВОТ ЭТОТ АБСТРАКТНЫЙ МЕТОД
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def close_dialog(self):
        print("Закрыть диалог.")


# Конкретный класс диалога для Windows
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


# Конкретный класс диалога для веба
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()


# Приложение
class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = self.read_application_config_file()

        if config['OS'] == "Windows":
            self.dialog = WindowsDialog()
        elif config['OS'] == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")

    def main(self):
        self.initialize()
        self.dialog.render()

    # Пример функции для чтения конфигурации (можно заменить реальной реализацией)
    @staticmethod
    def read_application_config_file():
        return {'OS': 'Windows'}  # Пример возвращаемого значения


# Запуск приложения
if __name__ == "__main__":
    app = Application()
    app.main()
