'''
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]
        self.minstack=[]
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        #if item to be added is greater than element in minstack, ignore
        
        if not self.minstack or self.minstack[-1]>=x:
            self.minstack.append(x)   
            
    def pop(self):
        """
        :rtype: None
        """
        #if element to be popped is in minstack,pop element out of minstack
        
        if self.items:
            if self.minstack and self.items.pop()==self.minstack[-1]:
                self.minstack.pop()  
                
    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
