import csv
import os

# ________________________________________________
# Carga de CSV:
# ________________________________________________
def cargar_paises_csv(ruta_archivo: str) -> list:
    lista_inicial = []
    if not os.path.exists(ruta_archivo):
        print(f"\nNo se encuentra el archivo '{ruta_archivo}'. Verifique su ruta de ingreso.")
        return lista_inicial
    
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo: 
            lector = csv.DictReader(archivo) 
            for fila in lector:
                try:
                    pais = { 
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    lista_inicial.append(pais)
                except (ValueError, KeyError) as e: 
                    print(f"Fila omitida por datos incorrectos: {e}")        
    except Exception as e:
        print(f"\nError al leer el archivo: {e}")
        
    return lista_inicial

# ________________________________________________
# Muestra de tabla CSV
# ________________________________________________
def tabla_final_(lista_paises: list):
    if lista_paises: 
        linea = "_" * 75
        print(f"\n{linea}\n{'NOMBRE DEL PAÍS':<22} | {'POBLACIÓN':<14} | {'SUPERFICIE KM²':<16} | {'CONTINENTE':<12}\n{linea}")
        for p in lista_paises:
            print(f"{p['nombre']:<22} | {p['poblacion']:<14,} | {p['superficie']:<16,} | {p['continente']:<12}")
        print(f"{linea}\n")

# ________________________________________________
# Agregar nuevo país (Opción 2)
# ________________________________________________
def agregar_pais(lista_paises: list):
    if not lista_paises: 
        print("\nLista vacía. Realice la carga inicial en la opción 1.")
        return        
    print("\nAGREGAR NUEVO PAÍS\nIngrese 'x' para cancelar.\n") 

# Ingreso de nombre:
    while True:
        nombre = input("Nombre del país: ").strip()      
        if nombre.lower() == 'x': 
            print("Operación cancelada.")
            return
        if not nombre: 
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
        if not nombre.replace(" ", "").isalpha(): 
            print("Dato inválido. Intente nuevamente.")
            continue

        existe = False
        for p in lista_paises:
            if p['nombre'].lower() == nombre.lower():
                existe = True
                break
        
        if existe:
            print(f"El país '{nombre}' ya existe. Intente nuevamente.")
            continue            
        break      

# Ingreso de continente:
    while True:
        nuevo_continente = input(f"Continente de {nombre}: ").strip()        
        if nuevo_continente.lower() == 'x': 
            print("Operación cancelada.")
            return
        if not nuevo_continente or not nuevo_continente.replace(" ", "").isalpha(): 
            print("Dato inválido o vacío. Intente nuevamente.")
            continue            
        break

# Ingreso de población:
    while True:
        ingreso = input(f"Población de {nombre}: ").strip()        
        if ingreso.lower() == 'x': 
            print("Operación cancelada.")
            return
        try:
            valor = int(ingreso)
            if valor <= 0: 
                print("Debe ser mayor a cero. Intente nuevamente.")
                continue
            poblacion = valor
            break 
        except ValueError: 
            print("Dato inválido. Intente nuevamente.")            

# Ingreso de superficie:
    while True:
        ingreso = input(f"Superficie en km² de {nombre}: ").strip()        
        if ingreso.lower() == 'x': 
            print("Operación cancelada.")
            return
        try:
            valor = int(ingreso)
            if valor <= 0: 
                print("Debe ser mayor a cero. Intente nuevamente.")
                continue
            superficie = valor
            break 
        except ValueError: 
            print("Dato inválido. Intente nuevamente.")

    lista_paises.append({ 
        'nombre': nombre, 'poblacion': poblacion,
        'superficie': superficie, 'continente': nuevo_continente
    })
    print(f"\n'{nombre}' fue agregado correctamente.")

# ________________________________________________
# Actualizar datos de un país (Opción 3)
# ________________________________________________
def actualizar_pais(lista_paises: list):
    if len(lista_paises) == 0: 
        print("\nLa lista de países está vacía. Realice la carga inicial en la opción 1.")
        return
        
    print("\nACTUALIZAR DATOS DE UN PAÍS")
    print("Ingrese 'x' para cancelar y volver al menú principal\n") 
    
    while True:
        pais_buscar = input("Ingrese el nombre del país a modificar: ").strip()        
        if pais_buscar.lower() == 'x': 
            print("Operación cancelada.")
            return
        if not pais_buscar:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue            

        busqueda_limpia = pais_buscar.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

        pais_encontrado = None
        for p in lista_paises:
            nombre_lista_limpio = p['nombre'].lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            
            if nombre_lista_limpio == busqueda_limpia:
                pais_encontrado = p
                break                
        
        if pais_encontrado is None: 
            print(f"El país '{pais_buscar}' no se encuentra. Intente nuevamente.")
            continue            
        break 
    
    cont_ant = pais_encontrado['continente']
    pobl_ant = pais_encontrado['poblacion']
    sup_ant = pais_encontrado['superficie']

    print(f"\nPaís seleccionado: {pais_encontrado['nombre']}")
    print("(Presione ENTER para conservar el valor actual sin cambios)\n")

# Modificar continente:
    while True:
        ingreso = input("Nuevo continente: ").strip()
        if ingreso.lower() == 'x':
            print("Operación cancelada.")
            return
        if not ingreso:
            break
        if not ingreso.replace(" ", "").isalpha():
            print("El dato ingresado no corresponde. Intente nuevamente.")
            continue
        pais_encontrado['continente'] = ingreso
        break
    
# Modificar población:
    while True:
        ingreso = input("Nueva población: ").strip()        
        if ingreso.lower() == 'x':
            print("Operación cancelada.")
            return
        if not ingreso:
            break            
        try:
            valor = int(ingreso)
            if valor <= 0:
                print("El número debe ser mayor a cero. Intente nuevamente.")
                continue
            pais_encontrado['poblacion'] = valor
            break
        except ValueError:
            print("Dato ingresado incorrecto. Intente nuevamente.")
            
# Modificar superficie:
    while True:
        ingreso = input("Nueva superficie en km²: ").strip()        
        if ingreso.lower() == 'x':
            print("Operación cancelada.")
            return
        if not ingreso:
            break  
        try:
            valor = int(ingreso)
            if valor <= 0:
                print("El número debe ser mayor a cero. Intente nuevamente.")
                continue
            pais_encontrado['superficie'] = valor
            break
        except ValueError:
            print("Dato ingresado incorrecto. Intente nuevamente.")
            
    print(f"\nLos datos de '{pais_encontrado['nombre']}' fueron actualizados.")
    print("—" * 75)
    print(f"DATOS ANTERIORES || Continente: {cont_ant} | Población: {pobl_ant:,} | Superficie: {sup_ant:,} km²")
    print(f"DATOS NUEVOS     || Continente: {pais_encontrado['continente']} | Población: {pais_encontrado['poblacion']:,} | Superficie: {pais_encontrado['superficie']:,} km²")
    print("—" * 75)

# ________________________________________________
# Buscar país (Opción 4) 
# ________________________________________________
def buscar_pais(lista_paises: list):
    if not lista_paises:
        print("\nLista vacía. Realice la carga inicial en la opción 1.") 
        return

    print("\nBUSCAR PAÍS\nIngrese 'x' para cancelar.\n") 

    while True:
        termino = input("Ingrese texto a buscar: ").strip()
        if termino.lower() == 'x': 
            print("Operación cancelada.")
            return            
        if not termino: 
            print("No se registraron datos. Intente nuevamente.")
            continue

        termino_limpio = termino.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

        encontrado = []
        for p in lista_paises:
            nombre_limpio = p['nombre'].lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            if termino_limpio in nombre_limpio:
                encontrado.append(p)
        if encontrado:
            print(f"\nResultados para '{termino}':")
            tabla_final_(encontrado)
        else:
            print(f"No se encontraron coincidencias para '{termino}'. Intente nuevamente.")
        break 

# ________________________________________________
# Filtrar países (Opción 5) 
# ________________________________________________
def filtrar_paises(lista_paises: list):
    if not lista_paises:
        print("\nLista vacía. Realice la carga inicial en la opción 1.")
        return

    print("\nFILTRADO DE PAÍSES\n1) Por continente\n2) Por población\n3) Por superficie\n4) Cancelar")
    opcion_filtro = input("\nSeleccione opción: ").strip()
   
    if opcion_filtro == "1":
        print("\nFILTRAR POR CONTINENTE\nIngrese 'x' para cancelar.\n") 
        while True:
            busca_cont = input("Continente: ").strip()
            if busca_cont.lower() == 'x': 
                return
            if not busca_cont or not busca_cont.replace(" ", "").isalpha(): 
                print("Dato incorrecto. Intente nuevamente.")
                continue
            
            busca_cont_limpio = busca_cont.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            
            resultado = []
            for p in lista_paises:
                cont_limpio = p['continente'].lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                if cont_limpio == busca_cont_limpio:
                    resultado.append(p)
            if resultado:
                print(f"\nHay {len(resultado)} países en '{busca_cont}':")
                tabla_final_(resultado)
                return 
            print(f"No se encontraron países en '{busca_cont}'. Intente nuevamente.")

    elif opcion_filtro in ("2", "3"):
        tipo = "poblacion" if opcion_filtro == "2" else "superficie"
        
        if tipo == "poblacion":
            print("\nFILTRAR POR POBLACIÓN")
        else:
            print("\nFILTRAR POR SUPERFICIE")
            
        print("Ingrese 'x' para cancelar.\n") 
        
        while True:
            min_ingreso = input("Mínimo: ").strip()
            if min_ingreso.lower() == 'x': return
            max_ingreso = input("Máximo: ").strip()
            if max_ingreso.lower() == 'x': return
            
            try:
                val_min, val_max = int(min_ingreso), int(max_ingreso)
                if val_min < 0 or val_max < 0 or val_max < val_min:
                    print("Valor ingresado inexistente. Intente nuevamente.")
                    continue
                
                resultado = []
                for p in lista_paises:
                    if val_min <= p[tipo] <= val_max:
                        resultado.append(p)

                if resultado:
                    print(f"\nResultados en el rango [{val_min:,} - {val_max:,}]:")
                    tabla_final_(resultado)
                    return 
                print("No hay países en este rango. Intente nuevamente")
            except ValueError: 
                print("Deben ser números enteros. Intente nuevamente.")
    else:
        print("\nOperación cancelada.")

# ________________________________________________
# Ordenar países (Opción 6)
# ________________________________________________
def ordenar_paises(lista_paises: list):
    if not lista_paises:
        print("\nLa lista está vacía. Realice la carga inicial.")
        return

    print("\nORDENAR PAÍSES\n1) Por nombre\n2) Por población\n3) Por superficie\n4) Cancelar")
    opcion = input("\nSeleccione una opción: ").strip()
    mapa_claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    if opcion not in mapa_claves:
        print("\nOperación cancelada.")
        return
    
    clave = mapa_claves[opcion]
    print("\n1) Ascendente\n2) Descendente")
    sentido = input("\nSeleccione sentido: ").strip()
    if sentido not in ("1", "2"): 
        print("\nOpción inválida. Intente nuevamente.")
        return

    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            val1 = lista_ordenada[j][clave].lower() if clave == "nombre" else lista_ordenada[j][clave]
            val2 = lista_ordenada[j + 1][clave].lower() if clave == "nombre" else lista_ordenada[j + 1][clave]
            
            debe_intercambiar = (sentido == "1" and val1 > val2) or (sentido == "2" and val1 < val2)
            if debe_intercambiar:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    print(f"\nLista ordenada por {clave.upper()}:")
    tabla_final_(lista_ordenada)

# ________________________________________________
# Estadísticas avanzadas y Salir (Opción 7)
# ________________________________________________
def mostrar_estadisticas(lista_paises: list):
    print("\nESTADÍSTICAS AVANZADAS")
    if not lista_paises:
        print("No hay datos cargados en el sistema para calcular estadísticas.\n" + "—"*75)
        return

    total_pobl = 0
    total_sup = 0
    for p in lista_paises:
        total_pobl += p['poblacion']
        total_sup += p['superficie']
    
    mayor_pobl = lista_paises[0]
    menor_pobl = lista_paises[0]

    for p in lista_paises:
        if p['poblacion'] > mayor_pobl['poblacion']: 
            mayor_pobl = p
        if p['poblacion'] < menor_pobl['poblacion']: 
            menor_pobl = p

    continentes_fin = {}
    for p in lista_paises:
        cont = p['continente']
        if cont in continentes_fin:
            continentes_fin[cont] += 1
        else:
            continentes_fin[cont] = 1

    cant_paises = len(lista_paises)

    print(f"1. Población total acumulada: {total_pobl:,} habitantes.")
    print(f"2. País con MAYOR población:  {mayor_pobl['nombre']} ({mayor_pobl['poblacion']:,} habitantes).")
    print(f"3. País con MENOR población:  {menor_pobl['nombre']} ({menor_pobl['poblacion']:,} habitantes).")
    print(f"4. Promedio de población:     {total_pobl / cant_paises:,.2f} habitantes por país.")
    print(f"5. Promedio de superficie:    {total_sup / cant_paises:,.2f} km² por país.")
    print("\n6. Cantidad de países por continente:")
    for continente, cantidad in continentes_fin.items():
        print(f"   - {continente}: {cantidad} país(es).")
    print("—"*75)

# ________________________________________________
# Menú:
# ________________________________________________
def main():
    lista_paises = []  
    while True:
        print("GESTIÓN DE DATOS DE PAÍSES\n")
        print("1) Carga inicial de países\n2) Agregar nuevo país\n3) Actualizar datos de un país")
        print("4) Buscar país\n5) Filtrar países\n6) Ordenar países\n7) Estadísticas avanzadas y Salir\n")
        
        try:            
            opcion = int(input("Ingrese una opción: ").strip())
            if opcion == 1:
                lista_paises = cargar_paises_csv("paises.csv")
                tabla_final_(lista_paises)
            elif opcion == 2:
                agregar_pais(lista_paises)
                tabla_final_(lista_paises)
            elif opcion == 3:
                actualizar_pais(lista_paises)
                tabla_final_(lista_paises)
            elif opcion == 4:
                buscar_pais(lista_paises)
            elif opcion == 5:
                filtrar_paises(lista_paises)
            elif opcion == 6:
                ordenar_paises(lista_paises)
            elif opcion == 7:
                mostrar_estadisticas(lista_paises)
                print("Sistema cerrado.")
                break
            else:
                print("\nOpción incorrecta. Ingrese un número del 1 al 7.")
        except ValueError:
            print("\nPor favor, ingrese un número entero.")

if __name__ == "__main__":
    main()