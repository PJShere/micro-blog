from xml.etree import ElementTree
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    translate_key = current_app.config['MS_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr/translate'
                     '?key={}&text={}&lang={}-{}'.format(
                         translate_key, text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    # return json.loads(r.content.decode('utf-8-sig'))
    tree = ElementTree.fromstring(r.text)
    return tree[0].text
