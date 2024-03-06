"""Language helper"""


def get_user_lang(req) -> str:

    # Prioritize lang parameter

    params = req.args.to_dict()

    if "lang" in params:
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
