from . import server_dict

import smtplib, ssl

def send(sender_email = '', password = '', message = 'default', 
         server = 'student', port = 465, receiver_email = 'guillermocamacho@ugr.es'):


    # Check all the variables

    #
    # SENDER EMAIL
    #
    # If the sender_email is empty, ask for it
    if sender_email == '':
        sender_email = input("Type your email and press enter: ")
        # Check that it is a valid email
        if '@' not in sender_email:
            print('Please, type a valid email')
            return
    #
    # RECEIVER EMAIL
    #
    # If the receiver_email is empty, ask for it
    if password == '':
        password = input("Type your password and press enter: ")

    #
    # MESSAGE
    #
    # If the message is default, set the default message
    if message == 'default':
        message = """\
Subject: HELPY

Hola soy Blanca, necesito ayuda urgente."""
    # Otherwise, check if the message has a subject
    elif 'Subject: ' in message:
        pass
    else:
        subject = """\
Subject: HELPY"""
        message = subject + '\n\n' + message

    #
    # SERVER
    #
    # If the server is not in the dictionary, use the default server
    server = server_dict.get(server, 'correo.ugr.es')
        

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(server, port, context=context) as server_:
        try:
            server_.login(sender_email, password)
            server_.sendmail(sender_email, receiver_email, message)
            return 'Helpy!'
        except Exception as e:
            print(f'Error: {e}')
            print('Please, check your email and password')
            return


