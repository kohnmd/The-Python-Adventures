def build_words( remaining_tiles, word, all_words, first ):
    
    if remaining_tiles:
        for i,tile in enumerate(remaining_tiles):
        
            if(first == 1):
                print remaining_tiles
        
            new_word = word + tile
            
            if(new_word not in all_words):
                all_words.append(new_word)
                #print(new_word)
            
            remaining_tiles.pop(i)
            build_words( remaining_tiles, new_word, all_words, 0 )
            
    return
            
        
            
    




def main():
    
    points = {'BLANK': 0, 'A': 1, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 3, 'I': 1, 'J': 10, 'K': 5, 'L': 2, 'M': 4, 'N': 2, 'O': 1, 'P': 4, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 5, 'W': 4, 'X': 8, 'Y': 3, 'Z': 10}
    
    #tiles = raw_input('Please enter your tiles:')
    tiles = 'A B C'
    tiles_list = tiles.upper().split(' ')
    
    all_words = []
    build_words( tiles_list, "", all_words, 1 )
    #print all_words
    

if __name__ == '__main__':
    print '---------------------------------------------------------------------------------------------'
    main()
