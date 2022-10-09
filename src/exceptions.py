class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass

class ListPythonVersionsNotFound(Exception):
    """Вызывается, когда не найден список с версиями Python."""