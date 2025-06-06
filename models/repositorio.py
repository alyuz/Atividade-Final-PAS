from database import DatabaseConnection

class MonitoramentoRepositorio:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()
        self.cursor = self.conn.cursor()

    def existe_data(self, data):
        self.cursor.execute("SELECT * FROM valores_sustentabilidade WHERE data = %s", (data,))
        return self.cursor.fetchone() is not None

    def inserir_dados(self, dados_valores, dados_resultados):
        insert_valores = """
            INSERT INTO valores_sustentabilidade 
            (data, valor_agua, valor_energia, valor_residuos, valor_reciclaveis, valor_transporte)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        insert_resultados = """
            INSERT INTO resultados_sustentabilidade 
            (data, consumo_agua, consumo_energia, geracao_residuos, uso_transporte)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_valores, dados_valores)
        self.cursor.execute(insert_resultados, dados_resultados)
        self.conn.commit()

    def buscar_id_por_data(self, data):
        self.cursor.execute("SELECT id FROM valores_sustentabilidade WHERE data = %s", (data,))
        return self.cursor.fetchone()

    def atualizar_dados(self, dados_valores, dados_resultados, data):
        update_valores = """
            UPDATE valores_sustentabilidade 
            SET valor_agua = %s, valor_energia = %s, valor_residuos = %s, 
                valor_reciclaveis = %s, valor_transporte = %s 
            WHERE data = %s
        """
        update_resultados = """
            UPDATE resultados_sustentabilidade 
            SET consumo_agua = %s, consumo_energia = %s, 
                geracao_residuos = %s, uso_transporte = %s 
            WHERE data = %s
        """
        self.cursor.execute(update_valores, (*dados_valores, data))
        self.cursor.execute(update_resultados, (*dados_resultados, data))
        self.conn.commit()

    def excluir_por_data(self, data):
        self.cursor.execute("DELETE FROM resultados_sustentabilidade WHERE data = %s", (data,))
        self.cursor.execute("DELETE FROM valores_sustentabilidade WHERE data = %s", (data,))
        self.conn.commit()

    def listar_todos(self):
        consulta = """
            SELECT v.data, v.valor_agua, r.consumo_agua, v.valor_energia, r.consumo_energia,
                   v.valor_residuos, v.valor_reciclaveis, r.geracao_residuos,
                   v.valor_transporte, r.uso_transporte
            FROM valores_sustentabilidade v
            JOIN resultados_sustentabilidade r ON v.data = r.data
            ORDER BY v.data DESC
        """
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

    def listar_resultados(self):
        self.cursor.execute("""
            SELECT consumo_agua, consumo_energia, geracao_residuos, uso_transporte 
            FROM resultados_sustentabilidade
        """)
        return self.cursor.fetchall()

    def fechar(self):
        self.cursor.close()
        self.conn.close()
