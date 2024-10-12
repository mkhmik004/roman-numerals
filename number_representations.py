def to_roman_numeral(number):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    #breakdown number to its place values,units,10th,100th...
    num_suffix=str(number)
    place_values=[]
    length=len(num_suffix)-1
    for suffix in (num_suffix):
        place_values.append(int(suffix+length*'0'))
        length-=1
    print(place_values)
    roman_value=''
    for value in place_values:
        if value in place_values:
            roman_value +=roman_numerals[value]
        
    return roman_value
print(to_roman_numeral(50))