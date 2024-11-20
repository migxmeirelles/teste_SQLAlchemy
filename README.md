seguindo os estudos de conexão entre Python e Banco de Dados, encontrei uma alternativa à biblioteca PYODBC, a biblioteca SQLAlchemy.

Nos arquivos deixei modelos de conexão que testei com diversos bancos de dados que tenho acesso, caso de Postgre e SQLite em meu computador pessoal, e SQL Server e Oracle em meu computador de serviço, portando obviamente após as conexões ocultei com "***" as informações.

### Código:
* começamos importando as bibliotecas necessárias.
* passamos as informações para conexão como servidor, usuário e senha (as informações variam de acordo com cada banco de dados).
* criamos uma url de conexão, usando as informações anteriores.
* usamos um método para printar se a conexão foi bem sucedida ou não, servindo de teste.
* usando a biblioteca pandas, criamos um data frame com a conexão e também uma query.
* finalizamos com um print do data frame, novamente como um teste.

### Observações:
* conexão com SQLite é muito mais simpes, não precisando passar muitas informações, somente o banco.
* na conexão com oracle foi preciso usar uma conexão com banco SID, pois era o único disponível para testar.
* na conexão com postgre, não ocultei tudo pois estava usando um banco de dados Pagila, que pode ser baixado pela internet e contém informações de uma locadora de filmes.

### Tecnologias Usadas:
* Banco de dados SQL: SQLite, PostgreSQL, SQL Server e Oracle.
* Python com bibliotecas Pandas e SQLAlchemy.
