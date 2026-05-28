# 📡 Ecossistema MQTT

> Projeto SENAI — IoT com MQTT, ESP32 e Sistema Web

---

## 👥 Times

| Frente | Integrantes |
|---|---|
| 🔵 **Hardware / Infra** | Samuel Gracias, Gustavo Zampiroca, Nicolas Luciani |
| 🟢 **Sistema Web** | Matheus Catarucci, Gabriel Leonardo, Moises Tafarello |

---

## 🔵 Frente 1 — Hardware / Infra

| Integrante | Responsabilidade |
|---|---|
| **Gustavo Zampiroca** | Instalar e configurar o Mosquitto no WSL. Garantir que o broker esteja acessível na rede local e documentar o IP. |
| **Samuel Gracias** | Desenvolver o firmware C++ da ESP32. Conectar ao broker, assinar o tópico de comando e acionar o dispositivo físico. |
| **Nicolas Luciani** | Validar a comunicação com testes de pub/sub. Ser o ponto de contato com o outro grupo na Tarefa 4 (trocar IPs e tópicos). |

---

## 🟢 Frente 2 — Sistema Web

| Integrante | Responsabilidade |
|---|---|
| **Matheus Catarucci** | `app.py` (rotas FastAPI) e `server.py` (cliente MQTT em Python, pub/sub). |
| **Gabriel Leonardo** | Templates HTML com Jinja2. Página principal, exibição de estado e botões de acionamento. |
| **Moises Tafarello** | CSS e arquivos estáticos. Estilo visual da interface, feedback de estado (cores, botões). |

---

## 📐 Tópicos MQTT — Contrato entre os Times

> Ambos os times devem usar exatamente estes nomes.

| Tópico | Quem publica | Quem assina | Valores |
|---|---|---|---|
| `senai/grupo1/dispositivo/cmd` | Sistema Web | ESP32 | `ON` / `OFF` |
| `senai/grupo1/dispositivo/status` | ESP32 | Sistema Web | `ON` / `OFF` |

---

## 🚀 Como Rodar o Projeto

### Frente 1 — Subir o Broker (Gustavo)

1. Abrir o WSL
2. Iniciar o Mosquitto com o `mosquitto.conf` configurado
3. Anotar o IP da máquina e repassar para a Frente 2
4. Confirmar que a porta `1883` está acessível na rede

### Frente 2 — Subir o Sistema Web (Matheus)

1. Abrir o terminal na pasta `web/`
2. Criar e ativar o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
```
3. Instalar as dependências:
```bash
pip install -r requirements.txt
```
4. Colocar o IP do broker no `server.py`
5. Subir a aplicação:
```bash
uvicorn app:app --reload
```
6. Acessar `http://localhost:8000` no navegador

---

## 📋 Checklist

### 🔵 Frente 1
- [ ] **Gustavo** — Broker rodando no WSL, IP documentado
- [ ] **Samuel** — ESP32 acionando dispositivo via MQTT
- [ ] **Nicolas** — Teste de pub/sub validado + contato feito com outro grupo

### 🟢 Frente 2
- [ ] **Matheus** — `server.py` e `app.py` funcionando
- [ ] **Gabriel** — Interface exibindo estado e respondendo aos botões
- [ ] **Moises** — CSS aplicado e interface apresentável

### Geral
- [ ] Repositório no GitHub com todos os arquivos
- [ ] Acionamento remoto do dispositivo do outro grupo funcionando
- [ ] Prints/evidências adicionados ao README

---

## 📸 Evidências

| Etapa | Responsável | Print/Vídeo |
|---|---|---|
| Broker rodando no WSL | Gustavo | _(inserir)_ |
| Pub/sub no terminal | Nicolas | _(inserir)_ |
| ESP32 acionando dispositivo | Samuel | _(inserir)_ |
| Interface web funcionando | Gabriel / Moises | _(inserir)_ |
| Integração entre grupos | Nicolas / Gabriel | _(inserir)_ |

---

*SENAI — Projeto MQTT Ecossistema*