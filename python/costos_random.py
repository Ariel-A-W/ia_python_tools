import json
import random
import os

# Parámetros
ubicaciones = [
    "Buenos Aires", "CABA", "Vicente López", "Florida", "Villa Martelli", "Florida Oeste",
    "Olivos", "La Lucila", "Munro", "Carapachay", "Villa Adelina", "Martínez", "Villa Adelina",
    "Boulogne", "Acassuso", "San Isidro", "Beccar", "Victoria", "Virreyes", "San Fernando", 
    "Tigre", "Troncos del Talar", "General Pacheco", "Ricardo Rojas", "El Talar", "Don Torcuato",
    "Rincón de Milberg", "Benavídez", "Dique Luján", "Villa Maipú", "San Martín", "Villa Lynch",
    "San Andrés", "Villa Ballester", "Billinghurst", "José León Suárez", "Loma Hermosa", 
    "Área de Promoción El Triángulo", "Tortuguitas", "Grand Bourg", "Pablo Nogués", "Los Polvorines",
    "Villa de Mayo", "Ingeniero Adolfo Sourdeaux", "Del Viso", "Tortuguitas", "José C. Paz",
    "San Miguel", "Muñiz", "Bella Vista", "Campo de Mayo", "Sáenz Peña", "Villa Raffo", "José Ingenieros",
    "Ciudadela", "Santos Lugares", "Caseros", "Villa Bosch", "Martín Coronado", 
    "Ciudad Jardín Lomas del Palomar", "Loma Hermosa", "Pablo Podestá", "El Libertador", "Churruca",
    "Once de Septiembre", "Remedios de Escalada", "Villa Sarmiento", "El Palomar", "Haedo", "Morón",
    "Castelar", "Hurlingham", "William C. Morris", "Villa Tesei", "Ituzaingó", "Udaondo", "Trujui",
    "Paso del Rey", "Moreno", "La Reja", "Francisco Álvarez", "Cuartel V", "Merlo", "San Antonio de Padua",
    "Libertad", "Parque San Martín", "Mariano Acosta", "Pontevedra", "Ramos Mejía", "Lomas del Mirador",
    "La Tablada", "Villa Madero", "Tapiales", "Aldo Bonzi", "San Justo", "Villa Luzuriaga", "Isidro Casanova",
    "Ciudad Evita", "Gregorio de Laferrere", "Rafael Castillo", "González Catán", "Virrey del Pino",
    "20 de Junio", "Dock Sud", "Avellaneda", "Piñeyro", "Gerli", "Crucecita", "Sarandí", "Villa Domínico",
    "Wilde", "Valentín Alsina", "Lanús Oeste", "Gerli", "Lanús", "Remedios de Escalada", "Monte Chingolo",
    "Villa Fiorito", "Ingeniero Budge", "Villa Centenario", "Banfield", "Lomas de Zamora", "Temperley",
    "Turdera", "Llavallol", "Don Bosco", "Bernal Oeste", "Bernal", "Quilmes", "Quilmes Oeste",
    "Ezpeleta", "Ezpeleta Oeste", "Villa La Florida", "San Francisco Solano", "San José", "José Mármol",
    "Rafael Calzada", "San Francisco Solano", "Claypole", "Adrogué", "Burzaco", "Malvinas Argentinas",
    "Don Orione", "Longchamps", "Glew", "Ministro Rivadavia", "9 de Abril", "Luis Guillón", "Monte Grande",
    "El Jagüel", "Canning", "Esteban Echeverría", "José María Ezeiza", "La Unión", "Tristán Suárez",
    "Canning", "Carlos Spegazzini", "Berazategui", "Berazategui Oeste", "Villa España", "Sourigues",
    "Ranelagh", "Plátanos", "Guillermo Hudson", "Juan María Gutiérrez", "El Pato", "Pereyra", 
    "Florencio Varela", "Gobernador Costa", "Zeballos", "Villa Vatteone", "Santa Rosa", "Bosques",
    "Villa San Luis", "Villa Brown", "Ingeniero Allan", "La Capilla", "Núñez", "Saavedra", "Coghlan",
    "Belgrano", "Villa Urquiza", "Palermo", "Colegiales", "Villa Ortúzar", "Parque Chas", "Chacarita",
    "Recoleta", "Barrio Norte", "Retiro", "Villa Pueyrredón", "Agronomía", "Villa Devoto", "Villa del Parque",
    "La Paternal", "Villa Crespo", "Villa Real", "Monte Castro", "Villa Santa Rita", "Villa General Mitre",
    "Caballito", "Almagro", "Balvanera", "San Nicolás", "Puerto Madero", "Monserrat", "San Telmo",
    "La Boca", "Constitución", "Barracas", "Parque Patricios", "San Cristóbal", "Boedo", "Parque Chacabuco",
    "Nueva Pompeya", "Flores", "Floresta", "Vélez Sársfield", "Villa Luro", "Versalles", "Liniers", 
    "Mataderos", "Parque Avellaneda", "Villa Soldati", "Villa Lugano", "Villa Riachuelo",                  
]
tipos_vivienda = ["Casa", "Departamento", "PH", "Duplex", "Quinta"]
datos_inmuebles = []

# Generar 1000 registros
for i in range(1, 1001):
    registro = {
        "Id": i,
        "Ubicacion": random.choice(ubicaciones),
        "TamanioM2": random.randint(40, 300),
        "Habitaciones": random.randint(1, 5),
        "Banios": random.randint(1, 3),
        "TipoVivienda": random.choice(tipos_vivienda),
        "Antiguedad": random.randint(0, 50),  # Antigüedad en años
        "Precio": random.randint(50000, 500000)  # Valor en dólares
    }
    datos_inmuebles.append(registro)

# Nombre del archivo
nombre_archivo = "inmuebles_buenos_aires.json"

# Guardar en archivo JSON
try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos_inmuebles, archivo, indent=4, ensure_ascii=False)
    print(f"Archivo generado correctamente: {os.path.abspath(nombre_archivo)}")
    print(f"Total de registros: {len(datos_inmuebles)}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")