

def readPackageList(fname):
    dic_uidToPackage = {}
    with open(fname, "r") as ins:
    	array = []
    	for line in ins:
            line = line.strip()
            ans = line.split(" ")
            package = ans[0]
            uid = ans[1]
            dire = ans[3] 
            if not uid in dic_uidToPackage:
               dic_uidToPackage[uid] = []
               dic_uidToPackage[uid].append(package)
            else:
               dic_uidToPackage[uid].append(package)
            #print (package, uid, dire)
    
    print (dic_uidToPackage)
    return (dic_uidToPackage)

def IsUiqueMapping(dic):
    for key in dic:
        if dic[key] and len(dic[key]) > 1:
           print (dic[key])
           return False
    return True
    

#if __name__ == "__main__":
fname = "/Users/ketian/Desktop/packages.list"
d = readPackageList(fname)
print (IsUiqueMapping(d))
