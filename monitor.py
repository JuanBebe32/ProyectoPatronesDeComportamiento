import requests
import time
from datetime import datetime

estado_servidor = {
    "status": "DESCONOCIDO",
    "tiempo_respuesta": None,
    "ultima_revision": None
}

URL = "https://watkit-api.onrender.com/"

# 🔔 TELEGRAM
TELEGRAM_TOKEN = "8676436127:AAHinYgikGendklc2Z09U72Zrmxpq5fmUjM"
CHAT_ID = "-5209230597"

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }

    try:
        response = requests.post(url, json=payload)
        print("📲 Telegram dice:", response.text)
    except Exception as e:
        print("❌ Error:", e)

def verificar_servidor():
    global estado_servidor

    try:
        inicio = time.time()
        response = requests.get(URL, timeout=1)
        tiempo = round(time.time() - inicio, 2)

        if response.status_code == 200:
            if estado_servidor["status"] == "DOWN":
                enviar_alerta("🟢 Servidor recuperado")

            estado_servidor["status"] = "UP"
        else:
            estado_servidor["status"] = "ERROR"

        estado_servidor["tiempo_respuesta"] = tiempo
        estado_servidor["ultima_revision"] = str(datetime.now())

    except:
        if estado_servidor["status"] != "DOWN":
            enviar_alerta("🔴 Servidor CAÍDO")

        estado_servidor["status"] = "DOWN"
        estado_servidor["tiempo_respuesta"] = None
        estado_servidor["ultima_revision"] = str(datetime.now())

def monitor_loop():
    while True:
        verificar_servidor()
        time.sleep(10)