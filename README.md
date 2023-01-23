#  Aviso de vencimento de certificado digital - NF-e | WTech 📜

Este projeto tem como objetivo notificar os clientes que estão com certificados digitais utilizados na emissão de notas fiscais eletrônicas (NF-e) vencidos.

## Como funciona? 📜

O projeto recebe uma tabela com as informações dos clientes e seus certificados digitais, corrige as informações padronizando-as e envia através do Whatsapp uma mensagem personalizada para cada cliente, informando razão social, produto e data de vencimento.

## Como utilizar? 📜

- Instale o Python 3.10.x;
- Instale a biblioteca PyWhatKit;
- adicione a tabela de clientes e certificados digitais na pasta raiz do projeto;
- execute o arquivo main.py;
- aguarde o envio das mensagens.

## Cuidados e observações 📜

- O envio das mensagens é feito através do Whatsapp Web, portanto, é necessário que ele esteja conectado previamente;
- Durante o envio das mensagens, o Whatsapp Web não deve ser utilizado;
- Evite executar o programa em horários de trabalho, já que o envio de mensagens necessita que o computador não seja utilizado;
- O envio de mensagens é feito de forma sequencial, portanto, quanto maior a quantidade de clientes, maior será o tempo de execução do programa;
- Caso o programa seja interrompido, ele recomeça a partir do primeiro cliente da tablela, para garantir que o cliente não receba a mensagem mais de uma vez, é necessário que o programa seja executado até o final;
- Se for interrompido, consulte o arquivo log.txt para verificar o cliente que foi interrompido, exclua-o da tabela, assim como os demais anteriores à ele e execute novamente.
- Mantenha uma cópia da tabela original, para que seja possível manter um controle dos dados.

## Como contribuir? 📜

- Faça um fork do projeto;
- Crie uma branch com a sua feature: `git checkout -b my-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: My new feature'`;
- Faça push para a sua branch: `git push origin my-feature`.


## Licença 📜

Este projeto está sob a licença MIT. Para mais informações, acesse o arquivo LICENSE.

## Créditos 📜

- [Python](https://www.python.org/)
- [PyWhatKit](https://pypi.org/project/pywhatkit/)
- [Lucas Borges](https://lucasborgess.com)

## Contato 📜

Caso tenha alguma dúvida, sugestão ou queira entrar em contato, envie um e-mail para [contato@lucasborgess.com] ou acesse o site [https://lucasborgess.com].

