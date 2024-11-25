class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0  # To count the number of jumps
        current_end = 0  # End of the current jump range
        farthest = 0  # Farthest point we can reach
        
        for i in range(n - 1):  # Stop before the last index
            farthest = max(farthest, i + nums[i])  # Update the farthest point reachable
            
            if i == current_end:  # If we've reached the end of the current jump
                jumps += 1
                current_end = farthest  # Move to the next jump range
            
            if current_end >= n - 1:  # Early exit if we can already reach the end
                break
        
        return jumps
