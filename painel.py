from flask import Flask, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def painel():
    res = supabase.table("disparos").select("*").execute()
    dados = res.data  
    return render_template('painel.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)