from registro import *


def principal():
    op = -1
    vec = []
    paso_4 = False
    fd = "proyecto.object"
    fd1 = "populares.dat"

    while op != 8:
        menu()
        op = validar_mayor_que(0, "➢ Ingrese la opción que desee: ", "\033[;31m✖ ¡ERROR! ➢ Ingrese una opción válida: \033[;m")
        if op == 1:
            cargar_vec(vec)
            input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 2 and len(vec) != 0:
            print("")
            tag_ingresado = input("➢ Ingrese un TAG a buscar: ")
            registros_tag, opcion = buscar_tag(vec, tag_ingresado)
            if opcion == 1:
                generar_archivo(fd, registros_tag)
                input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")
            elif opcion == 0:
                print("\n\033[;32m→ Ha decidido no crear un archivo.\033[;m")
                input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 3 and len(vec) != 0:
            print("")
            print("→ Buscando cantidad de proyectos por lenguaje...")
            input("↲ Presione <ENTER> para mostrar la cantidad de proyectos por cada lenguaje.")
            vec_lenguajes = registrar_lenguajes(vec)
            vec_conteo = conteo(vec, vec_lenguajes)
            mostrar_conteo(vec_conteo, vec_lenguajes)
            input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 4 and len(vec) != 0:
            print("")
            input("↲ Presione <ENTER> para generar la matriz de popularidad.")
            matriz = crear_matriz(vec)
            mostrar_matriz(matriz)
            m = validar_entre(1, 12, "\n➢ Ingrese un mes para ver el total de proyectos actualizados del mismo: ",
                              "\033[;31m✖ ¡ATENCIÓN! ➢ Ingrese un mes válido: \033[;m")
            contador = total_proyectos(matriz, m)
            if contador == 0:
                print(f"\n\033[;32m→ El mes {m} no ha tenido proyectos actualizados.\033[;m")
            else:
                print(f"\n\033[;32m→ El mes {m} ha tenido {contador} proyectos actualizados.\033[;m")
            input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")
            paso_4 = True

        elif op == 5 and len(vec) != 0:
            print("")
            rep = input("➢ Ingrese un repositorio para buscar: ")
            encontro = buscar_rep(vec, rep)
            if not encontro:
                print("\n\033[;32m→ No se ha encontrado ningún proyecto con ese repositorio.\033[;m")
            input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 6 and len(vec) != 0:
            print("")
            if paso_4:
                populares(matriz, fd1)
                input("\n\033[3;37m↲ Presione <ENTER> volver al menú de opciones.\033[;m")
            else:
                print("\033[;31m✖ ¡ATENCIÓN! Primero debe crear la matriz en el punto 4.\033[;m")
                input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 7:
            print("")
            vec_fd1 = leer_archivo(fd1)
            if vec_fd1 != -1:
                matriz_2 = crear_matriz_2(vec_fd1)
                mostrar_matriz(matriz_2)
            input("\n\033[3;37m↲ Presione <ENTER> para volver al menú de opciones.\033[;m")

        elif op == 8:
            print("\n\033[1;36m→ Ha decidido salir del programa ¡ADIÓS! ❤\n\033[;m")
        elif op > 8:
            print("\n\033[;31m✖ ¡ATENCIÓN! ➢ Ingrese una opción válida\033[;m")
        else:
            print("\n\033[;31m✖ ¡ATENCIÓN! ➢ Primero debe cargar el vector en la opción ❰ 1 ❱.\033[;m")


if __name__ == '__main__':
    principal()
