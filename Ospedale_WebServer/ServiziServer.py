# -*- coding: utf-8 -*-
"""
 Elaborato Programmazione di Reti
            a.a. 2020/2021
    Guidazzi Federico, Matricola: 915914
    Magistri Melissa, Matricola: 941818
    Grandi Luca, Matricola: 941717
               
            Traccia 2
        Python Web Server
"""

import http.server
import socketserver
import threading 
import sys, signal

#si effettua la scelta della porta, per default si sceglie la porta 8080
if sys.argv[1:]:
     port = int(sys.argv[1])
else:
    port = 8080

waiting_refresh = threading.Event()

class ServerManager(http.server.SimpleHTTPRequestHandler):
    def get(self):
        http.server.SimpleHTTPRequestHandler.get(self)
    
#creazione del server con le funzionalità multithreading, cioè la possibilità di accesso multiplo 
server = socketserver.ThreadingTCPServer(('127.0.0.1',port), ServerManager)


footer_html= """
    </body>
</html>
"""

Header_html= """
<!DOCTYPE html>
<html>
<head>
    <style>
    .container {
        position: relative;
        width: 50%;
    }

    .image {
        opacity: 1;
        display: block;
        max-width: 300px;
        height: auto;
        transition: .5s ease;
        backface-visibility: hidden;
    }

    .middle {
        transition: .5s ease;
        opacity: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%)
      }

    .container:hover .image {
        opacity: 0.3;
    }

    .container:hover .middle {
        opacity: 1;
    }

    .topnav {
        overflow: hidden;
        background-color: #111;
    }

    .topnav a {
        float: left;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
        font-size: 30px;
    }

    .topnav a:hover {
        background-color: #ddd;
        color: black;
    }

    .topnav a.active {
        background-color: #4CAF50;
        color: white;
    }
    </style>
</head>
<body>
"""

NavigationBar_html="""
<div class="topnav">
    <a href="http://127.0.0.1:{port}"> Servizi AUSL Romagna</a>
    <a class="active" href="http://127.0.0.1:{port}/info.pdf" download="info.pdf" style="float: right">Download info pdf</a>
</div>
<br>
<br>
<table align="center">
</table>
</body>
</html>
""".format(port=port)

#metodo che crea la pagina iniziale del server con le macro sezioni
def create_initial_page():
    f = open('index.html','w', encoding="utf-8")
    try:
        message = Header_html + NavigationBar_html
        message = message + '<th><h2><center>Lista Servizi</center></h2></th></tr>'
        message=message+'''<br>
            <center>
            <div class="container">
            <img src="/images/cardiologia.png" alt="Cardiologia" class="image" style="width:100%">
            <div class="middle">
            <a href="http://127.0.0.1:{port}/cardiologia.html">Cardiologia</a>
            </div>
            </div></center>'''.format(port=port) 
          
        message=message+'''<br>
            <br>
            <br>
            <center>
            <div class="container">
            <img src="/images/chirurgiaGenerale.jpg" alt="Chirurgia" class="image" style="width:100%">
            <div class="middle">
            <a href="http://127.0.0.1:{port}/chirurgia.html">Chirurgia</a>
            </div>
            </div></center>'''.format(port=port)
        message=message+'''<br>
            <br>
            <br>
            <center>
            <div class="container">
            <img src="/images/medicina.jpg" alt="Medicina" class="image" style="width:100%">
            <div class="middle">
            <a href="http://127.0.0.1:{port}/medicina.html">Medicina</a>
            </div>
            </div></center>'''.format(port=port) 
        message=message+'''<br>
            <br>
            <br>
            <center>
            <div class="container">
            <img src="/images/pediatria1.jpg" alt="Pediatria" class="image" style="width:100%">
            <div class="middle">
            <a href="http://127.0.0.1:{port}/pediatria.html">Pediatria</a>
            </div>
            </div></center>'''.format(port=port) 
            
        message = message + footer_html
    except:
        pass
    f.write(message)
    f.close() 
    
#implementazione delle singole pagine per ogni sezione 
def create_cardiologia_page():
    f = open('cardiologia.html','w', encoding="utf-8")
    try:
        message = Header_html + NavigationBar_html
        message = message + '''<th><h2><center>Lista dei Servizi di Cardiologia</center></h2></th></tr>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/cardiologia/"> Cardiologia </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/cardiologia-interventistica/"> Cardiologia Interventistica </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/cardiologia-pediatrica/"> Cardiologia Pediatrica </a>
        </center>
        '''
    except:
        pass
    f.write(message)
    f.close()

