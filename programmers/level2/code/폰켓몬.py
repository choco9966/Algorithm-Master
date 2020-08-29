def solution(nums):
    answer = 0
    # 항상 짝수로 제공 
    MAX_number = len(nums) / 2
    # 포켓몬 종류 
    nums = len(set(nums))
    return min(MAX_number, nums)
