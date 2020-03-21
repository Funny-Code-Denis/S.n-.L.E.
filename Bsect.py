eps = 10**-7
def f(x):
	y = x**2-x-4
	return y
def bsect(a, b): 
	with open('Bsect.txt', 'tw', encoding = 'utf-8') as File:
		if f(a) * f(b) > 0:
			print('Function is continious')
			File.write('Function is continious\n')
			return
		while abs(b - a) > eps:
			c = (a + b) / 2
			if f(a) * f(c) < 0:
				b = c
			if f(b) * f(c) < 0:
				a = c
			word = 'Point C = %.8f'%c + '\tInterval (%.8f'%a + ';%.8f'%b + ')\n'
			File.write(word)
a = int(input('Enter A: '))
b = int(input('Enter B: '))
bsect(a, b)
