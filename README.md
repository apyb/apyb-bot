# apyb-bot

## Automações

### Notificando novas mensagens no APyB/Comunidade por e-mail

A APyB se comunica com seus associados por meio de dois canais principais: o repositório [APyB/Comunidade](https://github.com/apyb/comunidade) e uma lista de e-mails gerenciada pelo Google Groups.

Para manter a lista de e-mails atualizada com as mensagens enviadas no repositório, é possível utilizar o comando `github:new-discussion-notification`.

Veja um exemplo de uso:
```bash
export GITHUB_TOKEN="*****"  # Token da API do Github
export EMAIL_NO_REPLY_PASSWORD="*****"  # Senha do e-mail usado para notificação
$ apyb-bot github:new-discussion-notification --id 43 --send-to lista-de-email@apyb
```

No exemplo acima, o comando utiliza a API do Github para buscar os detalhes da mensagem [#43](https://github.com/apyb/comunidade/discussions/43) no repositório APyB/Comunidade e envia um e-mail para o Google Groups da associação. Para que o comando funcione corretamente, é necessário fornecer o token da API do Github e a senha do e-mail utilizado para a notificação.
