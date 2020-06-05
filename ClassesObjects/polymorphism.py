# API PART
class PersonManager:
    def login(email, password):
        if email == 'suglanova@gmail.com' and password == 'Goldrubin1':
            return 1
        elif email == 'emmet.brown@gmail.com' and password == 'backtofuture':
            return 2
        elif email == 'beneger.hawk@gmail.com' and password == 'winteriscoming':
            return 3
        return 0

    def getPersonFromDB(id):
        if id == 1:
            return Person('Svetlana Uglanova')
        elif id == 2:
            return Doctor('Emmett Brown')
        elif id == 3:
            return Knight('Beneger Hawk')
        return None

class Person:
    def __init__(self, name):
        self.name = name
        self.HP = 100

 # polymorphic method
    def getTitle(self):
        return self.name

    def getHP(self):
        return self.HP
        
class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.healing = 10

    def getTitle(self):
        return 'Dr. ' + self.name

    def heal(self, patient):
        patient.HP += self.healing
        
class Knight(Person):
    def __init__(self, name):
        super().__init__(name)
        self.damage = 10
    
    def getTitle(self):
        return 'Sir ' + self.name

    def fight(self, enemy):
        enemy.HP -= self.damage

# DEVELOPER PART

# imagine form data comes from client request
# form = { 'email': 'suglanova@gmail.com', 'password': 'Goldrubin1' }
form = { 'email': 'emmet.brown@gmail.com', 'password': 'backtofuture' }
# form = { 'email': 'beneger.hawk@gmail.com', 'password': 'winteriscoming' }

# getting person
id = PersonManager.login(form['email'], form['password'])
p = PersonManager.getPersonFromDB(id)
print('Welcome ' + p.getTitle() + '!')
