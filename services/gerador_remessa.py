from services import processador_cnab


class GeradorRemessa:
    def __init__(self):
        self.root_path = '../shipment_folder/'

    def gerar_remessa(self, file):
        processador = processador_cnab(file)
        dados_cnab = processador.processar()


    

if __name__ == "__main__":
    c = GeradorRemessa()
    c.read_cnab("remessa.cnab")
