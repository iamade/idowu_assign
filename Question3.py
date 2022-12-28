def Exercise3(nums1, nums2, nums3, nums4):
    counter = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            for k in range(len(nums3)):
                for l in range(len(nums4)):
                    if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                        counter += 1
    return counter

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1, 2]
nums4 = [0, 2]

print('Question3', Exercise3(nums1,nums2, nums3, nums4))


