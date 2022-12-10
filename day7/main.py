from collections import defaultdict
lines = open('main.in', 'r').read().splitlines()
ans=0

cur_directory = ''
cur_folder = '/'
directory_sizes = defaultdict(int)
children = defaultdict(list)
vis = list()
bruh = list()

def recursively_add(cur):
    print('cur', cur)
    global directory_sizes
    if cur in vis:
        return 0
    vis.append(cur)
    if len(children[cur]) == 0:
        return directory_sizes[cur]
    ret = directory_sizes[cur]
    for child in children[cur]:
        ret += recursively_add(child)
    directory_sizes[cur] = ret
    return ret


def go_up():
    global cur_directory, cur_folder
    cur_directory = cur_directory[:cur_directory.rindex('/')]
    if (cur_directory == ''):
        cur_directory = '/'
        cur_folder = '/'
    else:
        cur_folder = cur_directory[cur_directory.rindex('/') + 1:]
    #print(cur_directory, cur_folder)

def go_in(x):
    global cur_directory, cur_folder
    cur_folder = x
    if x == '/':
        cur_directory = '/'
        cur_folder = '/'
    elif cur_directory == '':
        cur_directory = x
    elif cur_directory == '/':
        cur_directory += x
    else:
        cur_directory += f'/{x}'
    #print(cur_directory, cur_folder)

i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('$ cd'):
        if line[5:] == '..':
            go_up()
        else:
            go_in(line[5:])
        i += 1
    elif line.startswith('$ ls'):
        j = i + 1
        while j < len(lines) and not lines[j].startswith('$'):
            j += 1
        for k in range(i + 1, j):
            #print(k, lines[k])

            if lines[k].startswith('dir'):
                children[cur_directory].append(cur_directory + '/' + lines[k][4:] if cur_directory != '/' else cur_directory + lines[k][4:])
            else:
                #print(int(lines[k].split(' ')[0]), cur_folder)
                directory_sizes[cur_directory] += int(lines[k].split(' ')[0])
                #bruh.append(lines[k].split(' ')[1])
        i = j

st = list()
for directory in directory_sizes:
    #print(directory)
    st.append(directory)
for directory in st: 
    #print('help', directory)
    recursively_add(directory)
s=[]
for directory in directory_sizes:
    s.append(directory_sizes[directory])
s.sort()
i = 0
cur_free_space = 70000000 - directory_sizes['/']
needed_free_space = 30000000 - cur_free_space
while i < len(s) and s[i] < needed_free_space:
    i += 1
print(s[i])
