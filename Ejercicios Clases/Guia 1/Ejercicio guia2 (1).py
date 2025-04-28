t = 1
total = 0
total_pas_santiago = 0
total_pas_temuco = 0
total_pas_arica = 0
total_pas_concepcion = 0
t_ma = 0
while t == 1:
    print("*************************** Menu principal *********************")
    print("1) Santiago $18,000 por tramo")
    print("2) Arica $18,500 por tramo")
    print("3) Temuco $20,580 por tramo")
    print("4) Concepcion $18,600 por tramo")
    print("5) Salir")
    op = int(input("Ingrese opcion: "))
    print("****************************************************************")

    if op == 1:
        iv = input("Es ida y vuelta (s/n): ")
        if iv == "s":
            total += 18000 * 2
            total_pas_santiago += 2
        else:
            total = 18000
            total_pas_santiago += 1
        ma = int(input("Cuantas maletas lleva: "))
        if ma > 1:
            total = total + (ma - 1) * 5000
            t_ma = t_ma + ((ma - 1) * 5000)
        print("********************* Pasajes interurbanos ********************")
        if iv == "s":
            print("Destino: SANTIAGO ida y vuelta valor $", 18000 * 2)
        else:
            print("Destino: SANTIAGO ida valor $", 18000)
        print("Unidades de equipaje", ma, "valor $", (ma - 1) * 5000)
        print("Valor total: $", total)
    if op == 2:
        iv = input("Es ida y vuelta (s/n): ")
        if iv == "s":
            total += 18500 * 2
            total_pas_arica += 2
        else:
            total = 18000
            total_pas_arica += 1
        ma = int(input("Cuantas maletas lleva: "))
        if ma > 1:
            total = total + (ma - 1) * 5000
            t_ma = t_ma + ((ma - 1) * 5000)
        print("********************* Pasajes interurbanos ********************")
        if iv == "s":
            print("Destino: ARICA ida y vuelta valor $", 18600 * 2)
        else:
            print("Destino: ARICA ida valor $", 18600)
        print("Unidades de equipaje", ma, "valor $", (ma - 1) * 5000)
        print("Valor total: $", total)
    if op == 3:
        iv = input("Es ida y vuelta (s/n): ")
        if iv == "s":
            total += 20580 * 2
            total_pas_temuco += 2
        else:
            total = 20580
            total_pas_temuco += 1
        ma = int(input("Cuantas maletas lleva: "))
        if ma > 1:
            total = total + (ma - 1) * 5000
            t_ma = t_ma + ((ma - 1) * 5000)
        print("********************* Pasajes interurbanos ********************")
        if iv == "s":
            print("Destino: TEMUCO ida y vuelta valor $", 20580 * 2)
        else:
            print("Destino: TEMUCO ida valor $", 20580)
        print("Unidades de equipaje", ma, "valor $", (ma - 1) * 5000)
        print("Valor total: $", total)
    if op == 4:
        iv = input("Es ida y vuelta (s/n): ")
        if iv == "s":
            total += 18600 * 2
            total_pas_concepcion += 2
        else:
            total = 18000
            total_pas_concepcion += 1
        ma = int(input("Cuantas maletas lleva: "))
        if ma > 1:
            total = total + (ma - 1) * 5000
            t_ma = t_ma + ((ma - 1) * 5000)
        print("********************* Pasajes interurbanos ********************")
        if iv == "s":
            print("Destino: CONCEPCION ida y vuelta valor $", 18600 * 2)
        else:
            print("Destino: CONCEPCION ida valor $", 18600)
        print("Unidades de equipaje", ma, "valor $", (ma - 1) * 5000)
        print("Valor total: $", total)
    if op == 5:
        print("*********************** RESUMEN DEL DIA *************************")
        print("Resumen de ventas del dia:")
        print("Santiago: ", total_pas_santiago)
        print("Arica: ", total_pas_arica)
        print("Temuco: ", total_pas_temuco)
        print("Concepcion: ", total_pas_concepcion)
        print("TOTAL EN PASAJES: ", total)
        print("TOTAL EN MALETAS: ", t_ma)
        print("****************************************************************")
        t = 2
