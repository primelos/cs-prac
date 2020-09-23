# Sort Elements in a Stack
# Given a Stack class like the following:

# class Stack {
#   constructor() {
#     this.storage = [];
#   }

#   push(item) {
#     this.storage.push(item);
#   }

#   pop() {
#     return this.storage.pop();
#   }

#   peek() {
#     return this.storage[this.storage.length-1];
#   }

#   isEmpty() {
#     return this.storage.length === 0;
#   }

#   printContents() {
#     this.storage.forEach(elem => console.log(elem));
#   }
# }
# Write a function sortStack that receives a stack of integers and returns another stack containing those same integers in sorted order. You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure.

# Example:

# const s = new Stack();
# s.push(4);
# s.push(10);
# s.push(8);
# s.push(5);
# s.push(1);
# s.push(6);

# const sortedStack = sortStack(s); // sortedStack is also a Stack instance

# sortedStack.printContents();  // should print 1, 4, 5, 6, 8, 10
# Analyze the time and space complexity of your solution.



class Stack:
    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)

    def pop(self);
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0
    
    def print_contents(self):
        for item in self.storage:
            print(item)


stack = Stack()
stack.push(1)
stack.push(5)
stack.push(3)
stack.push(9)
stack.push(2)
stack.push(4)
stack.push(7)
stack.push(8)
stack.push(10)

def sort_stack(input):
    output = stack()
    while True:
        temp = None
        size = 0
        temp_changed = 0
        while not input.is_empty():
            size += 1
            nextVal = input.pop()
            if temp is None:
                temp = nextVal
                temp_changed += 1
            elif temp < nextVal:
                output.push(temp)
                temp = nextVal
                temp_changed += 1
            else:
                output.push(nextVal)
        output.push(temp)

        if temp_changed == size:
            return output 

        temp = None
        while not output.is_empty():
            nextVal = output.pop()
            if temp is None:
                temp = nextVal
            elif temp > nextVal:
                input.push(temp)
                temp = nextVal
            else:
                input.push(nextVal)
        
        input.push(temp)


sort_stack(stack).print_contents()
# repeat this process until the stack is sorted
  # keep track of how many element we touch
  # keep track of how many times temp is changed
  # repeat until the input stack is empty and temp is empty
  # take the top of the input stack and assign it to a temp var
  # compare the next value in our input stack with our temp, whichever is 
    # greater, we move to the other stack, and we assign the other value to temp
    

  # repeat until the output stack is empty and temp is empty
  # take the top of the output stack and assign it to a temp var
  # compare the next value in our input stack with our temp, whichever is 
    # smaller, we move to the other stack, and we assign the other value to temp
  
  