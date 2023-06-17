""" Header structure """
""" Nome	Significado	Obrigatorio	Posicao	Picture	Conteudo
TIPO DE REGISTRO	IDENTIFICAÇÃO DO REGISTRO HEADER	SIM	001 001	9(01)	0
OPERAÇÃO	TIPO DE OPERAÇÃO - REMESSA	SIM	002 002	9(01)	1
LITERAL DE REMESSA	IDENTIFICAÇÃO POR EXTENSO DO MOVIMENTO	SIM	003 009	X(07)	REMESSA
CÓDIGO DO SERVIÇO	IDENTIFICAÇÃO DO TIPO DE SERVIÇO	SIM	010 011	9(02)	"02"
LITERAL DE SERVIÇO	IDENTIFICAÇÃO POR EXTENSO DO TIPO DE SERVIÇO	SIM	012 026	X(15)	PIX
ISPB PARTICIPANTE	PSP DO USUARIO RECEBEDOR	SIM	027 034	X(08)	Deve ser preenchido com ISPB do PSP Recebedor
TIPO PESSOA RECEBEDOR	TIPO DE PESSOA RECEBEDOR	SIM	035 036	9(02)	NOTA 1
CPF CNPJ	CPF CNPJ DO USUARIO RECEBEDOR	SIM	037 050	9(14)	Identificação única do usuário recebedor
AGÊNCIA	AGÊNCIA DO USUARIO RECEBEDOR	NÃO	051 054	9(04)	Agência do usuário recebedor
CONTA	CONTA USUÁRIO RECEBEDOR	NÃO	055 074	9(20)	Número da conta transacional usuário recebedor
TIPO CONTA	TIPO CONTA USUÁRIO RECEBEDOR	NÃO	075 078	X(04)	NOTA 2
CHAVE Pix	CHAVE Pix	NÃO	079 155	X(77)	NOTA 3
DATA DE GERAÇÃO	DATA DE GERAÇÃO DO ARQUIVO	SIM	156 163	9(08)	AAAAMMDD
CÓDIGO DO CONVENIO	CÓDIGO DO CONVENIO	NÃO	164 193	X(30)	
EXCLUSIVO PSP RECEBEDOR	EXCLUSIVO PSP RECEBEDOR	NÃO	194 253	X(60)	Campo para uso exclusivo do PSP recebedor
NOME DO RECEBEDOR	NOME FANTASIA/RAZÃO SOCIAL DO RECEBEDOR	NÃO	254 353	X(100)	
BRANCOS	BRANCOS	NÃO	354 731	X(378)	
NÚMERO SEQUENCIAL DA REMESSA	NÚMERO SEQÜENCIAL DA REMESSA DO ARQUIVO	SIM	732 741	9(10)	
VERSAO DO ARQUIVO	VERSAO DO LAYOUT DO ARQUIVO	SIM	742 744	9(03)	002 CONTEÚDO PODE SER ALTERADO DE ACORDO COM VERSÃO DO LAYOUT
NÚMERO SEQUENCIAL DO REGISTRO	NÚMERO SEQÜENCIAL DO REGISTRO	SIM	745 750	9(06) """	

""" Details structure """



class CnabService:
    def __init__(self):
        self.root_path = '../shipment_folder/'

    def read_cnab(self, file):
        header_data = {}
        detail_data = {}
        with open(self.root_path + file, 'r', encoding='ascii') as file:
            for line in file:
                register_type = line[0]
                print(register_type + " - " + line)

                if register_type == '0':
                    self._header_process(line, header_data)
                elif register_type == '1':
                    self._detail_process(line, detail_data)
        return detail_data

    def _header_process(self, line, data):
        data['register_type'] = line[0:1].strip();
        data['operation'] = line[1:2].strip();
        data['literal'] = line[2:9].strip();
        data['service_code'] = line[9:11].strip();
        data['literal_service'] = line[11:26].strip();
        data['ispb'] = line[26:34].strip();
        data['type_person'] = line[34:36].strip();
        data['cpf_cnpj'] = line[36:50].strip();
        data['agency'] = line[50:54].strip();
        data['account'] = line[54:74].strip();
        data['type_account'] = line[74:78].strip();
        data['pix_key'] = line[78:155].strip();
        data['generation_date'] = line[155:163].strip();
        data['convenio_code'] = line[163:193].strip();
        data['exclusive_psp'] = line[193:253].strip();
        data['name'] = line[253:353].strip();
        data['blank'] = line[353:731].strip();
        data['sequential_number'] = line[731:741].strip();
        data['version'] = line[741:744].strip();
        data['sequential_number_register'] = line[744:750].strip();

        print(data)

    def _detail_process(self, line, data):
        data['register_type'] = line[0:1].strip();
        data['identifier'] = line[1:36].strip();
        data['type_of_receiver'] = line[36:38].strip();
        data['cpf_cnpj_receiver'] = line[38:52].strip();
        data['receiver_agency'] = line[52:56].strip();
        data['receiver_account'] = line[56:76].strip();
        data['type_receiver_account'] = line[76:80].strip();
        data['pix_key'] = line[80:157].strip();
        data['billing_type'] = line[157:158].strip();
        data['occurrence_code'] = line[158:160].strip();
        data['expiration_timestamp'] = line[160:174].strip();
        data['expiration_date'] = line[174:182].strip();
        data['validade_apos_vencimento'] = line[182:186].strip();
        data['valor_original'] = line[186:203].strip();
        data['tipo_pessoa_devedor'] = line[203:205].strip();
        data['cpf_cnpj_devedor'] = line[205:219].strip();
        data['nome_devedor'] = line[219:359].strip();
        data['solicitacao_pagador'] = line[359:499].strip();
        data['exclusivo_psp_recebedor'] = line[499:559].strip();
        data['brancos'] = line[559:744].strip();
        data['sequencial_registro'] = line[744:750].strip();

        print(data);

if __name__ == "__main__":
    c = CnabService()
    c.read_cnab("remessa.cnab")
