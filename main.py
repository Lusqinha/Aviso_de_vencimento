from pywhatkit import sendwhatmsg_instantly
import csv
from datetime import datetime

hoje = datetime.now().date()
hoje = hoje.strftime('%m/%Y')

print(f'Programa iniciado - mês: {hoje}')

def envia_mensagens(cliente, contato, produto, data_col):
    try:
        print(f'Enviando mensagem para {cliente}...')
        mensagem = f"Olá {cliente}, sou o Atendente da Prática Certificação Digital! \n\nQuero avisar sobre o *vencimento* do seu Certificado Digital *{produto}* no dia *{data_col} Renove o seu certificado* e evite a perda dos seus prazos fiscais.\n\nPara a renovação, é só vir até o escritório que fica na Rua Barão do Triunfo, 753 - Sala 04. *Aqui em São Lourenço do Sul*, em frente ao cartório Nardi. De segunda a sexta das 8:30 as 11:45 e das 13:30 as 17:45. Trazendo um documento com foto original. Ou agendar por este WhatsApp uma videoconferência, caso não esteja na cidade."
        sendwhatmsg_instantly(contato, mensagem , wait_time=20, tab_close=True)
        print('mensagem enviada, buscando próximo contato.')
        return True
    except Exception as e:
        print(f'Erro ao enviar mensagem para o contato: {contato} - cliente: {cliente}')
        return False


def data_filter(data:str):
    years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015']
    for y in years:
        if data.endswith(f'/{y}'):
            data = data.removesuffix(f'/{y}')
            return data



file = open('arquivo_teste.csv')
csv_file = csv.reader(file)

vencimentos_hoje = []

for row in csv_file:
    try:
        slice_row = row[0].split(';')
        if slice_row[0] == 'ï»¿emissÃ£o':
            print('Linha de cabeçalho, pulando...')
            continue
        print(slice_row)
        data = slice_row[0]
        print(data)
        vencimentos_hoje.append(slice_row)
    except Exception as e:
        print('Erro ao ler linha')
        continue

for row in vencimentos_hoje:
    try:
        cliente = row[3].capitalize()
        print(cliente)
        data_col = row[0]
        print(data_col)
        contato = row[4].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if contato == '':
            continue
        elif not contato.startswith('53'):
            contato = '53' + contato

        contato = '+55' + contato
        print(contato)
        contato = '+5553991939740'
        produto = row[2].replace('(nÃƒÂ£o usar) ', '')
        print(produto)
        data_col = data_filter(data_col)
        envia_mensagens(cliente, contato, produto, data_col)
    except Exception as e:
        print(f'Erro ao enviar mensagem para {cliente} - {contato} - {data_col}')

print('Execução finalizada!')
