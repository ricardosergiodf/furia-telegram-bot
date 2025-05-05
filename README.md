# 🤖 FURIA Telegram Bot

Um bot informativo feito com Python e Telebot para compartilhar informações sobre os times, conquistas e redes sociais da organização de esports FURIA.

---

## 🚀 Funcionalidades

- 📜 Histórico da organização
- 👥 Lineups atualizadas por modalidade
- 🏆 Conquistas notáveis da equipe
- 🌐 Links das redes sociais oficiais
- 🤖 Respostas automáticas a saudações e despedidas
- 🔧 Comando `/comandos` com menu interativo

---

## 🧠 Comandos disponíveis

| Comando | Descrição |
|--------|-----------|
| `/start` ou `/help` | Saudação inicial e instruções |
| `/comandos` | Lista todos os comandos disponíveis |
| `/historia` | Mostra a história da FURIA |
| `/times` | Exibe as lineups atuais por modalidade (com botões) |
| `/conquistas` | Lista conquistas importantes da FURIA |
| `/redes_sociais` | Links das redes sociais oficiais |

---

## 📦 Estrutura do Projeto

```
furia-bot/
│
├── main.py             # Código principal do bot
├── src/
│   └── config.py       # Arquivo de configuração com dados fixos
└── README.md           # Este arquivo
```

---

## 🔐 Configuração (src/config.py)

```python
TOKEN = 'SEU_TOKEN_AQUI'
BOT_USERNAME = '@Furia_BotDoBot'
```

### 📌 Variáveis importantes:

- `SAUDACAO_IN`, `DESPEDIDA_IN`: Palavras-chave que ativam respostas automáticas.
- `LINEUPS`: Lineups por modalidade (ex: CS2, Valorant, LoL, etc).
- `CONQUISTAS`: Títulos importantes, com colocação, adversário e premiação.
- `REDES_SOCIAIS`: Links oficiais.

---

## 💬 Mensagens automáticas

- O bot responde automaticamente a:
  - Saudações: `oi`, `bom dia`, `boa tarde`, `boa noite`
  - Despedidas: `tchau`, `flw`, `bye`, etc.
- Em grupos: ele só responde se for **mencionado**.
- Em privado: responde normalmente.

---

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ricardosergiodf/furia-telegram-bot
   ```

2. Instale as dependências:
   ```bash
   pip install pyTelegramBotAPI
   ```

3. Configure seu token no arquivo `src/config.py`.

4. Execute o bot:
   ```bash
   python main.py
   ```

---

## 📷 Exemplo de uso

```text
Usuário: /times
Bot: (envia botões com modalidades)

Usuário: /conquistas
Bot: (envia lista formatada de títulos da FURIA)

Usuário: @Furia_BotDoBot oi
Bot: Fala, Furioso(a)! Use /comandos para ver o que consigo fazer.
```

---

## 👥 Créditos

Desenvolvido por Ricardo Duarte ⚡  
Inspirado na organização brasileira de esports: [FURIA](https://www.furia.gg/)
