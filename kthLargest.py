import random
def findKthLargest(nums, k):

    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:  # If the list contains only one element,
            return nums[left]  # return that element

        # select a random pivot_index between
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)


nums = [3, 12, 3, 6, 4, 7, 9, 10, 4, 6, 7, 14, 5, 5, 1]
k = 6
print(findKthLargest(nums, k))