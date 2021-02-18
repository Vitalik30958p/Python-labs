class Notebook:
    laba = 1

    @staticmethod
    def static_method():
        return Notebook.laba

    def __init__(self, name="", speed=0, memory=0):
        self.name = name
        self.speed = speed
        self.memory = memory

    def __str__(self):
        return f"name: {self.name} \nspeed: {self.speed}GHz \nmemory: {self.memory}Gb \n(Static: {self.laba})"

    def __del__(self):
        print('Destructor called, Employee deleted')
        del self


def main():

    if __name__ == "__main__":
        main()


obj1 = Notebook("HP", 3.6, 8)
obj2 = Notebook("Lenovo", 4.0, 16)
obj3 = Notebook("Acer", 3.5, 8)
print(obj1.__str__(), "\n")
print(obj2.__str__(), "\n")
print(obj3.__str__(), "\n")
