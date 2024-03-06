"""Language helper"""

from urllib.parse import parse_qs


def get_user_lang(req) -> str:

    # Prioritize lang parameter
    stripped_url = req.url.split("?")
    if len(stripped_url) == 2:
        args = parse_qs([1])
        params = {k: v[0] if len(v) == 1 else v for k, v in args.items()}
        arg_keys = params.keys()

        if "lang" in arg_keys:
            lang_param = params["lang"]
            if lang_param in ["fr", "en"]:
                return lang_param

    # If no valid lang parameter, take user preferred lang
    accept_language = req.headers.get("Accept-Language")
    languages = [lang.strip().split(";")[0] for lang in accept_language.split(",")]

    if languages:
        user_preferred_language = languages[0][:2]
        if user_preferred_language in ["fr", "en"]:
            return user_preferred_language

    # If no valid user preferred lang, return default (fr)
    return "en"
