import requests

from src.tools.username_gen import gen as genAvailableNicks


def main():
    print(genAvailableNicks(2)) # return 2 avaliable nicks
    

if __name__ == "__main__":
    main()
