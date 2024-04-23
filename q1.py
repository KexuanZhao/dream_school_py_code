def min_num_of_subsequences(source: str, target: str) -> int:
    source_set = set(source)
    target_set = set(target)
    # if any character in target is not in source, return -1
    if not target_set.issubset(source_set):
        return -1
    m = len(source)
    count = 0
    source_ptr = 0
    for char in target:
        # increment count when the source pointer starts from 0 again.
        if source_ptr == 0:
            count += 1
        # loop over the source string until it matches the character in target
        # in each iteration, increment the source pointer by 1
        while source[source_ptr] != char:
            source_ptr = (source_ptr + 1) % m 
            if source_ptr == 0:
                count += 1
        source_ptr = (source_ptr + 1) % m

    return count

if __name__ == "__main__":
    test_cases = [
        ("abc", "abcbc"),
        ("abc", "acdbc"),
        ("xyz", "xzyxz"),
    ]

    for source, target in test_cases:
        print(min_num_of_subsequences(source, target))