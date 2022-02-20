from helpers import Helper
from listas import Listas
from pilas import Pilas
from colas import Colas
import os
import time

#Gotoxy
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

#Repite el listado
helper = Helper()
lista = ["1) Listas","2) Pilas","3) Colas","4) Salir"]
opcion=""

#Menu principal
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista," MENÚ PRINCIPAL ")
  
  #Menu Lista
  if opcion == "1":
    opc1=""
    while opc1 != "7":
      os.system("cls")
      opc1 = helper.menu(["1) Push ","2) Pop","3) Mostrar","4) Eliminar","5) Agregar","6) Buscar","7) Salir"]," LISTAS ")
      os.system("cls")
      datos = Listas()

      #ingreso de elementos
      if opc1 == "1":
        print("INGRESE ELEMENTO EN LA LISTA:")
        valor = input("Ingrese el elemento: ")
        datos.ingresar(valor)
        input("Elemento ingresado satisfactoriamente, presione ENTER para continuar...")
        
      #eliminar ultimo elemento
      elif opc1 == "2":
        print("ELIMINAR ULTIMO ELEMENTO")
        if len(datos.lista) == 0:
              print("La lista está Vacía.......")
              print("")
        else:
          print("Borrando el ultimo elemento...");time.sleep(1)
          gotoxy(0,2);print("El elemento que usted eliminó fué: "+datos.eliminar());gotoxy(60,2);print(" "*80)
          print("\033[3A")
          print("\033[0B")
        input("Presione una tecla para continuar...")
        
      
      #mostrar elementos de la lista
      elif opc1 == "3":
        print("MOSTRAR ELEMENTOS")
        datos.mostrar()
        print("")
        input("Presione una tecla para continuar...")   
      
      #eliminar dicho elemento
      elif opc1 == "4":
        print("ELIMINAR UN ELEMENTO")
        if len(datos.lista) == 0:
              print("La lista está Vacía.......")
              print("")
        else:
          while True:
              try:
                elimi=int(input("Ingrese la posición del elemento que desea eliminar: "))
                datos.eliminarElemento(elimi)
                break
              except ValueError:
                gotoxy(54,2);print("Ingrese solo números.");time.sleep(1);gotoxy(54,2);print(" "*80)
                print("\033[3A")    
        input("Presione una tecla para continuar...")
        print("\033[A")  
      
      #agregar dicho elemento
      elif opc1 == "5":
        print("AGREGAR UN ELEMENTO")
        if len(datos.lista) == 0:
          print("La lista está Vacía.......")
          print("")
        else:
          while True:
            try:
              pos=int(input("Ingrese la posición en la que desea agregar el elemento: "))
              if pos < 0 or pos > (len(datos.lista)+1):
                gotoxy(0,2);print("Esa posición no exite......."+" "*60);time.sleep(1)
                print("\033[3A")
              else:
                ele=input("Ingrese el nuevo elemento: ")
                datos.ingresarElemento(pos,ele)
              break
            except ValueError:
              gotoxy(58,2);print("Ingrese solo números");time.sleep(1);gotoxy(58,2);print(" "*100)
              print("\033[3A")        
        input("Presione una tecla para continuar...")
        print("\033[A") 
        
      
      #buscar elemento      
      elif opc1 == "6":
        print("BUSCAR UN ELEMENTO")
        if len(datos.lista) == 0:
              print("La lista está Vacía.......")
              print("")
              
        else:
          ele=input("Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input("Presione una tecla para continuar...") 

  #Menu pila      
  elif opcion == "2":       
    opc2=""
    os.system("cls")
    print(" PILAS ")
    while True:
      try:
        lim=int(input("Cuantos elementos tendrá la pila?: ")) 
        break
      except ValueError:
        gotoxy(36,2);print("Ingrese solo números.");time.sleep(1);gotoxy(36,2);print(" "*80)
        print("\033[3A")
    datos=Pilas(lim)
    os.system("cls")
    while opc2 != "6":
      os.system("cls")
      opc2 = helper.menu(["1) Push","2) Pop","3) Mostrar","4) Buscar","5) Longitud","6) Salir"]," PILAS ")
      os.system("cls")

      #ingreso un elemento
      if opc2 == "1":
        nombre= ""
        os.system("cls")
        print("INGRESAR ELEMENTO A LA PILA")
        datos.ingresar()
        input("Dato ingresado satisfactoriamente, presione una tecla para continuar...")
      
      #eliminar ultimo elemento
      elif opc2 == "2":
        print("ELIMINAR EL ÚLTIMO ELEMENTO")
        datos.eliminar()
        print("\033[0B")
        input("Presione una tecla para continuar...")
      
      #mostrar elementos
      elif opc2 == "3":
        print("MOSTRAR PILA")
        datos.mostrar()
        print("")
        input("Presione una tecla para continuar...")
      
      #buscar elementos  
      elif opc2 == "4":
        print("BUSCAR ELEMENTO EN LA PILA")
        if len(datos.lista) == 0:
              print("La Pila está Vacía.......")
        else:
          ele=input("Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input("Presione una tecla para continuar...")
      
      #longitud
      elif opc2 == "5":
        print("LONGITUD DE LA PILA")
        datos.longitud()
        input("Presione una tecla para continuar...")
  
  #Menu Cola
  elif opcion == "3":       
    opc3=""
    os.system("cls")
    print(" COLAS ")
    while True:
          try:
            lim=int(input("Cuántos elementos tendrá la cola?: "))
            break
          except ValueError:
            gotoxy(39,2);print("Ingrese solo números.");time.sleep(1);gotoxy(39,2);print(" "*80)
            print("\033[2A")
    datos=Colas(lim)
    os.system("cls")
    while opc3 != "6":
      os.system("cls")
      opc3 = helper.menu(["1) Ingresar","2) Eliminar","3) Mostrar","4) Buscar","5) Longitud","6) Salir"]," COLAS ")
      os.system("cls")

      #ingreso
      if opc3 == "1":
        nombre= ""
        os.system("cls")
        print("INGRESAR ELEMENTO A LA COLA")
        datos.ingresar()
        input("Datos ingresados satisfactoriamente, presione una tecla para continuar...")
      
      #eliminar primer elemento
      elif opc3 == "2":
        print("ELIMINAR EL PRIMER ELEMENTO")
        datos.eliminar()
        input("Presione una tecla para continuar...")

      #mostrar cola  
      elif opc3 == "3":
        print("MOSTRAR COLA")
        datos.mostrar()
        print("")
        input("Presione una tecla para continuar...")
       
      #buscar elementos  
      elif opc3 == "4":
        print("BUSCAR ELEMENTO EN LA COLA")
        if len(datos.lista) == 0:
              print("La Cola está Vacía.......")
        else:
          ele=input("Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input("Presione una tecla para continuar...")
      
      #longitud
      elif opc3 == "5":
        print("LONGITUD DE LA COLA")
        datos.longitud()
        input("Presione una tecla para continuar...")
        
print("ELIGIÓ SALIR")
print("GRACIAS POR SU VISITA :3")
        
        
        
       
    
        
