import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii") # needed in python 3
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
j=0
for i in ssids:
    ssids[j]=i[9:]
    j+=1
for x in ssids:
    if x=='':
        ssids.remove(x)
    else:
        x.strip()
for i in ssids:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print(f"{i} : {results[0]}")
    except IndexError:
        print(f"{i} : {''}")