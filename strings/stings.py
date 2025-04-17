# STRING MASTERCLASS IN ONE SCRIPT

# 1. Declaring Strings
first_name = 'John'
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# 2. Multi-line String
bio = """John Doe is a software engineer,
loves Python, and enjoys teaching."""
print("\nBio:\n" + bio)

# 3. String Formatting
age = 30
intro = f"My name is {full_name} and I am {age} years old."
print("\nFormatted Intro:", intro)

# 4. String Methods
message = "  Welcome to Python Programming!  "
print("\nOriginal:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Stripped:", message.strip())
print("Replaced:", message.replace("Python", "Java"))
print("Split:", message.split())

# 5. Indexing & Slicing
language = "Python"
print("\nFirst letter:", language[0])
print("Last letter:", language[-1])
print("Slice (0:3):", language[0:3])
print("Reversed:", language[::-1])