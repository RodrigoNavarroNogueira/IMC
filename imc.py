def abertura():
    print('*-' * 30)
    print('{:=^60}'.format(' BEM-VINDO AO CALCULO DO SEU IMC! '))
    print('*-' * 30)


abertura()

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.1f}')

if imc <= 18.4:
    print('Voce está abaixo do peso')

elif imc <= 25:
    print('Voce está com o peso ideal')

elif imc <= 30:
    print('Voce está com sobre peso')

elif imc <= 40:
    print('Voce está com obesidade')

elif imc > 40:
    print('Voce está com obesidade morbida!')

else:
    print('Opção invalida, tente novamente')
