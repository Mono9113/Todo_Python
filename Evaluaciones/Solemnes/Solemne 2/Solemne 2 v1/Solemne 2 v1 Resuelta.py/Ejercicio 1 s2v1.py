candidatos= [('Farkas','F'),('Boris','B'),('Profe','P')]
votos = [('I', 'BFBBBFFPF'), ('II', 'PBPPFFBBPF'), ('RM', 'PPPFFBBPFP')]

# A. Función que indica el ganador de una región
def local(region, votos):
    for reg, secuencia in votos:
        if reg == region:
            conteo = {}
            for voto in secuencia:
                conteo[voto] = conteo.get(voto, 0) + 1
            return max(conteo, key=conteo.get)  # etiqueta con más votos
    return None  # si no se encuentra la región

# B. Función que indica el ganador nacional (más regiones ganadas)
def ganador(candidatos, votos):
    etiquetas_a_nombres = {etq: nom for nom, etq in candidatos}
    conteo_regiones = {}

    for reg, _ in votos:
        etiqueta_ganadora = local(reg, votos)
        if etiqueta_ganadora:
            conteo_regiones[etiqueta_ganadora] = conteo_regiones.get(etiqueta_ganadora, 0) + 1

    etiqueta_mas_regiones = max(conteo_regiones, key=conteo_regiones.get)
    return etiquetas_a_nombres[etiqueta_mas_regiones]

print(local('I', votos))  
print(local('II', votos))  # 'F'
print(local('III', votos))
print(local('RM',votos))  
print(ganador(candidatos, votos))  # 'Profe de Progra'
