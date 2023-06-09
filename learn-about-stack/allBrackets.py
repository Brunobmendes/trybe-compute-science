def bracketIsClosed(code):
    brackets = code.count("{") == code.count("}")
    parentheses = code.count("(") == code.count(")")

    if brackets and parentheses:
        return True
    return False


print(bracketIsClosed("{{}()}"))
