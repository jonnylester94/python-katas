# extract_domain_name

The function `extract_domain_name` should take a URL as a string and return just the domain name.

## Examples

```py
extract_domain_name("https://www.reddit.com/")
# reddit.com
extract_domain_name("https://github.com/northcoders/de-py-katas")
# github.com
extract_domain_name("https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2")
# google.com
```

💡Hint: The [regex module](https://docs.python.org/3/library/re.html) may come in handy here
