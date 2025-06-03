# === Composite Pattern ===

class InstrumentComponent:
    def display(self):
        raise NotImplementedError()


# Leaf — окремий інструмент
class InstrumentItem(InstrumentComponent):
    def __init__(self, instrument):
        self.instrument = instrument

    def display(self):
        self.instrument.display()


# Composite — колекція інструментів
class InstrumentGroup(InstrumentComponent):
    def __init__(self, group_name):
        self.group_name = group_name
        self.instruments = []

    def add(self, component: InstrumentComponent):
        self.instruments.append(component)

    def remove(self, component: InstrumentComponent):
        self.instruments.remove(component)

    def display(self):
        print(f"\nКолекція інструментів: {self.group_name}")
        for instrument in self.instruments:
            instrument.display()


# === Конкретні типи інструментів ===

class StringInstrument:
    def __init__(self, name, maker, string_count):
        self.name = name
        self.maker = maker
        self.string_count = string_count

    def display(self):
        print(f"[Струнний] {self.name} — виробник: {self.maker} (Кількість струн: {self.string_count})")


class WindInstrument:
    def __init__(self, name, maker, key_type):
        self.name = name
        self.maker = maker
        self.key_type = key_type

    def display(self):
        print(f"[Духовий] {self.name} — виробник: {self.maker} (Тип клавіш: {self.key_type})")


# === Facade Pattern ===

class InstrumentCollectionManager:
    def __init__(self):
        self.main_collection = InstrumentGroup("Головна Колекція Інструментів")

    def add_string_instrument(self, name, maker, string_count):
        instrument = StringInstrument(name, maker, string_count)
        self.main_collection.add(InstrumentItem(instrument))

    def add_wind_instrument(self, name, maker, key_type):
        instrument = WindInstrument(name, maker, key_type)
        self.main_collection.add(InstrumentItem(instrument))

    def create_subgroup(self, group_name):
        subgroup = InstrumentGroup(group_name)
        self.main_collection.add(subgroup)
        return subgroup

    def add_to_subgroup(self, subgroup: InstrumentGroup, item: InstrumentComponent):
        subgroup.add(item)

    def show_collection(self):
        self.main_collection.display()


# === Демонстрація ===

def demo_instrument_collection():
    manager = InstrumentCollectionManager()

    print("== Додавання інструментів ==")
    manager.add_string_instrument("Гітара", "Fender", 6)
    manager.add_wind_instrument("Флейта", "Yamaha", "Клавішна")

    print("\n== Створення підколекції ==")
    vintage_group = manager.create_subgroup("Вінтажні інструменти")
    manager.add_to_subgroup(vintage_group, InstrumentItem(StringInstrument("Віолончель", "Stradivari", 4)))
    manager.add_to_subgroup(vintage_group, InstrumentItem(WindInstrument("Саксофон", "Selmer", "Клавішний")))

    print("\n== Вміст колекції ==")
    manager.show_collection()


if __name__ == "__main__":
    demo_instrument_collection()
