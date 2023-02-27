from MainPatients import*
import h5py
import tensorflow as tf
from QuickSortExam import*

modelo = tf.keras.models.load_model(r'C:\Users\Victor J. Villadiego\OneDrive\Escritorio\Programas Visual Code\Python\modelo_completo.h5')
modelo1 = tf.keras.models.load_model(r'C:\Users\Victor J. Villadiego\OneDrive\Escritorio\Programas Visual Code\Python\modelo_completo.h6')

def createDummiesPatients(amount, doctors):
  try:
    if amount > 0:
      
      list1=[]

      for i in range(0,amount):
        Patient1=Patient()
        list1.append(Patient1)
        item = [Patient1.Age, Patient1.IMC, Patient1.BloodPressure, Patient1.severity]
        ResultTime = modelo.predict([item])
        item2 = [doctors]
        TimeDoctors = modelo1.predict([item2])
        TimeDoctors = int(TimeDoctors) 
        ResultTime = int(ResultTime)
        Patient1.time=ResultTime+TimeDoctors+5+60+30
        if ResultTime==2:
          Patient1.time=15+TimeDoctors+10+70+40
        if ResultTime==3:
          Patient1.time=60+TimeDoctors+20+90+55
        if ResultTime==4:
          Patient1.time=120+TimeDoctors+25+120+70
        if ResultTime==5:
          Patient1.time=240+TimeDoctors+30+180+100
        
      return list1
      
  except:
    return None


def watchList(list1):
  i=1
  for item in list1:
    print(f'({i}) {item}')
    i+=1

if __name__=='__main__':
  
  doctors = int(input('Cuantos medicos y enfermero(a)(s) hay en turno?'))
  data = createDummiesPatients(int(input("¿Cuantas Pacientes quiere crear?")), doctors)
  dataOrg = quicksort(data)
  watchList(dataOrg)
