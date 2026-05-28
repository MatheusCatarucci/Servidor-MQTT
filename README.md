# 📡 Ecossistema MQTT — Documentação do Projeto

> Projeto acadêmico SENAI — Comunicação IoT com MQTT, ESP32 e Sistema Web

---

## 👥 Divisão do Grupo

O grupo de 6 pessoas está dividido em duas frentes de trabalho que operam em paralelo e se integram ao final.

| Frente | Responsabilidade Principal | Integrantes |
|---|---|---|
| **Back-end / Hardware** | Broker MQTT, ESP32 e firmware | Pessoa 1, Pessoa 2, Pessoa 3 |
| **Front-end / Web** | API Python, servidor MQTT e interface | Pessoa 4, Pessoa 5, Pessoa 6 |

> ⚠️ As duas frentes precisam alinhar os **nomes dos tópicos MQTT** antes de começar a programar. Esse é o único ponto de contrato entre os dois times.

---

## 🗂️ Estrutura de Pastas do Projeto

```
mqtt-ecossistema/
│
├── broker/                  → Configurações do Mosquitto (Frente 1)
│   └── mosquitto.conf
│
├── firmware/                → Código C++ da ESP32 (Frente 1)
│   └── main.cpp
│
├── web/                     → Sistema Web em FastAPI (Frente 2)
│   ├── app.py               → API principal + rotas
│   ├── server.py            → Cliente MQTT (subscriber/publisher)
│   ├── controllers/
│   ├── models/
│   ├── views/
│   │   └── templates/       → HTML Jinja2
│   └── static/              → CSS, JS, imagens
│
└── README.md                → Esta documentação
```

---

## 🔵 Frente 1 — Back-end / Hardware

> Responsáveis pelo broker MQTT rodando no WSL e pelo firmware da ESP32.

---

### ✅ Tarefa 1 — Configuração do Broker MQTT (Mosquitto no WSL)

**Objetivo:** Instalar e deixar o broker acessível na rede local para que tanto a ESP32 quanto o sistema web consigam se conectar.

**O que precisa ser feito:**

- Instalar o Mosquitto no WSL (Ubuntu)
- Editar o arquivo `mosquitto.conf` para:
  - Permitir conexões anônimas (ambiente de desenvolvimento)
  - Escutar na porta `1883`
  - Permitir acesso externo (não só localhost)
- Descobrir o IP da máquina na rede local (`ip addr` no WSL ou `ipconfig` no Windows)
- Testar com dois terminais: um publicando e outro assinando um tópico
- Anotar o IP fixo ou configurar IP estático para que ESP32 e web usem o mesmo endereço

**Entregável:** Broker rodando, IP documentado, print do teste de pub/sub funcionando.

---

### ✅ Tarefa 2 — Firmware da ESP32

**Objetivo:** Conectar a ESP32 ao broker MQTT e acionar um dispositivo físico (LED, relé, etc.) via mensagem.

**O que precisa ser feito:**

- Configurar as credenciais Wi-Fi no código (`SSID` e `senha`)
- Configurar o IP do broker e a porta `1883`
- Assinar o tópico de comando (ex: `senai/grupo1/dispositivo/cmd`)
- Ao receber a mensagem `"ON"`, ligar o dispositivo
- Ao receber a mensagem `"OFF"`, desligar o dispositivo
- Publicar o estado atual no tópico de status (ex: `senai/grupo1/dispositivo/status`) após cada acionamento
- Manter a reconexão automática ao broker caso a conexão caia

**Entregável:** ESP32 respondendo a comandos MQTT enviados pelo terminal. Print ou vídeo do dispositivo sendo acionado.

---

## 🟢 Frente 2 — Front-end / Web

> Responsáveis pela API FastAPI, pelo cliente MQTT em Python e pela interface visual.

---

### ✅ Tarefa 3 — Sistema Web (FastAPI + MQTT)

Essa frente é composta por três arquivos principais com responsabilidades distintas.

---

#### 📄 `server.py` — Cliente MQTT

**Responsável:** _(definir internamente no grupo)_

**Objetivo:** Conectar ao broker como cliente MQTT, receber mensagens de status da ESP32 e disponibilizá-las para a API.

**O que precisa fazer:**

- Conectar ao broker usando o IP combinado com a Frente 1
- Assinar o tópico de status (ex: `senai/grupo1/dispositivo/status`)
- Armazenar o último estado recebido em uma variável compartilhada (em memória, dicionário ou arquivo)
- Rodar em uma thread separada para não bloquear a API
- Expor uma função para **publicar** mensagens de comando (ex: `senai/grupo1/dispositivo/cmd`)

---

#### 📄 `app.py` — API FastAPI

**Responsável:** Matheus

**Objetivo:** Servir a interface web e expor as rotas para monitoramento e acionamento do dispositivo.

**O que precisa fazer:**

- Inicializar o `server.py` junto com a aplicação (ao subir o FastAPI)
- Servir as páginas HTML via Jinja2 (padrão MVC)
- Expor as rotas abaixo:

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Página principal com o painel de controle |
| `GET` | `/status` | Retorna o estado atual do dispositivo (JSON) |
| `POST` | `/comando` | Envia `ON` ou `OFF` para o broker |

