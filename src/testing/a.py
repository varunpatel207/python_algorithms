class A:
    def __init__(self, value=None):
        self.value = value

    def __add__(self, object_2):
        return self.value + object_2.value

    def __repr__(self):
        return f"A({self.value})"

    def a_class_method(self):
        return "This is A class method."
