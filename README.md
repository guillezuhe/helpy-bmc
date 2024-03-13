# helpy-bmc

Este repositorio me envía un correo cuando BMC está en apuros. Llamado de emergencia.

## Instalación

Para instalar este paquete descarga este repositorio. Abre la carpeta raíz del paquete en la terminal y ejecuta:

```
pip install .
```

Si quieres instalar el paquete en el modo editable (los cambios en el código afectan inmediatamente al paquete sin reinstalarlo), ejecuta:

```
pip install -e .
```


## Instrucciones
Puedes llamar a la función desde cualquier código, por ejemplo:

```python
from helpybmc import sendhelpy

sendhelpy.send()
```

Así escrito te pedirá el usuario y la contraseña cada vez que lo uses, y puede ser algo engorroso. Para solucionar esto, puedes crear un script como el siguiente (se encuentra disponible en la carpeta raíz del paquete como `example.py`):

```python
from helpybmc import sendhelpy

# Set your email
sender_email = 'your_email@correo.ugr.es'
password = 'your_password'
server = 'student'

message = 'default'

# Send the email
sendhelpy.send(sender_email=sender_email, password=password, message=message, server=server)
```


## Documentación

Hay un único módulo con una única función en este paquete: El módulo **sendhelpy** con la función **send()**, teniendo la siguiente definición:


### sendhelpy.send()

This function sends an emergency email.

```python
send(sender_email, password, message, server, port, receiver_email)
```

**Parameters:**

- `sender_email` (str): The email address from which you want to send the emergency call. If none is provided, it will be requested via the terminal.
- `password` (str): The password for the sender's email. If none is provided, it will be requested via the terminal.
- `message` (str): The message you want to send. If none is provided, the default is "Hola soy Blanca, necesito ayuda urgente."
- `server` (str): The server to use for sending the email. Options are:
  - `"student"`: UGR student email
  - `"pdi"`: UGR PDI email
  - `"gmail"`: Gmail (note: does not work with Gmail accounts by default due to security reasons)
- `port` (int): 465 por defecto para SSL
- `receiver_email` (str): Quién va a recibir el llamado de emergencia, por defecto está el email del humilde servidor que escribe estas líneas.

**Returns:**

This function returns `"Helpy!"` if the message is succesfully sent or `None` otherwise.
