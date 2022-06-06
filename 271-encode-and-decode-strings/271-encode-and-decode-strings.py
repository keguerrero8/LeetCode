class Codec:

    def encode(self, strs):
        if strs == [""]:
            return ""
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        return "".join(encoded)
        

    def decode(self, s):
        if s == "":
            return [""]
        decoded = []
        i = 0
        while i < len(s):
            startLength = i 
            while s[i] != "#":
                i += 1
            endLength = i
            length = int(s[startLength:endLength]) 
            start = i + 1 
            end = length + start 
            decoded.append(s[start:end]) 
            i = end
        return decoded
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

#["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
#"5#63/Rc1h13#BmI3FS~J9#vmk"