- Passar o estado do dispositivo para o template HTML ao renderizar a página

---

#### 📄 Templates HTML (Views)

**Responsável:** _(definir internamente no grupo)_

**Objetivo:** Interface visual para monitorar e acionar o dispositivo.

**O que precisa mostrar:**

- Estado atual do dispositivo (ex: `● LIGADO` / `○ DESLIGADO`)
- Dois botões: **Ligar** e **Desligar**
- Atualização do estado após o clique (via reload de página ou JavaScript)
- Identificação do grupo no layout

---

## 🔴 Tarefa 4 — Integração entre Grupos (Desafio Extra)

**Objetivo:** Conectar o sistema web do grupo no broker de **outro grupo** e acionar o dispositivo deles remotamente.

**O que precisa ser feito:**

- Obter o IP do broker do outro grupo e os nomes dos tópicos que eles usam
- Na interface web, adicionar uma seção "Controle Externo" com os mesmos botões de ligar/desligar
- No `app.py`, criar uma rota separada (ex: `/externo/comando`) que publique no broker do outro grupo
- No `server.py`, assinar também o tópico de status do outro grupo para monitorar o estado do dispositivo deles
- Validar que o acionamento remoto funciona com os dois grupos presentes

**Entregável:** Print ou vídeo mostrando o dispositivo do outro grupo sendo acionado pela interface do seu grupo.

---

## 📐 Tópicos MQTT — Contrato entre as Frentes

> Este é o ponto de integração entre Frente 1 e Frente 2. Ambos os times devem usar exatamente os mesmos nomes.

| Tópico | Direção | Publicado por | Assinado por | Valores Esperados |
|---|---|---|---|---|
| `senai/grupo1/dispositivo/cmd` | Web → ESP32 | Sistema Web | ESP32 | `ON` / `OFF` |
| `senai/grupo1/dispositivo/status` | ESP32 → Web | ESP32 | Sistema Web | `ON` / `OFF` |

> 💡 Substituir `grupo1` pelo identificador real do grupo. Manter esse padrão facilita a integração com outros grupos na Tarefa 4.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Função | Frente |
|---|---|---|
| **Mosquitto** | Broker MQTT | Frente 1 |
| **WSL (Ubuntu)** | Ambiente do broker no Windows | Frente 1 |
| **ESP32** | Microcontrolador com Wi-Fi | Frente 1 |
| **C++ / Arduino** | Firmware da ESP32 | Frente 1 |
| **Python 3** | Linguagem do back-end web | Frente 2 |
| **FastAPI** | Framework da API web | Frente 2 |
| **Paho-MQTT** | Cliente MQTT em Python | Frente 2 |
| **Jinja2** | Templating HTML | Frente 2 |
| **HTML/CSS** | Interface visual | Frente 2 |

---

## 🔗 Dependências do Projeto Web

Arquivo `requirements.txt` da pasta `web/`:

```
fastapi
uvicorn
paho-mqtt
jinja2
python-multipart
```

---

## 🚀 Como Executar o Projeto

### Frente 1 — Subir o Broker

1. Abrir o WSL
2. Iniciar o Mosquitto com o arquivo de configuração customizado
3. Verificar o IP da máquina na rede local
4. Confirmar que a porta `1883` está acessível

### Frente 2 — Subir o Sistema Web

1. Instalar as dependências com `pip install -r requirements.txt`
2. Confirmar que o IP do broker em `server.py` está correto
3. Executar a aplicação com `uvicorn app:app --reload`
4. Acessar `http://localhost:8000` no navegador

---

## 📋 Checklist de Entrega

### Frente 1
- [ ] Mosquitto instalado e configurado no WSL
- [ ] Broker acessível na rede local
- [ ] Teste de pub/sub funcionando (print)
- [ ] ESP32 conectada ao broker
- [ ] Dispositivo físico sendo acionado via MQTT (print ou vídeo)
- [ ] Tópicos documentados e alinhados com a Frente 2

### Frente 2
- [ ] `server.py` conectando ao broker e recebendo mensagens
- [ ] `app.py` com rotas funcionando
- [ ] Interface exibindo estado do dispositivo
- [ ] Botões de ligar/desligar funcionando
- [ ] Print da interface em funcionamento

### Geral
- [ ] Repositório no GitHub criado
- [ ] `README.md` atualizado com prints
- [ ] Comunicação com o broker de outro grupo funcionando (Tarefa 4)
- [ ] Documentação completa conforme critérios da atividade

---

## 📸 Seção de Evidências

> _Adicionar aqui os prints e fotos conforme o sistema for sendo desenvolvido._

| Etapa | Evidência |
|---|---|
| Broker rodando no WSL | _(inserir print)_ |
| Teste de pub/sub no terminal | _(inserir print)_ |
| ESP32 acionando o dispositivo | _(inserir foto/vídeo)_ |
| Interface web funcionando | _(inserir print)_ |
| Integração entre grupos | _(inserir print/vídeo)_ |

---

*Documentação gerada para o projeto MQTT Ecossistema — SENAI*