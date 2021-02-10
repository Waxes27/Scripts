import requests


drive = 'https://drive.google.com/file/d/1_nqx5eEJMbGXwem-Jl2_qcqr5VYkOYEu/view'

stuff = requests.get(drive).content

for i in stuff.splitlines():
    if b'href' in i:
        print(i)
        print()