# 🌍 Voice-to-Voice Translator

## 📌 Overview
The **Voice-to-Voice Translator** is an AI-powered application that allows you to speak in one language and instantly hear the translation in another language.  
It combines **speech recognition**, **machine translation**, and **text-to-speech (TTS)** in a single Gradio interface.  

This tool is especially useful for:
- Language learners 🧑‍🎓  
- Travelers 🌎  
- Cross-cultural communication 🤝  
- Real-time assistance for meetings or study sessions 📚  

---

## 🎯 Features
✅ Record speech in one language  
✅ Automatic transcription (speech → text)  
✅ Neural machine translation using **Facebook’s M2M100** multilingual model  
✅ Text-to-Speech output in the target language  
✅ Dual-panel Gradio UI (Side-by-side: input & translated output)  
✅ Supports multiple languages (English, French, German, Arabic, Spanish, Turkish — and more coming soon!)  

---

## 🛠️ Tech Stack
- **[Gradio](https://gradio.app/)** → User interface  
- **[Whisper](https://github.com/openai/whisper)** → Speech-to-text transcription  
- **[M2M100](https://huggingface.co/facebook/m2m100_418M)** → Multilingual machine translation  
- **[Transformers](https://huggingface.co/docs/transformers)** → Model loading and inference  
- **Text-to-Speech** → Gradio’s `TTS` or external libraries  

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Malakgholam/EchoTranslate
cd EchoTranslate
