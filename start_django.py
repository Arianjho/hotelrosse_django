import os
import webbrowser
import subprocess
import time

# Cambia el directorio al lugar donde se encuentra tu proyecto Django.
os.chdir('C:\\Users\\arian\\OneDrive\\Proyectos VScode\\hotelrosse_django')

# Inicia el servidor de Django.
subprocess.Popen(['python', 'manage.py', 'runserver'])

# Espera unos segundos para dar tiempo al servidor de Django de iniciarse.
time.sleep(5)

# Abre el navegador con la URL del servidor de desarrollo de Django.
webbrowser.open('http://127.0.0.1:8000/')
