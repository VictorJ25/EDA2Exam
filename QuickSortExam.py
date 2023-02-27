def quicksort(data):

    if len(data)<1:
        return data

    pivot=data[len(data)//2].time

    minordata=[ item for item in data if item.time < pivot]
    equaldata= [item for item in data if item.time == pivot]
    greaterdata=[item for item in data if item.time > pivot]

    return quicksort(minordata) + equaldata + quicksort(greaterdata)