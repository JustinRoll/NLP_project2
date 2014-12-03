vsm = {}
vsm_file = r"data/vsm.txt"

def loadVSM():
    f = open(vsm_file, encoding="utf8")
    for line in f.readlines():
        parts = line.split()
        word = parts[0]
        parts = parts[1:]
        parts = [float(part) for part in parts]
        vsm[word] = parts

def getVector(word):
    if vsm == {}:
        loadVSM()
    if word in vsm.keys():
        return vsm[word]
    return []

