def dedupe_adjacent(alist):
    cur =[alist[-1]]
    cnt = [1]
    for i in range(len(alist) -2, -1, -1):
        if alist[i] != cur[-1]:
            #print(i,alist[i],cur[-1])
            cur.append(alist[i])
            cnt.append(1)
            #print(cur,cnt)
        else:
            cnt[-1]+=1
    #print(cur,cnt)
    return list(zip(cur,cnt))

a=list('mmaw')
t=dedupe_adjacent(a)

def solve(cases):
    ret = 0
    uniCase = [list(x) for x in dedupe_adjacent(cases[0])]
    #print(uniCase)
    for case in cases[1:]:
        j = 0
        for i in range(len(uniCase)-1,-1,-1):
            tmp = uniCase[i][0]
            cnt = 0
            while j <len(case) and case[j]==tmp:
                cnt+=1
                j+=1
            if cnt==0:
                return "Fegla Won"
            uniCase[i].append(cnt)
        #print(j,len(case))
        if j <len(case):
            
            return "Fegla Won"
    #print('new',uniCase)
    for i in uniCase:
        tmp =i[1:]
        #print(tmp)
        if tmp[1:]!=tmp[:-1]:
            rm= 10000000
            for j in range(min(tmp),max(tmp)+1):
                #print('j',j)
                tmprm = 0
                for k in tmp:
                    #print(k,abs(k-j))
                    tmprm+=abs(k-j)
                rm = min(rm,tmprm)
                #print('tmprm',tmprm,'rm',rm)
            ret+=rm
            #print('ret',ret)
    return str(ret)
            
    
def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = [x.replace('\n','') for x in a_in.readlines()]
    N = int(results[0])
    a_out = open('A_output_large.txt','w',encoding = 'utf-8')
    tmp = 0
    for i in range(1,N+1):
        n = int(results[i+tmp])
        cases = [list(x) for x in results[i+tmp+1:i+tmp+1+n]]
        tmp += n
        print('Case',i)
        rels = "Case #"+str(i)+": "+solve(cases)
        a_out.write(rels+'\n')

run('A-large-practice.in')
#cases = [list('byfypfejaojjcluxzhvrvqdiqdwlqjzdihbzoikpwtyahuxibuzwkcgdhfozoqcyzgznojemfdmmzlubfvzszivgpl'),list('yfypfejaojjcluxzhvrvqdiqdwlqjzdihbzoikpwtyahuxibuzwkcgdhfozoqcyzgznojemfdmmzlubfvzszivgpl')]
#cases=[list('rggrrjjjjcccccccaawlrzzxxxxuuuqpppppppppppppuuuuuufkncaaaaqkkhhhhhcbbyvvvvvppppppppmmnvvvvddddddwaaa'),list('rggrjjjjcccawlrrzzxuqqqpuuufknnncaqkhhhcccbyyvvvvpmnnvdwa')]
cases=[list('impjusftihrmnniehwkoyfzogbcypdkxqzjmrqfzxzmmmwqtsckrjlf'),list('impjusftihrmnniehwkoyfzogbcypdkxqzjmrqfzxzmmmwqtsckrjlfs')]
t=solve(cases)
