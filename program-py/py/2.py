import jieba
dk = {}
with open('D:\programme\program-py\py\data.txt','r') as f:
    s=f.readlines()
for i in s:
    k=jieba.lcut(s,cut_all = True)
    for j in k:
        if len(j)==2:
            dk[j]=dk.get(j,0)+1
dp = list(dk.items())
dp.sort(key= lambda x:int(x[1]), reverse = True)
for i in range(10):
    print('{}:{}'.format(dp[i][0],dp[i][1]))
