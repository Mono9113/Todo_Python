nombre=input("Ingrese su nombre: ")
direccion=input("Ingrese su direccion: ")
total=0
cantidad=0
total_choc=0
cantidad_choc=0
total_mast=0
cantidad_mast=0
total_papas=0
cantidad_papas=0
total_ramitas=0
cantidad_ramitas=0
total_vain=0
cantidad_vain=0
total_frut=0
cantidad_frut=0
total_past=0
cantidad_past=0
total_caz=0
cantidad_caz=0
cat_dulce=0
cat_salad=0
cat_helados=0
cat_colaciones=0
total_pago=0
desc_cola=0
desc_dulce=0
desc_salado=0
desc_helado=0
desc_cat=0
desc_todo=0

t=1
while t==1:
    print("**************************** Menu principal ***********************")
    print("Bienvenido a Dulce Tentacion, eliga una categoria:")
    print("1) Dulces")
    print("2) Salados")
    print("3) Helados")
    print("4) Colaciones")
    print("5) Finalizar compra")
    op= int(input("Ingrese una opcion: "))
    print("*******************************************************************")
    while op==1:
        print("Dulces")
        print("1) Chocolate $1500")
        print("2) Masticable $1000")
        print("3) Menu principal")
        producto=int(input("Eliga producto: "))
        if producto==1:
            cant=(int(input("Ingrese cantidad: ")))
            total_choc=total_choc+cant*1500
            cantidad_choc=cantidad_choc+cant
            total=total_choc+total
            cantidad=cantidad_choc+cantidad
            cat_dulce=cat_dulce+cantidad_choc
        if producto==2:
            cant=(int(input("Ingrese cantidad: ")))
            total_mast=total_mast+cant*1000
            cantidad_mast=cantidad_mast+cant
            total=total_mast+total
            cantidad=cantidad_mast+cantidad
            cat_dulce=cat_dulce+cantidad_mast
        if producto==3:
            print("**************************** Menu principal ***********************")
            print("Bienvenido a Dulce Tentacion, eliga una categoria:")
            print("1) Dulces")
            print("2) Salados")
            print("3) Helados")
            print("4) Colaciones")
            print("5) Finalizar compra")
            op = int(input("Ingrese una opcion: "))
            print("*******************************************************************")
    while op==2:
        print("Salados")
        print("1) Papas fritas $2500")
        print("2) Ramitas $1500")
        print("3) Menu principal")
        producto=int(input("Eliga producto: "))
        if producto==1:
            cant=(int(input("Ingrese cantidad: ")))
            total_papas=total_papas+cant*2500
            cantidad_papas=cantidad_papas+cant
            total=total_papas+total
            cantidad=cantidad_papas+cantidad
            cat_salad=cat_salad+cantidad_papas
        if producto==2:
            cant=(int(input("Ingrese cantidad: ")))
            total_ramitas=total_ramitas+cant*1500
            cantidad_ramitas=cantidad_ramitas+cant
            total=total_ramitas+total
            cantidad=cantidad_ramitas+cantidad
            cat_salad=cat_salad+cantidad_ramitas
        if producto==3:
            print("**************************** Menu principal ***********************")
            print("Bienvenido a Dulce Tentacion, eliga una categoria:")
            print("1) Dulces")
            print("2) Salados")
            print("3) Helados")
            print("4) Colaciones")
            print("5) Finalizar compra")
            op = int(input("Ingrese una opcion: "))
            print("*******************************************************************")
    while op == 3:
        print("Helados")
        print("1) Vainilla $1250")
        print("2) Frutilla $1250")
        print("3) Menu principal")
        producto = int(input("Eliga producto: "))
        if producto == 1:
            cant = (int(input("Ingrese cantidad: ")))
            total_vain = total_vain + cant * 1250
            cantidad_vain = cantidad_vain + cant
            total=total_vain+total
            cantidad=cantidad_vain+cantidad
            cat_helados=cat_helados+cantidad_vain
        if producto == 2:
            cant = (int(input("Ingrese cantidad: ")))
            total_frut = total_frut + cant * 1250
            cantidad_frut = cantidad_frut + cant
            total=total_frut+total
            cantidad=cantidad_frut+cantidad
            cat_helados=cat_helados+cantidad_frut
        if producto == 3:
            print("**************************** Menu principal ***********************")
            print("Bienvenido a Dulce Tentacion, eliga una categoria:")
            print("1) Dulces")
            print("2) Salados")
            print("3) Helados")
            print("4) Colaciones")
            print("5) Finalizar compra")
            op = int(input("Ingrese una opcion: "))
            print("*******************************************************************")
    while op==4:
        print("Colaciones")
        print("1) Pastel de papas $6000")
        print("2) Cazuela $7500")
        print("3) Menu principal")
        producto=int(input("Eliga producto: "))
        if producto==1:
            cant=(int(input("Ingrese cantidad: ")))
            total_past=total_past+cant*6000
            cantidad_past=cantidad_past+cant
            total=total_past+total
            cantidad=cantidad_past+cantidad
            cat_colaciones=cat_colaciones+cantidad_past
        if producto==2:
            cant=(int(input("Ingrese cantidad: ")))
            total_caz=total_caz+cant*7500
            cantidad_caz=cantidad_caz+cant
            total=total_caz+total
            cantidad=cantidad_caz+cantidad
            cat_colaciones=cat_colaciones+cantidad_caz
        if producto==3:
            print("**************************** Menu principal ***********************")
            print("Bienvenido a Dulce Tentacion, eliga una categoria:")
            print("1) Dulces")
            print("2) Salados")
            print("3) Helados")
            print("4) Colaciones")
            print("5) Finalizar compra")
            op = int(input("Ingrese una opcion: "))
            print("*******************************************************************")
    if op==5:
        print("Eliga medio de pago: ")
        print("1) Debito")
        print("2) Credito")
        print("3) Transferencia")
        print("4) Vovler al menu principal")
        metodo_pago= int(input("Ingrese su metodo de pago: "))
    while metodo_pago==1:
        print("************************ Factura ******************************")
        print("Nombre: ", nombre)
        print("Direccion: ", direccion)
        print("Medio de pago: Debito")
        print("Detalle de la compra:\n")
        if cantidad_choc >= 1:
            print("Producto: Chocolate")
            print("Cantidad:", cantidad_choc)
            print("Precio unitario: $1500")
            print("Subtotal: ", total_choc)
        if cantidad_mast >= 1:
            print("Producto: Masticable")
            print("Cantidad:", cantidad_mast)
            print("Precio unitario: $1000")
            print("Subtotal: ", total_mast)
        if cantidad_papas >= 1:
            print("Producto: Papas Fritas")
            print("Cantidad:", cantidad_papas)
            print("Precio unitario: $2500")
            print("Subtotal: ", total_papas)
        if cantidad_ramitas >= 1:
            print("Producto: Ramitas")
            print("Cantidad:", cantidad_ramitas)
            print("Precio unitario: $1500")
            print("Subtotal: ", total_ramitas)
        if cantidad_vain >= 1:
            print("Producto: Helado vainilla")
            print("Cantidad:", cantidad_vain)
            print("Precio unitario: $1250")
            print("Subtotal: ", total_vain)
        if cantidad_frut >= 1:
            print("Producto: Helado Frutilla")
            print("Cantidad:", cantidad_frut)
            print("Precio unitario: $1250")
            print("Subtotal: ", total_frut)
        if cantidad_past >= 1:
            print("Producto: Pastel e papas")
            print("Cantidad:", cantidad_past)
            print("Precio unitario: $6000")
            print("Subtotal: ", total_past)
        if cantidad_caz >= 1:
            print("Producto: Cazuela")
            print("Cantidad:", cantidad_caz)
            print("Precio unitario: $7500")
            print("Subtotal: ", total_caz)
        print(" ")
        if cat_dulce >= 5:
                desc_dulce = (total_choc+total_mast) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_salad >= 5:
                desc_salado = (total_papas+total_ramitas) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_helados >= 5:
                desc_helado = (total_vain+total_frut) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_colaciones >= 5:
                desc_cola = (total_past+total_caz) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if desc_cat > 0:
            print("Descuento por cantidad en la misma categoria: ", desc_cat)
        if cat_dulce >= 10 and cat_salad >= 10 and cat_helados >= 10 and cat_colaciones >= 10:
            print("Descuento por compras en mas de 10 en todas las categorias:",total*0.10)
            total_pago = total*0.10
        print("Descuento asociado a pago con tarjeta de debito: ", total*0.02)
        pago_debito = total*0.02
        print("\n Total a pagar: $",total-total_pago-desc_cat-pago_debito)
        t==2
    while metodo_pago==2:
        print("************************ Factura ******************************")
        print("Nombre: ", nombre)
        print("Direccion: ", direccion)
        print("Medio de pago: Credito")
        print("Detalle de la compra:\n")
        if cantidad_choc >= 1:
            print("Producto: Chocolate")
            print("Cantidad:", cantidad_choc)
            print("Precio unitario: $1500")
            print("Subtotal: ", total_choc)
        if cantidad_mast >= 1:
            print("Producto: Masticable")
            print("Cantidad:", cantidad_mast)
            print("Precio unitario: $1000")
            print("Subtotal: ", total_mast)
        if cantidad_papas >= 1:
            print("Producto: Papas Fritas")
            print("Cantidad:", cantidad_papas)
            print("Precio unitario: $2500")
            print("Subtotal: ", total_papas)
        if cantidad_ramitas >= 1:
            print("Producto: Ramitas")
            print("Cantidad:", cantidad_ramitas)
            print("Precio unitario: $1500")
            print("Subtotal: ", total_ramitas)
        if cantidad_vain >= 1:
            print("Producto: Helado vainilla")
            print("Cantidad:", cantidad_vain)
            print("Precio unitario: $1250")
            print("Subtotal: ", total_vain)
        if cantidad_frut >= 1:
            print("Producto: Helado Frutilla")
            print("Cantidad:", cantidad_frut)
            print("Precio unitario: $1250")
            print("Subtotal: ", total_frut)
        if cantidad_past >= 1:
            print("Producto: Pastel e papas")
            print("Cantidad:", cantidad_past)
            print("Precio unitario: $6000")
            print("Subtotal: ", total_past)
        if cantidad_caz >= 1:
            print("Producto: Cazuela")
            print("Cantidad:", cantidad_caz)
            print("Precio unitario: $7500")
            print("Subtotal: ", total_caz)
        print(" ")
        if cat_dulce >= 5:
                desc_dulce = (total_choc+total_mast) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_salad >= 5:
               desc_salado = (total_papas+total_ramitas) * 0.02
               desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_helados >= 5:
                desc_helado = (total_vain+total_frut) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_colaciones >= 5:
                desc_cola = (total_past+total_caz) * 0.02
                desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if desc_cat > 0:
               print("Descuento por cantidad en la misma categoria: ", desc_cat)
        if cat_dulce >= 10 and cat_salad >= 10 and cat_helados >= 10 and cat_colaciones >= 10:
              print("Descuento por compras en mas de 10 en todas las categorias:",total*0.10)
              total_pago = total*0.10
        print("\n Total a pagar: $", total - total_pago - desc_cat)
        print("Cantidad total de productos: ", cantidad)
        t==2
    while metodo_pago==3:
        print("************************ Factura ******************************")
        print("Nombre: ", nombre)
        print("Direccion: ", direccion)
        print("Medio de pago: Transferencia")
        print("Detalle de la compra:\n")
        if cantidad_choc >= 1:
                print("Producto: Chocolate")
                print("Cantidad:", cantidad_choc)
                print("Precio unitario: $1500")
                print("Subtotal: ", total_choc)
        if cantidad_mast >= 1:
                print("Producto: Masticable")
                print("Cantidad:", cantidad_mast)
                print("Precio unitario: $1000")
                print("Subtotal: ", total_mast)
        if cantidad_papas >= 1:
                print("Producto: Papas Fritas")
                print("Cantidad:", cantidad_papas)
                print("Precio unitario: $2500")
                print("Subtotal: ", total_papas)
        if cantidad_ramitas >= 1:
                print("Producto: Ramitas")
                print("Cantidad:", cantidad_ramitas)
                print("Precio unitario: $1500")
                print("Subtotal: ", total_ramitas)
        if cantidad_vain >= 1:
                print("Producto: Helado vainilla")
                print("Cantidad:", cantidad_vain)
                print("Precio unitario: $1250")
                print("Subtotal: ", total_vain)
        if cantidad_frut >= 1:
                print("Producto: Helado Frutilla")
                print("Cantidad:", cantidad_frut)
                print("Precio unitario: $1250")
                print("Subtotal: ", total_frut)
        if cantidad_past >= 1:
                print("Producto: Pastel e papas")
                print("Cantidad:", cantidad_past)
                print("Precio unitario: $6000")
                print("Subtotal: ", total_past)
        if cantidad_caz >= 1:
                print("Producto: Cazuela")
                print("Cantidad:", cantidad_caz)
                print("Precio unitario: $7500")
                print("Subtotal: ", total_caz)
        print(" ")
        if cat_dulce >= 5:
            desc_dulce = (total_choc+total_mast) * 0.02
            desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_salad >= 5:
            desc_salado = (total_papas+total_ramitas) * 0.02
            desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_helados >= 5:
            desc_helado = (total_vain+total_frut) * 0.02
            desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if cat_colaciones >= 5:
            desc_cola = (total_past+total_caz) * 0.02
            desc_cat = desc_dulce + desc_salado + desc_helado + desc_cola
        if desc_cat > 0:
            print("Descuento por cantidad en la misma categoria: ", desc_cat)
        if cat_dulce >= 10 and cat_salad >= 10 and cat_helados >= 10 and cat_colaciones >= 10:
            print("Descuento por compras en mas de 10 en todas las categorias:",total*0.10)
            total_pago = total*0.10
        print("Envio gratis por pago con transferencia")
        print("\n Total a pagar: $", total - total_pago - desc_cat)
        print("Cantidad total de productos: ", cantidad)
        print("*********************************************************")
        t==2
    if metodo_pago == 4:
        print("**************************** Menu principal ***********************")
        print("Bienvenido a Dulce Tentacion, eliga una categoria:")
        print("1) Dulces")
        print("2) Salados")
        print("3) Helados")
        print("4) Colaciones")
        print("5) Finalizar compra")
        op = int(input("Ingrese una opcion: "))
        print("*******************************************************************")
        
    













