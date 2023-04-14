# bubble_sort

A [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) is an inefficient sorting algorithm that takes a list of numbers and iterates through them comparing 2 neighbouring numbers at a time.

If the first number is greater than the second number the algorithm will switch their places and move on to the next pair. If the first number is less than the second number the algorithm will move on to the next pair doing nothing.

It will continue looping through the array until there are no more changes to make.

```py
initialList = [1, 4, 2, 3]

bubble_sort(initial_list) # [1,2,3,4]

# the algorithm starts at the beginning of the array
1 > 4? # no, move on

[1,4,3,2]
4 > 3? # yes, switch them

[1,3,4,2]
4 > 2? # yes, switch them

[1,3,2,4]
# loop through again

1 > 3? # no, move on
[1,3,2,4]

3 > 2? # yes, switch them
[1,2,3,4]

3 > 4? # no, move on
[1,2,3,4]

# no more changes to make
finalList = [1, 2, 3, 4]
```
