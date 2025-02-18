class Pet:

    def __init__(self, the_name, the_color, the_sex):
        ## Data ##
        self.name = the_name
        self.color = the_color
        self.sex = the_sex
        self._owner = None

    def vocalize(self):
        print('*animal sounds*')

    def get_adopted(self,thing):
        self.vocalize()
        self._owner = thing

    def i_love(self, thing):
        print(f'I love {thing}!')

class Cat(Pet):

    ## Methods ##
    def vocalize(self):
        print("Meeeooowwwww")


class Dog(Pet):

    def vocalize(self):
        print("Woof")

    


