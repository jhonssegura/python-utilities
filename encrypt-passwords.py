import crypt
import os

"""
Para crear una variable de entorno, ejecutar en la terminal la siguiente instruccion
export SALT=nombre_que_desee
"""

sentence = 'Este es un password en texto plano'
salt = os.environ.get('SALT')

password = crypt.crypt(sentence, salt)
print(password)