from populares import *
import pickle
import datetime
import os


class Proyecto:
    def __init__(self, nombre, repositorio, fecha, lenguaje, likes, tags, url):
        self.nombre = nombre
        self.repositorio = repositorio
        self.fecha = fecha
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

    def __str__(self):
        res = f"Nombre de usuario: {str(self.nombre)}    |    Repositorio: {str(self.repositorio)}    |    Fecha de " \
              f"actualización: {str(self.fecha)}    |    Lenguaje: {str(self.lenguaje)}    |    Likes: {str(self.likes)}" \
              f"    |    Tags: {str(self.tags)}    |    Url: {str(self.url)}"
        return res


gris = "\033[2;32m"
blanco = "\033[;m"


def menu():
    print(f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
          f"┃{'MENÚ DE OPCIONES':^20}┃\n"
          f"┗━━━━━━━━━━━━━━━━━━━━┛")
    print("❰ 1 ❱ Cargar el contenido ordenado según el repositorio")
    print("❰ 2 ❱ Filtrar por TAG")
    print("❰ 3 ❱ Determinar cantidad de proyectos por cada lenguaje")
    print("❰ 4 ❱ Generar matriz de popularidad")
    print("❰ 5 ❱ Buscar proyecto según el repositorio para actualizarlo")
    print("❰ 6 ❱ Crear archivo binario con los datos de la matriz de popularidad")
    print("❰ 7 ❱ Mostrar archivo creado en el punto [6]")
    print("❰ 8 ❱ Salir del programa")


def validar_mayor_que(inf, mensaje1, mensaje2):
    n = int(input(mensaje1))
    while n < inf:
        n = int(input(mensaje2))
    return n


# PUNTO 1 ##############


