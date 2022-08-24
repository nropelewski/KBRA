class Solution:
    def romanToInt(self, s: str) -> int:
        # Converts a Roman Numeral string into its integer representation
        total = 0
        lastRNum = ""
        s = s.upper()
        
        # iterate over each character in s starting at i=0
        for i,val in enumerate(s):
            if val == "I":
                total += 1
            elif val == "V":
                total += 5
                # if the last Roman Num was 1, subtract (1*2) because it was
                #   wrongfully added in the last iteration
                if lastRNum == "I":
                    total -= 2
            elif val == "X":
                total += 10
                if lastRNum == "I":
                    total -= 2
            elif val == "L":
                total += 50
                if lastRNum == "X":
                    total -= 20
            elif val == "C":
                total += 100
                if lastRNum == "X":
                    total -= 20
            elif val == "D":
                total += 500
                if lastRNum == "C":
                    total -= 200
            elif val == "M":
                total += 1000
                if lastRNum == "C":
                    total -= 200
            # set the lastRNum variable for the next iteration
            lastRNum = val
            
        return total
