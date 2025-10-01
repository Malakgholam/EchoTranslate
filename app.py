import gradio as gr
import whisper
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from gtts import gTTS


#Load Models
print("Loading Whisper model...")
whisper_model = whisper.load_model("base")

print("Loading M2M100 model...")
m2m_model_name = "facebook/m2m100_418M"
m2m_tokenizer = M2M100Tokenizer.from_pretrained(m2m_model_name)
m2m_model = M2M100ForConditionalGeneration.from_pretrained(m2m_model_name)


# Translation Function
def translate_text(text, src_lang, tgt_lang):
    m2m_tokenizer.src_lang = src_lang
    encoded = m2m_tokenizer(text, return_tensors="pt")
    generated_tokens = m2m_model.generate(
        **encoded,
        forced_bos_token_id=m2m_tokenizer.get_lang_id(tgt_lang)
    )
    return m2m_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]


# Main Pipeline

def transcribe_and_translate(audio, src_lang, tgt_lang):
    if audio is None:
        return None, "No audio provided", None, "No text"

    # Step 1: Transcribe speech
    result = whisper_model.transcribe(audio, language=src_lang)
    original_text = result["text"]

    # Step 2: Translate
    translated_text = translate_text(original_text, src_lang, tgt_lang)

    # Step 3: Convert translated text to speech
    tts = gTTS(translated_text, lang=tgt_lang)
    tts.save("translated_audio.mp3")

    return audio, original_text, "translated_audio.mp3", translated_text


# Gradio UI

with gr.Blocks() as demo:
    gr.Markdown("# 🌍 EchoTranslate")
    gr.Markdown("🎤 Speak → 📝 Transcribe → 🌎 Translate → 🔊 Listen")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🎙️ Source Language")
            src_lang = gr.Dropdown(
                ["en", "ar", "fr", "de", "es", "zh", "ru","tr"],
                label="Choose source language",
                value="en"
            )
            audio_in = gr.Audio(sources=["microphone"], type="filepath", label="Record your voice")
            original_text_out = gr.Textbox(label="Transcription")

        with gr.Column():
            gr.Markdown("### 🌎 Target Language")
            tgt_lang = gr.Dropdown(
                ["ar", "en", "fr", "de", "es", "zh", "ru","tr"],
                label="Choose target language",
                value="ar"
            )
            translated_audio_out = gr.Audio(label="Translated Speech", type="filepath")
            translated_text_out = gr.Textbox(label="Translation")

    btn = gr.Button("🚀 Translate")

    btn.click(
        fn=transcribe_and_translate,
        inputs=[audio_in, src_lang, tgt_lang],
        outputs=[audio_in, original_text_out, translated_audio_out, translated_text_out]
    )

# Launch App

if __name__ == "__main__":
    demo.launch()
