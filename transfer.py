with open('words.csv', 'r') as old, open('new_words.txt', 'w') as new:
  words_file_lines = old.readlines()
  words = [col[1][6:].lower() for col in [line.split(',') for line in words_file_lines]]
  for w in words:
    new.write(w)
    new.write('\n')