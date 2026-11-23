import subprocess

name = input("Введите имя:")

subprocess.run(["/bin/echo", "Привет!", name], check=True)
