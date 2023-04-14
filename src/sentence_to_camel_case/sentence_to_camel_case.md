# sentence_to_camel_case

This function should take a sentence and convert it to upper or lower camel case.

The function takes two arguments; the sentence, and a boolean - true if UpperCamelCase is to be returned and false if lowerCamelCase is to be returned.

## Examples:

```python
sentence_to_camel_case("this sentence", True)
# should return "ThisSentence"
```

```python
sentence_to_camel_case("this sentence", False)
# should return "thisSentence"
```

```python
sentence_to_camel_case("This Bigger strange Sentence", True)
# should return "ThisBiggerStrangeSentence"
```
