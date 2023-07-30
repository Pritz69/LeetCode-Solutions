class MinStack {
    Stack<Long> s= new Stack<>();
    Long m;
    public MinStack() {
        m=Long.MAX_VALUE;
    }
    
    public void push(int value) {
        Long val=Long.valueOf(value);
        if(s.isEmpty())
        {
            m=val;
            s.push(val);
        }
        else
        {
            if (val < m)
            {
                s.push(2*val - m);
                m = val;
            }
            else
            {
                s.push(val);
            }
        }
    }
    
    public void pop() {
        if (s.isEmpty())
        {
            return;
        }
        Long v=s.peek();
        if (v<m)
        {
            m=(2*m-v);
        }
        s.pop();
    }
    
    public int top() {
        Long v=s.peek();
        if (v<m)
        {
            return m.intValue();
        }
        else
        {
            return v.intValue();
        }
    }
    
    public int getMin() {
        return m.intValue();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
