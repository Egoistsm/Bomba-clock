from cx_Freeze import setup, Executable

setup(
    name="Bomba clock",
    version="0.1",
    description="This's bomb file virus.",
    executables=[Executable("Bomba.py")],
)
