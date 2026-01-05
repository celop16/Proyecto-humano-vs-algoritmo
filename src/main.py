def crear_grilla(filas, columnas):
    grilla = []
    for _ in range(filas):
        fila = ["." for _ in range(columnas)]
        grilla.append(fila)
    return grilla

def main():
    print("Proyecto: Pensamiento Humano vs Algorítmico")
    print("Inicializando entorno...") 

    grilla = crear_grilla(5,5)
    for fila in grilla:
        print(" ".join(fila))

if __name__ == "__main__":
    main()

