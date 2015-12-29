import os

from . import conf


_templates = {}


def get(name):
    if name in _templates:
        return _templates[name]

    tmplpath = os.path.join(conf.TEMPLATES_DIR, "{}.tmpl".format(name))
    if not os.path.exists(tmplpath):
        raise Exception("{} template does not exist".format(tmplpath))

    try:
        with open(tmplpath, "rb") as tmpl:
            _templates[name] = tmpl.read()
    except:
        raise Exception("Error reading {}".format(tmpl))

    return _templates[name]
