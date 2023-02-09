![Screenshot](./assets/fundo.png)

# Desafio Back End Python
De posse de um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Precisa criar uma maneira para que estes dados sejam importados para um banco de dados.

O objetivo do Projeto é criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

A aplicação web DEVE:<br>

=> Ter uma tela (via um formulário) para fazer o upload do arquivo.
Interpretar ("parsear") o arquivo recebido, normalizar os dados e salvar corretamente a informação em um banco de dados relacional.<br> 

=> Exibir uma lista das operações importadas por lojas, sendo que essa lista deve conter um totalizador do saldo em conta por loja.

Seguirá os conceitos de api RestFul, utilizando Django Rest e SQLite 3.

## Tecnologias
<div>
<img align="center" alt="css" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img align="center" alt="css" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">  
</div>
<br>

## Documentação do CNAB
<div>
<img align="center" alt="css" src="https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/documentacao_cnab.png">

<br>

## Documentação sobre os tipos das transações
<img align="center" alt="css" src="https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/tipo_transacao.png">  
</div>

<br>

## Clonando o repositório:

1. Copie o code SSH do repositório do Projeto

<img align="center" alt="css" src="https://i.im.ge/2023/02/09/a6UwzL.code-repositorio.png">  

<br>

2. No Terminal faça um clone do repositorio:
```bash
git clone git@github.com:marcuspvh/Desafio_Backend_m6.git
```

3. Abra seu VSCode, selecione a pasta do seu repositorio.


<br>
## A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Baixe as bibliotecas e extensões contidas no `requirements.txt`:
```shell
pip install -r requirements.txt
```


4. Agora faça a atualização do pip:
```shell
python.exe -m pip install --upgrade pip
```

5. Agora faça as Migrations, com o comando:
```shell
python manage.py makemigrations
```

6. Agora faça as Migrate, para criação ou atualização do DB, com o comando:
```shell
python manage.py migrate
```

## Rodando o Servidor

- Rodando o servidor:
```shell
python manage.py runserver
```

- Acessando a page do Servidor:
```shell
ctrl + clique na porta:
Starting development server at http://127.0.0.1:8000/
```

<img align="center" alt="css" src="https://i.im.ge/2023/02/09/a6he6K.localhost.png">  

<br>

- page do Servidor:
<img align="center" alt="css" src="https://i.im.ge/2023/02/09/a6iyxS.pade-do-servidor.png"> 


## Acessando os Formularios:

- Para acessar o formularios, deve acrescentar "api/upload/":
```navegador
http://127.0.0.1:8000/api/upload/
```
<img align="center" alt="css" src="https://i.im.ge/2023/02/09/a6ifd4.formulario-upload.png"> 


<br>


- Selecionar o arquivo e clicar em enviar:
```navegador
selecinar arquivo CNAB_file.txt,
em seguida, clicar em eviar
```
<img align="center" alt="css" src="https://i.im.ge/2023/02/09/a6iBLm.arquivo-selecionado.png"> 

<br>
