l = ""
while (True):
	try:
		x = raw_input()
	except EOFError:
		break
	l = l + x + '\n'

print l
