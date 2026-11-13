# Sistema de Cadastro e Consulta de Análises Químicas

Aplicação desenvolvida em **Python** com integração ao banco de dados **SQLite**, com o objetivo de cadastrar e consultar informações relacionadas a análises químicas.

O projeto foi desenvolvido como atividade prática de aprendizado em programação, utilizando conceitos de lógica, manipulação de dados e persistência em banco de dados.

## Objetivo

Desenvolver um sistema simples para organizar informações de análises químicas, permitindo registrar substâncias, suas respectivas concentrações e unidades de medida.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **SQLite:** banco de dados utilizado para armazenar os registros.
- **SQL:** linguagem utilizada para manipulação dos dados no banco.

## Funcionalidades

- Cadastro de informações sobre substâncias químicas.
- Armazenamento das concentrações e unidades de medida.
- Consulta dos registros armazenados no banco de dados.

## Estrutura do banco de dados

O banco de dados utilizado é o `laboratorio.db`, que contém a tabela `analises`.

| Campo | Descrição |
|---|---|
| `id` | Identificador do registro |
| `substancia` | Nome da substância química |
| `concentracao` | Concentração da substância |
| `unidade` | Unidade de medida da concentração |

### Exemplo de registro

| Substância | Concentração | Unidade |
|---|---:|---|
| Ácido Clorídrico | 0.5 | mol/L |

## Como executar o projeto

1. Tenha o Python instalado no computador.
2. Clone este repositório:

   ```bash
   git clone https://github.com/isabelaaraujo-code/Sistema-de-An-lises-Qu-micas.git
   ```

3. Abra a pasta do projeto no Visual Studio Code.
4. Execute o arquivo principal da aplicação pelo terminal:

   ```bash
   python analise.amostras.py
   ```

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos importantes, como:

- Lógica de programação com Python.
- Conexão entre Python e SQLite.
- Criação e manipulação de tabelas em banco de dados.
- Operações de inserção e consulta de registros.
- Organização e armazenamento de informações.

## Autora

**Isabela Araujo**

Estudante de Engenharia de Software, em desenvolvimento contínuo de conhecimentos em programação, banco de dados e tecnologia.

- GitHub: [@isabelaaraujo-code](https://github.com/isabelaaraujo-code)

---

Projeto acadêmico desenvolvido para fins de aprendizado e prática em programação.