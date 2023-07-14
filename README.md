# Maximum Subarray Sum using Divide-and-Conquer

This repository contains a Python implementation of the maximum subarray sum problem using a divide-and-conquer algorithm.

## Problem Description

Given an array of integers, the maximum subarray sum refers to the sum of a contiguous subarray with the largest possible sum.

The goal is to find an efficient algorithm that can determine the maximum subarray sum for a given array.

## Solution Overview

The solution provided in this repository uses a divide-and-conquer approach to find the maximum subarray sum.

The `max_subarray_sum` function recursively divides the array into two halves until reaching the base case of an array with only one element. Then, it combines the results from the left and right halves with the maximum subarray sum that crosses the midpoint.

The `max_crossing_sum` function calculates the maximum subarray sum that crosses the midpoint of the array.

## Test Cases

The repository includes test cases to verify the correctness of the solution. Here are a few examples:

- Test case 0:
  - Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
  - Expected output: `6`

- Test case 1:
  - Input: `[1, 2, 3, 4, 5]`
  - Expected output: `15`

- Test case 2:
  - Input: `[-1, -2, -3, -4, -5]`
  - Expected output: `-1`

- Test case 3:
  - Input: `[1, -2, 3, -4, 5]`
  - Expected output: `5`

- Test case 4:
  - Input: `[7]`
  - Expected output: `7`

- Test case 5:
  - Input: `[0, 0, 0, 0, 0]`
  - Expected output: `0`

- Test case 6:
  - Input: `[1, -2, 3, -4, 5, -6, 7]`
  - Expected output: `7`

- Test case 7:
  - Input: `[-10]`
  - Expected output: `-10`


## How to Use

To use this implementation, you can clone the repository and run the code using a Python interpreter.

Step One: Clone The Repository.
```bash
git clone [<repository_url>](https://github.com/Reddragon300/Max-Subarray-Divide-Conquer
```
Step Two: Change into the program directory.
```bash
cd max-subarray-sum-divide-conquer
```
Step Three: After cloning the repository and navigating to the appropriate directory, you can run the code using a Python interpreter.
```bash
python max_subarray_sum.py
```

## Make sure you have Python installed on your machine.

Contribution
Contributions to this repository are welcome. If you have any suggestions for improvements or alternative approaches, feel free to open a pull request.

License
This repository is licensed under the MIT License.

Feel free to modify the contents of the README.md file according to your preference and add any additional sections or information that you find relevant.
