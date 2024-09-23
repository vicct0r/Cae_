# Central de Atendimento ao Estudante

## Descrição do Projeto
Este projeto visa replicar o funcionamento de um sistema de Central de Atendimento ao Estudante (CAE), atuando como um assistente para universitários. O sistema oferece suporte e acesso a recursos que visam melhorar a qualidade dos estudos acadêmicos.

**Palavras-chave:** Sistema Django, Heroku, gestão acadêmica, acessibilidade.

## Funcionalidades
O projeto inclui diversas funcionalidades para gestão e acessibilidade, tais como:
- Acesso a conteúdo letivo (livros em PDF).
- Controle de acesso, com categorias para professores e alunos.
- Sistema de empréstimo de armários.
- Disponibilidade de eventos para visualização e inscrições para alunos.
- Atendimento específico para alunos.

Para mais detalhes, consulte a [documentação do Django](https://www.djangoproject.com/) e a [documentação do Heroku](https://devcenter.heroku.com/articles/getting-started-with-django).

## Como Contribuir
Contribuidores são bem-vindos para utilizar e colaborar no projeto. É recomendável ter uma noção básica de como utilizar Django com Class-Based Views (CBV). Para mais informações, consulte a [documentação do Django](https://docs.djangoproject.com/en/stable/topics/class-based-views/).

Sugestões de correções e melhorias são sempre bem-vindas. Ao enviar um pull request, destaque os pontos importantes de alteração no código para facilitar a avaliação antes do merge.

### Diretrizes para Pull Requests
Espero que os contribuidores sigam as diretrizes a seguir nos pull requests:
- Destaquem as principais alterações realizadas.
- Incluam testes, se aplicável.
- Mantenham a organização do código.

## Problemas Conhecidos
Atualmente, existem alguns problemas identificados que estão em processo de correção:
- Responsividade em algumas páginas não funciona corretamente em telas móveis.
- Ao fazer login como admin e acessar a página inicial, ocorre um erro de QuerySet. No futuro, será implementada uma versão que permitirá a participação de contas superuser no site.
- A estrutura do projeto ainda está desorganizada; planejamos uma reordenação nos diretórios dos apps.
- Um desafio significativo é a manutenção dos arquivos de mídia quando o aplicativo é publicado no Heroku. Estou trabalhando na implementação do AWS S3 para resolver esse problema. Consulte a [documentação do Heroku](https://devcenter.heroku.com/articles/using-amazon-s3-with-heroku) para mais detalhes.

## Configuração da Minha Máquina
Informações relevantes da minha máquina para o desenvolvimento do projeto:

- **Sistema Operacional:** Ubuntu 22.04.5 LTS
- **Versão do Python:** 3.10.12
- **Dependências:** Certifique-se de que as bibliotecas necessárias estão instaladas, como Django e outras dependências especificadas no `requirements.txt`.
- **Ambiente Virtual:** É recomendável usar um ambiente virtual para isolar as dependências do projeto.

- **Dependências:** django, django-role-permissions, model-mommy, gunicorn, django-stdimage, dj-static
