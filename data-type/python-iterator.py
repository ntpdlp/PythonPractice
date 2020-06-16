#! /usr/bin/env python3


def main():
    nums = [1,2,3,4,5,6,8]
    it = iter(nums)
    n = len(nums)
    while n>0:
        print(next(it))
        n = n-1


if __name__ == '__main__':main()
