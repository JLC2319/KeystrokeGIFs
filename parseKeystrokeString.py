


def parseSequence(string:str):

    def parseCombo(string: str):
        comboArray = []
        splitup = string.split('+')
        for n,key in enumerate(splitup):
            arr = splitup[:n+1]; comboArray.append(arr)

        return comboArray

    kestrokeArray = []

    splitup = string.split(';')
    
    for segment in splitup:
        if '+' in segment:
            kestrokeArray.extend(parseCombo(segment))

        else:
            arr = [segment]
            kestrokeArray.append(arr); kestrokeArray.append([''])

    return kestrokeArray

if __name__ == "__main__":
    print(parseSequence('alt;h;m;m'))
