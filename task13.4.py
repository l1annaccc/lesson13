class Logger:
    """Через Singleton"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"LOG {message}")


class ServiceSingleton:
    """Через Dependency Injection"""
    def __init__(self):
        self.logger = Logger()

    def run(self, text):
        self.logger.log(text)


class ConsoleLogger:
    def log(self, message):
        print(f"CONSOLE {message}")


class FileLogger:
    def log(self, message):
        print(f"FILE {message}")


class ServiceDI:
    def __init__(self, logger):
        self.logger = logger

    def run(self, text):
        self.logger.log(text)


if __name__ == "__main__":
    s1 = ServiceSingleton()
    s1.run("Singleton message")

    s2 = ServiceDI(ConsoleLogger())
    s2.run("Console message")

    s3 = ServiceDI(FileLogger())
    s3.run("File message")