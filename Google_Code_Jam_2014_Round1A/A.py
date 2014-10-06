def solve(s,ar1,ar2,start):
    ret=[]
    if set(ar1)==set(ar2):
        return 0
    
    return "NOT POSSIBLE"
    
def change(idx, ar):
    tmp = list(ar)
    for i in range(idx):
        if ar[i]=='1':
            tmp[i]='0'
        elif ar[i]=='0':
            tmp[i]='1'
    return ''.join(tmp)
def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = a_in.readlines()
    N = int(results[0].replace('\n',''))
    a_out = open('A_output.txt','w',encoding = 'utf-8')
    gap=0
    for i in range(1,N+1):
        gap=2*(i-1)
        t= int(results[i+gap].replace('\n','').split()[0])
        s = int(results[i+gap].replace('\n','').split()[1])
        ar1=results[i+gap+1].replace('\n','').split()
        ar2 =results[i+gap+2].replace('\n','').split()
        rels = "Case #"+str(i)+": "+str(solve(s,ar1,ar2))
        #print(t,s,ar1,ar2)
        a_out.write(rels+'\n')
run("A-small-attempt0.in")
