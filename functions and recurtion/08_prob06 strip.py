
def remove_and_strip(string, word):
    newstr=string.replace(word,"an engineer")
    return newstr.strip()


hi="        subha is a doctor       "
print(hi.strip())
n= remove_and_strip(hi, "a doctor")
print(n)