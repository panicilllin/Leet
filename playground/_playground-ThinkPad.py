class ParseError(Exception):
  ...
  
def parse_compute_averages(input_arguments: str) -> str:
    keys = input_arguments.split(' ')
    arrays = {}
    # print(keys)
    for item in keys:
        name = item.split('=')[0]
        name_format = "".join([i for i in name if i.isalpha() or i.isnumeric()])
        if name_format != name:
            raise ParseError('Invalid argument name')
        value = item.split('=')[1]
        avg = count_avg(value)
        if avg == 'NaN':
            arrays[name] = 'nan'
        # elif avg == False:
        #     raise ParseError(f'Input value "{value}" is invalid')
        else:
            arrays[name] = format(round(avg,2), '.2f')
    # print(arrays)
    res = ''
    for key,val in arrays.items():
        res = res + ' ' + key + '=' + str(val)
    return res[1:]

def count_avg(input_str):
    if input_str[0] != '[':
        raise ParseError(f'Input value "{input_str}" is invalid')
    value_list = []
    this_value = ''
    i=1
    while i < len(input_str):
        this_char = input_str[i]
        if this_char == '[':
            substr = find_substr(input_str[i:])
            # print(f"input_str=={input_str} :: substr=={substr}")
            value_list.append(count_avg(substr))
            i+= len(substr)
            continue
        elif this_char in [';', ']']:
            numberlize_value = is_number(this_value)
            # print(f"numberlize_value={numberlize_value},this_value={this_value}")
            if numberlize_value is not False:
                value_list.append(numberlize_value)
            elif this_value == 'NaN':
                value_list.append('nan')
            elif this_value == '':
                i+=1
                continue
            else:
                # print(f"this_char={this_char} :: this_value={this_value}")
                raise ParseError(f'Input value "{input_str}" is invalid')
            this_value = ''
            if this_char == ']':
                # print(f"end_char: i={i},len_str = f{len(input_str)}")
                if i != len(input_str)-1:
                    raise ParseError()
        else:
            this_value += this_char
        i+=1
    # print(f"input_str={input_str} :: value_list={value_list}")
    if 'nan' in value_list:
        return 'nan'
    elif len(value_list) == 0:
        return 0
    else:
        return sum(value_list)/len(value_list)

def find_substr(input_str):
    count=0
    for i in range(0,len(input_str)):
        this_char = input_str[i]
        if this_char == '[':
            count +=1
        elif this_char == ']':
            count -=1
        if count == 0 :
            return input_str[:i+1]

def is_number(s):
    try:
        float(s)
        return float(s)
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return unicodedata.numeric(s)
    except (TypeError, ValueError):
        pass
 
    return False
        
        

if __name__ == "__main__":
    # a = parse_compute_averages("--a1=[1;2;3;[6;7];[]] arg02=[1.337] a3=[NaN;1;-2] a4=[-42.0] --arg5=thisisastring")
    # a = parse_compute_averages("arg1=[1;2;3] arg2=[-42.0]")
    # a = parse_compute_averages("a1=[1;2;3;[6;7];[]] arg02=[1.337]")
    # a = parse_compute_averages('--arg1="thisisastring"')
    TEST_CASES = [
    # Basic test cases
    ("arg=[1.0;2.0;3.0]", "arg=2.00", "Basic example"),
    ("arg=[1;[1;2;3];3]", "arg=2.00", "Some nesting"),
    ("arg1=[1;2;3] arg2=[-1;-2;-3]", "arg1=2.00 arg2=-2.00", "Multiple args and negative values"),
    ("arg=[]", "arg=0.00", "Single empty list"),
    ("arg=[1.0;NaN;3.0]", "arg=nan", "NaNs should be handled"),

    # # Trickier test cases
    ("xyz=[[[];[];[]];[];[[[[]]]]]", "xyz=0.00", "Argument with heavily nested empty lists is valid"),
    ("a0=[1;[NaN]] stuff=[1;3;1;3]", "a0=nan stuff=2.00", "NaN in one arg is not a NaN for all"),
    ("key=[1.3333333337]", "key=1.33", "Output should be rounded to 2 decimal points"),
    ("nest=[1;[1;[1;[1;[1;2];2];2];2];2]", "nest=1.50", "Deeply nested list is okay"),
    ("a0=[0] a1=[1] a2=[2] a3=[3]", "a0=0.00 a1=1.00 a2=2.00 a3=3.00", "Many args are fine"),

    # # Errors
    # ("arg=2.00", ParseError, "We always want at least one top-level list"),
    ("a2=[2-1]", ParseError, "Expressions are not valid values"),
    ("a1=['abc']", ParseError, "Strings aren't valid values"),
    ("arg=[print)(]", ParseError, "Random incorrect Python code definitely isn't a valid value"),
    ("a1=[2,3,4]", ParseError, "Commas are not valid delimiters"),
    ("arg=[1.0][2.0]", ParseError, "List followed by incorrectly placed empty list"),
    ("[1]=[1]", ParseError, "Invalid argument name"),
    ("a1=[[2,3.4,[4],[[5]]],[[3]] a2=[]", ParseError, "Mismatched bracket in deeply nested list"),
    (" ", ParseError, "Empty input is an error (whitespace isn't relevant)"),
    ("a0=['wrong';NaN]", ParseError, "A value with NaN literal can also just be wrong"),
]
    for case in TEST_CASES:
        # print(case[0])
        try:
            a = parse_compute_averages(case[0])
        except:
            a = ParseError
        # a = parse_compute_averages(case[0])
        if a == case[1]:
            print("pass")
        else:
            print(f"Wrong=====\ncase={case}\nans:: {a}  |||  right_ans:: {case[1]}")
            break
