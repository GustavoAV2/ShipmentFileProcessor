from log import logger
from services.cnab_processor import CnabProcessor


class ShipmentGenerate:
    def __init__(self):
        pass

    @staticmethod
    def shipment_generate(file):
        process = CnabProcessor(file)
        dados_cnab = process.process()


if __name__ == "__main__":
    c = ShipmentGenerate()
    c.shipment_generate("remessa.cnab")
