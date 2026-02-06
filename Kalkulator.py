import sys

def Wylicz():
        n_str = sys.stdin.readline().strip()
        if not n_str:
            return

        n = int(n_str)
        for _ in range(n):
            dzialanie = sys.stdin.readline().strip()
            if dzialanie:
                print(eval(dzialanie))

if __name__ == "__main__":
    Wylicz()
