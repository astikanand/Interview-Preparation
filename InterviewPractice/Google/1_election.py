import heapq

class Candidate:
    def __init__(self, candidate_id, vote_count):
        self.candidate_id = candidate_id
        self.vote_count = vote_count

    def __lt__(self, other):
        return self.vote_count < other.vote_count


class Election:
    def __init__(self):
        self.candidates = {}
    
    def vote_candidate(self, candidate_id):
        self.candidates[candidate_id] = self.candidates.get(candidate_id, 0) + 1
    
    def get_top_k_candidates(self, k):
        candidate_heap = []
        for candidate_, votes in self.candidates.items():
            heapq.heappush(candidate_heap, Candidate(candidate_, votes))
        
        top_k_candidates = heapq.nlargest(k, candidate_heap)
        for candidate_ in top_k_candidates:
            print("Candidate ID: {} Vote Count: {}".format(candidate_.candidate_id, candidate_.vote_count))
        


print("Election Starts . . . . .")
election = Election()
election.vote_candidate("astik")
election.vote_candidate("preety")
election.vote_candidate("vasram")
election.vote_candidate("manpal")
election.vote_candidate("preety")
election.vote_candidate("vasram")
election.vote_candidate("preety")
print("\nTop 2 Candidate at this point:")
election.get_top_k_candidates(2)
election.vote_candidate("preety")
election.vote_candidate("vasram")
election.vote_candidate("preety")
election.vote_candidate("vasram")
election.vote_candidate("vasram")
election.vote_candidate("vasram")
print("\nTop 2 Candidate Final:")
election.get_top_k_candidates(2)