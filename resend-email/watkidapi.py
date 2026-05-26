import resend
import os

resend.api_key = os.environ.get("RESEND_API_KEY")

def send_pipeline_notification(status: str, image_tag: str, health: str):
    asunto = "[Watkit API] Deploy exitoso" if status == "success" \
              else "[Watkit API] Rollback ejecutado"

    cuerpo = f"""
    <h2>Reporte de Pipeline - Watkit API</h2>
    <p><b>Estado:</b> {status}</p>
    <p><b>Imagen:</b> {image_tag}</p>
    <p><b>Health:</b> {health}</p>
    """

    params: resend.Emails.SendParams = {
        "from": "onboarding@resend.dev",
        "to": ["hmaciel2004@gmail.com"],
        "subject": asunto,
        "html": cuerpo,
    }

    email = resend.Emails.send(params)
    return email

if __name__ == "__main__":
    resultado = send_pipeline_notification(
        status="success",
        image_tag="watkit-api:latest",
        health="ok"
    )
    print(resultado)
