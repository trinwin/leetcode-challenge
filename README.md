# Leetcode Challenge

I use this repository to keep track of my leetcode progress. I decided to take on May Leetcode challenge to practice solving coding challenge problem everyday using python 3.

## [1.firstBadVersion.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_01.firstBadVersion.py)

1. Think simply, sometimes use while instead of for loop

2. Binary search if you know the answer should be in the other half.

## [2.jewelsAndStones.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_02.jewelsAndStones.py)

1. List comprehension

2. Check if char is in string

## [3.ransomNote.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_03.ransomNote.py)

1. Use string replace(str, char, count) to remove a number of char in string

## [4.numberComplement.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_04.numberComplement.py)

1. bin() convert int to binary number

2. int(bin, 2) convert binary number to int

## [5.firstUniqueChar.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_05.firstUniqueChar.py)

1. Learn Counter collection for String - return a dictionary with key is distinct char in string and value is char's number of occurances

2. string.index(char) return the index of first char occurrence in string

## [6.majorityElement.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_06.majorityElement.py)

1. lambda function in built in function. ex: max(counter, key = lambda ...) to filter out values

## [7.cousinsInBinaryTree.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_07.cousinsInBinaryTree.py)

1. Learn to apply recursion to traverse a Binary Search Tree

2. Finding depth of a node

## [8.checkStraightLine.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_08.checkStraightLine.py)

1. Straight line --> same slope or Use Cross product

2. Check for ZeroDivisionError

## [9.validPerfectSquare.py](https://github.com/trinityng/leetcode-challenge/blob/master/may_challenge/_09.validPerfectSquare.py)

1. Check perfec square without using sqrt --> Use i \* i or num \*\* 0.5

## [10.findTownJudge.py]()

1. [0] \* N --> Create empty list size of N

2. Using index as a key is faster

## [11.floodFill.py]()

1. Practice recursion for 2D array

2. Find 4-directionally connected neighbor of an element

## [12.singleElement.py]()

1. Find single element that appears exactly once

2. Traverse through array by 2 elements and compare element and the one next to it to find unequality

## [13.removeKDigit.py]()

1. Use stack - append and pop digit that greater then its preceding one

2. If no digit that greater then its preceding one then pop the greatest digit

3. To remove leading zeros, use lstrip('0')

## [14.implementTrie.py]()

1. N/A

## [15.maxSumCircularSubarray.py]()

1. Learn Kadane's algorithm

2. Learn Dynamic Programming

## [16.oddEvenLinkedList.py]()

1. Review Linked List

2. Learn multi-chain assignment (a = b = 5)

## [17.findAllAnagramInString.py]()

1. Use Counter

2. Learn to convert char to ASCII Code using ord()

3. Quicken algorithm by reducing the number of loop through array using Sliding Window

## [18.permutationInString.py]()

1. Practice the Sliding Window techniques again and optimized sliding window. This problem is similar to findAnagram

## [19.onlineStockSpanner]()

1. Practice more with Dynamic Programming

2. Use Stack to save data to reduce the memory and run time
