import glob, os

os.chdir('Moje dokumenty')

for file in glob.glob("*.txt"):
    with open(file, "r") as f:
        content = f.readlines()
        for line in content:
            if file[:10] in line:
                print line[0:-1]