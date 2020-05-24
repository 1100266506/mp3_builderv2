from cx_Freeze import setup, Executable
import os.path

#run in terminal "python3 setup.py build"

includefiles = ["/home/benjamin/Python/mp3_builder/src/Song.py",
                "/home/benjamin/Python/mp3_builder/src/mp3_player.py",
                "/home/benjamin/Python/mp3_builder/setup.py",
                "/home/benjamin/Python/mp3_builder/testing/mp3_player_testing.py",
                "/home/benjamin/Python/mp3_builder/testing/Song_test.py",
                "/home/benjamin/Python/mp3_builder/README.md"]

exe = Executable(
    script = "mp3_main.py",
    initScript = None,
    base = None,
    targetName = "mp3_builder",
    icon = "mp3_icon.ico"
)

setup(
    name = "mp3_builder",
    version = '2.0',
    description = "Benjamin Ahn's unique mp3 player for computer",
    options = {"build_exe": {"packages":["pygame"], "include_files":includefiles}},
    executables = [exe]
)
