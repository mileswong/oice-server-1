import babel

from ...config import get_default_lang


def normalize_language(language):
    if language:
        language = language.replace('_', '-')
    else:
        language = ''

    try:
        parts = babel.Locale.parse(language, sep='-')
    except (babel.UnknownLocaleError, ValueError):
        parts = babel.Locale(get_default_lang())

    language = parts.language
    script   = parts.script
    region   = parts.territory

    # Special handle for Chinese
    if language == 'zh':
        if region not in ['HK', 'TW', 'CN']:
            if script == 'Hans':
                region = 'CN'
            else:
                region = 'TW'
        language += '-' + region

    return language


def normalize_ui_language(language):
    if language == 'ja' or language[:2] == 'zh':
        return language
    return get_default_lang()


def get_language_code_for_translate(language):
    language_code = language.lower()

    # zh will be regarded as Simplified Chinese
    if language_code[:2] == 'zh' and ('hk' in language_code or 'tw' in language_code):
        language_code = 'zh-TW'
    else:
        language_code = language_code[:2]
        
    return language_code