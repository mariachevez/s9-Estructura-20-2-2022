#Gotoxy
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

import time
class Listas:
    
    def __init__(self,datos=[]):
       self.lista = datos
    
    def empty(self):
        return len(self.lista) == 0
        
    def ingresar(self,dato):
        self.lista.append(dato)
        
        
    def eliminar(self):
        if self.empty():
            return print("La lista está Vacía.......")
              
        else:
            dato = self.lista.pop()
            return dato
    
    def eliminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
            gotoxy(0,2);print("No existe esa posición en la Lista"+" "*50);time.sleep(1)
            print("\033[3A")
            return print("No existe esa posición en la Lista")
        else:    
            self.lista.pop(pos)
            return print("el elemento eliminado es: {}".format(self.lista[pos]))
    
    def ingresarElemento(self,pos,elem):
        if pos < 0 or pos > (len(self.lista)+1):
            gotoxy(39,2);print("Posición incorrecta");time.sleep(1);gotoxy(39,2);print(" "*80)
            print("\033[3A")
        else:    
            self.lista.insert(pos,elem)
            print("El elemento insertado fue: {}".format(elem))
        return 
    
    def buscar(self,buscado):
        op=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                op=True
                break
        if op==True:
            return print("El elemento que buscó se encuentra en la posición: {}".format(pos))
        else:
            return print("El elemento que busca no se encuentra en la lista")
    
    def mostrar(self):
        if self.empty():
            return print("La lista está Vacía.......")
        else:                    
            return print(self.lista)