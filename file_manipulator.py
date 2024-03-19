def reverse(inputpath,outputpath):
    with open(inputpath,'r') as inputfile:
        content = inputfile.read()
    reversed_content = content[::-1]

    with open(outputpath,'w') as outputfile:
        outputfile.write(reversed_content)

def copy(inputpath,outputpath):
    with open(inputpath,'r') as inputfile:
        content = inputfile.read()
    with open(outputpath , 'w') as outputfile:
        outputfile.write(content)

def duplicate_contents(inputpath,n):
    with open(inputpath , 'r') as inputfile:
        content = inputfile.read()
    duplicated_content = content*n

    with open(inputpath,'w') as outputfile:
        outputfile.write(duplicated_content)

def replace_string(inputpath, needle, newstring):
    with open(inputpath , 'r') as inputfile:
        content = inputfile.read()
    updated_content = content.replace(needle, newstring)
    with open(inputpath,'w') as outputfile:
        outputfile.write(updated_content) 

replace_string('sample.txt', 'test' , 'hpge')
