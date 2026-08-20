class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model=model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla','Model 3')
# print(my_car.make)
my_car.moves()

my_car.get_make_model()

your_car=Vehicle('Cadillac','Escalade')
your_car.get_make_model()
your_car.moves()



class Airplane(Vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)
        self.faa_id=faa_id

    def moves(self):
        print('Flies Along...')

class truck(Vehicle):
    def moves(self):
        print('Rumbles along....')

class golfcart(Vehicle):
    pass

cessna = Airplane('Cessna','Skyhawk','82833')
mack=truck('Mack','Pionnacle')
golf=golfcart('Golfcart','Mercedes')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golf.get_make_model()
golf.moves()

print('\n\n')

for v in (my_car,your_car,cessna,mack,golf):
    v.get_make_model()
    v.moves()
