class user():
    #Constructor
    def __init__(self, name:str, email:str, id:int, phone:int):
        self.name=name
        self.email=email
        self.id=id
        self.phone=phone

    #Definimos una función para crear al usuario
    def createUser(self, name, email, id, phone):
        self.__init__(name, email, id, phone)
        print("User has been created")
        