import requests
import time
from datetime import datetime

# URL del servidor que quieres monitorear
URL = "https://google.com"  # cámbialo por tu servidor

# Intervalo en segundos
INTERVALO = 10

def verificar_servidor():
    try:
        inicio = time.time()
        response = requests.get(URL, timeout=5)
        tiempo = round(time.time() - inicio, 2)

        if response.status_code == 200:
            print(f"[{datetime.now()}] 🟢 UP - Tiempo: {tiempo}s")
        else:
            print(f"[{datetime.now()}] ⚠️ RESPUESTA RARA: {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[{datetime.now()}] 🔴 DOWN - No responde")

while True:
    verificar_servidor()
    time.sleep(INTERVALO)