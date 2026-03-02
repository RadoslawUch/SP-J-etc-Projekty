import sys

def Wylicz():
    for dzialanie in sys.stdin:
        dzialanie = dzialanie.strip()
        if not dzialanie:
            continue
        try:
            print(eval(dzialanie))
        except:
            pass

if __name__ == "__main__":
    Wylicz()
