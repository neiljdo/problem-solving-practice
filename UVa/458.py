import sys


def main():
    while True:
        encoded = sys.stdin.readline().strip()
        if not encoded:
            break
        decoded = ""
        for c in encoded:
            decoded += chr(ord(c) - 7)
        print(decoded)
        

if __name__ == "__main__":
    main()
