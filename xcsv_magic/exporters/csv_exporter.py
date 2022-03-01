from nbgrader.plugins import ExportPlugin
from nbgrader.api import Gradebook, MissingEntry
import pandas as pd


class CsvExport(ExportPlugin):
    def get_columns(self, assignments):
        return [f"{a.name} | max_score: {int(a.max_score)}" for a in assignments]

    def get_assignments(self, gb: Gradebook):
        return sorted(
            filter(lambda x: not ("-tg" in x.name), gb.assignments),
            key=lambda x: x.name,
        )

    def export(self, gb: Gradebook, ns) -> None:
        assignments = self.get_assignments(gb)
        data = []
        columns = ["Brukernavn"] + self.get_columns(assignments)

        for student in gb.students:
            row = [student.id]
            for assignment in assignments:
                score = None
                try:
                    submission = gb.find_submission(assignment.name, student.id)
                    score = submission.score
                except MissingEntry:
                    pass
                row.append(score)
            data.append(row)

        df = pd.DataFrame(data=data, columns=columns)
        names = pd.json_normalize(ns["data"])
        df = names.merge(df, on="Brukernavn", how="outer")
        df.sort_values(by=["Etternavn", "Fornavn"], inplace=True)
        return df
