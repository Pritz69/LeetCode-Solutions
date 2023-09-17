// CODING DECODED
class Solution {
    public int shortestPathLength(int[][] graph) {
        if(graph.length==1)
			return 0;
		int finalState = (1 << graph.length) - 1;
		Queue<int []> qu = new LinkedList<>();
		//Adding all nodes initially because we can start anywhere.
		for(int i=0; i<graph.length; i++) 
        {
			qu.add(new int [] {i, 1 << i});

		}
		int [][] visitedMap = new int [graph.length][finalState+1];
		int shortestPath = 0;
		while(!qu.isEmpty()){
			int size = qu.size();
			shortestPath++;
			for(int i=0; i<size; i++)
            {
				int [] head = qu.poll();
				int nodeId = head[0];
				int visitedNodeBitState = head[1];
				for(int neighbor : graph[nodeId])
                {
					int newVisitedNodeBitState = visitedNodeBitState | (1 << neighbor);
					if(visitedMap[neighbor][newVisitedNodeBitState] == 1)             
                    {
                        continue;
                    }  
					visitedMap[neighbor][newVisitedNodeBitState] = 1;    
                    if(newVisitedNodeBitState==finalState)
					{
                        return shortestPath;
                    }
					qu.add(new int [] {neighbor, newVisitedNodeBitState});
				}
			}
		}
		return -1;
    }
}
