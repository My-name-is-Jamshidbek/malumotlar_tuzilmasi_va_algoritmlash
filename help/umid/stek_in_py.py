class Stack:
    def __init__(self):
        self.stack = []
        self.max = None
        self.max_ind =None

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            n=0
            for value in self.stack:
                if value > self.max:
                    self.max = value
                    self.max_ind = n
                n+=1
        return removed

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1:
            self.max = item
            self.max_ind = 0
        if item > self.max:
            self.max_ind = len(self.stack)-1

    def get_max(self):
        return self.max

    def get_max_ind(self):
        return self.max_ind








s_u = int(input('Stek uzunligini kiriting>>'))
st = Stack()
for i in range(s_u):
    n = int(input(f"{i+1}-element>>"))
    st.push(n)

m = st.pop()
st1 = Stack()
st1.push(m)

for i in range(s_u-1):
    n = st.pop()
    if n>m:m = n
    st1.push(n)

st = Stack()

for i in range(s_u):
    n = st1.pop()
    st.push(n)
    print(n)
    if n==m:
        st.push(0)
        print(0)





