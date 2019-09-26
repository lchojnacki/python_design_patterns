class Singleton:
    
    __single_instance = None
    
    def __init__(self, x = 0):
        print("Creating object...")
        if(type(self).__single_instance == None):
            self.__x = x
            type(self).__single_instance = self
        else:
            raise Exception("Can't create more than one object of this type.")

    def __str__(self):
        return "Value: " + str(self.__x)

    @staticmethod
    def get_instance():
        if (Singleton.__single_instance is not None):
            return Singleton.__single_instance
        else:
            Singleton.__single_instance = Singleton()
            return Singleton.__single_instance
        

if __name__ == "__main__":

    try:
        a = Singleton(3)
        print(a)
    except Exception as e:
        print(e)

    try:
        b = Singleton(4)
        print(b)
    except Exception as e:
        print(e)
        b = Singleton.get_instance()
        

    print(Singleton.get_instance())
    print(a.get_instance())
    print(b.get_instance())
