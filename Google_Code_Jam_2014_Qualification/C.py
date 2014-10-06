import copy
def solve(case):
    R,C,M =case
    #print(R,C,M)
    
    return "Impossible"
  

def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = a_in.readlines()
    N = int(results[0].replace('\n',''))
    a_out = open('C_output.txt','w',encoding = 'utf-8')
    for i in range(1,N+1):
        case = list(map(int,results[i].replace('\n','').split()))
        #print(case)
        rels = "Case #"+str(i)+": "+str(solve(case))
        a_out.write(rels+'\n')

run('C_t.txt')


