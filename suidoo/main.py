def met():
    print ('Ola mundo');

def soma (a, b):
    return a + b;
print(soma(1,2))

notas = [7,6,3,4]

notas.append (10)

print(notas)

print(round(sum(notas)/len(notas),3))

#for == para
#while == enquanto
var1 = "ola"
lista = [0,1,2,3,4,5,6]

for i in var1 :
    print(i)

print(list(range(1,10,2)))

pares = list(range(0,13,2))

for n in pares:
    print (n ** 3)
    
x = 0
while x <= 10:
    print (x**3)
    x =x +2
    
    
clickbt = True

while clickbt == True :
    clickbt = input('Quer continuar? S/N? ')
    if clickbt != 'S':
        break
    
print([x for x in range(11) if n % 2 == 0])


