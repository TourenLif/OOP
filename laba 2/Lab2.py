from abc import ABC, abstractmethod

# Абстрактна дія з базовим логуванням
class Action(ABC):
    @abstractmethod
    def execute(self):
        print(f"Action started: {self.__class__.__name__}")

# Конкретна дія A
class AlphaAction(Action):
    def __init__(self, target, content):
        self.target = target
        self.content = content

    def execute(self):
        super().execute()
        return f"Alpha sent to {self.target} with content: '{self.content}'"

# Конкретна дія B
class BetaAction(Action):
    def __init__(self, identifier, payload):
        self.identifier = identifier
        self.payload = payload

    def execute(self):
        super().execute()
        return f"Beta delivered to {self.identifier}: '{self.payload}'"

# Трекер дій
class Tracker:
    def record(self, action: Action):
        print(action.execute())

# Запуск
def initiate():
    act1 = AlphaAction("node@domain.net", "Initialize protocol")
    act2 = BetaAction("ID#998877", "Start sequence")

    track = Tracker()
    track.record(act1)
    track.record(act2)

if __name__ == "__main__":
    initiate()
