import csv

def read_csv(path):
    with open(path, 'r') as f:
        lines = f.read()
    
    for i in lines.split('\n\n')[0].split('\n')[1:]:
        print(i)
    
    print('-'*75)

    for i in lines.split('\n\n')[1].split('\n')[1:]:
        print(i)