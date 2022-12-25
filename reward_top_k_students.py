class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        mp = {}
        for sentence, id in zip(report, student_id): 
            point = 0 
            for word in sentence.split(): 
                if word in positive_feedback: point += 3
                elif word in negative_feedback: point -= 1
            mp[id] = point 
        return sorted(mp, key=lambda x: (-mp[x], x))[:k]
