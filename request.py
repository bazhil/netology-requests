import requests

def translate_it(source, result, source_lang, result_lang='ru'):
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

    with open(source, encoding='utf-8') as file:

        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

        lang = source_lang + '-' + result_lang

        params = {
            'key': key,
            'lang': lang,
            'text': file,
        }

        response = requests.get(url, params=params).json()
        text = (' '.join(response.get('text', []))).replace('\n', '')
        result_text = open(result, 'w')
        result_text.write(text)

translate_it('ES.txt', 'text_ES.txt', 'es', 'ru')
translate_it('FR.txt', 'text_FR.txt', 'fr', 'ru')
translate_it('DE.txt', 'text_DE.txt', 'de', 'ru')


