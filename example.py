from helpybmc import sendhelpy

# Set your email
sender_email = 'your_email@correo.ugr.es'
password = 'your_password'
server = 'student'

message = 'default'

# Send the email
try:
    succes = sendhelpy.send(sender_email=sender_email, password=password, message=message, server=server)
    print(succes)
except:
    print('Error sending the email')