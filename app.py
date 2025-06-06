from flask import Flask, render_template, request, redirect, url_for
from controllers.monitoramento_controller import MonitoramentoController

app = Flask(__name__)
controller = MonitoramentoController()

@app.route('/')
def index():
    registros = controller.listar()
    return render_template('index.html', registros=registros)

@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        data = request.form['data']
        litros = float(request.form['litros'])
        energia = float(request.form['energia'])
        residuos = int(request.form['residuos'])
        reciclados = int(request.form['reciclados'])
        opc1 = request.form.get('opc1', 'N')
        opc2 = request.form.get('opc2', 'N')
        opc3 = request.form.get('opc3', 'N')
        opc4 = request.form.get('opc4', 'N')
        opc5 = request.form.get('opc5', 'N')
        opc6 = request.form.get('opc6', 'N')
        msg = controller.inserir(data, litros, energia, residuos, reciclados, opc1, opc2, opc3, opc4, opc5, opc6)
        return redirect(url_for('index'))
    return render_template('inserir.html')

@app.route('/excluir/<data>')
def excluir(data):
    controller.excluir(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
