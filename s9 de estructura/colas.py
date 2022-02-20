import time

#Gotoxy
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

class Colas:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
        
    def empty(self):
        return self.tope == 0
    
    def ingresar(self):
        while self.tope < self.size:
            self.lista += []
            self.tope += 1 
            nombre=input("ingresa un elemento: ")
            self.lista.append(nombre)
            return True
        return print("La Cola está Llena.......")
    
    def eliminar(self):
        if self.empty():
            return print("La Cola está Vacía.......")
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1::1]
            print("Borrando el ultimo elemento.......");time.sleep(1)
            gotoxy(0,2);print("El elemento eliminado fué: "+top);gotoxy(40,2);print(" "*80)
            print("\033[3A")
            
    def longitud(self):
        return print("La longitud es: [{}/{}]".format(self.tope,self.size))
        
    def mostrar(self):
        if self.empty():
            return print("La Cola está Vacía.......")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))   
    
    def buscar(self,buscado):
        op=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                op=True
                break
        if op==True:
            return print("El elemento que buscó se encuentra en la posición: {}".format(pos))
        else:
            return print("El elemento que no se encuentra")