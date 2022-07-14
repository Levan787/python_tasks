"""
You are given  words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
Constraints: 
1 <= n = 10^5
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, n. 
The next n lines each contain a word.
Output Format
Output 2 lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
Explanation
There are 3 distinct words. 
Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. 
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output."""

n_ish = int(input("enter a number: ")) 

counter_dict = {} 
words_list = [] 

for i in range(n_ish): 
  word = input("enter a string: ") 
  words_list.append(word)   
  if word in counter_dict: 
    counter_dict[word] += 1 
  else:
    counter_dict[word] = 1 
print(len(counter_dict)) 
print(' '.join([str(counter_dict[word]) for word in counter_dict])) 
