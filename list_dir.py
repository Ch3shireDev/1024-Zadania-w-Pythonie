import os

path = ".\\OI\\"
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            full_path = os.path.join(r, file).replace('\\', '/')
            print('\\begin{zadanie}')
            print('\\includepdf{%s}' % full_path)
            print('\\end{zadanie}')
