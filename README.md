# BloxNickGenerator

## Introduction

BloxNickGenerator is a Python package that allows you to generate available usernames for Roblox. It checks the availability of usernames and ensures that the generated usernames do not contain profanity.

## Features

- Generate a specified number of usernames.
- Check for profanity using an external API.
- Verify if usernames are already taken on Roblox.


## Usage
```python
from bloxnickgenerator.generator import genUsername

usernames = genUsername(3) # gen 3 usernames
print("Generated Usernames:", usernames)
``` 
## Installation

You can install BloxNickGenerator using pip:

```bash
pip install bloxnickgenerator
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.