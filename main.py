from controller.controller import MonitoramentoController

def menu():
    print("\nMenu Monitoramento Sustentabilidade")
    print("1 - Inserir dados")
    print("2 - Alterar dados")
    print("3 - Excluir dados")
    print("4 - Listar dados")
    print("5 - Sair")

def main():
    controller = MonitoramentoController()
    while True:
        menu()
        opc = input("Escolha uma opção: ")
        if opc == "1":
            data = input("Data (YYYY-MM-DD): ")
            litros = float(input("Litros de água: "))
            energia = float(input("Energia (kWh): "))
            residuos = int(input("Resíduos gerados (kg): "))
            reciclados = int(input("Resíduos reciclados (kg): "))
            print("Transporte: S para sim, N para não")
            opc1 = input("Transporte público: ").upper()
            opc2 = input("Bicicleta: ").upper()
            opc3 = input("Caminhada: ").upper()
            opc4 = input("Carro (fósseis): ").upper()
            opc5 = input("Carro elétrico: ").upper()
            opc6 = input("Carona compartilhada (fósseis): ").upper()
            resultado = controller.inserir(data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6)
            print(resultado)

        elif opc == "2":
            data = input("Data (YYYY-MM-DD) do registro para alterar: ")
            litros = float(input("Litros de água: "))
            energia = float(input("Energia (kWh): "))
            residuos = int(input("Resíduos gerados (kg): "))
            reciclados = int(input("Resíduos reciclados (kg): "))
            print("Transporte: S para sim, N para não")
            opc1 = input("Transporte público: ").upper()
            opc2 = input("Bicicleta: ").upper()
            opc3 = input("Caminhada: ").upper()
            opc4 = input("Carro (fósseis): ").upper()
            opc5 = input("Carro elétrico: ").upper()
            opc6 = input("Carona compartilhada (fósseis): ").upper()
            resultado = controller.alterar(data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6)
            print(resultado)

        elif opc == "3":
            data = input("Data (YYYY-MM-DD) do registro para excluir: ")
            resultado = controller.excluir(data)
            print(resultado)

        elif opc == "4":
            registros = controller.listar()
            for r in registros:
                print(f"Data: {r['data']} | Água: {r['valor_agua']} ({r['consumo_agua']}) | Energia: {r['valor_energia']} ({r['consumo_energia']})")
                print(f"Resíduos: {r['valor_residuos']} ({r['geracao_residuos']}) | Recicláveis: {r['valor_reciclaveis']}")
                print(f"Transporte: {r['valor_transporte']} ({r['uso_transporte']})")
                print('-'*50)
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
