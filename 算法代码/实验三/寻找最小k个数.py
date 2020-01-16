class Solution:
  def PartitionOfK(self, numbers, start, end, k):
    if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
      return
    low, high = start, end
    key = numbers[low]
    while low < high:
      while low < high and numbers[high] >= key:
        high -= 1
      numbers[low] = numbers[high]
      while low < high and numbers[low] <= key:
        low += 1
      numbers[high] = numbers[low]
    numbers[low] = key
    if low < k:
      self.PartitionOfK(numbers, start + 1, end, k)
    elif low > k:
      self.PartitionOfK(numbers, start, end - 1, k)
  def GetLeastNumbers_Solution(self, list, k):
    # write code here
    if k <= 0 or list  == [] or k > len(list):
      return []
    self.PartitionOfK(list, 0, len(list) - 1, k)
    return sorted(list[0:k])
#测试：
sol = Solution()
listNum = [4,5,1,6]
rel = sol.GetLeastNumbers_Solution(listNum, 2)
print(rel)