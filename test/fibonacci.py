def fibonacci(n: int) -> list[int]:
    """返回前 n 个斐波那契数。"""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    print(fibonacci(10))
