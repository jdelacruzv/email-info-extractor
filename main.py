import os
import re


popular_domains = {'gmail' : 'Google', 'yahoo' : 'Yahoo', 'hotmail' : 'Microsoft', 'outlook' : 'Microsoft'}
special_characters = ['!', '#', '$', '%', '&', '\'', '*', '+', '-', '/', '=', '?', '^', '_', '`', '.', '{', '|', '}', '~', ' ']


def leave_sys():
	while True:
		leave = input('¿Desea continuar? (S / N): ').lower()
		if leave == 's':
			main()
		elif leave == 'n':
			os._exit(0)
		else:
			print('Entrada no válida')


def validate_email(email):
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	if re.match(pattern, email):
		return True
	else:
		return False


def get_email():
	email = input('Ingrese su correo electrónico: ').strip().lower()
	if validate_email(email):
		return email
	else:
		print("El correo electrónico no es válido")
		leave_sys()


def split_email(email):
	email = email.split('@')
	return email


def get_user_name(email):
	email_list = split_email(email)
	user = email_list[0]
	for letter in user:
		if letter in special_characters:
			return user[:user.index(letter)].capitalize()
	return user.capitalize()


def get_domain_name(email):
	email_list = split_email(email)
	domain = email_list[1]
	return domain[:domain.index('.')]


def print_message(email):
	user_name = get_user_name(email)
	domain_name = get_domain_name(email)
	if domain_name in popular_domains.keys():
		print(f'Hola {user_name}, estoy viendo que tu email está registrado con {popular_domains[domain_name]}. ¡Eso es genial!.')
		leave_sys()
	else:
		print(f'Hola {user_name}, estoy observando que estás utilizando un dominio personalizado de {domain_name}. ¡Impresionante!.')
		leave_sys()


def main():
	email = get_email()
	split_email(email)
	print_message(email)


main()