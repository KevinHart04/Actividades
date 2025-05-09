import stack
import random
import colores as color

class Trajes:
    def __init__(self,mod, peli, estado):
            self.mod = mod
            self.peli = peli
            self.estado = estado
    
    def __str__(self):
        print("-" * 75)
        return color.color(f"| {self.mod:^20} | {self.peli:<30} | {self.estado:^15} |", color.NEGRITA)



modelo = {
    1: "Mark I",
    2: "Mark V",
    3: "Mark XLIV",
    4: "Mark LXXXV",
    5: "Mark L",
    6: "Mark III"
}

pelicula = {
    1: "Iron Man",
    2: "Iron Man 2",
    3: "Avengers: Age of Ultron",
    4: "Spider-Man: Homecoming",
    5: "Capitan America: Civil War"
}

estado = {
    1: "Impecable",
    2: "Dañado",
    3: "Destruido"
}

def cargar_pila(pila:stack.Stack):
    usados = set()
    mark_lxxxv_cargado = False

    for i in range(10):
        mod = random.choice(list(modelo.values()))
        peli = random.choice(list(pelicula.values()))
        est = random.choice(list(estado.values()))        
        clave = (mod, peli)
        
        if mod == "Mark LXXXV" and not mark_lxxxv_cargado:
            usados.add(clave)
            mark_lxxxv_cargado = True
            pila.push(Trajes(mod, peli, est))
            continue
        
        if clave not in usados:
            usados.add(clave)
            traje = Trajes(mod, peli, est)
            pila.push(traje)    
    return pila


def hulkbuster(pila:stack.Stack):
    pila_aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        pila_aux.push(traje)
        if traje.mod == "Mark XLIV":
            print(color.color(f"[+] Se encontro el Mark XLIV en la pelicula {traje.peli}", color.VERDE))
        
    while not pila_aux.size() == 0:
        pila.push(pila_aux.pop())


def dañados(pila:stack.Stack):
    pila_aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.estado == "Dañado":
            print(color.color(f"[+] Se encontro un traje dañado en la pelicula {traje.peli}", color.AMARILLO))
        pila_aux.push(traje)
    
    while not pila_aux.size() == 0:
        pila.push(pila_aux.pop())

def destruidos(pila:stack.Stack):
    pila_aux = stack.Stack()
    while not pila.size() == 0:
        traje = pila.pop()
        if traje.estado == "Destruido":
            print(color.color(f"[+] Se encontro el traje {traje.mod} destruido en la pelicula {traje.peli}", color.ROJO))
        else:
            pila_aux.push(traje)
    
    while not pila_aux.size() == 0:
        pila.push(pila_aux.pop())

def in_peli (pila:stack.Stack):
    pila_aux = stack.Stack()
    
    while not pila.size() == 0:
        traje = pila.pop()
        
        if traje.peli in ["Capitan America: Civil War", "Spider-Man: Homecoming"]:
            print(color.color(f"[+] En la película {traje.peli} ha sido usado el traje {traje.mod}", color.AMARILLO))
        
        pila_aux.push(traje)  # Siempre lo guardamos en la auxiliar, pase lo que pase
    
    # Restauramos la pila original
    while not pila_aux.size() == 0:
        pila.push(pila_aux.pop())

def main():
    pila = stack.Stack()
    cargar_pila(pila)
    
    print(color.color("[*] Trajes cargados en la pila:", color.MAGENTA))
    pila.show()
    
    hulkbuster(pila)
    dañados(pila)
    destruidos(pila)
    in_peli(pila)

if __name__ == "__main__":
    main()


