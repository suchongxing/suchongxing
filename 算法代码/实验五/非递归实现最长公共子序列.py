 # 最长公共子序列 python3
word_a = "fish"
word_b = "fosh" #最长公共子串为2，子序列为3
def sub_count(word_a,word_b):
    cell = {}
    for i in range(len(word_a)):
        cell[i]={}
        for j in range(len(word_b)):
            cell[i][j]=0 #初始化网格，全部赋值0
            if i < 1 or j < 1: #判断第一行，第一列的值
                if word_a[i] == word_b[j]:
                    if i==0 and j==0:
                        cell[i][j] = 1
                        print(word_a[i],end=",")
                    elif i == 0 and j>=1:
                        cell[0][j] = cell[0][j-1]+1
                        print(word_a[i],end=",")
                    else:
                        cell[i][0] = cell[i-1][0]+1
                        print(word_a[i],end=",")
                else:
                    if i==0 and j==0:
                        cell[i][j] = 0
                    elif i == 0 and j>=1:
                        cell[0][j] = cell[0][j-1]
                    else:
                        cell[i][0] = cell[i-1][0]
            else: #根据第一行、第一列累加
                if word_a[i] == word_b[j]:
                    cell[i][j]=cell[i-1][j-1]+1
                    print(word_a[i],end=",")
                else:
                    cell[i][j]=max(cell[i-1][j],cell[i][j-1])
    sim_len = []
    for i in cell.values():
        for j in i.values():
            sim_len.append(j)
    return(cell,max(sim_len))
mat,sim_len = sub_count(word_a,word_b)
print(sim_len)
