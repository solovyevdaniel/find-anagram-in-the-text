# Returns a list of the indexes string 'b' that elements
# The value of which is equal to the first element of string 'a'
def check(str_a, str_b):
    founded_indexes = []
    for i in range(0, len(str_b)):
        if str_a[0] == str_b[i]:
            founded_indexes.append(i)
    return founded_indexes


def main():
    str_a = 'abcd'
    str_b = 'jfxbacdabwaczd'
    # Check whether there is a substring of the letters string 'a' in string 'b'
	# Anagrams otherwise not be in string 'b'
    if check(str_a, str_b) != []:
        for i in check(str_a, str_b):
            # Take all substrings with length string 'a' 
            for j in range(i - len(str_a) + 1, i + 1):
                if 0 <= j <= len(str_b) - len(str_a):
                    if set(str_a) == set(str_b[j:j+len(str_a)]):
                        return True
    return False