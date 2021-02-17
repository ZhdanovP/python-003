class Example:
    name ="Example"
    @staticmethod
    def static():
        print("static method")

class Offspring(Example):
    name="ofspring"


#classmethod  - no instatances;
class Ex1:
    @classmethod
    def static():
        pass