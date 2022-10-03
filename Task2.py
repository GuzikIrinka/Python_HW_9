my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(I ='am', he='is', she='is')
biggest_dict(second_one='everything will work out', third_one='we will survive', fourth_one='peace')

print(my_dict)
        
