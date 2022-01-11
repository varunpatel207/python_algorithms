from src.testing.a import A


class B(A):
    def __init__(self, a):
        A.__init__(self, a)

    def b_class_method(self):
        return_value = self.a_class_method()
        print(return_value)
        return "This is B class method."

b_object = B(a=8)
b_return = b_object.b_class_method()
print(b_return)
