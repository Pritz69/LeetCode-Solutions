class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<numCourses;i++)
        {
            adj.add(new ArrayList<>());
        }
        int n=prerequisites.length;
        for(int i=0;i<n;i++)
        {
            adj.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
        int indegree[]=new int[numCourses];
        for(int i=0;i<numCourses;i++)
        {
            for(int it:adj.get(i))
            {
                indegree[it]++;
            }
        }
        Queue<Integer>q=new LinkedList<Integer>();
        for(int i=0;i<numCourses;i++)
        {
            if(indegree[i]==0)
            {
                q.add(i);
            }
        }
        int c=0;
        while (!q.isEmpty())
        {
            int node=q.peek();
            q.remove();
            c +=1;
            for ( int it:adj.get(node))
            {
                indegree[it]--;
                if (indegree[it]==0)
                {
                    q.add(it);
                }
            }
        }
        if (c==numCourses)
        {
            return true;
        }
        return false;
    }
}
