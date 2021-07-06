farmer_pk="8190af1b5c7421d8a8eac95ba01d516cc95855a67cf9fe7833b8eb2963882f65a24c132814da06ab8076481602091f1c"
pool_pk="b74da85d96ca721c341c019130bb89099b1078a8e76efd8984a3ca0965f71a6377110ef9dc2ff3727cd0514965c2fec4"

t=["D","E"]
d=["F","G"]
cpu=16
lt = len(t)
for i in range(lt):
    name = t[i] + ".bat"
    t2 = t[(i+1)%lt]
    with open(name, 'w') as f:
        command = ".\chia_plot.exe -t "+ t[i] + ":\ -2 " + t2+ ":\ -d " + d[i] + ":\ -r " + str(int(cpu/lt-1)) + " -p " + pool_pk + " -f " + farmer_pk + " -n -1"
        f.write(command)
    