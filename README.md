# Financial API
Consulta de pontos da bolsa de valores utilizando o Alpha Vantage

## Front-end
Para a criação do front-end foi utilizado
- Jquery
- Bootstrap

Para acessar o site, basta abrir o arquivo index.html em ~/financial_api/front/index.html

## Back-end
Este projeto foi desenvolvido utilizando o microframework Flask

## Configuração do back-end
No diretório do projeto abra o prompt e execute o seguinte comando para instalação das bibliotecas 

`$ pip install -r requirements.txt`

Em seguida este
`$ export FLASK_APP=app.py  `

Para a execução dos CRUD's é necessário o ter o postgresql instalado.
Crie um banco de dados com o nome de : 

`database_api`

No arquivo app.py,na linha 12
```python
#Altere a seguinte linha
"postgresql://postgres:123Senha@localhost:5432/database_api"
#Para 
"postgresql://user:password@localhost:port/database_api"
#user: Usuário do seu postgress
#password: Senha do seu usuário
#port: Porta da conexão com o banco
```
Rodar as migrates para a criação das tabelas no banco

`$flask db init`

`$flask db migrate`

`$flask db upgrade`

Para iniciar o projeto

`$ flask run`

## EndPoints

## Ibovespa

Consulta dos pontos do Ibovespa
Método GET
Url :http://127.0.0.1:5000/ibovespa
## Empresas

Consulta de pontos de outras empresas
Método GET
Url :http://127.0.0.1:5000/points/< symbol >

Exemplo : http://127.0.0.1:5000/points/ITUB

## CRUD Usuario

Método GET
Url : http://127.0.0.1:5000/user

Retorna todos os registros cadastrados no banco

Url : http://127.0.0.1:5000/user/< id >

Retorna o registro do id

Método POST
Url :http://127.0.0.1:5000/user

Body da requisição com json com as seguintes chaves: user_name ,company, password

Método PUT
Url : http://127.0.0.1:5000/user/< id >

Body da requisição com json com as seguintes chaves: user_name ,company, password
Atualiza o registro

Método DELETE
Url : http://127.0.0.1:5000/user/< id >

Deleta o registro que possua o id

## CRUD Empresa

Método GET
Url : http://127.0.0.1:5000/company

Retorna todos os registros cadastrados no banco

Url : http://127.0.0.1:5000/company/< id >

Retorna o registro do id

Método POST
Url : http://127.0.0.1:5000/company

Body da requisição com json com as seguintes chaves: name ,symbol

Método PUT
Url : http://127.0.0.1:5000/company/< id >

Body da requisição com json com as seguintes chaves:  name ,symbol
Atualiza o registro

Método DELETE
Url : http://127.0.0.1:5000/company/< id >

Deleta o registro que possua o id

## CRUD Preço

Método GET
Url : http://127.0.0.1:5000/price

Retorna todos os registros cadastrados no banco

Url : http://127.0.0.1:5000/price/< id >

Retorna o registro do id

Método POST
Url : http://127.0.0.1:5000/price

Body da requisição com json com as seguintes chaves: id_company ,price

Método PUT
Url : http://127.0.0.1:5000/price/< id >

Body da requisição com json com as seguintes chaves:  id_company ,price
Atualiza o registro

Método DELETE
Url : http://127.0.0.1:5000/price/< id >

Deleta o registro que possua o id

## Testes

Para realização dos testes execute o seguinte comando no diretorio do projeto
`$ py.test`

Para gerar um relatório sobre os testes , execute os seguintes comandos

`$ coverage run --source=app -m py.test  `

`$ coverage report -m   `

`$ coverage html`

Será gerado um pasta com o nome de htmlcov na raiz do projeto, dentro da pasta abra o arquivo index.html para melhor visualização do relatório.
