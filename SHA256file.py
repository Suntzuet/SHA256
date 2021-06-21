"""Este programa funciona comop el sha-256 pero en base 8"""

palabra = str(input("¿Qué quieres encriptar?: "))

lpalabra= str(hex((len(palabra)*8)).lstrip("0x")) #longitud de la palabra en hexadecimal
n = int(input("número máximo de elementos: ")) #es el numero máximo de elementos, originalmente son 64
palabra1 = ""
for i in palabra:
    palabra1 = str(palabra1 + hex(ord(str(i))).lstrip("0x"))

if len(palabra1) < ((n/4)*(7/8)*32): # 56 ya que son 8 caracteres por Wi y es hasta W7
    palabra1 = palabra1 + "8"
print(len(palabra1))
print((n/4)*(7/8)*32)
while len(palabra1) < ((n/4)*(7/8)*32):
    palabra1 = palabra1 + "0"


while (len(palabra1) < (n/4)*32-len(lpalabra)):
     palabra1 = palabra1+"0"

palabra1= palabra1+lpalabra
palabra1 = palabra1

print(palabra1)
print(len(palabra1))


# En mi caso, Wt8 contiene   elementos y cada palabra tiene 32 bits, para simplificar cálculos, los primeros 16
# registros en Wt (original) serán 4 en este programa y los últimos 48, 12.

# El primer bloque por tanto será





