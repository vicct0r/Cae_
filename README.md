# Central de Atendimento ao Estudante

## Status do Projeto
Este repositório está **fechado**. O projeto foi interrompido devido à limitação do Heroku em gerenciar arquivos de mídia, que são efêmeros e não persistem após a reinicialização dos dynos. 

Para uma versão funcional do projeto que utiliza o Amazon S3 para gerenciar arquivos de mídia e estáticos, acesse o repositório de continuidade:

[Projeto Django com Amazon S3](https://github.com/vicct0r/django-heroku-s3)

## Descrição do Projeto
Este projeto visa replicar o funcionamento de um sistema de Central de Atendimento ao Estudante (CAE), atuando como um assistente para universitários.

**Palavras-chave:** Sistema Django, gestão acadêmica, acessibilidade.

## Problemas Conhecidos
Os principais desafios enfrentados incluíam:
- A manutenção dos arquivos de mídia no Heroku, que não suporta armazenamento persistente.

## Configuração da Minha Máquina
Informações relevantes da minha máquina para o desenvolvimento do projeto:

- **Sistema Operacional:** Ubuntu 22.04.5 LTS
- **Versão do Python:** 3.10.12
- **Dependências:** Certifique-se de que as bibliotecas necessárias estão instaladas, como Django e outras dependências especificadas no `requirements.txt`.
- **Ambiente Virtual:** É recomendável usar um ambiente virtual para isolar as dependências do projeto.

**Dependências:** django, django-role-permissions, model-mommy, gunicorn, django-stdimage, dj-static
