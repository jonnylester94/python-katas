# create_counter

The function `create_counter` should accept a number as it's only argument.

It should return a dictionary containing two functions the can be invoked to change and return the counters value.

## Examples

```py
counter = create_counter(10)
up = counter['up']
down = counter['down']

print(up()) # 11

print(down()) # 10

print(down()) # 9

print(up()) # 10
```
