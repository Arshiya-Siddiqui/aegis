# 🛡️ Aegis: Runtime Application Self-Protection for LLMs 

🚀 **Making AI Safer, One Prompt at a Time**  

---

## ❌ Problem
Large Language Models (LLMs) are powerful — but also fragile.  
- **Prompt Injection & Jailbreaks**: Attackers trick models into ignoring rules and leaking secrets.  
- **Data Exfiltration Risks**: Sensitive data (PII, API keys, system prompts) can be exposed.  
- **Enterprise Adoption Barriers**: Healthcare, finance, and regulated industries can’t risk sending unprotected prompts to third-party APIs.  
- **Poor User Experience**: Existing defenses just block requests, frustrating users and developers alike.  

In short: **LLM apps today are vulnerable, noisy, and hard to secure.**

---

## ✅ Solution
**Aegis** is a **self-hosted Runtime Application Self-Protection (RASP) proxy** for LLMs.  
- **Intercepts** every prompt and response in real-time.  
- **Detects threats** with a layered defense pipeline.  
- **Sanitizes instead of blocking** — neutralizing attacks while preserving UX.  
- **Logs every event** for audit, analysis, and continuous improvement.  
- **Privacy-first**: Runs entirely inside your environment (Dockerized). No data leaves your perimeter.  

Think of Aegis as an **immune system** for your LLM applications.  

---

## ✨ Key Features
- 🔍 **Hybrid Detection** — combines rule-based heuristics with modern ML classifiers.  
- 🛑 **Sanitize, Don’t Block** — neutralizes malicious inputs while keeping user flow smooth.  
- 🔒 **Privacy by Design** — self-hosted container, data never leaves your VPC.  
- 📜 **Transparent Logging** — every intercepted request and response is recorded for audit and tuning.  
- ⚡ **Lightweight & Fast** — minimal latency overhead, designed for production use.  
- 🧩 **Extensible** — add new detection modules and policies easily.  
- 🔐 **Secure by Default** — CI/CD pipelines with code scanning, dependency checks, and secret detection baked in.  

---

## ⚙️ Tech Stack
Aegis is designed to be:  
- **Lightweight** — built on modern Python frameworks for performance.  
- **Portable** — packaged as a Docker container for easy deployment.  
- **Extensible** — integrates with open-source NLP/ML models for smarter detection.  
- **Secure by Default** — CI/CD pipelines with automated code scanning, dependency checks, and secret detection.  

*(We keep the detection logic private to preserve security integrity.)*

---

## 🌍 Why It Matters (Impact)
- **For Developers**: Plug-and-play security, no need to be a security expert.  
- **For Enterprises**: A deployable guardrail that enables LLM adoption in regulated industries.  
- **For Users**: Seamless, safe interactions without “access denied” roadblocks.  
- **For the Ecosystem**: Moves AI security forward by focusing on **runtime protection**, not just static scans.  

Aegis helps teams **ship AI faster, safer, and with confidence.**

---

## 🚀 Quick Start
```bash
docker build -t aegis-proxy .
docker run -p 8080:8080 \
  -e UPSTREAM_URL=https://api.openai.com/v1/chat/completions \
  -e UPSTREAM_KEY=$OPENAI_API_KEY \
  aegis-proxy
