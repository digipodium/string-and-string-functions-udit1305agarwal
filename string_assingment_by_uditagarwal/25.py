string = "this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated"
words = string.split()
avg = sum(len(i) for i in words) / len(words)
print(avg)