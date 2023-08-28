class MyStack {
    Queue<Integer> q;
    public MyStack() 
    {
        q=new LinkedList<Integer>();
    }
    public void push(int x) 
    {
        q.add(x);
    }
    public int pop() 
    {
        int size=q.size();
        for(int i=1;i<=size-1;i++)
        {
            q.add(q.poll());
        }
        return q.poll();
    }
    public int top() 
    {
        int size=q.size();
        for(int i=1;i<=size-1;i++)
        {
            q.add(q.poll());
        }
        int tp=q.poll();
        q.add(tp);
        return tp;
    }
    public boolean empty() 
    {
        if (q.size()==0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
