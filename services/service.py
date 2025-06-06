from repositories.monitoramento_repositorio import MonitoramentoRepositorio
from utils.criptografia import criptografia, descriptografia

class MonitoramentoService:
    def __init__(self):
        self.repo = MonitoramentoRepositorio()

    def classif_agua(self, litros):
        if litros < 150:
            return "Alta Sustentabilidade"
        elif 150 <= litros <= 200:
            return "Moderada Sustentabilidade"
        else:
            return "Baixa Sustentabilidade"

    def classif_energia(self, energia):
        if energia < 5:
            return "Alta Sustentabilidade"
        elif 5 <= energia <= 10:
            return "Moderada Sustentabilidade"
        else:
            return "Baixa Sustentabilidade"

    def classif_reciclados(self, reciclados):
        if reciclados > 50:
            return "Alta Sustentabilidade"
        elif 20 <= reciclados <= 50:
            return "Moderada Sustentabilidade"
        else:
            return "Baixa Sustentabilidade"

    def classif_transporte(self, opc1, opc2, opc3, opc4, opc5, opc6):
        if (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and opc4 == "N" and opc6 == "N":
            return "Alta Sustentabilidade"
        elif (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and (opc4 == "S" or opc6 == "S"):
            return "Moderada Sustentabilidade"
        elif opc1 == "N" and opc2 == "N" and opc3 == "N" and opc5 == "N" and (opc4 == "S" or opc6 == "S"):
            return "Baixa Sustentabilidade"
        else:
            return 'Moderada Sustentabilidade'

    def montar_transportes_str(self, opc1, opc2, opc3, opc4, opc5, opc6):
        transportes_str = ""
        if opc1 == 'S':
            transportes_str += "| Transporte Público |"
        if opc2 == 'S':
            transportes_str += "| Bicicleta |"
        if opc3 == 'S':
            transportes_str += "| Caminhada |"
        if opc4 == 'S':
            transportes_str += "| Carro (combustível fósseis) |"
        if opc5 == 'S':
            transportes_str += "| Carro Elétrico |"
        if opc6 == 'S':
            transportes_str += "| Carona compartilhada (Fósseis) |"
        return transportes_str

    def inserir_dados(self, data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6):
        if self.repo.existe_data(data):
            raise ValueError("Já existe um registro para essa data.")

        consumo_agua = criptografia(self.classif_agua(litros))
        consumo_energia = criptografia(self.classif_energia(energia))
        geracao_residuos = criptografia(self.classif_reciclados(reciclados))
        uso_transporte = criptografia(self.classif_transporte(opc1, opc2, opc3, opc4, opc5, opc6))
        transportes_str = self.montar_transportes_str(opc1, opc2, opc3, opc4, opc5, opc6)

        dados_valores = (data, litros, energia, residuos, reciclados, transportes_str)
        dados_resultados = (data, consumo_agua, consumo_energia, geracao_residuos, uso_transporte)

        self.repo.inserir_dados(dados_valores, dados_resultados)

    def alterar_dados(self, data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6):
        if not self.repo.existe_data(data):
            raise ValueError("Nenhum registro encontrado para essa data.")

        consumo_agua = criptografia(self.classif_agua(litros))
        consumo_energia = criptografia(self.classif_energia(energia))
        geracao_residuos = criptografia(self.classif_reciclados(reciclados))
        uso_transporte = criptografia(self.classif_transporte(opc1, opc2, opc3, opc4, opc5, opc6))
        transportes_str = self.montar_transportes_str(opc1, opc2, opc3, opc4, opc5, opc6)

        dados_valores = (litros, energia, residuos, reciclados, transportes_str)
        dados_resultados = (consumo_agua, consumo_energia, geracao_residuos, uso_transporte)

        self.repo.atualizar_dados(dados_valores, dados_resultados, data)

    def excluir_dados(self, data):
        if not self.repo.existe_data(data):
            raise ValueError("Nenhum registro encontrado para essa data.")
        self.repo.excluir_por_data(data)

    def listar_todos(self):
        registros = self.repo.listar_todos()
        # Descriptografar resultados
        lista = []
        for row in registros:
            data, valor_agua, consumo_agua, valor_energia, consumo_energia, valor_residuos, valor_reciclaveis, geracao_residuos, valor_transporte, uso_transporte = row
            lista.append({
                "data": data,
                "valor_agua": valor_agua,
                "consumo_agua": descriptografia(consumo_agua),
                "valor_energia": valor_energia,
                "consumo_energia": descriptografia(consumo_energia),
                "valor_residuos": valor_residuos,
                "valor_reciclaveis": valor_reciclaveis,
                "geracao_residuos": descriptografia(geracao_residuos),
                "valor_transporte": valor_transporte,
                "uso_transporte": descriptografia(uso_transporte),
            })
        return lista
