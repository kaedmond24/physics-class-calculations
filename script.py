import typing

# Uncomment this when you reach the "Use the Force" section
# Test variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function to convert temperature in Fahrenheit to Celsius
def f_to_c(fahrenheit_temp: int) -> int:
  c_temp = (fahrenheit_temp - 32) * 5/9
  return c_temp

# Test function: f_to_c(fahrenheit_temp)
f100_in_celsius = f_to_c(100)
print(f"100 degress Fahrenheit is {f100_in_celsius} degress Celsius.")
print(" ")

# Function to convert temperature in Celsius to Fahrenheit
def c_to_f(celsius_temp: int) -> int:
  f_temp = celsius_temp * (9/5) + 32
  return f_temp

# Test function: c_to_f(celsius_temp) 
c0_in_fahrenheit = c_to_f(0)
print(f"0 degrees Celsius is {c0_in_fahrenheit} degrees Fahrenheit.")
print(" ")

# Calculate amount of Newtons of Force
def get_force(mass: int, acceleration: int) -> int:
  return mass * acceleration

# Test function: get_force(train_mass, train_acceleration)
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")
print(" ")

# Calculate amount of Energy
# c is a constant, usually set to the speed of light
def get_energy(mass: int, c: int=3*10**8) -> int:
  return mass * c**2

# Test function: get_energy(mass, c=3*10**8)
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
print(" ")

# Calculate Joules of Work done by Force
def get_work(mass: int, acceleration: int, distance: int) -> int:
  return get_force(mass, acceleration) * distance

# Test function: get_work(mass, acceleration, distance)
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
print(" ")
