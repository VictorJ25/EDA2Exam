from DataExam import*
import random

class Patient:
  def __init__(self):

    self.Name= Create_names()
    self.IMC = IMC(15.5, 45.5)
    self.BloodPressure = BloodPressure(110, 150)
    self.Age = Age(0,90)
    self.severity = Severity(1,5)
    self.time = 0
 
  def __str__(self):
    return f'Paciente:[{self.Name}| {self.Age} years | {self.IMC} kg/m^2 | {self.BloodPressure} mmHg | {self.severity} Several | {self.time} min]'
    
def Create_names():
  name = random.choice(men_names)
  last_name1 = random.choice(men_lastnames)
  last_name2 = random.choice(men_lastnames)

  return f'{name} {last_name1} {last_name2}'  

def Age(limit_up,limit_down):
  return random.randint(limit_up, limit_down)

def IMC(limit_up,limit_down):
  Number=random.uniform(limit_up, limit_down)
  Number=round(Number,1)
  return Number

def BloodPressure(limit_up,limit_down):
  return random.randint(limit_up, limit_down)

def Severity(limit_up,limit_down):
  Number=random.uniform(limit_up, limit_down)
  Number=round(Number,1)
  return Number
