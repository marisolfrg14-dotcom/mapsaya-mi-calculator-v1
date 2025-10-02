def calcular_porcentaje(parte, total):
    """
    Calcula el porcentaje de 'parte' con respecto a 'total'.
    Fórmula: (parte / total) * 100
    """
    if total == 0:
        return "Error: El total (denominador) no puede ser cero."
    return (parte / total) * 100


num1 = float(input("Ingresa la PARTE (o numerador): "))
num2 = float(input("Ingresa el TOTAL (o denominador): "))


resultado_porcentaje = calcular_porcentaje(num1, num2)


print(f"El número {num1} es el {resultado_porcentaje:.2f}% de {num2}.")