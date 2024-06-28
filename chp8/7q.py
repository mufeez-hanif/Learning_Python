li = ['Hammad','Ahmed','Atif','Ateeb','Attique','At']

def stripAndRemove(names,word):
    names.remove(word)
    n= []
    for i in names:
        if(i!=word):
            n.append(i.strip(word))
    
    return n

print(stripAndRemove(li,'At'))