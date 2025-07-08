import requests
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

INSTANCE_ID = os.getenv("INSTANCE_ID")
INSTANCE_TOKEN = os.getenv("INSTANCE_TOKEN")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")

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
