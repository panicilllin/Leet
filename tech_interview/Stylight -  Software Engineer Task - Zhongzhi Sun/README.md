
### Requirement from stylight

### General notes:

Through this test, we would like to get a taste of your coding skills and also to see
how you would approach and solve a simple problem. We are not looking for a
perfect solution. We don’t expect you to spend more than 3-4 hours on this task.
Please do not overthink it - we know that certain things definitely take more than
planning.

### Task spec:

We would like you to implement a simple class to find matching strings from a list of
given strings without considering the order of the characters.
You will write a Python class which takes a list of strings in the constructor. This class
will then have another function called find which takes a string to be matched. In the
end this find function will return all the strings from the list which contain the EXACT
same characters and number of characters as the given string. We do not care about
the order of the characters in the strings, but only to find all the matching strings.
For example, the given list of strings could be as follows:
["helloworld", "foo", "bar", "stylight_team", "seo", "oose", "eso"]
Calling the find function with a parameter of "eos" should yield a list of strings ["seo",
"eso"]. If there is no match, simply return an empty list.

### Important instructions:

- state your assumptions. If you feel something is unclear, please just  make an assumption and document it down so that we can understand.
- We hope you can use Python 3.9 or higher to implement this task.
- The codes should be clean and well documented. Please find the balance between comments and self-explanatory codes.
- Please minimise the number of external library dependencies as much as possible if you can. We would prefer to see your python skills instead of your mastery of external library dependencies.
- We value performance and efficiency so please make sure your codes are optimised as much as possible.
- Tests would also be much appreciated on our side. Feel free to choose any testing framework and write tests to "show off" the quality of your solution, its performance, its edge cases and so on.
- To better understand the solution, it would be great if you could add several bullet points explaining the approach in words. Please also give pros/cons of your approach and if there are, some use cases where it might fail.
- When the time is up, send us a zip archive of all source files and a README with instructions on how to build and run your app. Any other materials that can help us understand your approach are also welcome to be included.

### Please also answer these questions:

- How do time complexity and space complexity look like in your approach? Can both of them be optimised? If so, please explain how you would optimise them?
- If the size of the initial string list is very large, would that influence the efficiency of the approach? And what if the number of "find" requests gets extremely large? Do you need to restructure/rethink the approach? If so, please explain how you would rework on your approach.


## Content from Zhongzhi Sun

### guide of this program

 - stylight.py: main code.
 - test_stylight.py: test file
 - readme.md: docuement of this program

### assumptions
1. for hash method, I assume the input only have lowercase letters and underscores. (I could generate a UTF-8 set hash but that would be ugly and long).
2. if the input word is not string, I will pass this word (or throw an exception if require)
3. I assume target word could be pretty large and the word list could be pretty long.
4. I assume the machine have enough memory to read each word in one time.

### Environement

I use python 3.10 and only import  pytest for unit test.

### Complexity

I give two funcion, hash is better in space, sort is better in time.


### Q&A
1. How do time complexity and space complexity look like in your approach? Can both of them be optimised? If so, please explain how you would optimise them?

    hash method:
        time complexity: O(n^2) :: O(n) for length of word list and O(n) for length of each word
        space complexity: O(1) :: length of word hash is pretty sure (unless for some case there is 10^100 time of single letter)
    sort method:
        time complexity: O(nlogn) :: O(n) for length of word list and O(logn) for length of each word.
        space complexity: O(n): O(n) for length of each word.

2. If the size of the initial string list is very large, would that influence the efficiency of the approach? 
    sadly, yes. I need to at least one travel through of this list to find the similar word.

3. And what if the number of "find" requests gets extremely large? Do you need to restructure/rethink the approach?
    If the word become insaine large, Gigebyte kind large, I would prefer hash method, and try to split the word and count the hash by each part, and then sum them to get the final hash of this large word.
    
### About the time I use:

I use about 30 minute to write the code :)
and use one hour and a half to write the test, comment and readme document :(

