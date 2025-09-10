# 🛡️ Project Aegis: RASP for LLM Applications  

🚀 **Making AI Safer, One Prompt at a Time**  

---

## 🎯 The Problem  
Large Language Models (LLMs) are powerful, but also vulnerable.  
Attackers can trick them with **prompt injections**, **jailbreaks**, and **malicious payloads** that bypass safety filters.  

⚠️ Right now, there’s **no reliable, lightweight, open-source RASP (Runtime Application Self-Protection) for LLM apps**.  
That means developers are forced to choose between:  
- Building **fragile custom defenses**, or  
- **Risking their users’ safety**.  

---

## 💡 Our Solution: Aegis  
Aegis is a **plug-and-play runtime shield** for any LLM-powered app.  

Think of it as **an antivirus for AI prompts**:  
🧹 **Sanitizes user inputs** (catches jailbreaks, injections, hidden malicious instructions)  
🔍 **Monitors runtime activity** (detects abnormal requests in real time)  
🚫 **Blocks unsafe actions** before they ever reach the model  

> 🛡️ With Aegis, devs can focus on building apps, not chasing the latest jailbreak.  

---

## ✨ Key Features (MVP)  
✅ Input Sanitizer – strips out harmful instructions  
✅ Runtime Monitor – detects & logs attacks  
✅ Lightweight Middleware – drop it into any Python LLM app  
✅ Open-Source & Developer Friendly  

---

## 🔧 Tech Stack  
- **Flask** (for demo + easy integration)  
- **Python** (core sanitizer + monitoring logic)  
- Future: Plug-ins for FastAPI, LangChain, and cloud deployments  

---

## 📊 Why It Matters (Impact)  
🌍 **Universal Problem** → Every LLM app is at risk  
⏱️ **Low Integration Cost** → 5-minute setup for devs  
🔒 **User Safety First** → Protects against real-world jailbreaks  

---

## 🤝 Join Us  
We’re building this because **AI safety shouldn’t be an afterthought.**  
If you believe in safer AI apps, Aegis is for you.  

---

## 🧪 Quick Start  

```bash
# Clone repo
git clone https://github.com/Arshiya-Siddiqui/aegis-llm-rasp.git
cd aegis-llm-rasp

# Setup environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
