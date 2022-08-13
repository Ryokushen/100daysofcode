#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

for names in open('Input\\Names\\invited_names.txt', mode='r'):
    ndot = names.strip()
    with open('Input\\Letters\\starting_letter.txt', mode='r') as template1, open(f'Output\\ReadyToSend\\{ndot}.txt', 'w') as template2:
        for line in template1.readlines():
            template2.write(line.replace(f'[name]', ndot))



