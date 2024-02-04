from googletrans import Translator

def traduire_texte(texte, langue_cible):
    translator = Translator(service_urls=['translate.google.com'])
    traduction = translator.translate(texte, dest=langue_cible)
    return traduction.text

texte_a_traduire = "مرحبا"
langue_cible = "en"

traduction = traduire_texte(texte_a_traduire, langue_cible)
print(f"Texte d'origine : {texte_a_traduire}")
print(f"Traduction en français : {traduction}")