class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#"
            result += word

        return result

        # [[hello], [world]]
        # result "5#hello5#world"
        # decode: "hello", "world"


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            result.append(s[i:j])
            i = j
        
        return result
            

    # "5#hello5#world" 
    #  ij

    # "5#hello5#world" 
    #    i    j

    # "5#hello5#world" 
    #         i     j

    # "5#hello5#world" 
    #           i    j