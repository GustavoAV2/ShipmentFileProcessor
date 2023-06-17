
class CnabService:
    def __init__(self):
        self.root_path = '../shipment_folder/'

    def read_cnab(self, file):
        data = {}
        with open(self.root_path + file, 'r', encoding='ascii') as file:
            for line in file:
                register_type = line[0]

                if register_type == '0':
                    self._header_process(line, data)
                elif register_type == '1':
                    self._detail_process(line, data)
        return data

    def _header_process(self, line, data):
        return

    def _detail_process(self, line, data):
        return


if __name__ == "__main__":
    c = CnabService()
    c.read_cnab("remessa.cnab")
