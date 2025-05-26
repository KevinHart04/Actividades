from cola import Queue
from datetime import datetime, time
from colores import color, VERDE, AMARILLO, CIAN, MAGENTA, ROJO, NEGRITA

def eliminar_notificaciones_facebook(cola: Queue) -> None:
    """
    Elimina de la cola todas las notificaciones provenientes de la aplicación Facebook.
    """
    cola_aux = Queue()
    while cola.size() > 0:
        noti = cola.attention()
        if noti["app"] != "Facebook":
            cola_aux.arrive(noti)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

def mostrar_twitter_con_python(cola: Queue) -> None:
    """
    Muestra todas las notificaciones de Twitter cuyo mensaje contenga la palabra 'Python',
    sin modificar el contenido de la cola original.
    """
    for _ in range(cola.size()):
        noti = cola.move_to_end()
        if noti["app"] == "Twitter" and "Python" in noti["mensaje"]:
            mensaje = color(noti["mensaje"], MAGENTA + NEGRITA)
            print(f"{color('[Twitter]', CIAN)} {mensaje} - {noti['hora']}")

def str_a_time(hora_str: str) -> time:
    """
    Convierte una hora en formato HH:MM a un objeto time.
    """
    return datetime.strptime(hora_str, "%H:%M").time()

def contar_notificaciones_en_rango(cola: Queue) -> int:
    """
    Usa una pila para almacenar las notificaciones cuya hora esté entre las 11:43 y las 15:57,
    y devuelve la cantidad total de estas.
    """
    pila = []
    cola_aux = Queue()
    desde = time(11, 43)
    hasta = time(15, 57)

    while cola.size() > 0:
        noti = cola.attention()
        hora = str_a_time(noti["hora"])
        if desde <= hora <= hasta:
            pila.append(noti)
        cola_aux.arrive(noti)

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

    return len(pila)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    cola_notis = Queue()
    cola_notis.arrive({"hora": "10:30", "app": "Facebook", "mensaje": "Nuevo post"})
    cola_notis.arrive({"hora": "12:15", "app": "Twitter", "mensaje": "Python es genial"})
    cola_notis.arrive({"hora": "14:45", "app": "Instagram", "mensaje": "Nueva historia"})
    cola_notis.arrive({"hora": "15:50", "app": "Twitter", "mensaje": "Python tips"})
    cola_notis.arrive({"hora": "16:00", "app": "Facebook", "mensaje": "Otro post"})
    cola_notis.arrive({"hora": "13:00", "app": "Twitter", "mensaje": "Java vs Python"})
    
    print(color("Cola de notificaciones inicial:", VERDE))
    cola_notis.show()

    print(color("\nMostrando notificaciones de Twitter con 'Python':", VERDE))
    mostrar_twitter_con_python(cola_notis)

    print(color("\nEliminando notificaciones de Facebook...", AMARILLO))
    eliminar_notificaciones_facebook(cola_notis)
    print(color("Cola después de eliminar Facebook:", VERDE))
    cola_notis.show()

    print(color("\nContando notificaciones entre 11:43 y 15:57...", CIAN))
    cantidad = contar_notificaciones_en_rango(cola_notis)
    print(f"{color('Cantidad en rango:', NEGRITA + CIAN)} {color(str(cantidad), VERDE)}")