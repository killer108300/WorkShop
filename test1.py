s = "{[()]}"
stack_openpar = []
def pop(input_stack):
    input_stack = input_stack.remove()
def push(input_stack, open_index):
    input_stack.append(open)
dicts = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
}
for x in range(len(s)):
    if dicts.get(s[x]) is not None:
        #open
        push(stack_openpar,s[x])
    elif dicts.get(s[x]) is None:
        #close
        if Exception:
            pass
            print("123")
            
