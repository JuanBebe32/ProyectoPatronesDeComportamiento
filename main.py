from fastapi import FastAPI
import threading
from contextlib import asynccontextmanager
from monitor import monitor_loop, estado_servidor

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🚀 Inicia el monitor al arrancar
    hilo = threading.Thread(target=monitor_loop, daemon=True)
    hilo.start()
    
    yield
    
    # (opcional) aquí podrías cerrar cosas al apagar

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"mensaje": "Radar de servidor activo"}

@app.get("/estado")
def obtener_estado():
    return estado_servidor