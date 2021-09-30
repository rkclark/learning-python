from cx_Freeze import setup, Executable

setup(
    name="myExportedExe",
    version="0.1",
    description="Print some stuff from a regex",
    executables=[Executable("regexes.py")],
)
