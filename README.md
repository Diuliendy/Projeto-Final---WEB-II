# Projeto-Final-WEB-II
# Sistema de cadastro de alunos
---
O sistema de cadastramento criado foi projetado no modelo CRUD e utilizando o framework Flask.Seu propósito é organizar e facilitar o acesso de fórma rápida e fácil aos dados cadastrados pelo usuário.
- ### Estrutura de pastas:
```
pf/
│── app/
│   ├── controllers/
│   │   └── view.py
│   ├── models/
│   │   └── alunos.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── cadastro.html
│   │   ├── editar.html
│   │   └── listar.html
│   ├── instance/
│   │   └── alunos.db
│── run.py
│── README.md
```

- ### Funcionalidades:
* Edição de dados
* Remover registros
* Interface simples em HTML + CSS
* Banco de dados SQLite com SQLAlchemy

- ### Tecnologias Utilizadas:

 * Python 3
 * Flask
 * SQLAlchemy
 * HTML5
 * CSS3
 * JavaScript (opcional)
 * SQLite

- ### Rotas Principais:

| Rota            | Descrição       |
| --------------- | --------------- |
| `/`             | Página inicial  |
| `/alunos`       | Lista de alunos |
| `/cadastro`     | Cria novo aluno |
| `/editar/<id>`  | Edita aluno     |
| `/deletar/<id>` | Remove aluno    |

- ### Autores:
  * João Victor Martins Costa
  * José Luís da Silva Baltazar
  * Diuli Endy Porfírio Pinheiro


