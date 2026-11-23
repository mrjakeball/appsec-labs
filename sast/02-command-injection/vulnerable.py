import subprocess

name = input("Введите имя:")

command = f"echo Привет!, {name}"

subprocess.run(command, shell=True, check=True)
