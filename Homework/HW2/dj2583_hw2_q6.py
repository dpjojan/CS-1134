def two_sum(srt_lst, target):
    first = 0
    second = len(srt_lst)-1
    while second < len(srt_lst):
        current_sum = srt_lst[first] + srt_lst[second]
        if current_sum == target:
            return first, second
        if current_sum > target:
            second -= 1
        else:
            first += 1
        