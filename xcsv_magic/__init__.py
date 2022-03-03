import os


def _jupyter_nbextension_paths():
    paths = [
        dict(
            section="tree",
            src=os.path.join("nbextensions", "export"),
            dest="export",
            require="export/main",
        ),
    ]
    return paths


def _jupyter_server_extension_paths():
    paths = [
        dict(module="xcsv_magic.server_extensions.export_grades"),
    ]
    return paths
