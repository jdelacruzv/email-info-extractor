popular_domains = {'gmail' : 'Google', 'yahoo' : 'Yahoo', 'hotmail' : 'Microsoft', 'outlook' : 'Microsoft'}
special_characters = ['!', '#', '$', '%', '&', '\'', '*', '+', '-', '/', '=', '?', '^', '_', '`', '.', '{', '|', '}', '~', ' ']

# TODO: validar el email
email = input('Ingrese su correo electrónico: ').strip().lower()
# Asignando valores a una tupla
user, domain = email.split('@')


def get_user_name():
	user_list = list(user)
	for letter in user_list:
		if letter in special_characters:
			break
	return user[:user.index(letter)].capitalize()


def get_domain_name():
	return domain[:domain.index('.')]


def main():
	user_name = get_user_name()
	domain_name = get_domain_name()
	if domain_name in popular_domains.keys():
		print(f'Hola {user_name}, estoy viendo que tu email está registrado con {popular_domains[domain_name]}. ¡Eso es genial!.')
	else:
		print(f'Hola {user_name}, estoy observando que estás utilizando un dominio personalizado de {domain_name}. ¡Impresionante!.')


main()