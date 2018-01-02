"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """


def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """


def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
