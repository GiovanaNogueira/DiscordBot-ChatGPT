# Atividade 07

**PRINCIPAL (900XP)**
- Criar um bot para o Discord;
- Ele terá diferentes comandos, dentre eles:
  - Comando para acessar a alguma info via WebScrapping;
  - Integrar com a API do Chat GPT para que possa conversar com o bot;
- Paralelo a esse bot, deve ser implementada uma API, na qual será feito o LOG do comando:
  - Nome do comando utilizado;
  - Nome do usuário que usou o comando;
  - Data de envio do comando;
- A API também deve ter um CRUD para os LOGs;

**EXTRA (300XP)**
- Só permitir que o usuário realize comandos se ele tiver logado, através da API (verificar como fazer login usando Flask);
- Para logar, será necessário ter uma persistência de dados (TXT/JSON/XML/MongoDB);