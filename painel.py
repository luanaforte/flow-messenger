from flask import Flask, render_template
from supabase import create_client

app = Flask(__name__)

url = "https://ruqmxigenlqqmyxszkff.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1cW14aWdlbmxxcW15eHN6a2ZmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTkyNjgxOCwiZXhwIjoyMDY3NTAyODE4fQ.hK-JKJwFrzJP0KspRA8LhQbxPJwqH7sS4ghJPWagQzE"
supabase = create_client(url, key)

@app.route('/')
def painel():
    res = supabase.table("disparos").select("*").execute()
    dados = res.data  
    return render_template('painel.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)