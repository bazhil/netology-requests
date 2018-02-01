import requests

def translate_it(text):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    text=open('DE.txt', 'r')
    text_de = open('text_de.txt', 'w')

    params = {
        'key': key,
        'lang': 'de-ru',
        'text': text,
        'text_de': text_de
    }

    response = requests.get(url, params=params).json()
    print(' '.join(response.get('text', [])))


    text_de.write(' '.join(response.get('text', [])))
    text_de.close()
    text.close()

    text = open('ES.txt', 'r')
    text_es = open('text_es.txt', 'w')
    params = {
        'key': key,
        'lang': 'es-ru',
        'text': text,
        'text_es': text_es
    }
    response = requests.get(url, params=params).json()
    print(' '.join(response.get('text', [])))

    text_es.write(' '.join(response.get('text', [])))
    text_es.close()
    text.close()

    text = open('FR.txt', 'r')
    text_fr = open('text_fr.txt', 'w')
    params = {
        'key': key,
        'lang': 'fr-ru',
        'text': text,
        'text_fr': text_fr,
    }
    response = requests.get(url, params=params).json()
    print(' '.join(response.get('text', [])))

    text_fr.write(' '.join(response.get('text', [])))
    text_fr.close()
    text.close()

a = translate_it('Привет')
print(a)