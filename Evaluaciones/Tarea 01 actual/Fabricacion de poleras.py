t=1
lista=[]
poleras2=[]
poleras1=[]
lista= lista + poleras1 + poleras2  #Para integrar ls listas
while t==1:
    op=0
    while op not in range(1,6):
        print("\n************* MENU *************")
        print("\n SISTEMA DE PLANIFICACION DE FABRICACION DE POLERAS")
        print("1) Generar plan de fabricacion.")
        print("2) Ingresar cantidad y precio de fabricacion por tipo de polarea y dia.")
        print("3) Visualizar el ingreso total de un tipo de polera especifica.")
        print("4) Visualisar el ingreso total de todos los tipos de poleras en uun dia especifico.")
        print("5) Salir del programa.")
        op=int(input("Ingrese su opcion: "))
        if op not in range(1,6):
            print("****************************************************************************")
            print("\nNumero no valido, intente nuevamente.")
        if op==1:
            print("**********************************************")
            print("\nGENERAR PLAN DE FABRICACION") 
            #Para salir puedes poner una opcion de salir sub menu y definir op a 0 para vovler.
            #Ingresar numero de tipos de poleras.
            #Ingresar numero de dias de fabricacion
            

            print("\nPlan de fabricacion.")
            print("******************************")

        if op==5:
            print("Fin del programa")
            print("VUELVA PRONTO.")
            t==0