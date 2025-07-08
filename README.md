# Documentação do Projeto *Flow-Messenger*

Projeto para **envio automatizado** de mensagens via WhatsApp usando a API **Z-API**, com disparos configurados em banco **Supabase** e painel web para monitoramento.

---

## Estrutura do Projeto
```
flow-messenger/
│
├── disparos.py         # Envia mensagens via Z-API usando dados do Supabase
├── painel.py           # Aplicação Flask que exibe painel web com disparos
├── templates/
│   └── painel.html     # Template HTML para painel de disparos
├── .env                # Variáveis de ambiente (não subir no Git!)
```


---

## Arquivos e Funções

### disparos.py

- Busca disparos pendentes no Supabase.
- Monta e envia mensagens personalizadas via API Z-API.
- Atualiza o status dos disparos (enviado ou erro).

  Funções principais:

- montar_mensagem(nome, link): Cria o texto da mensagem para enviar.
- enviar_mensagem(telefone, mensagem): Envia mensagem para o WhatsApp usando a API da Z-API.
- main(): Busca disparos pendentes, envia as mensagens e atualiza o status.

### painel.py

- Roda servidor Flask.
- Renderiza o template painel.html com os dados.
- Exibe todos os disparos em tabela web.

### templates/painel.html

- Página web com tabela que mostra nome, telefone, link e status.
- Status colorido para facilitar visualização.

### .env

> **Importante:** Arquivo com variáveis sensíveis.

---

## 🚀 Como usar

Siga os passos abaixo para executar o sistema de disparos automáticos com painel web:

### 1. Clone o repositório

```bash
git clone https://github.com/luanaforte/flow-messenger.git
cd flow-messenger
```

### 2. Configure o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes variáveis com seus dados:

```env
SUPABASE_URL=https://sua-instancia.supabase.co
SUPABASE_KEY=sua_chave_supabase
INSTANCE_ID=seu_instance_id
INSTANCE_TOKEN=seu_instance_token
CLIENT_TOKEN=seu_client_token
```

### 3. Execute os disparos de mensagens

Execute o script responsável por ler os dados do Supabase e enviar as mensagens via Z-API:

```bash
python disparos.py
```

Esse script irá:

- Buscar todos os contatos com status = pendente na tabela disparos;
- Enviar a mensagem personalizada para cada número;
- Atualizar o status para enviado ou erro conforme a resposta da API.

### 4. Inicie o painel web com Flask

O painel web permite acompanhar os disparos feitos, seus status e links enviados. Para iniciar, execute o comando:

```bash
python painel.py
```

### 5. Acesse o painel no navegador

Abra seu navegador e acesse:

> http://127.0.0.1:5000


No painel, você verá uma tabela listando os contatos importados do Supabase, incluindo:

- Nome
- Telefone
- Link do repositório
- Status da mensagem (pendente, enviado ou erro)
- Data do disparo (se disponível)

Essa interface é útil para monitorar o envio das mensagens e validar se houve sucesso ou falha em cada disparo.

No painel, você verá uma tabela listando os contatos importados do Supabase, incluindo:

- Nome
- Telefone
- Link do repositório
- Status da mensagem (pendente, enviado ou erro)
- Data do disparo (se disponível)

Essa interface é útil para monitorar o envio das mensagens e validar se houve sucesso ou falha em cada disparo.

## Direitos e Segurança

- **Proteção dos Dados Sensíveis:**  
  Todas as credenciais e tokens de acesso (como as chaves da Supabase e tokens da Z-API) estão armazenados em variáveis de ambiente no arquivo `.env`, que não deve ser versionado no Git para garantir a segurança dos dados.

- **Uso Responsável das APIs:**  
  O sistema utiliza tokens autorizados para interagir com o Supabase e Z-API, garantindo que apenas usuários autenticados possam enviar mensagens e acessar os dados.

- **Privacidade dos Contatos:**
  Os números de telefone e informações pessoais utilizadas no sistema são tratados com confidencialidade e usados exclusivamente para o propósito do envio das mensagens autorizadas.

- **Responsabilidade do Usuário:**  
  Este sistema é fornecido para facilitar comunicações legítimas e autorizadas. O uso indevido para spam ou mensagens não solicitadas é de responsabilidade exclusiva do usuário.
