replace_eggdriver_standard_library_here = ""

f = open("features.txt")
lines = f.readlines()
f.close()

features = []
last_feature_name = ""
last_feature_description = ""
first_feature = True

for i in range(len(lines)):
    line = lines[i]
    EOF = (i == len(lines) - 1)
    
    if first_feature:
        first_feature = False
        last_feature_name = line.strip("#").strip()

    elif len(line) > 0:

        if line[0] == "#" or EOF:
            features.append((last_feature_name, last_feature_description.strip()))

        if line[0] == "#":
            last_feature_name = line.strip("#").strip()
            last_feature_description = ""
        
        elif line[0] != "~":
            last_feature_description += line.strip()

    else:
            last_feature_description += line.strip()

features.sort(key = lambda x: x[0]) # sort features by name

for i in range(len(features)):
    replace_eggdriver_standard_library_here += f"## {i + 1}. " + features[i][0] + "\n\n"
    replace_eggdriver_standard_library_here += features[i][1]
    
    if i != len(features) - 1:
        replace_eggdriver_standard_library_here += "\n\n"

print("We will add the following lines in 'index.md':\n")
print(replace_eggdriver_standard_library_here)
