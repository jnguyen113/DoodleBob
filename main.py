import DoodleBob

while True:
	text = input('DoodleBob > ')
	result, error = DoodleBob.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)