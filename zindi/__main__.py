import sys 


def main():
    args = sys.argv[1:]

    for arg in args:
        print(f'argument passed : {arg}')

if __name__ == "__main__":
    main()