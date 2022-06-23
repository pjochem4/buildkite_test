import sys


def add_two(n: int) -> int:
    return n + 2

def add_one(n: int) -> int:
    return n + 1

if __name__ == "__main__":
    
    if add_one(1) == 2:
        sys.exit(0)
    sys.exit(1)
