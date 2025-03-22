A = int(input())
for _ in range (A):
    q = input()

    sore = 0      
    current_sore = 0     

    for i in q:
        if i == 'O':     
            current_sore += 1  
            sore += current_sore 
        else:             
            current_sore = 0   

    print(sore)   
