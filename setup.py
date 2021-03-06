from setuptools import setup, find_packages
import os

extension_files = []
for (dirname, dirnames, filenames) in os.walk("xcsv_magic/nbextensions"):
    root = os.path.relpath(dirname, "xcsv_magic")
    for filename in filenames:
        extension_files.append(os.path.join(root, filename))

static_files = []
for (dirname, dirnames, filenames) in os.walk(
    "xcsv_magic/server_extensions/formgrader/static"
):
    root = os.path.relpath(dirname, "xcsv_magic/server_extensions/formgrader")
    for filename in filenames:
        static_files.append(os.path.join(root, filename))
for (dirname, dirnames, filenames) in os.walk(
    "xcsv_magic/server_extensions/formgrader/templates"
):
    root = os.path.relpath(dirname, "xcsv_magic/server_extensions/formgrader")
    for filename in filenames:
        static_files.append(os.path.join(root, filename))

setup_args = dict(
    name="xcsv_magic",
    version="0.0.1",
    description="xcsv_magic",
    author="Lauri Koikkalainen",
    author_email="lauri.koikkalainen@ntnu.no",
    packages=find_packages(),
    package_data={
        "xcsv_magic": extension_files,
        "xcsv_magic.server_extensions.formgrader": static_files,
    },
    install_requires=["nbgrader", "e2xgrader"],
)

if __name__ == "__main__":
    setup(**setup_args)
