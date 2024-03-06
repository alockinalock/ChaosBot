import random

# 0-9 is repeated 3 times for an increased chance of picking a number
valid_chars = "abcdefghijklmnopqrstuvwxyz123456789012345678901234567890"

def name_gen() -> str:
    generated_string = ""
    n = random.randint(20, 30)
    for _ in range(n):
        j = random.randint(0, len(valid_chars) - 1)
        generated_string += valid_chars[j-1:j]
    return generated_string

# TODO: temp, delete once unneeded
if __name__ == "__main__":
    print(name_gen())
