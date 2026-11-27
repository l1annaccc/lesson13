class ClassValidatorMeta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "":
            raise ValueError("Class name cannot be empty")
        if "version" not in namespace:
            raise AttributeError(f"{name} must define version")
        if "execute" not in namespace or not callable(namespace["execute"]):
            raise TypeError(f"{name} must implement execute()")

        namespace["created_at"] = "2026-11"
        return super().__new__(mcs, name, bases, namespace)


class SampleTask(metaclass=ClassValidatorMeta):
    version = "1.0"

    def execute(self):
        return "Executing task"


if __name__ == "__main__":
    task = SampleTask()
    print(task.version)
    print(task.created_at)
    print(task.execute())