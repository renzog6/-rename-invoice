import os

# Leer listado de archivos en el directorio


def getList(path):
    lst = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            lst.append(file)
            print(os.path.join(">", file))
    return lst
