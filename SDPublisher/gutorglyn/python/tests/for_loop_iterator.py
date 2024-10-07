import re 

my_string = "rub rob rub rab rob"

for hit in re.finditer(my_string, 'rob'):
        
    start_pos = hit.start()

val_list = [m.start() for m in re.finditer('test', 'test test test test')]
print type(val_list)

