def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    return media


resultado = calcular_media(8, 6)

print(resultado)

