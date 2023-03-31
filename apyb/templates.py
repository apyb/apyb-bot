from .config import BASE_DIR


def render_template(template_name: str, **kwargs) -> str:
    template_path = BASE_DIR / f"templates/{template_name}"

    if not template_path.exists():
        raise ValueError(f"Template {template_name} not found")

    with template_path.open() as fp:
        template = fp.read()

    return template.format(**kwargs)
