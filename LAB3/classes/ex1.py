class Stringgg:
    def __init__(self):
        self.string = ""

    def get_string(self, input_string):
        self.string = input_string

    def print_string(self):
        print("String in uppercase:", self.string.upper())


cl = Stringgg()
cl.get_string("something")
cl.print_string()
