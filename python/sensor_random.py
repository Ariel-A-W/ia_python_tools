import json
import random

# Número de transacciones a generar
NUM_TRANSACTIONS = 1000
TOGGLE = 0

# Generar datos simulados
transactions = []
for _ in range(NUM_TRANSACTIONS):   
    TOGGLE = TOGGLE + 1;  
    if (TOGGLE < 700): 
        transaction = { 
            "Temperatura": round(random.randrange(850, 870), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
            "Vibracion": round(random.randrange(12, 15), 2) / 10,  # Vibración 0.1 hasta 2.5
            "Humedad": round(random.randrange(50, 60), 2),  # Humedad 0% hasta 50%
            "IsFaulty": True 
        }
        transactions.append(transaction)         
    else: 
        transaction = { 
            "Temperatura": round(random.randrange(790, 820), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
            "Vibracion": round(random.randrange(5, 8), 2) / 10,  # Vibración 0.1 hasta 2.5
            "Humedad": round(random.randrange(40, 45), 2),  # Humedad 0% hasta 50%
            "IsFaulty": False 
        }
        transactions.append(transaction)         


    # if (TOGGLE > -1 & TOGGLE < 100):
    #     transaction = { 
    #         "Temperatura": round(random.randrange(850, 870), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
    #         "Vibracion": round(random.randrange(12, 15), 2) / 10,  # Vibración 0.1 hasta 2.5
    #         "Humedad": round(random.randrange(50, 60), 2),  # Humedad 0% hasta 50%
    #         "IsFaulty": True  
    #     }
    #     transactions.append(transaction)        
    #     # TOGGLE = 1 
    # elif(TOGGLE > 99 & TOGGLE < 350):
    #     transaction = { 
    #         "Temperatura": round(random.randrange(790, 820), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
    #         "Vibracion": round(random.randrange(5, 8), 2) / 10,  # Vibración 0.1 hasta 2.5
    #         "Humedad": round(random.randrange(40, 45), 2),  # Humedad 0% hasta 50%
    #         "IsFaulty": False 
    #     }
    #     transactions.append(transaction)  
    # elif(TOGGLE > 349 & TOGGLE < 500):   
    #     transaction = { 
    #         "Temperatura": round(random.randrange(850, 870), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
    #         "Vibracion": round(random.randrange(12, 15), 2) / 10,  # Vibración 0.1 hasta 2.5
    #         "Humedad": round(random.randrange(50, 60), 2),  # Humedad 0% hasta 50%
    #         "IsFaulty": True  
    #     }
    #     transactions.append(transaction)              
    # else:
    #     transaction = { 
    #         "Temperatura": round(random.randrange(790, 820), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
    #         "Vibracion": round(random.randrange(5, 8), 2) / 10,  # Vibración 0.1 hasta 2.5
    #         "Humedad": round(random.randrange(40, 45), 2),  # Humedad 0% hasta 50%
    #         "IsFaulty": False 
    #     }
    #     transactions.append(transaction)        
    #     # TOGGLE = 0

    # transaction = { 
    #     "Temperatura": round(random.randrange(300, 1800), 2),  # Temperatura Kelvin 0 (-273.15 C°) - 3731.5 (1000 C°)
    #     "Vibracion": round(random.randrange(1, 25), 2) / 10,  # Vibración 0.1 hasta 2.5
    #     "Humedad": round(random.randrange(0, 50), 2),  # Humedad 0% hasta 50%
    #     "IsFaulty": True if(round(random.randint(0, 1)) == 1) else False 
    # }
    # transactions.append(transaction)

# Guardar los datos en un archivo JSON
output_file = "sensor.json"
with open(output_file, "w") as file:
    json.dump(transactions, file, indent=4)

print(f"Datos generados y guardados en {output_file}")