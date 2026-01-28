from googletrans import Translator, LANGUAGES

translator = Translator()

source_lang = input("Enter source language code (e.g. en, hi, fr): ").lower()

text = input("Enter text to translate: ")

print("\nSupported languages:")
for code, lang in LANGUAGES.items():
    print(code, "->", lang)

target_lang = input("Enter target language code (e.g. en, hi, fr): ").lower()

if source_lang not in LANGUAGES:
    print("Invalid source language code!")
    exit()

if target_lang not in LANGUAGES:
    print("Invalid target language code!")
    exit()

try:
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    print("\nTranslated Text:")
    print(translated.text)
except Exception as e:
    print("Translation failed:", e)
