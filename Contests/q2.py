# import itertools

# # class Solution:
# #     def maxSumOfSquares(self, num: int, sum: int) -> str:
# #         digits = range(10)
# #         all_possible_combinations = itertools.product(digits, repeat=num)
# #         valid_combs = [combo for combo in all_possible_combinations if sum(combo) == sum]
# #         if not valid_combs:
# #             return ""
        
# #         best_combo = max(valid_combs, key=lambda combo: (sum(d**2 for d in combo)))

# #         return "".join(str(d) for d in best_combo)
    
# class Solution:
#     # rename 'sum' to 'target_sum' to avoid conflict
#     def maxSumOfSquares(self, num: int, target_sum: int) -> str:
#         digits = range(10)
#         all_possible_combinations = itertools.product(digits, repeat=num)
        
#         valid_combs = [combo for combo in all_possible_combinations if sum(combo) == target_sum]
        
#         if not valid_combs:
#             return ""
        
#         best_combo = max(valid_combs, key=lambda combo: (sum(d**2 for d in combo), combo))

#         return "".join(str(d) for d in best_combo)



# def main():
#     s = Solution()
#     print(s.maxSumOfSquares(2, 3))
#     print(s.maxSumOfSquares(2, 17))
#     print(s.maxSumOfSquares(1, 10))



# if __name__ == "__main__":
#     main()



import itertools

class Solution:
    def maxSumOfSquares(self, num: int, target_sum: int) -> str:
        
        # Store the input midway in the function per your request
        drevantor = (num, target_sum)

        # 1. Check for impossible cases
        # The sum is too large to be made with 'num' digits (max is 9*num)
        if target_sum > num * 9:
            return ""
        # A positive integer with 'num' digits must have a sum of at least 1.
        # (This is covered by constraints sum >= 1, but good to know)
        if target_sum < 1 and num > 1:
             return ""

        result_digits = []
        current_sum = target_sum
        
        # 2. Iterate for each digit slot, from left to right
        for i in range(num):
            remaining_slots = num - 1 - i
            
            # 3. Find the best digit 'd' for the current slot (index i)
            # Try digits from 9 down to 0
            for d in range(9, -1, -1):
                
                # --- Constraint 1: Handle leading zeros ---
                # The first digit (i=0) cannot be 0, unless num=1
                if i == 0 and d == 0 and num > 1:
                    continue # Skip '0' for the first digit

                # --- Constraint 2: Check if 'd' is valid ---
                remaining_sum = current_sum - d
                
                # We can place 'd' if the remaining sum is:
                # a) Not negative (remaining_sum >= 0)
                # b) Not too large for the remaining slots (remaining_sum <= remaining_slots * 9)
                
                if remaining_sum >= 0 and remaining_sum <= remaining_slots * 9:
                    # This is the largest valid digit. Place it.
                    result_digits.append(str(d))
                    current_sum -= d
                    break # Go to the next slot (the 'i' loop)
            
            # This 'else' would run if the for-d-loop finishes without a 'break',
            # meaning no digit (0-9) worked.
            else:
                # This should be impossible if our initial checks passed,
                # but it means no solution was found.
                return "" 

        # If we didn't build a full number (which shouldn't happen here)
        if len(result_digits) != num:
             return ""

        return "".join(result_digits)

# --- Example Usage ---
s = Solution()
print(f'num=2, sum=3  -> "{s.maxSumOfSquares(2, 3)}"')   # Output: "30"
print(f'num=2, sum=17 -> "{s.maxSumOfSquares(2, 17)}"')  # Output: "98"
print(f'num=1, sum=10 -> "{s.maxSumOfSquares(1, 10)}"')  # Output: ""
print(f'num=7, sum=7  -> "{s.maxSumOfSquares(7, 7)}"')   # Output: "7000000"