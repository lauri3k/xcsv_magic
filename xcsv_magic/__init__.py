import os


def _jupyter_nbextension_paths():
    paths = [
        dict(
            section="tree",
            src=os.path.join("nbextensions", "export"),
            dest="export",
            require="export/export",
        ),
        """
        dict(
            section="tree",
            src=os.path.join("nbextensions", "test"),
            dest="test",
            require="test/test",
        ),
        """,
    ]

    return paths


def _jupyter_server_extension_paths():
    paths = [
        dict(module="xcsv_magic.server_extensions.formgrader"),
    ]
    return paths
