def plusOne(self, digits: List[int]) -> List[int]:
    strd = ""
    intd = []
    for i in digits:
        i = str(i)
        strd+=i
    strd = int(strd)+1
    strd = str(strd)
        
    for i in strd:
        i = int(i)
        intd.append(i)

    return intd
