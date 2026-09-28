from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

html_code = """
<!DOCTYPE html><html><body style="background:#111;color:white;text-align:center;padding:50px;font-family:sans-serif">
<h1>Comic Craft AI</h1>
<input id="p" style="width:80%;padding:10px" value="Thanos in Tirupattur">
<button onclick="gen()" style="padding:10px">Generate</button>
<pre id="o" style="white-space:pre-wrap;text-align:left;background:#222;padding:20px;margin-top:20px"></pre>
<script>
async function gen(){
document.getElementById('o').innerText='Loading...';
let r=await fetch('/api/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:document.getElementById('p').value})});
let d=await r.json(); document.getElementById('o').innerText=d.story;
}
</script></body></html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html_code

@app.post("/api/generate")
async def genapi(request: Request):
    d=await request.json(); pr=d.get("prompt","comic")
    try:
        import google.generativeai as genai
        key="AQ.Ab8RN6L3vTOWjfRRVCpJZ_M4CFK0VDZ1dOkdztqlKIzXHHsRFQ"
        genai.configure(api_key=key)
        m=genai.GenerativeModel('gemini-1.5-flash')
        resp=m.generate_content(f"Create a funny 4 panel comic story about: {pr}")
        return {"story": resp.text}
    except Exception as e:
        return {"story": f"Error: {e} Prompt was: {pr}"}