def add_in_order(vec, proyecto):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if proyecto.repositorio == vec[c].repositorio:
            pos = c
            break
        if proyecto.repositorio < vec[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [proyecto]


def buscar_repe(param, repositorios):
    for i in range(len(repositorios)):
        if param == repositorios[i]:
            return -1
    return param


def cargar_vec(vec):
    m = open("proyectos_dados.csv", mode="rt", encoding="utf8")
    repositorios = []
    contador_proyectos = contador_repetidos = contador_total = 0
    linea = m.readline()

    while linea != "":
        clases = linea.split("|")
        repetido = buscar_repe(clases[1], repositorios)
        tags_separados = clases[6].split(",")
        if clases[4] != "" and repetido != -1 and contador_total != 0:
            repositorios.append(clases[1])
            nombre = clases[0]
            repositorio = clases[1]
            fecha = clases[3]
            lenguaje = clases[4]
            likes = float(clases[5][:-1])
            tags = tags_separados
            url = clases[7]
            proyecto = Proyecto(nombre, repositorio, fecha, lenguaje, likes, tags, url)
            add_in_order(vec, proyecto)
            contador_proyectos += 1
        elif contador_total != 0:
            contador_repetidos += 1
        linea = m.readline()
        contador_total += 1
    m.close()
    print(f"\033[;32m\n→ Cantidad de proyectos cargados: {contador_proyectos}"
          f"\n→ Cantidad de proyectos omitidos: {contador_repetidos}\033[;m")


def mostrar_vec(vec):
    for proyecto in vec:
        print(proyecto)


# PUNTO 2 ##############


def estrellas(likes):
    if 0 < likes <= 10:
        return 1
    elif 10.1 < likes <= 20:
        return 2
    elif 20.1 < likes <= 30:
        return 3
    elif 30.1 < likes <= 40:
        return 4
    else:
        return 5


def crear_linea(vec, indice):
    linea = vec[indice]
    return linea


def buscar_tag(vec, tag_ingresado):
    existio = False
    registros_tag = []
    print(f"→ El vector con el TAG \" {tag_ingresado} \" tiene los siguientes datos:")
    opcion = -1
    for i in range(len(vec)):
        for tags in vec[i].tags:
            if tags == tag_ingresado:
                existio = True
    if existio:
        print(f"{gris}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓{blanco}\n"
              f"{gris}┃{blanco}{'Repositorio':^42}{gris}┃{blanco}{'Fecha de actualización':^25}{gris}┃{blanco}{'Estrellas':^15}{gris}┃{blanco}")
        for i in range(len(vec)):
            for tags in vec[i].tags:
                if tags == tag_ingresado:
                    registros_tag.append(vec[i])
                    print(f"{gris}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━┫{blanco}")
                    print(
                        f"{gris}┃{blanco}{vec[i].repositorio:^42}{gris}┃{blanco}{vec[i].fecha:^25}{gris}┃{blanco}{estrellas(vec[i].likes):^15}{gris}┃{blanco}")
        print(f"{gris}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛{blanco}")
        opcion = det_opcion()

    if not existio:
        print("\n\033[;31m✖ ¡ERROR! No se ha encontrado ningún proyecto con ese tag.\033[;m")
    return registros_tag, opcion


def det_opcion():
    opcion = int(input(
        "\n¿Desea almacenar el listado en un archivo de texto separado? \n→ [ 0 ] para NO\n→ [ 1 ] para SI\n➢ Ingrese su elección: "))
    while opcion != 0 and opcion != 1:
        opcion = int(input(f"\033[;31m✖ ¡ATENCIÓN! presione [ 0 ] para NO || [ 1 ] para SI: \033[;m"))
    return opcion


def generar_archivo(fd, registros_tag):
    m = open(fd, "wt")
    m.write(
        "nombre_usuario     |    repositorio     |     fecha_actualización     |     lenguaje     |     estrellas     |     tags     |     url\n\n")
    for i in range(len(registros_tag)):
        tags_sep = ",".join(registros_tag[i].tags)
        m.write(f"{registros_tag[i].nombre}     |    {registros_tag[i].repositorio}     |    {registros_tag[i].fecha}"
                f"     |    {registros_tag[i].lenguaje}     |     {registros_tag[i].likes}     |    {tags_sep}     |    {registros_tag[i].url}\n")
    m.close()
    print("\n\033[;32m✔ ¡ARCHIVO GENERADO!\033[;m")


# PUNTO 3 ##############


def registrar_lenguajes(vec):
    vec_lenguajes = []
    for i in range(len(vec)):
        if len(vec_lenguajes) == 0:
            vec_lenguajes.append(vec[i].lenguaje)
        elif vec[i].lenguaje not in vec_lenguajes:
            vec_lenguajes.append(vec[i].lenguaje)
    return vec_lenguajes


def det_indice(lenguaje, vec_lenguajes, vec_conteo):
    for i in range(len(vec_lenguajes)):
        if lenguaje == vec_lenguajes[i]:
            vec_conteo[i] += 1
            return i


def conteo(vec, vec_lenguajes):
    vec_conteo = [0] * len(vec_lenguajes)
    for i in range(len(vec)):
        det_indice(vec[i].lenguaje, vec_lenguajes, vec_conteo)
    return vec_conteo


def ordenamiento(vec_conteo, vec_lenguajes):
    n = len(vec_conteo)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec_conteo[i] < vec_conteo[j]:
                vec_conteo[i], vec_conteo[j] = vec_conteo[j], vec_conteo[i]
                vec_lenguajes[i], vec_lenguajes[j] = vec_lenguajes[j], vec_lenguajes[i]


def mostrar_conteo(vec_conteo, vec_lenguajes):
    ordenamiento(vec_conteo, vec_lenguajes)
    print("")
    print(f"{gris}┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓{blanco}\n"
          f"{gris}┃{blanco}{'Lenguaje':^18}{gris}┃{blanco}{'Cantidad de proyectos':^25}{gris}┃{blanco}")
    for i in range(len(vec_conteo)):
        print(f"{gris}┣━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━┫{blanco}")
        print(f"{gris}┃{blanco}{vec_lenguajes[i]:^18}{gris}┃{blanco}{vec_conteo[i]:^25}{gris}┃{blanco}")
    print(f"{gris}┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┛")


# PUNTO 4 ##############


def validar_entre(inf, sup, mensaje, mensaje2):
    n = int(input(mensaje))
    while n < inf or n > sup:
        n = int(input(mensaje2))
    return n


def crear_matriz(vec):
    matriz = [[0] * 5 for _ in range(12)]
    for proyecto in vec:
        fecha = proyecto.fecha.split("-")
        estrellita = estrellas(proyecto.likes)
        fecha_2 = int(fecha[1])
        matriz[fecha_2 - 1][estrellita - 1] += 1
    return matriz


def mostrar_matriz(matriz):
    print("")
    print(f"{gris}┏━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓{blanco}\n"
          f"{gris}┃        ┃{blanco}{'1 Estrella':^15}{gris}┃{blanco}{'2 Estrellas':^15}{gris}┃{blanco}{'3 Estrellas':^15}{gris}┃{blanco}{'4 Estrellas':^15}{gris}┃{blanco}{'5 Estrellas':^15}{gris}┃{blanco}\n"
          f"{gris}┣━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━┫{blanco}\n", end="")
    for f in range(len(matriz)):
        print(f"{gris}┃{blanco} Mes {f + 1:<3}{gris}┃{blanco}", end="")
        for c in range(len(matriz[f])):
            print(f"{matriz[f][c]:^15}{gris}┃{blanco}", end="")
        if f != 11:
            print(f"\n{gris}┣━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━┫{blanco}")
    print(f"\n{gris}┗━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┛{blanco}")


def total_proyectos(matriz, m):
    contador = 0
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if f + 1 == m:
                contador += matriz[f][c]
    return contador


# PUNTO 5 ##############


def buscar_rep(vec, rep):
    encontro = False
    for i in range(len(vec)):
        if vec[i].repositorio == rep:
            encontro = True
            print(f"\n\033[;32m→ Datos del proyecto con el repositorio {rep}:\n")
            print(f"→ {vec[i]}\033[;m")
            url_solicitado = input("➢ Ingrese la URL a reemplazar en el proyecto mostrado: ")
            print("\n→ Actualizando fecha y URL ingresado...")
            input("↲ Presione <ENTER> para mostrar el proyecto actualizado.")
            vec[i].url = url_solicitado
            fecha = datetime.datetime.now()
            fecha_ahora = fecha.strftime("%Y-%m-%d")
            vec[i].fecha = fecha_ahora
            print(f"\033[;32m\n{vec[i]}\033[;m")
    return encontro


# PUNTO 6 ##############


def populares(matriz, fd):
    m = open(fd, "wb")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                mes = f
                estrellas_ = c
                cantidad = matriz[f][c]
                popular = Popular(mes, estrellas_, cantidad)
                pickle.dump(popular, m)
    print("\033[;32m→ ✔ ¡ARCHIVO BINARIO CREADO!\033[;m")

    m.close()


# PUNTO 7 ##############


def leer_archivo(fd1):
    vec_fd1 = []
    if os.path.exists(fd1):
        m = open(fd1, "rb")
        tamanio = os.path.getsize(fd1)
        while m.tell() < tamanio:
            archivo = pickle.load(m)
            vec_fd1.append(archivo)
    else:
        print("\033[;31m✖ ¡ATENCIÓN! No se ha creado el archivo\033[;m")
        return -1
    return vec_fd1


def crear_matriz_2(vec_fd1):
    matriz_2 = [[0] * 5 for _ in range(12)]
    for i in range(len(vec_fd1)):
        estrellita = vec_fd1[i].estrellas
        mes = vec_fd1[i].mes
        matriz_2[mes][estrellita] += vec_fd1[i].cantidad

    print("\033[;32m→ ✔ ¡MATRIZ CREADA A PARTIR DEL ARCHIVO!\033[;m")
    input("\n↲ Presione <ENTER> para mostrar la matriz creada a partir del archivo.")
    return matriz_2
