a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))


if (a+b>c) and (a+c>b) and (b+c>a):
    if a == b and b == c:
        print("É um triângulo equilátero!")

    elif a == b or a == c or b == c:
        print("É um triângulo isósceles!")

    else:
        print("É um triângulo escaleno!")

else:
    print("Isso não parece um triângulo.")