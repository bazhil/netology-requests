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
    text=''''Starke 45 Minuten waren genug: Der FC Bayern hat zum Auftakt des 13. Bundesliga-Spieltags gegen Mainz 05 gewonnen, einen frühen Rückstand drehten die Münchner noch vor der Pause. Durch das 3:1 (2:1) hat das Team von Trainer Carlos Ancelotti 30 Punkte - so viele wie RB Leipzig, der Tabellenführer spielt am Samstagabend gegen Schalke (18.30 Uhr, High-Liveticker SPIEGEL ONLINE).

"In der ersten Halbzeit haben wir so gespielt wie lange nicht mehr", sagte Arjen Robben, einer der Torschützen, nach der Partie: "Die vergangenen Wochen haben uns ein bisschen die Überraschungen gefehlt. Das war heute gut. Eigentlich hätten wir schon in der ersten Hälfte mehr Tore erzielen müssen."

Ancelotti hatte sich einige Gedanken zur Aufstellung gemacht, Philipp Lahm aus der Abwehr ins defensive Mittelfeld beordert, auf den Flügeln konnten zum ersten Mal seit neun Monaten Franck Ribéry und Arjen Robben mal wieder von Beginn an spielen. Der zuletzt heftig kritisierte Jérôme Boateng ("down to earth") saß auf der Bank, neben Mats Hummels stand Javier Martínez in der Innenverteidigung.
'''

    params = {
        'key': key,
        'lang': 'de-ru',
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

a = translate_it('Привет')
print(a)