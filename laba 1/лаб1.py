class Device:
    def __init__(self, model, power_source):
        self.__model = model  # Закритий атрибут
        self.__power_source = power_source  # Закритий атрибут

    def operate(self):
        raise NotImplementedError("Subclasses must implement the operate method")

    def describe(self):
        return f"This is a {self.__class__.__name__} model {self.__model}."

    def power_info(self):
        return f"The {self.__class__.__name__} model {self.__model} runs on {self.__power_source}."

    # Геттери
    def get_model(self):
        return self.__model

    def get_power_source(self):
        return self.__power_source

    # Сеттери
    def set_model(self, new_model):
        self.__model = new_model

    def set_power_source(self, new_power):
        self.__power_source = new_power


class Laptop(Device):
    def operate(self):
        return "Booting up the system..."


class Smartphone(Device):
    def operate(self):
        return "Launching the mobile interface..."


class Camera(Device):
    def operate(self):
        return "Capturing high-resolution photo..."


# Створення колекції об'єктів
devices = [
    Laptop("ThinkPad X1", "battery"),
    Smartphone("iPhone 14", "battery"),
    Camera("Canon EOS", "battery")
]

# Проходження по всіх елементах колекції і виклик абстрактного методу
for device in devices:
    print(device.describe())
    print(device.operate())
    print(device.power_info())
    print()

# Взаємодія з атрибутами через сеттери
print("Changing laptop's model to Dell XPS...")
devices[0].set_model("Dell XPS")
print(devices[0].describe())

print()
print("Changing smartphone's power source to solar")
devices[1].set_power_source("solar")
print(devices[1].power_info())