def findMedian(nums1, nums2):
    total = nums1 + nums2
    total.sort()
    if len(total) % 2 == 0:
        i = total[len(total)//2]
        j = total[len(total)//2 + 1]
        return (i+j)/2
    else:
        return total[len(total)//2]

nums1 = [1, 2, 4]
nums2 = [3, 4, 5, 7, 9]
print(findMedian(nums1, nums2))