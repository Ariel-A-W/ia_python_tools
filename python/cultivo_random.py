import json
import random
import os

# Parámetros
cultivoTipo = [ "Trigo", "Maíz", "Arróz", "Algodón", "Papa", "Soja" ]

datos_cultivo = []

area = 0 
lluviaAnual = 0
eficienciaRiego = 0
retencionAguaSuelo = 0
temperatura = 0
huellaHidrica = 0


# Generar 1000 registros
for i in range(1, 1001):
    tipCult = random.choice(cultivoTipo) 

    if (tipCult == "Trigo"):
        area = random.randrange(1, 100)                # por hectaria ha 
        lluviaAnual = random.randrange(400, 700)       # milímetros
        eficienciaRiego = random.randrange(50, 80)     # eficiencia de riego
        retencionAguaSuelo = random.randrange(40, 60)  # retención de agua en el suelo 
        temperatura = random.randrange(15, 25)         # temperatura
        huellaHidrica = random.randrange(1100, 1800)   # huella hídrica
    elif (tipCult == "Maíz"):
        area = random.randrange(1, 150)               
        lluviaAnual = random.randrange(600, 1000)       
        eficienciaRiego = random.randrange(60, 85)     
        retencionAguaSuelo = random.randrange(50, 70)  
        temperatura = random.randrange(20, 30)        
        huellaHidrica = random.randrange(800, 1200) 
    elif (tipCult == "Arróz"):
        area = random.randrange(1, 50)               
        lluviaAnual = random.randrange(800, 1200)       
        eficienciaRiego = random.randrange(40, 60)     
        retencionAguaSuelo = random.randrange(70, 85)  
        temperatura = random.randrange(20, 35)         
        huellaHidrica = random.randrange(1200, 1800)
    elif (tipCult == "Algodón"):
        area = random.randrange(1, 30)               
        lluviaAnual = random.randrange(500, 900)       
        eficienciaRiego = random.randrange(50, 75)     
        retencionAguaSuelo = random.randrange(40, 60)  
        temperatura = random.randrange(25, 35)         
        huellaHidrica = random.randrange(1200, 1800)
    elif (tipCult == "Papa"): 
        area = random.randrange(1, 50)               
        lluviaAnual = random.randrange(300, 600)       
        eficienciaRiego = random.randrange(60, 85)     
        retencionAguaSuelo = random.randrange(50, 70)  
        temperatura = random.randrange(10, 20)           
        huellaHidrica = random.randrange(600, 1000) 
    elif (tipCult == "Soja"):
        area = random.randrange(1, 200)               
        lluviaAnual = random.randrange(400, 800)       
        eficienciaRiego = random.randrange(55, 80)     
        retencionAguaSuelo = random.randrange(40, 65)  
        temperatura = random.randrange(20, 30)        
        huellaHidrica = random.randrange(900, 1500)

    registro = {
        "TipoCultivo" : tipCult,
        "Area": area/10, 
        "LluviaAnual": lluviaAnual, 
        "EficienciaRiego": eficienciaRiego, 
        "RetencionAguaSuelo": retencionAguaSuelo, 
        "Temperatura": temperatura,
        "HuellaHidrica": huellaHidrica
    }
    datos_cultivo.append(registro)

# Nombre del archivo
nombre_archivo = "cultivo.json"

# Guardar en archivo JSON
try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos_cultivo, archivo, indent=4, ensure_ascii=False)
    print(f"Archivo generado correctamente: {os.path.abspath(nombre_archivo)}")
    print(f"Total de registros: {len(datos_cultivo)}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")