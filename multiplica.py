#!/usr/bin/python3

lista = list(range(1,11));
 
for i in lista:
	print("--------------\n" + "Tabla del " + str(i) + '\n' + "--------------\n");
	for j in lista:
		multi = i * j;
		print(str(i) + " * " + str(j) + " = " + str(multi));
		if j == 10:
			print('\n');

