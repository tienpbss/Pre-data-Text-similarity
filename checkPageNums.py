import os
import fitz


path = 'D:\\Document-CSDLDPT'
path2 = 3


files = os.listdir(path)

nums = []

delete = []

for file in files:
    f = os.path.join(path, file)
    doc = fitz.open(f)
    nums.append(len(doc))
    # if (len(doc) < 20):
    #     doc.close()
    #     os.remove(f)
    #     print(f"Delete {file}")


nums.sort()
print(nums)
print(len([i for i in nums if i < 20]))
print(len([i for i in nums if i >= 20]))