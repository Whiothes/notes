#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
# pattern = r"[aeiou]"

# if re.search(pattern, "grey"):
#     print("Match 1")

# if re.search(pattern, "qwertyuiop"):
#     print("Match 2")

# if re.search(pattern, "rhythm myths"):
#     print("Match 3")

# pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern, "LS8"):
#     print("Match 1")

# if re.search(pattern, "E3"):
#     print("Match 2")

# if re.search(pattern, "lab"):
#     print("Match 3")

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
