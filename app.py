#!/usr/bin/env python3
"""Local-only monitor test page."""
from http.server import BaseHTTPRequestHandler,HTTPServer
import threading,webbrowser
PAGE=r"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Screencheck</title><style>
*{box-sizing:border-box}body{margin:0;background:#111827;color:white;font:15px system-ui}header{padding:16px;background:#1b2435;display:flex;justify-content:space-between}h1{font-size:20px;color:#cba6f7;margin:0}.tools{padding:12px;display:flex;gap:7px;flex-wrap:wrap}button,input{padding:9px 12px;border:1px solid #46536e;border-radius:8px;background:#26334a;color:white}.stage{height:calc(100vh - 120px);margin:0 12px;background:#000;border:1px solid #46536e;position:relative}.stage:fullscreen{height:100vh;margin:0;border:0}#read{color:#a6e3a1}</style><header><h1>SCREENCHECK</h1><span id="read">Move pointer over test area</span></header><nav class="tools"><button data-m="black">Black</button><button data-m="white">White</button><button data-m="red">Red</button><button data-m="green">Green</button><button data-m="blue">Blue</button><button data-m="gray">Gray ramp</button><button data-m="gradient">Gradient</button><button data-m="grid">Grid</button><input id="c" type="color"><button id="full">Fullscreen</button></nav><main class="stage" id="s"></main><script>
const s=document.querySelector('#s'),read=document.querySelector('#read');function mode(m){s.style.backgroundImage='';s.style.background=m;if(m==='gray')s.style.background='linear-gradient(90deg,#000,#fff)';if(m==='gradient')s.style.background='linear-gradient(90deg,#000,#f00,#ff0,#0f0,#0ff,#00f,#f0f,#fff)';if(m==='grid')s.style.background='linear-gradient(#89b4fa 1px,transparent 1px),linear-gradient(90deg,#89b4fa 1px,transparent 1px)',s.style.backgroundSize='40px 40px'}document.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>mode(b.dataset.m));document.querySelector('#c').oninput=e=>mode(e.target.value);document.querySelector('#full').onclick=()=>s.requestFullscreen?.();s.onmousemove=e=>{let r=s.getBoundingClientRect();read.textContent='X '+Math.round(e.clientX-r.left)+' · Y '+Math.round(e.clientY-r.top)};document.onkeydown=e=>{if(e.key==='Escape')document.exitFullscreen?.()};mode('black')
</script>"""
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  b=PAGE.encode();self.send_response(200);self.send_header("Content-Type","text/html; charset=utf-8");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
 def log_message(self,*a):pass
def main():
 s=HTTPServer(("127.0.0.1",8765),H);u="http://127.0.0.1:8765";print("Screencheck:",u,"Ctrl+C to stop");threading.Timer(.5,lambda:webbrowser.open(u)).start()
 try:s.serve_forever()
 except KeyboardInterrupt:s.server_close()
if __name__=="__main__":main()
