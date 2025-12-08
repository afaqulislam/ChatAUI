# 🤖 ChatAUI (Advance Chat Agent — AI Chatbot powered by Chainlit & OpenAI Agents SDK)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) [![Framework](https://img.shields.io/badge/Framework-Chainlit-2ea44f?logo=chainlit)](https://docs.chainlit.io) [![Auth](https://img.shields.io/badge/Auth-Google%20%7C%20GitHub-orange?logo=google)](https://console.cloud.google.com/) [![Cloud](https://img.shields.io/badge/Deployed%20on-Render-blue?logo=render)](https://render.com)

> **Advance Chat Agent** is an intelligent conversational system built with **Chainlit**, **OpenAI Agents SDK**, and **UV**, offering a seamless chat experience with **OAuth authentication**, **stateful memory**, and **real-time LLM reasoning**.

---

## ✨ Features

- 🧠 **OpenAI Agents SDK** — Intelligent reasoning with function tools
- 💬 **Chainlit UI** — Clean, reactive, streaming chat interface
- 🔐 **OAuth Authentication** — Secure sign-in via GitHub or Google
- 💾 **Stateful Conversations** — Memory across user sessions
- ⚙️ **Custom Tools Support** — Extend with APIs or local functions
- ☁️ **Render Cloud Ready** — Smooth HTTPS deployment for OAuth
- 🧩 **Flexible LLM Support** — Works with OpenRouter, Gemini, GPT, etc.

---

## 🧱 Tech Stack

| Layer               | Technology                 |
| :------------------ | :------------------------- |
| **Language**        | Python 3.10+               |
| **Framework**       | Chainlit                   |
| **AI SDK**          | OpenAI Agents SDK          |
| **Env Manager**     | python-dotenv              |
| **Runtime Manager** | UV                         |
| **Auth Providers**  | Google OAuth, GitHub OAuth |

---

## ⚙️ Getting Started

### 1️⃣ Install UV

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

---

### 2️⃣ Initialize the Project

```bash
uv init chataui-app
cd chataui-app
```

---

### 3️⃣ Install Dependencies

```bash
uv add chainlit python-dotenv openai-agents
```

---

### 4️⃣ Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

---

### 5️⃣ Test Chainlit Installation

```bash
chainlit hello
```

Then open:

```
http://localhost:8000
```

✅ You should see:

```
Your name is: Afaq Ul Islam
Chainlit installation is working successfully!
```

---

### 6️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openrouter_llm_model

OAUTH_GITHUB_CLIENT_ID=your_github_client_id
OAUTH_GITHUB_CLIENT_SECRET=your_github_client_secret

OAUTH_GOOGLE_CLIENT_ID=your_google_client_id
OAUTH_GOOGLE_CLIENT_SECRET=your_google_client_secret

CHAINLIT_AUTH_SECRET=your_chainlit_auth_secret
```

#### 🔑 Where to get keys:

- [OpenRouter API Keys](https://openrouter.ai/settings/keys)
- [OpenRouter Models](https://openrouter.ai/models?q=free)
- [GitHub OAuth Apps](https://github.com/settings/applications)
- [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials)
- Chainlit Auth Secret:

  ```bash
  chainlit create-secret
  ```

---

### 7️⃣ Create Chainlit Configuration

Add `chainlit.yaml` to your root directory:

```yaml
chainlit: 2.4.1

# Interface settings
ui:
  name: "ChatAUI Using Chainlit"
  description: "A Advance Question Answering Stateful chatbot with GitHub and Google authentication built with Python, UV, and Chainlit."
```

---

### 8️⃣ Run the App 🚀

```bash
chainlit run main.py -w
```

Visit:

```
http://localhost:8000
```

✅ Login with **Google** or **GitHub** → start chatting with your **Advance Chat Agent**!

---

## ☁️ Deployment on Render (Recommended)

Render gives full HTTPS, perfect for OAuth (GitHub + Google) and other secure features.

---

## 1️⃣ Create `render.yaml` in project root

```yaml
services:
  - type: web
    name: chataui-app
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "chainlit run main.py --host 0.0.0.0 --port $PORT"
    envVars:
      - key: OPENROUTER_API_KEY
        sync: false
      - key: OAUTH_GITHUB_CLIENT_ID
        sync: false
      - key: OAUTH_GITHUB_CLIENT_SECRET
        sync: false
      - key: OAUTH_GOOGLE_CLIENT_ID
        sync: false
      - key: OAUTH_GOOGLE_CLIENT_SECRET
        sync: false
      - key: CHAINLIT_AUTH_SECRET
        sync: false
      - key: PYTHON_VERSION
        value: 3.10
```

---

## 2️⃣ Push your code to GitHub

---

## 3️⃣ Go to Render → **New Web Service**

- Select your repo
- Auto-detect `render.yaml`
- Deploy
- Render gives you a URL like:

```
https://chataui.onrender.com
```

---

## 4️⃣ Update OAuth callback URL

### GitHub OAuth:

```
https://chataui.onrender.com/auth/github/callback
```

### Google OAuth:

```
https://chataui.onrender.com/auth/google/callback
```

---

## 📂 Folder Structure

```
chataui-app/
│
├── main.py                # Core chatbot logic
├── instructions.py        # Define Chatbot behaviour
├── data.py                # Portfolio / structured data
├── public/                # Custom Logo/Avatar/Banner
├── .env                   # Environment variables
├── chainlit.yaml          # Chainlit configuration
├── requirements.txt       # Optional dependency export
├── render.yaml            # Render deployment configuration
└── README.md              # Project documentation
```

---

## 🧑‍💻 Author

**👨‍💻 Afaq Ul Islam**
Frontend Developer | SEO + Freelancer + Agentic AI Developer with Python
🌐 [Portfolio Website](https://afaqulislam.github.io) • 💼 [LinkedIn](https://www.linkedin.com/in/afaqulislam) • 🐙 [GitHub](https://github.com/afaqulislam)

> Passionate about building intelligent, user-centric, and production-ready software.

---

### 🧠 Made with ❤️ using

**Python**, **Chainlit**, **OpenAI Agents SDK**, and **Google + Github Oauth**
