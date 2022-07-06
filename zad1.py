#!/usr/bin/python3

def find_pdf_size(top):
    import os
    size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.endswith('.pdf'):
                fullpath = os.path.join(root, name)
                size += os.path.getsize(fullpath)
    return name, size

print('Rozmiar pliku pdf: {} bajtów'.format(find_pdf_size('.')))
