from service.monitoramento_service import MonitoramentoService
from model.repositorio import MonitoramentoRepositorio

class MonitoramentoController:
    def __init__(self):
        self.servico = MonitoramentoService()
        self.repositorio = MonitoramentoRepositorio()

    def executar(self):
        while True:
            print("\nMenu:\n1. Inserir dados\n2. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_dados()
            elif opcao == "2":
                self.repositorio.fechar()
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")

    def inserir_dados(self):
        data = input("Data (YYYY-MM-DD): ")
        if self.repositorio.existe_data(data):
            print("Registro já existe.")
            return

        litros = int(input("Litros de água: "))
        energia = float(input("Energia (kWh): "))
        residuos = float(input("Resíduos não recicláveis (kg): "))
        reciclados = int(input("Percentual reciclado (%): "))

        print("Informe os meios de transporte usados (1 a 6). Use S/N:")
        opcoes = [str(i) for i in range(1, 7) if input(f"{i}. Usado? (S/N): ").strip().upper() == 'S']

        c_agua, c_energia, c_residuos, c_transporte = self.servico.processar_dados(
            litros, energia, residuos, reciclados, opcoes
        )

        transportes_str = " | ".join([f"Opção {o}" for o in opcoes])
        self.repositorio.inserir_valores((data, litros, energia, residuos, reciclados, transportes_str))
        self.repositorio.inserir_resultados((data, c_agua, c_energia, c_residuos, c_transporte))
        self.repositorio.salvar()

        print("Dados inseridos com sucesso.")
