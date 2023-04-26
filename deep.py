def deepEquals(a, b):
   
    if a == b:
        return True
    if a is None or b is None or type(a) != type(b):
        return False
    if isinstance(a, (str, int, float, bool)):
        return a == b
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not deepEquals(a[i], b[i]):
                return False
        return True

 
    return vars(a) == vars(b)
#For Strings
string1='Paktolus'
string2='Paktolus'
string3='Computer'
string4='IT'
#For Numbers
number1=123
number2=123
number3=321
number4=456
#For Boolean
b1=1<1
b2=1<1
b3=1>2
b4=1>5
#For Symbols
sym1='#'
sym2='#'
sym3='+'
sym4='-'
#For array
arr1=[1,2,3]
arr2=[1,2,3]
arr3=['a','b','c']
arr4=[3,2,1]
print(deepEquals(string1,string2))
print(deepEquals(string3,string4))
print(deepEquals(number1,number2))
print(deepEquals(number4,number3))
print(deepEquals(b1,b2))
print(deepEquals(b3,b4))
print(deepEquals(sym1,sym2))
print(deepEquals(sym3,sym4))
print(deepEquals(arr1,arr2))
print(deepEquals(arr3,arr4))
