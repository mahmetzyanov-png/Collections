def main( ):
    #digits = [1, 2, 3, 3, 4]
    #digits = [1, 2, 3, 3, 4, 3]
    #digits = [1, 2, 3, 3, 8, 4] 
    #digits = [1, 2, 3, "3", 4]
    digits = ['1', '2', '3', '4', '5','6']
    letters = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L'] 
    letters_len = len(letters) 
    letters.extend(digits) 
    digits.clear()
    digits.extend(letters[:letters_len])
    del letters[:letters_len]
    print('digits: ',  digits  )
    print(f'letters:  { letters }' )

main( )