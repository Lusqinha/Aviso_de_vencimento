from pywhatkit import sendwhatmsg_instantly
from datetime import datetime
import csv


""" Modelo de arquivo CSV
emissão | pedido | produto | cliente | telefone | email | indicador
"""


class EmissorDeAvisos:

    def __init__(self, path):
        self.hoje = datetime.now().strftime('%d/%m/%Y | %H:%M:%S')
        self.dia = datetime.now().strftime('%d-%m-%Y')
        self.vencimentos_hoje = []
        self.clientes_avisados = 0
        self.file = open(path)
        self.csv_file = csv.reader(self.file)
        print(f'Programa iniciado - mês: {self.hoje}')

    def envia_mensagens(self, cliente, contato, produto, data_col):
        try:
            print(f'Enviando mensagem para {cliente}...')
            mensagem = f"Olá {cliente}, sou o Atendente da Prática Certificação Digital! \n\nQuero avisar sobre o *vencimento* do seu Certificado Digital *{produto}* no dia *{data_col} Renove o seu certificado* e evite a perda dos seus prazos fiscais.\n\nPara a renovação, é só vir até o escritório que fica na Rua Barão do Triunfo, 753 - Sala 04. *Aqui em São Lourenço do Sul*, em frente ao cartório Nardi. De segunda a sexta das 8:30 as 11:45 e das 13:30 as 17:45. Trazendo um documento com foto original. Ou agendar por este WhatsApp uma videoconferência, caso não esteja na cidade."
            sendwhatmsg_instantly(
                contato, mensagem, wait_time=20, tab_close=True)
            print('mensagem enviada, buscando próximo contato.')
            return True
        except Exception as e:
            print(
                f'Erro ao enviar mensagem para o contato: {contato} - cliente: {cliente}')
            return False

    def data_filter(self, data: str):
        years = ['2023', '2022', '2021', '2020',
                 '2019', '2018', '2017', '2016', '2015']
        for y in years:
            if data.endswith(f'/{y}'):
                data = data.removesuffix(f'/{y}')
                return data

    def contato_filter(self, contato: str):
        ddds = [61, 62, 64, 65, 66, 67, 41, 42, 43,
                44, 45, 46, 51, 53, 54, 55, 47, 48, 49]

        contato = contato.replace('(', '').replace(')', '').replace(
            '-', '').replace(' ', '').replace('.', '')

        if contato == '':
            return False
        for ddd in ddds:
            if contato.startswith(str(ddd)):
                print('DDD encontrado')
                break
        else:
            contato = '53' + contato

        contato = '+55' + contato
        return contato

    def gerar_lista(self):
        for row in self.csv_file:
            try:
                slice_row = row[0].split(';')
                if slice_row[0] == 'ï»¿emissÃ£o':
                    print('Linha de cabeçalho, pulando...')
                    continue
                print(slice_row)
                data = slice_row[0]
                print(data)
                self.vencimentos_hoje.append(slice_row)
            except Exception as e:
                print('Erro ao ler linha')
                continue

    def enviar_mensagens(self):
        for row in self.vencimentos_hoje:
            try:
                cliente = row[3].capitalize()
                print(cliente)
                data_col = row[0]
                print(data_col)
                contato = self.contato_filter(row[4])
                print(contato)
                produto = row[2].replace(
                    '(nÃƒÂ£o usar) ', '').replace('(nÃ£o usar) ', '')
                print(produto)
                data_col = self.data_filter(data_col)

                with open(f'log/log{str(self.dia)}.txt', 'a') as log:
                    log.write(
                        f'{cliente} - {contato} - {data_col} - {produto} - {self.hoje}\n\n----------Novo-Cliente--------------\n\n')
                    log.close()

                # self.envia_mensagens(cliente, contato, produto, data_col)
            except Exception as e:
                with open(f'log/log{str(self.dia)}.txt', 'a') as log:
                    log.write(
                        f'Erro ao enviar mensagem para {cliente} - {contato} - {data_col} - {self.hoje}\n\n----------Novo-Cliente--------------\n\n')
                    log.close()
                print(
                    f'Erro ao enviar mensagem para {cliente} - {contato} - {data_col}')
            self.clientes_avisados += 1



if __name__ == '__main__':
    emissor = EmissorDeAvisos('vencimentos.csv')
    emissor.gerar_lista()
    emissor.enviar_mensagens()
