
nota1 = float(input("Digite a primeira Nota: "))
nota2 = float(input("Digite a segunda Nota: "))
nota3 = float(input("Digite a terceira Nota: "))

media = (nota1 + nota2 + nota3)/3
if media <= 4:
        print(media, "REPROVADO")
elif media >= 5 and media < 7:
        print(media, "PROVA FINAL")
else:
        print(media, "APROVADO")
