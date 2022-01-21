#constants
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c=3*10**8

#functions
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp
f100_in_celsius=f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp=(c_temp*(9/5))+32
  return f_temp
c0_in_fahrenheit=c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass,acceleration):
  return mass*acceleration
train_force=get_force(train_mass,train_acceleration)
print("The GE train supplies",train_force, "Newtons of force.")

def get_energy(mass,c):
  return mass*(c**2)
bomb_energy=get_energy(bomb_mass,c)
print("A 1kg bomb supplies",bomb_energy, "Joules.")

def get_work(mass,acceleration,distance):
  result= get_force(mass,acceleration)*distance
  return result
train_work=get_work(train_mass,train_acceleration,train_distance)
print("The GE train does",train_work,"of work over",train_distance,"meters.")


"""
OUTPUT:

37.77777777777778
32.0
The GE train supplies 226800 Newtons of force.
A 1kg bomb supplies 90000000000000000 Joules.
The GE train does 22680000 of work over 100 meters.

"""
