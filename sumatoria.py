def sumatoria_cubica(n):
	suma = 0
	for i in range(1, n+1):
		for j in range(1, i+1):
			for k in range(j, i+j+1):
				suma = suma + 1
	return suma			

def sumatoria_constante(n):
	suma = int((n*(n+1)*(n+2))/3)
	return suma
