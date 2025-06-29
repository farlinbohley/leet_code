from two_sums import Solution

# Example of how to instantiate the class and use its method:
if __name__ == "__main__":
    # 1. Instantiate the class
    solver = Solution()

    # 2. Prepare some example data
    example_nums = [2, 7, 11, 15]
    example_target = 9

    # 3. Call the method on the instance
    result_indices = solver.twoSum(example_nums, example_target)
    print(f"For nums = {example_nums} and target = {example_target}, the indices are: {result_indices}")

    example_nums_2 = [3, 2, 4]
    example_target_2 = 6
    result_indices_2 = solver.twoSum(example_nums_2, example_target_2)
    print(f"For nums = {example_nums_2} and target = {example_target_2}, the indices are: {result_indices_2}")

    example_nums_3 = [3, 3]
    example_target_3 = 6
    result_indices_3 = solver.twoSum(example_nums_3, example_target_3)
    print(f"For nums = {example_nums_3} and target = {example_target_3}, the indices are: {result_indices_3}")
