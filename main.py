import os, json
OK = '\033[92m'  # Colors for terminal
FAIL = '\033[91m'
END = '\033[0m'
currentpath = os.getcwd()
requiredRam = int(input('How many RAM modules every server needs: '))
print()
problems = []
for pathname in os.listdir(currentpath):
    if os.path.isdir(currentpath + '/' + pathname) and ("%3A" in pathname or ":" in pathname):
        with open(currentpath + '/' + pathname + '/outputs/identify.json') as jsonfile:
            data = json.load(jsonfile)  # Data loading
            ram = int(data['memory']['count'])
            node = data['meta']['node']
            if ram < requiredRam:  # Compare RAM
                print(node + ' ' + pathname.replace('%3A', ':') + ' ' + FAIL + str(ram) + ' pcs' + END)
                problems.append([node, pathname.replace('%3A', ':')])
            else:
                print(node + ' ' + pathname.replace('%3A', ':') + ' ' + OK + str(ram) + ' pcs' + END)
if problems == []:
    print('\n\nEverything is OK')
else:
    print('\n\n' + str(len(problems)) + " hosts don't have enough RAM modules:")
    for host in problems:
        print(host[0], host[1])