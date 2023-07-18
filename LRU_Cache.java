class LRUCache {
    class Node
    {
        Node prev,next;
        int key,value;
        Node(int k,int v)
        {
            key=k;
            value=v;
        }
    }
    Node head= new Node(0,0);
    Node tail= new Node(0,0);
    Map<Integer,Node> m=new HashMap<Integer,Node>();
    int size;
    public LRUCache(int capacity) {
        size=capacity;
        head.next=tail;
        tail.prev=head;
    }
    public int get(int key) {
        if(m.containsKey(key))
        {
            Node node=m.get(key);
            remove(node);
            insert(node);
            return node.value;
        }
        else
        {
            return -1;
        }
    }
    public void put(int key, int value) {
        if(m.containsKey(key))
        {
            remove(m.get(key));
        }   
        if(m.size()==size)
        {
            remove(tail.prev);
        }
        insert(new Node(key,value));
    }
    private void remove(Node node)
    {
        m.remove(node.key);
        node.prev.next=node.next;
        node.next.prev=node.prev;
    }
    private void insert(Node node)
    {
        m.put(node.key,node);
        Node headnxt= head.next;
        head.next=node;
        node.prev=head;
        node.next=headnxt;
        headnxt.prev=node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
