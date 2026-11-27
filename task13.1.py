import inspect


class ObjectAnalyzer:
    def get_type(self, obj):
        """Метод повинен повертати назву типу об'єкта."""
        return type(obj).__name__

    def get_attributes(self, obj):
        """Метод повинен повертати список атрибутів об'єкта без спеціальних атрибутів Python."""
        result = []
        for name in dir(obj):
            if name.startswith("__"):
                continue
            value = getattr(obj, name)
            if not callable(value):
                result.append(name)
        return result

    def get_methods(self, obj):
        """Метод повинен знаходити доступні методи та їхні сигнатури."""
        methods = {}
        for name, member in inspect.getmembers(obj, predicate=callable):
            if name.startswith("__"):
                continue
            try:
                methods[name] = str(inspect.signature(member))
            except (ValueError, TypeError):
                methods[name] = " "
        return methods

    def get_inheritance(self, obj):
        """Метод повинен повертати ієрархію успадкування."""
        cls = obj if isinstance(obj, type) else type(obj)
        return [base.__name__ for base in cls.__mro__]

    def get_documentation(self, obj):
        """Метод повинен отримувати документацію об'єкта."""
        return inspect.getdoc(obj) or ""

    def get_attribute(self, obj, name):
        """Метод повинен повертати значення атрибута, якщо він існує."""
        return getattr(obj, name, None)

    def set_attribute(self, obj, name, value):
        """Метод повинен дозволяти встановлювати нові атрибути."""
        setattr(obj, name, value)

    def analyze(self, obj):
        """Метод повинен об'єднувати всі результати аналізу в один структурований звіт."""
        return {
            "type": self.get_type(obj),
            "attributes": self.get_attributes(obj),
            "methods": self.get_methods(obj),
            "inheritance": self.get_inheritance(obj),
            "documentation": self.get_documentation(obj),
        }