def create_chirurgia_page():
    f = open('chirurgia.html','w', encoding="utf-8")
    try:
        message = Header_html + NavigationBar_html
        message = message + '''<th><h2><center>Lista dei Servizi di Chirurgia</center></h2></th></tr>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-durgenza/"> Chirurgia di Urgenza </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-pediatrica/"> Chirurgia Pediatrica </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-plastica-e-centro-ustioni/"> Cardiologia Plastica e Centro Ustioni </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-senologica/"> Chirurgia Senologica </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-toracica/"> Chirurgia Toracica </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/chirurgia-vascolare/"> Chirurgia Vascolare </a>
        </center>
        '''
    except:
        pass
    f.write(message)
    f.close()
    
def create_medicina_page():
    f = open('medicina.html','w', encoding="utf-8")
    try:
        message = Header_html + NavigationBar_html
        message = message + '''<th><h2><center>Lista dei Servizi di Medicina</center></h2></th></tr>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/medicina-del-lavoro-e-tossicologia-industriale/"> Medicina del lavoro e Tossicologia industriale </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/medicina-del-sonno/"> Medicina del sonno </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/medicina-interna-a-indirizzo-angiologico-e-coagulativo/"> Medicina interna a indirizzo angiologico e coagulativo </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/lungodegenza-critica/"> Medicina interna e Lungodegenza critica </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/medicina-nucleare/"> Medicina nucleare </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/medicina-riabilitativa/"> Medicina Riabilitativa </a>
        </center>
        '''
    except:
        pass
    f.write(message)
    f.close()

def create_pediatria_page():
    f = open('pediatria.html','w', encoding="utf-8")
    try:
        message = Header_html + NavigationBar_html
        message = message + '''<th><h2><center>Lista dei Servizi di Pediatria</center></h2></th></tr>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/pediatria-e-oncoematologia/"> Pediatria e oncoematologia </a>
        </center>
        '''
        message = message + '''
        <br>
        <br>
        <center>
        <a href="https://www.ao.pr.it/curarsi/reparti-e-servizi-sanitari/pediatria-generale-e-durgenza-2/"> Pediatria generale e d'urgenza </a>
        </center>
        '''
    except:
        pass
    f.write(message)
    f.close()

#inizializzazione del dizionario contentente le coppie username e password 
def initialize_dictionary_authentication():
    d = {}
    with open("login.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d

#metodo che implementa il processo di autenticazione
def authentication_process():
    dictionary = initialize_dictionary_authentication()
    risposta=input('sei gia registrato a questo sito? risondere si o no\n')
    if(risposta == 'si'):
        username = input('Inserire l\'username:\n')
        password = input('Inserire la password:\n')
        if(username in dictionary):
            if(dictionary.get(username)!=password):
                print('password sbagliata, riprovare\n')
                authentication_process()
        else:
            print('Credenziali di accesso sbagliate, riprovare\n')
            authentication_process()
    else:
        risposta = input('Per continuare devi prima autenticarti, Vuoi procedere alla registrazione? rispondere si o no\n')
        if(risposta == 'si'):
            username = input('Inserire un username\n')
            if(username in dictionary):
                print('username gia in utilizzo, sceglierne un altro')
                authentication_process()
            else:
                password = input('inserire una password\n')
                with open("login.txt", "a") as myfile:
                  myfile.write("\n" + username + ' ' + password)
                print('sei stato registrato, ora puoi navigare senza problemi.')
        else:
            sys.exit()
        
   

def create_all():
    print('Inzio creazione delle pagine')
    create_initial_page()
    create_cardiologia_page()
    create_chirurgia_page()
    create_medicina_page()
    create_pediatria_page()
    print('Fine creazione')
    
#metodo che permette di uscire dal server con il controllo Ctrl+C
def signal_handler(signal, frame):
    print( 'Uscita dal http server (Ctrl+C premuto)')
    try:
      if(server):
        server.server_close()
    finally:
      # fermo il thread del refresh senza busy waiting
      waiting_refresh.set()
      sys.exit()
   
    
def main():
    
    #variabile che assicura la terminazione di tutti i thread generati attraverso la combinazione Crtl+C
    server.daemon_threads = True 
    
    #variabile che consente il riutilizzo del socket, anche se non è stato rilasciato precendentemente, sovrascrivendoolo
    server.allow_reuse_address = True  
    
    #interrompe l'esecuzione se da tastiera grazie al comando: (CTRL + C) 
    signal.signal(signal.SIGINT, signal_handler)
    
    #Processo di autentificazione, assicura che l'user sia utenticato prima di poter accedere al sito oppure permette di registrarsi
    authentication_process()
    
    #crea tutte le pagine
    create_all()
    
    #entra nel loop infinito
    try:
      while True:
        server.serve_forever()
    except KeyboardInterrupt:
      pass
    server.server_close()

if __name__ == "__main__":
    main()