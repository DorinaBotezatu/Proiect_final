import sys
import smtplib

sys.path.append("C:\\Users\\admin\\Documents\\__PyThOn\\0 PyP\\_module")  # pt pftp


"""
2. Adaugati o solutie in clasa Stoc care sa va avertizeze automat cand stocul unui produs este mai mic decat o 
limita minima, predefinita per produs. Limita sa poata fi variabila (per produs). Preferabil sa 
transmita automat un email de avertizare;"""


def expediaza_alerta_stoc(limita):
    expeditor = 'botezatudorinaa@gmail.com'
    destinatar = ['office@infoacademy.net', 'paul@infoacademy.net']
    username = 'botezatudorinaa@gmail.com'
    subiect = 'Alerta STOC!!'
    mesaj = """From: {0}
    To: {1}
    Subject: {2}
    Content-type: text/html
    <html>
    Alereta Stoc,
        <head>
            <title></title>
            <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
            <link href="../../../default.css" rel="stylesheet" type="text/css" />
        </head>
        <body style="background:none;margin:0px">
            <h1 class=jobstitle>Practica individuala curs 2</h1>
        </body>
    <p>Paul limita {3}</p>
    </html>
    """.format(expeditor, destinatar, subiect, limita)

    try:
        print("Incercare expediere")
        smtp_ob = smtplib.SMTP('smtp.mail.ru', 465)
        smtp_ob.starttls()  # protocol criptare
        smtp_ob.login("botezatudorinaa@gmail.com", 'parola')
        for i in destinatar:
            smtp_ob.sendmail(expeditor, i, mesaj)
            print(f'Mesaj to {i} expediat cu succes!')
        smtp_ob.close()
    except Exception as e:
        print(e)
        print('Mesajul nu a putut fi expediat!')





def expediaza_fisa_produs():
    expeditor = 'botezatudorinaa@gmail.com'
    destinatar = ['office@infoacademy.net', 'paul@infoacademy.net']
    username = 'botezatudorinaa@gmail.com'
    subiect = 'Fisa Produs!!'
    mesaj = """From: {0}
    To: {1}
    Subject: {2}
    Content-type: text/html
    <html>
    Fisa produsului,
        <head>
            <title></title>
            <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
            <link href="../../../default.css" rel="stylesheet" type="text/css" />
        </head>
        <body style="background:none;margin:0px">
            <h1 class=jobstitle>Practica individuala curs 2</h1>
        </body>
    <p>Paul limita {3}</p>
    </html>
    """.format(expeditor, destinatar, subiect)

    try:
        print("Incercare expediere")
        smtp_ob = smtplib.SMTP('smtp.mail.ru', 465)
        smtp_ob.starttls()  # protocol criptare
        smtp_ob.login("botezatudorinaa@gmail.com", 'parola')
        for i in destinatar:
            smtp_ob.sendmail(expeditor, i, mesaj)
            print(f'Mesaj to {i} expediat cu succes!')
        smtp_ob.close()
    except Exception as e:
        print(e)
        print('Mesajul nu a putut fi expediat!')

if __name__ == '__main__':
    pass
