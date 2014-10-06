import random
b_out=open('D_t2.txt','w',encoding = 'utf-8')
b_out.write(str(1000)+'\n')
for i in range(1000):
    a=[random.random() for _ in range(0, 50)]
    b=[random.random() for _ in range(0, 50)]
    b_out.write('50'+'\n')
    b_out.write(' '.join(map(str,a))+'\n')
    b_out.write(' '.join(map(str,b))+'\n')
