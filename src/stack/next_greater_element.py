"""
2024-02-14

496. Next Greater Element I (https://leetcode.com/problems/next-greater-element-i)

Code ref
https://leetcode.com/problems/next-greater-element-i/solutions/3285190/496-space-92-75-solution-with-step-by-step-explanation/
"""


class NextGreaterElementSolution:
    def solution(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        daily temperatures problem fundamental task

        nums1의 ith element를 nums2에서 찾고, nums2에서 해당 value보다 큰 값을 right side에서 찾아서 return
        O(nums1.length + nums2.length) solution은?

        nums2 element에서 각 value 별로 greater 값 찾기 필요(nums1과 상관없이)
        1. nums2 순회하면서 각 value 별 greater 값 hashmap 생성 => O(N)
        2. nums1 순회하면서 1의 hashmap에서 greater 값 조회. 없으면 -1
        """
        # Create a dictionary to store the next greater element of each number in nums2
        next_greater = {}
        # Create a stack to keep track of the elements whose next greater element is not found yet
        stack = []
        
        # Loop through each element in nums2
        for num in nums2:
            # While the stack is not empty and the current number is greater than the top element in the stack
            while stack and num > stack[-1]:
                # Pop the top element from the stack and set its next greater element to the current number
                next_greater[stack.pop()] = num
            # Add the current number to the stack
            stack.append(num)
        
        # Create a list to store the next greater element of each number in nums1
        result = []
        # Loop through each element in nums1
        for num in nums1:
            # If the next greater element of the current number is found
            if num in next_greater:
                # Append it to the result list
                result.append(next_greater[num])
            else:
                # Otherwise, append -1 to the result list
                result.append(-1)
        
        return result

