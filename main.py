from app.controllers.monitoramento_controller import MonitoramentoController
from app.views.menu_view import exibir_menu


def main():
    controller = MonitoramentoController()

    while True:
        opcao = exibir_menu()

        if opcao == 1:
            controller.inserir_monitoramento()
        elif opcao == 2:
            controller.alterar_monitoramento()
        elif opcao == 3:
            controller.excluir_monitoramento()
        elif opcao == 4:
            controller.listar_monitoramentos()
        elif opcao == 5:
            controller.calcular_medias()
        elif opcao == 6:
            print("\nSaindo do sistema...")
            controller.encerrar_conexao()
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
