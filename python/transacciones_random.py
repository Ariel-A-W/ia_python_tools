import json
import random

# Número de transacciones a generar
NUM_TRANSACTIONS = 1000

# Generar datos simulados
transactions = []
for _ in range(NUM_TRANSACTIONS):
    transaction = {
        "Monto": round(random.uniform(10, 10000), 2),  # Cantidad entre 10 y 10000
        "Frecuencia": random.randint(1, 30),  # Frecuencia de la transacción en días
        "TiempoTransaccion": round(random.uniform(0, 24), 2)  # Hora del día (0-24 horas)
    }
    transactions.append(transaction)

# Guardar los datos en un archivo JSON
output_file = "transacciones.json"
with open(output_file, "w") as file:
    json.dump(transactions, file, indent=4)

print(f"Datos generados y guardados en {output_file}")