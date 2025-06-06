from app.services.classificadores import Classificador
from app.services.criptografia import Criptografia
from app.models.repositorio import RepositorioMonitoramento


class MonitoramentoController:
    def __init__(self):
        self.repositorio = RepositorioMonitoramento()
        self.classificador = Classificador()
        self.criptografia = Criptografia()

    def inserir_monitoramento(self):
        dados = self.repositorio.coletar_dados_usuario()
        classificacoes = {
            "agua": self.criptografia.criptografar(self.classificador.classificar_agua(dados["litros"])),
            "energia": self.criptografia.criptografar(self.classificador.classificar_energia(dados["energia"])),
            "residuos": self.criptografia.criptografar(self.classificador.classificar_residuos(dados["reciclados"])),
            "transporte": self.criptografia.criptografar(
                self.classificador.classificar_transporte(
                    dados["opc1"], dados["opc2"], dados["opc3"], dados["opc4"], dados["opc5"], dados["opc6"]
                )
            )
        }
        self.repositorio.inserir_dados(dados, classificacoes)

    def alterar_monitoramento(self):
        dados = self.repositorio.coletar_dados_usuario(alteracao=True)
        classificacoes = {
            "agua": self.criptografia.criptografar(self.classificador.classificar_agua(dados["litros"])),
            "energia": self.criptografia.criptografar(self.classificador.classificar_energia(dados["energia"])),
            "residuos": self.criptografia.criptografar(self.classificador.classificar_residuos(dados["reciclados"])),
            "transporte": self.criptografia.criptografar(
                self.classificador.classificar_transporte(
                    dados["opc1"], dados["opc2"], dados["opc3"], dados["opc4"], dados["opc5"], dados["opc6"]
                )
            )
        }
        self.repositorio.atualizar_dados(dados, classificacoes)

    def excluir_monitoramento(self):
        self.repositorio.excluir_por_data()

    def listar_monitoramentos(self):
        registros = self.repositorio.buscar_todos()
        if not registros:
            print("\nNenhum monitoramento cadastrado.")
            return

        for registro in registros:
            self.repositorio.exibir_monitoramento(registro, self.criptografia)

    def calcular_medias(self):
        dados = self.repositorio.buscar_classificacoes()
        self.repositorio.exibir_medias(dados, self.criptografia)

    def encerrar_conexao(self):
        self.repositorio.fechar()
