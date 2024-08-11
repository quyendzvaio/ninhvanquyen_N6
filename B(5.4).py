my_dict = {
    'n':1500,
    'm':2,
    'CLUSTERS':3,
    'ITER':10000,
    'METHOD':'FCM',
    'MEASURE':'EUCLIDEAN',
    'YEARS':51
}

def main() :
    print(my_dict)

    GT = my_dict['MEASURE']
    my_dict['MANHATAN'] = GT
    del my_dict['MEASURE']

    print(my_dict['METHOD'])

    my_dict['LOSS FUNCTION'] = 'NORM_2'
    print(my_dict)

    del my_dict['YEARS']

    S = str(input('nhap vao sau S: '))
    print(S in my_dict.keys())
    my_set = set()
    list = []
    for value in my_dict.values() :
        my_set.add(value)
        list.append(value)
    print(my_set)
    print(list)

main()
