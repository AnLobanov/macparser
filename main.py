import zipfile, os, json, shutil
OK = '\033[92m'  # Colors for terminal
FAIL = '\033[91m'
END = '\033[0m'
currentpath = os.getcwd() + '/'
if not os.path.exists(currentpath + 'temp'):
    os.mkdir(currentpath + 'temp')
try:
    with zipfile.ZipFile(input('File name (file should be located in current path): '), 'r') as zf:
        zf.extractall(currentpath + 'temp')
except FileNotFoundError:
    print('The file was not found. Check the file name and its extension and try again')
    os._exit(1)
requiredRam = int(input('How many GB of RAM every server needs: '))
print()
problems = []
for path in os.listdir(currentpath + 'temp'):
    with open(currentpath + 'temp/' + path + '/outputs/identify.json') as jsonfile:
        data = json.load(jsonfile)  # Data loading
        ram = int(data['memory']['total'].replace(' GB', ''))
        if ram < requiredRam:  # Compare RAM
            print(path.replace('%3A', ':') + ' ' + FAIL + str(ram) + ' GB' + END)
            problems.append(path.replace('%3A', ':'))
        else:
            print(path.replace('%3A', ':') + ' ' + OK + str(ram) + ' GB' + END)
shutil.rmtree(currentpath + 'temp')  # Delete temp directory
if problems == []:
    print('\n\nEverything is OK')
else:
    print('\n\n' + str(len(problems)) + " hosts don't have enough RAM:")
    for host in problems:
        print(host)