import subprocess

from replace_eggdriver import replace_eggdriver_standard_library_here

f = open("README.md", "r")
text = f.read()
f.close()

content = text.replace("replace_eggdriver_standard_library_here", replace_eggdriver_standard_library_here)

md = open("index.md", "w")
md.write(content)
md.close()

subprocess.call([".\m2r", "index.md"])
