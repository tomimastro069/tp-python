A = input("Ingrese la palabra hipopotamo: ")
B = A.upper()

while B != "HIPOPOTAMO":
    A = input("Por favor, ingrese la palabra hipopotamo: ")
    B = A.upper()
C = len(B)
print("la cuarta letra es: ", B[3])

print("la quinta letra es: ", B[4])
