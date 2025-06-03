import copy

# Базовий клас для копіювання
class Configuration:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address

    def clone(self):
        return copy.deepcopy(self)

    def info(self):
        raise NotImplementedError("Subclasses must implement info()")

# Конфігурація веб-сервера (без SSL)
class WebServer(Configuration):
    def __init__(self, hostname, ip_address, port):
        super().__init__(hostname, ip_address)
        self.port = port

    def info(self):
        print(f"WebServer:\n Hostname: {self.hostname}\n IP: {self.ip_address}\n Port: {self.port}\n")

# Конфігурація бази даних
class DatabaseServer(Configuration):
    def __init__(self, hostname, ip_address, engine, storage_gb):
        super().__init__(hostname, ip_address)
        self.engine = engine
        self.storage_gb = storage_gb

    def info(self):
        print(f"DatabaseServer:\n Hostname: {self.hostname}\n IP: {self.ip_address}\n Engine: {self.engine}\n Storage: {self.storage_gb} GB\n")

# Демонстрація копіювання
def execute_cloning():
    print("== Оригінальні шаблони ==")
    web_template = WebServer("web01", "192.168.0.10", 80)
    db_template = DatabaseServer("db01", "192.168.0.20", "PostgreSQL", 256)

    web_template.info()
    db_template.info()

    print("== Копії з модифікаціями ==")
    web_copy = web_template.clone()
    web_copy.hostname = "web02"
    web_copy.ip_address = "192.168.0.11"
    web_copy.port = 8080

    db_copy = db_template.clone()
    db_copy.hostname = "db02"
    db_copy.ip_address = "192.168.0.21"
    db_copy.storage_gb = 512

    web_copy.info()
    db_copy.info()

if __name__ == "__main__":
    execute_cloning()
