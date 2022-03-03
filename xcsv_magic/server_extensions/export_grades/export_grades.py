from notebook.utils import url_path_join as ujoin

from jinja2 import Environment, FileSystemLoader
from tornado import web
from traitlets import default
import os

from nbconvert.exporters import HTMLExporter as Eek
from nbgrader.apps import NbGrader

from . import handlers


class ExportGradesExtension(NbGrader):
    def init_tornado_settings(self, webapp):
        jinja_env = Environment(
            loader=FileSystemLoader([handlers.template_path]),
            autoescape=True,
        )

        tornado_settings = dict(export_jinja2_env=jinja_env)

        webapp.settings.update(tornado_settings)

    def init_handlers(self, webapp):
        h = []
        h.extend(handlers.default_handlers)
        h.extend(
            [
                (
                    r"/csv_magic/static/(.*)",
                    web.StaticFileHandler,
                    {"path": handlers.static_path},
                ),
            ]
        )

        def rewrite(x):
            pat = ujoin(webapp.settings["base_url"], x[0].lstrip("/"))
            # self.log.info((pat,) + x[1:])
            return (pat,) + x[1:]

        webapp.add_handlers(".*$", [rewrite(x) for x in h])


def load_jupyter_server_extension(nbapp):
    """Load the fancypants extension"""
    nbapp.log.info("Loading the xcsv_magic serverextension")
    webapp = nbapp.web_app
    exportapp = ExportGradesExtension(parent=nbapp)
    exportapp.log = nbapp.log
    exportapp.initialize([])
    exportapp.init_tornado_settings(webapp)
    exportapp.init_handlers(webapp)
