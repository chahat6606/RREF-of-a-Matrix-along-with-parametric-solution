f=open("textfile_math.txt","r")
lines = f.readlines()
n = int(lines[0])
m = int(lines[1])
A = []
for i in range(2,len(lines)):
    A.append(lines[i].strip('\n').split())
A2 = []
for line in A:
    line = [eval(x) for x in line]
    A2.append(line)
A = A2
def echelon(A, n, m):
    for k in range(0, m-1):
        for i in range(k+1, n):
            if A[k][k] == 0:
                continue
            if A[i][k] != 0.0:
                #print(k)
                lam = A[i][k]/A[k][k]
                #print(k,lam)
                for j in range(0, m):
                    #print("row:",i)
                    A[i][j] = A[i][j] - lam*A[k][j]
        
    return A
print("ECHELON:")
print(echelon(A,n,m))
print()
def rref(M):
    if len(M) == 0:
         return

    rc,cc = len(M), len(M[0])

    l = 0

    for r in range(0, rc):

        if l >= cc:
            return M
        i = r
        while M[i][l] == 0:
            i += 1
            if i == rc:
                i = r
                l += 1
                if cc == l:
                    return M
        ### swap M[r], M[i]
        temp = M[i]
        M[i] = M[r]
        M[r] = temp

        lv = temp[l]

        temp2 = []
        for a in M[r]:
            temp2.append(a/float(lv))

        M[r] = temp2

        for i in range(0, rc):
            if i != r:
                lv = M[i][l]
                new_Mi = []
                for rv,iv in zip(M[r],M[i]):
                    new_Mi.append((iv - lv*rv))
                
                M[i] = new_Mi
        
        l = l + 1
    return M
M=rref(A)
print("RREF:")
print(M)
print()
for i in range(len(M)*(-1),0):
    if M[i].count(0)==len(M[0]):
        M.pop(i)
# print(M)
n=len(M)
m=len(M[0])
pl=[]
for i in range(n):
    for j in range(m):
        if M[i][j]!=0:
            pl.append(j)
            break       
# print (pl)
colms=[j for j in range(m)]  
np=[i for i in colms if i not in pl]
# print(np)
freevars=[]
for i in np:
    freevars.append("x_"+str(i))
# print(freevars)
star=[]
for j in range(m):
    star.append(0)
# print(star)
fin=""
for i in range(len(np)):
    a=''
    b=np[i]
    l=[]
    for j in range(n):
        l.append(-M[j][b])
    # print(l)
    for q in np:
        if q!=b:
            l.insert(q,0)
    l.insert(b,1)
    # print(l)
    f=str(l)
    d=np[i]
    # print(f)
    a="x-"+str(d)+"*"+f
    fin=fin+"+"+a
# print(fin)
print("SOlUTION:")
if "x" not in fin:
    print("NO FREE VARIABLES(ONLY TRIVIAL SOLUTION) ")
    print(star)
else:
    print(star,"+",fin)
