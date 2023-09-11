class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> sizeToGroup = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < groupSizes.length; i++) 
        {
            int size = groupSizes[i];
            sizeToGroup.putIfAbsent(size, new ArrayList<>());
            List<Integer> group = sizeToGroup.get(size);
            group.add(i);
            
            // map.computeIfAbsent(groupSizes[i], k -> new ArrayList()).add(i);

            if (group.size() == size) 
            {
                res.add(group);
                sizeToGroup.put(size, new ArrayList<>());

                // sizeToGroup.remove(size);
            }
        }
        
        return res;
    }
}