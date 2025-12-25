# 🤖 ChatAUI

### Advanced Chat Agent — AI Chatbot powered by Chainlit & OpenAI Agents SDK

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python" />
  </a>
  <a href="https://docs.chainlit.io">
    <img src="https://img.shields.io/badge/Framework-Chainlit-0f172a?logo=react&logoColor=61dafb" />
  </a>
  <a href="https://openai.com">
    <img src="https://img.shields.io/badge/AI-OpenAI%20Agents%20SDK-black?logo=openai" />
  </a>
  <a href="https://huggingface.co">
    <img src="https://img.shields.io/badge/Deployed%20on-Hugging%20Face-yellow?logo=huggingface" />
  </a>
  <a href="https://console.cloud.google.com/">
    <img src="https://img.shields.io/badge/Auth-Google%20%7C%20GitHub-orange?logo=google" />
  </a>
</p>

> **ChatAUI** is an advanced, stateful conversational AI system built with **Chainlit**, **OpenAI Agents SDK**, and **UV**, featuring **OAuth authentication**, **custom UI elements**, and **real-time streaming responses**.

---

## ✨ Features

- 🧠 **OpenAI Agents SDK** — Intelligent reasoning with tool calling
- 💬 **Chainlit UI** — Reactive UI with token streaming
- 🔐 **OAuth Authentication** — GitHub & Google login support
- 💾 **Stateful Conversations** — Memory preserved per session
- 🧩 **Custom UI Elements** — JSX-based loaders and components
- ⚙️ **Custom Tools Support** — Local functions & API tools
- ☁️ **Hugging Face Deployment** — HTTPS-ready, Docker-based
- 🔌 **Flexible LLM Support** — OpenRouter, GPT, Gemini, etc.

---

## 🧱 Tech Stack

| Layer               | Technology                 |
| ------------------- | -------------------------- |
| **Language**        | Python 3.10+               |
| **Framework**       | Chainlit                   |
| **AI SDK**          | OpenAI Agents SDK          |
| **Env Manager**     | python-dotenv              |
| **Runtime Manager** | UV                         |
| **Auth Providers**  | Google OAuth, GitHub OAuth |
| **Cloud Platform**  | Hugging Face Spaces        |

---

## ⚙️ Getting Started (Local Development)

### 1️⃣ Install UV

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify:**

```bash
uv --version
```

### 2️⃣ Initialize Project

```bash
uv init chataui-app
cd chataui-app
```

### 3️⃣ Install Dependencies

```bash
uv add chainlit python-dotenv openai-agents
```

### 4️⃣ Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 5️⃣ Test Chainlit

```bash
chainlit hello
```

**Open:**

```
http://localhost:8000
```

If you see the Chainlit welcome screen, setup is correct.

### 6️⃣ Environment Variables

Create a `.env` file in the root:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=your_model_name

OAUTH_GITHUB_CLIENT_ID=your_github_client_id
OAUTH_GITHUB_CLIENT_SECRET=your_github_client_secret

OAUTH_GOOGLE_CLIENT_ID=your_google_client_id
OAUTH_GOOGLE_CLIENT_SECRET=your_google_client_secret

CHAINLIT_AUTH_SECRET=your_chainlit_auth_secret
```

Generate Chainlit secret:

```bash
chainlit create-secret
```

### 7️⃣ Chainlit Configuration

Create `chainlit.yaml`:

```yaml
chainlit: 2.9.4

ui:
  name: "ChatAUI"
  description: "Advanced stateful AI chatbot with OAuth authentication built using Chainlit and OpenAI Agents SDK."
```

### 8️⃣ Run the App 🚀

```bash
chainlit run main.py -w
```

**Visit:**

```
http://localhost:8000
```

Login with **Google** or **GitHub** and start chatting.

---

## ☁️ Deployment on Hugging Face (Docker Space)

Hugging Face Spaces provide **automatic HTTPS**, making them ideal for **OAuth-based Chainlit apps**.

---

### 1️⃣ Space Settings

- **SDK**: Docker
- **Port**: `7860`
- **Visibility**: Public or Private

---

### 2️⃣ Dockerfile

Create `Dockerfile` in project root:

```dockerfile
FROM python:3.11-slim

WORKDIR /

# Install Python packages manually
RUN pip install --no-cache-dir chainlit
RUN pip install --no-cache-dir openai-agents
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir openai
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir httpx
RUN pip install --no-cache-dir pydantic

COPY . .

EXPOSE 7860

# ---- Start Chainlit ----
CMD ["chainlit", "run", "main.py", "--host", "0.0.0.0", "--port", "7860"]
```

---

### 3️⃣ Hugging Face Secrets

In **Space → Settings → Secrets**, add:

```ini
OPENROUTER_API_KEY=xxxx
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=your_model

OAUTH_GITHUB_CLIENT_ID=xxxx
OAUTH_GITHUB_CLIENT_SECRET=xxxx

OAUTH_GOOGLE_CLIENT_ID=xxxx
OAUTH_GOOGLE_CLIENT_SECRET=xxxx

CHAINLIT_AUTH_SECRET=xxxx
```

⚠️ Never commit `.env` to GitHub.

---

### 4️⃣ OAuth Callback URLs

Replace callbacks in GitHub / Google dashboards with:

**GitHub**

```
https://<your-space-name>.hf.space/auth/github/callback
```

**Google**

```
https://<your-space-name>.hf.space/auth/google/callback
```

---

## 📂 Folder Structure

```
chataui-app/
│
├── public
│   ├── elements
│   │   └── DottedLoader.jsx
│   ├── avatar.png
│   ├── favicon.png
│   ├── github_banner.png
│   ├── logo_dark.png
│   ├── logo_light.png
│   └── theme.json
├── .gitignore
├── README.md
├── chainlit.md
├── chainlit.yaml
├── data.py
├── instructions.py
├── main.py
├── pyproject.toml
└── uv.lock
```

---

## 🧑‍💻 Author

**👨‍💻 Afaq Ul Islam**
Frontend Developer | SEO Specialist | Freelancer | Agentic AI Developer
🌐 [Afaq Ul Islam - Portfolio](https://afaqulislam.github.io)
💼 [Afaq Ul Islam - Linkedin](https://www.linkedin.com/in/afaqulislam)
🐙 [Afaq Ul Islam - Twitter(X)](https://x.com/afaqulislam708)

> Passionate about building intelligent, scalable, and production-ready AI systems.

---

### 🧠 Built with

**Python · Chainlit · OpenAI Agents SDK · OpenRouter · Hugging Face · OAuth**
