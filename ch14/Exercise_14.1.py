import os

for root, dirs, files in os.walk(os.getcwd()):
    print root + ' contains:'
    for name in files:
        print os.path.join(root, name)
    if '.git' in dirs:
        dirs.remove('.git')