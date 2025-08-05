if __name__ == '__main__':
  sentence = input('请输入一段话:')
  counter = {}
  for char in sentence:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
      counter[char] = counter.get(char, 0) + 1
  sorted_keys = sorted(counter,key=counter.get,reverse=True)
  for key in sorted_keys:
    print(f'{key}出现了{counter[key]}次')