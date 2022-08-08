from Calculadora import Calculadora

class ControlCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()
        self.opcao = -1

    def menu(self):
        print("Escolha o tipo de oprecação: \n\n" +
              "0.Sair\n" +
              "1.Somar\n" +
              "2.Subtrair\n" +
              "3.Multiplicar\n" +
              "4.Dividir\n")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()
            if self.opcao == 0:
                print("Obtigado!")
            if self.opcao == 1:
                print("Informe o Primeiro Numero:")
            numero1 = int(input())
            print("\nInforme o Segundo Numero:")
            numero2 = int(input())
            print("A resposta é: " + numero1 + numero2)

            self.calculadora.subtrair.(numero1, numero2)
        elif self.opcao == 2:
        print("Informe o Primeiro Numero:")
        numero1 = int(input())
        print("\n Informe o Segundo Numero:")
        numero2 = int(input())
        print("A resposta é; " + numero1 + numero2)