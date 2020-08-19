# OK


HZ = 35184372089371

nums = ['11']
for i in range(10 ** 6 + 1):
    prev = nums[-1]
    if prev[:2] == '11':
        cur = prev.replace('11', '10') + '1'
    else:
        cur = prev.replace('01', '10')
    nums.append(cur)
nums = list(map(lambda item: int(item, 2), nums))
nums = [num % HZ for num in nums]

x = int(input())
query = []
for _ in range(x):
    query.append(int(input()))

for e in query:
    print(nums[e-1])
