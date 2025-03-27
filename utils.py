# Turns an array of decimal ascii values and returns the equivalent word
def arrayToAscii(arr: list):
    word = ""
    for num in arr:
        word+=chr(num)
    return word
