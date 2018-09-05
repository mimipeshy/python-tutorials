def is_isogram(argument):
  word_seen=set()
  if type(argument) != str:
    raise TypeError('Argument should be a string')
  if argument==" " :
    return(argument,False)
  argument.lower()
  argument = ''.join(argument.split())
  for letter in argument:
    if letter in word_seen:
      return(argument,False)
    word_seen.add(letter)
  return (argument,True)
