import os
from tornado import web
from nbgrader.server_extensions.formgrader.base import (
    BaseHandler,
    BaseApiHandler,
    check_xsrf,
)
from ...exporters import CsvExport


class ExportHandler(BaseHandler):
    def render(self, name, **ns):
        template = self.settings["export_jinja2_env"].get_template(name)
        return template.render(**ns)


class ExportCombineHandler(BaseApiHandler):
    def initialize(self):
        self.__exporter = CsvExport()

    """
    @web.authenticated
    @check_xsrf
    def get(self):
        self.set_header("Content-Type", 'text/csv; charset="utf-8"')
        self.set_header("Content-Disposition", "attachment; filename=grades.csv")
        self.write(
            self.__exporter.export(self.gradebook).to_csv(
                index=False, float_format="%.0f", sep=";", encoding="utf-8-sig"
            )
        )
        self.finish()
    """

    @web.authenticated
    @check_xsrf
    def post(self):
        self.set_header("Content-Type", 'text/csv; charset="utf-8"')
        self.set_header("Content-Disposition", "attachment; filename=grades.csv")
        self.write(
            self.__exporter.export(self.gradebook, self.get_json_body()).to_csv(
                index=False, float_format="%.0f", sep=";", encoding="utf-8-sig"
            )
        )
        self.finish()


class ExportGradesHandler(ExportHandler):
    @web.authenticated
    @check_xsrf
    def get(self):
        html = self.render("export_grades_combine.tpl", base_url=self.base_url)
        self.write(html)


root_path = os.path.dirname(__file__)
template_path = os.path.join(root_path, "templates")
static_path = os.path.join(root_path, "static")

default_handlers = [
    (r"/export_grades/combine/?", ExportCombineHandler),
    (r"/export_grades/?", ExportGradesHandler),
]
