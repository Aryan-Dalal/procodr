#to check if brackets are balanced or not

def main():
  inp = input("series of brackets\n")
  brackets = list(inp)
  tokens = {
    "(" : ")",
    "[" : "]",
    "{" : "}"}

  def compute_stack(bracs):
    global stack
    stack = []
    global last_complete
    last_complete = 0
    stack.append(bracs[0])

    for i in range(1, len(bracs)):
      if not stack:
        last_complete = i
        if i < len(bracs)-1:
          stack.append(bracs[i])
          continue
      if bracs[i] == tokens.get(stack[0-1]):
        stack.pop()
      elif bracs[i] != tokens.get(stack[0-1]):
        stack.append(bracs[i])

  def check_brackets(bracs):
    if not bracs:
      print("Empty string of brackets has been given")
      exit
    
    compute_stack(bracs)

    if not stack:
      print("the brackets are balanced")

    else:
      print("The brackets are not balanced")

  def check_total_balance(bracs):  
      compute_stack(bracs)
      if not stack:
        print(len(bracs))
      if stack:
        print(last_complete)

  check_brackets(brackets)
  check_total_balance(brackets)

if __name__ == "__main__":
  main()


"""
  create a stack for the active brackets
  create a dictionary for the token of the opposite bracket

  for no. of brackets:
    read the first bracket and add it to stack
    move to the next bracket and see if it matches the latest append to the stack,
      if yes, move one and pop stack
      if no, add the bracket to a stack

"""