# BloxNickGenerator
## Introduction
BloxNickGenerator is a Python package that allows you to generate available usernames for Roblox. It checks the availability of usernames and ensures that the generated usernames do not contain profanity.

## Features
- Generate a specified number of usernames.
- Check for profanity using an external API.
- Verify if usernames are already taken on Roblox.
- Customize generated usernames with optional prefixes, suffixes, and length constraints.


# Usage
You can generate nicknames with various customization options. Here are some examples:

### Basic Usage
Generate a specified number of nicknames:

```python
from bloxnickgenerator.generator import genNicknames

generated_nicks = genNicknames(3) # Generate 3 nicknames
print("Generated Nicknames:", generated_nicks)
```

### Using Prefixes and Suffixes
You can add prefixes and suffixes to the generated nicknames:

```python
from bloxnickgenerator.generator import genNicknames

generated_nicks = genNicknames(3, prefix='Xx_', suffix='test') # Generate nicknames with a prefix and suffix 
print("Generated Nicknames:", generated_nicks)
```

### Length Constraints
Set minimum and maximum lengths for the nicknames:

```python
from bloxnickgenerator.generator import genNicknames

generated_nicks = genNicknames(3, min_length=5, max_length=16) # Generate nicknames within specific length constraints 
print("Generated Nicknames:", generated_nicks)
```

### Example
```python
from bloxnickgenerator.generator import genNicknames

nicks = genNicknames(3, prefix='Xx_', suffix='test', min_length=5, max_length=16) 
print("Generated Nicknames:", nicks) 
# Result: ['Xx_jasonlongtest', 'Xx_jessica63test', 'Xx_znixontest']
```

- Note: Depending on the number of nicknames you want to generate, it may take a while.

# Installation
### You can install BloxNickGenerator using pip:

```bash
pip install bloxnickgenerator
```

- https://pypi.org/project/bloxnickgenerator/0.1.2/

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Give a ⭐ to support the project for future updates
