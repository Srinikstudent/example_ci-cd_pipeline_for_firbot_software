def func(x):
    m = x * x
    return m
n = func(5)


class maths():
    def add(x,y):
        add = x + y
        return add
    def sub(x,y):
        sub = x - y
        return sub




def locate_number(list1,querry):
    first_index = 0
    last_index = len(list1)-1
    while first_index <= last_index:
        mid_index = (first_index +last_index) //2
        mid_number = list1[mid_index]
        #print('low: ', first_index, 'high: ', last_index, 'mid:', mid_index, 'mid_number: ', mid_number)
        if mid_number == querry:
           return mid_index
        elif mid_number < querry:
            last_index = mid_index -1
        elif mid_number > querry:
            first_index = mid_index +1

    return 'number not in the list'

list1 = [10, 9, 7, 6, 5, 4, 3, 2, 1]
test1 = {'input': {'list1': list1, 'querry': 7}, 'output': 2}
output = locate_number(test1['input']['list1'],test1['input']['querry'])
if  output == test1['output']:
    print('docker_image_succesfully_running_on_host_server')
    print('example_for_firebot_software')
    

