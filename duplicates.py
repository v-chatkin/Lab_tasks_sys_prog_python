#!/usr/bin/python3
import os
import sys
import hashlib


def get_filenames(dir_name):
    filenames = []
    for dir, dir_list, files in os.walk(dir_name):
        for file in files:
            path = os.path.join(dir, file)
            filenames.append(path)
    return filenames


def get_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def dup_search(filenames):
    originals = []
    dup_list = []
    for file in filenames:
        hash = get_md5(file)
        if originals.__contains__(hash):
            dup_list.append(file)
        else:
            originals.append(hash)
    return dup_list


def main():
    # Код разбора командной строки
    # Получим список аргументов командной строки, отбросив [0] элемент, 
    # который содержит имя скрипта
    args = sys.argv[1:]
    if not args:
        print('usage: directory path')
        sys.exit(1)

    dir_name = args[0]
    filenames= get_filenames(dir_name)
    print("Cписок дубликатов:\n", dup_search(filenames))

  
if __name__ == '__main__':
    main()
