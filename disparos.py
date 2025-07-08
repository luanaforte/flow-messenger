import requests
from supabase import create_client

url = "https://ruqmxigenlqqmyxszkff.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1cW14aWdlbmxxcW15eHN6a2ZmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTkyNjgxOCwiZXhwIjoyMDY3NTAyODE4fQ.hK-JKJwFrzJP0KspRA8LhQbxPJwqH7sS4ghJPWagQzE"
supabase = create_client(url, key)

INSTANCE_ID = "3E3DAC456B9B90A80B14764AFE850DAC"
INSTANCE_TOKEN = "489DDA3C171E861775DAAADB"
CLIENT_TOKEN = "F778a0d56c08c47858f52c005956db677S"

ZAPI_URL = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{INSTANCE_TOKEN}/send-text"

HEADERS = {
    "Client-Token": CLIENT_TOKEN,
    "Content-Type": "application/json"
}

def montar_mensagem(nome, link):
    return f"""Olá {nome}, tudo bem?

Meu nome é Luana, e quero fazer parte da b2bfow.

Esse é meu disparo de mensagem para o teste.

Deixarei o código utilizado no seguinte repositório do GitHub

Link repositório: {link}

Estou à disposição"""

def enviar_mensagem(telefone, mensagem):
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    response = requests.post(ZAPI_URL, json=payload, headers=HEADERS)
    return response.ok, response.text

def main():
    res = supabase.table("disparos").select("*").eq("status", "pendente").execute()
    disparos = res.data

    if not disparos:
        print("Nenhum disparo pendente.")
        return

    for disparo in disparos:
        nome = disparo["nome"]
        telefone = disparo["telefone"]
        link = disparo["link_repositorio"]
        mensagem = montar_mensagem(nome, link)

        sucesso, resposta = enviar_mensagem(telefone, mensagem)
        print(f"\n📤 Enviando para {nome} ({telefone})")
        print("✅ Sucesso:", sucesso)
        print("📨 Resposta:", resposta)

        novo_status = "enviado" if sucesso else "erro"
        supabase.table("disparos").update({"status": novo_status}).eq("id", disparo["id"]).execute()

if __name__ == "__main__":
    main()
