import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["PySide6", "pycep_correios"],
    "include_files": ["py.ico", "lupa.ico"],
    "excludes": ["tkinter"]
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Cadastro de Clientes PySide-Json",
    version="3.3",
    url="https://github.com/SkyArtur/cadastro-de-cliente-PySide6-Json",
    author="SkyArtur",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("cadastro_de_clientes.py", icon="launch.ico", base=base)],
)
