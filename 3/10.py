# sposób 1 
roman_dict1 = {
    'I': 1,
    'V': 5, 
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# sposób 2
roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
roman_values = [1, 5, 10, 50, 100, 500, 1000]
roman_dict2 = dict(zip(roman_symbols, roman_values))

def roman2int(roman_str):
    result = 0
    prev_value = 0
    
    for char in reversed(roman_str.upper()):
        curr_value = roman_dict1[char]
        
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
            
        prev_value = curr_value
        
    return result

assert roman2int('III') == 3
assert roman2int('IV') == 4
assert roman2int('IX') == 9
assert roman2int('LVIII') == 58
assert roman2int('MCMXCIV') == 1994
