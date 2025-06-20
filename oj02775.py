def parse_input():
    data_sets=[]
    current_set=[]
    while True:
        line=input().strip()
        if line=='#':
            break
        if line=='*':
            data_sets.append(current_set)
            current_set=[]
        else:
            current_set.append(line)
    return data_sets
def build_directory_structure(data):
    root={'name':'ROOT','dirs':[],'files':[]}
    stack=[root]
    i=0
    while i<len(data):
        line=data[i]
        if line[i]==']':
            stack.pop()
        elif line[0]=='d':
            new_dir={'name':line,'dirs':[],'files':[]}
            stack[-1]['dirs'].append(new_dir)
            stack.append(new_dir)
        elif line[0]=='f':
            stack[-1]['files'].append(line)
        i+=1
    return root
def print_directory_structure(root,depth=0):
    indent='|     '*depth
    print(indent+root['name'])
    for dir in root['dirs']:
        print_directory_structure(dir,depth + 1)
    root['files'].sort()
    for file in root['files']:
        print(indent+'|     '+file)
def solve():
    data_sets=parse_input()

    for idx,data_set in enumerate(data_sets):
        if idx > 0:
            print()
        print(f"DATA SET {idx + 1}:")
        root = build_directory_structure(data_set)
        print_directory_structure(root)

solve()