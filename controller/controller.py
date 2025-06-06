from services.service import MonitoramentoService

class MonitoramentoController:
    def __init__(self):
        self.service = MonitoramentoService()

    def inserir(self, data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6):
        try:
            self.service.inserir_dados(data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6)
            return "Registro inserido com sucesso."
        except ValueError as e:
            return f"Erro: {e}"

    def alterar(self, data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6):
        try:
            self.service.alterar_dados(data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6)
            return "Registro alterado com sucesso."
        except ValueError as e:
            return f"Erro: {e}"

    def excluir(self, data):
        try:
            self.service.excluir_dados(data)
            return "Registro excluído com sucesso."
        except ValueError as e:
            return f"Erro: {e}"

    def listar(self):
        return self.service.listar_todos()
