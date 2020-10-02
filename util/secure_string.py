import emoji

class SecureString:
    # nimmt den übergebenen String und ersetzt alle potenziell gefährlichen Zeichen
    # poder alle Zeichen, die nicht mit der Datenbank funktionieren

    """
    Zeichen die Ersetzt werden:
    - "
    - # -> {hashtag}, da mysql keine solche sonderzeichen übergeben kann
    - alle emojis -> :emoji_name:
    """
    def secureString(string):
        return emoji.demojize(string.replace('"', "\"").replace("{hashtag}", "#").replace("'", "\'"))
