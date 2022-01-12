list_ = [["NORTH", "SOUTH" ], ['SOUTH', 'NORTH'],['EAST', 'WEST'],['WEST', 'EAST'] ]
def dirReduc(arr):
    if len(arr) <=2:
        return arr if arr not in list_ else []

    for i in range(len(arr)-1):
        if arr[i:i+2] in list_:
            arr = dirReduc(arr[:i] + arr[i+2:])
    return arr