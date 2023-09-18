class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_counts = {}
        repeated_sequences = set()
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            
            if sequence in sequence_counts:
                repeated_sequences.add(sequence)
            else:
                sequence_counts[sequence] = 1
        
        return list(repeated_sequences)