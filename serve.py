#!/usr/bin/env python3
"""Servidor local simples para abrir o site personalizado do Miguel."""
import argparse, http.server, os, socketserver, threading, webbrowser
from functools import partial
ROOT=os.path.dirname(os.path.abspath(__file__))
parser=argparse.ArgumentParser(); parser.add_argument('--open',action='store_true'); parser.add_argument('--port',type=int,default=8000); args=parser.parse_args()
os.chdir(ROOT)
class Server(socketserver.ThreadingMixIn,http.server.HTTPServer): daemon_threads=True; allow_reuse_address=True
with Server(('127.0.0.1',args.port),partial(http.server.SimpleHTTPRequestHandler,directory=ROOT)) as httpd:
    url=f'http://127.0.0.1:{args.port}/'
    print('Site Miguel Franco'); print('Abrindo:',url); print('Deixe esta janela aberta. Ctrl+C para encerrar.')
    if args.open: threading.Timer(.5,lambda:webbrowser.open(url)).start()
    try: httpd.serve_forever()
    except KeyboardInterrupt: print('Servidor encerrado.')
