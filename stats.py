def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2


def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return min(modes)


def main():
    test_list = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
    print("Test list:", test_list)
    print("Mean:", mean(test_list))
    print("Median:", median(test_list))
    print("Mode:", mode(test_list))


if __name__ == "__main__":
    main()
