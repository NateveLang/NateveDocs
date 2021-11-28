import subprocess

file = "README"

subprocess.call([".\m2r", file + ".md"])

f = open(file + ".rst")
text = f.read()
f.close()

index = open("index.rst", "w")
index.write(text)
index.close()

