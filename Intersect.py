def Intersect(nums1, nums2):
    lst3 = [value for value in nums1 if value in nums2]
    return lst3
    

nums1, nums2 = [1,2,2,1], [2,2]
print(Intersect(nums1, nums2))
   