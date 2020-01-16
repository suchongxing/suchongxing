def merge_sort(list):    #不断递归调用自己一直到拆分成成单个元素
    if len(list) == 1:
        return list
    mid = len(list) // 2   # 取拆分的中间位置    拆分过后左右两侧子串
    left = list[:mid]
    right = list[mid:]    # 对拆分过后的左右再拆分 一直到只有一个元素为止
    leftlist = merge_sort(left)
    rightlist= merge_sort(right)
    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并 leftlist 和 rightlist
    return merge(leftlist,rightlist)
def merge(left, right):
    # 这里接收两个列表
    # 从两个有顺序的列表里边依次取数据比较后放入resultlist
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入resultlist
    resultlist = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            resultlist.append(left.pop(0))
        else:
            resultlist .append(right.pop(0))
# while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    resultlist  += left
    resultlist  += right
    return resultlist
if __name__ == '__main__':
    list = [8,4,5,7,1,3,6,2]
    print(merge_sort(list))