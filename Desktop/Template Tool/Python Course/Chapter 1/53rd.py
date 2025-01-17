try:
    f=open("file.txt")
    #print(name)
    
except Exception as v:
    print(v)    
else:
    print(f.read())
    f.close()
    