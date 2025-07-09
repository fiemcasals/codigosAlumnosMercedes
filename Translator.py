# traductor español-ingles basado en GoogleTranslator
from deep_translator import GoogleTranslator

print("Traductor español → inglés (usa GoogleTranslator)")
while True:
    texto = input("Escribe una oración en español (o 'salir' para terminar): ")
    if texto.lower() == 'salir':
        break
    traduccion = GoogleTranslator(source='auto', target='en').translate(texto)
    print("Traducción:", traduccion)