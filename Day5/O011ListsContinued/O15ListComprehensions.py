import pprint
sentence = "the quick brown fox jumps over lazy dog"

word_list = sentence.split()
print(word_list)
word_len = [len(i) for i in word_list]
print(word_len)
print("_" * 40)

word_len1 = [(i, len(i)) for i in word_list]
pprint.pprint(word_len1, indent=True)
print("_" * 40)

nums = [34.56, -203.56, 4.6, 12.55, 2.3]
new_list_int = [int(n) for n in nums]
print(new_list_int)
print("_" * 40)

pow2 = [2**x for x in range(1, 11)]
print(pow2)
print("_" * 40)

pow2 = [2**x for x in range(1, 11) if x % 2 == 0]
print(pow2)

print("_" * 40)
combine = [actor + " " + actress for actor in ["Venkatesh", "Chiranjivi"]
           for actress in ["Sri devi", "Hema Malini"]]
pprint.pprint(combine, indent=True)
