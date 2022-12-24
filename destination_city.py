class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_list = [path[0] for path in paths]
        destination_list = [path[1] for path in paths]
        for destination in destination_list:
            if destination not in source_list:
                return destination
        
