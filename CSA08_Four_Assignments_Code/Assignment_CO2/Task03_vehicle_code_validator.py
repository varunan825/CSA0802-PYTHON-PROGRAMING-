def validate_code(code):
    code = code.replace(" ", "").replace("-", "").upper()
    if len(code) not in (9, 10):
        return False
    if not code[:2].isalpha() or not code[2:4].isdigit():
        return False
    if not code[4:-4].isalpha() or not code[-4:].isdigit():
        return False
    return True

code = input("Enter code: ")
print("Valid Code" if validate_code(code) else "Invalid Code")
