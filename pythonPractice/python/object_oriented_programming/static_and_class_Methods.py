#understanding static and class methods
class ClassTest:
    @classmethod
    def instance_method(self):
        print(f"Called instance_method of {self}")

text=ClassTest()
ClassTest.instance_method()  # Output: Called instance_method of <__main__.ClassText object at