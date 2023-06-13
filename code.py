L = int(input()) # take the L input
PicNum= int(input()) # take the number of pic we will review
for i in range(PicNum):
    String = input() # take the pic dimensions as "x y" 
    String2 = list(String.split(" ")) #spilt them 
    String3 = [] 
    for j in String2:
        j = int(j)
        String3.append(j) # turn them into sperate ints in a list
    if String3[0] < L or String3[1]< L : 
        print("UPLOAD ANOTHER") # apply required operations
        continue    
    if String3[0] == String3[1] :
        print("ACCEPTED")
        continue
    else:
        print("CROP IT")
        continue # we used continue so we can re iterate over the next pic and scan it for the specific requirements.
    
