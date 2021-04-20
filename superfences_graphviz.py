from graphviz import Source, ENGINES


def format(
    source, language, css_class, options, md, classes=None, id_value="", **kwargs
):
    return (
        Source(source, engine=options.get("engine", "dot"))
        .pipe(format="svg")
        .decode("utf-8")
    )


def validate(language: str, options: dict) -> bool:
    allowed_options = {"engine": lambda v: v in ENGINES}
    for opt in options.keys():
        if opt not in allowed_options:
            return False
    return True