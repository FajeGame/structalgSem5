def tribonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

def main() -> None:
    s = input().strip()
    print(tribonacci(int(s)) if s else 0)

if __name__ == "__main__":
    main()

# Как я понял ничего выводить не нужно