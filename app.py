import os
os.system("cls")
# El programa debe: 
IVA = 0.19 
PRESUPUESTO_MAXIMO = 50000000
presupuesto_elevado_en_10 = PRESUPUESTO_MAXIMO * 0.90
try:
    
    nombre_del_proyecto = input("ingrese nombre del proyecto\n").title()
    metros_a_construir = int(input("ingrese metros cuadrdados a construir\n"))
    costo_por_metro_cuadrado = int(input("ingrese costo x metro cuadrado\n")) 
    cantidad_de_trabajadores = int(input("ingrese cantidad de trabajadores\n")) 
    pago_por_trabajador = int(input("ingrese remuneracion por trabajador\n"))
    
    if metros_a_construir > 0 and costo_por_metro_cuadrado > 0 and cantidad_de_trabajadores > 0 and pago_por_trabajador > 0:
        costo_de_materiales = metros_a_construir * costo_por_metro_cuadrado 
        costo_mano_de_obra = cantidad_de_trabajadores * pago_por_trabajador
        costo_bruto = costo_mano_de_obra + costo_de_materiales
        valor_iva = costo_bruto * IVA
        costo_total = costo_bruto + valor_iva
        
        if costo_total <= PRESUPUESTO_MAXIMO:
            estado = "Dentro del presupuesto"
        elif costo_total > PRESUPUESTO_MAXIMO and costo_total <= presupuesto_elevado_en_10:
            estado = "Presupuesto ajustado"
        else:
            estado = "Fuera de presupuesto"
        
        os.system("cls")
        print(f"******")    
        print(f"Nombre del proyecto: {nombre_del_proyecto}")
        print(f"Costo total: ${costo_total}")
        print(f"Estado del proyecto: {estado}")
        print(f"******")
        
    else:
        print("uno de sus datos no esta correcto")
except:
    print("el valor ingresado debe ser numerico") 



# En caso de error, manejar la situación con try-except. 
# 4.	Calcular: 
# o	Costo de materiales = metros cuadrados × costo por metro 
# o	Costo de mano de obra = trabajadores × pago por trabajador 
# o	Costo neto = suma de ambos 
# o	IVA aplicado 
# o	Costo total del proyecto 
# 5.	Usar variables auxiliares para almacenar cálculos intermedios. 
# 6.	Determinar el estado del proyecto: 
# o	Si el costo total es menor o igual al presupuesto → Dentro del presupuesto 
# o	Si supera el presupuesto hasta en un 10% → Presupuesto ajustado 
# o	Si supera en más de un 10% → Fuera de presupuesto 
# 7.	Mostrar un resumen con: 
# o	Nombre del proyecto 
# o	Costo total (redondeado a 2 decimales) 
# o	Estado del proyecto 
# ________________________________________
