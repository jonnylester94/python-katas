# Python Katas

This repo contains a series of katas, varying in difficulty level, designed to demonstrate how I solve problems and write code in Python using test-driven development. I created a Makefile to help build the project and used the following commands to setup the repo:

```bash
- make create-environment
- source venv/bin/activate
- make pytest
```
The first command brings the venv directory into the project folder, the second activates the virtual environment, and the third installs pytest. I then used these commands to run my tests (the first runs all tests and the second runs tests for a specific kata): 

```bash
- make run-checks
- make unit-test <path to test file>
```

Each sub-directory in the src directory relates to a specific kata. Each sub-directory contains a Python file with code to solve the kata and a markdown file with a description of the kata to be solved. The requirements.txt file contains the dependencies necessary to run the code and tests.


## Katas:
- sentence_to_camel_case;
- get_distinct_letters;
- get_frequencies;
- create_counter;
- lengthen_date;
- get_century;
- years_of_growth;
- herd_the_babies;
- sum_ascii;
- bubble_sort;
- extract_domain_name;
- caesar_cipher;
- roman_numeral_encoder;
- alphabet_position
