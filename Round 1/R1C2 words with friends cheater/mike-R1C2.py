def get_word_output(word, tiles_list):
    letter_list = [letter for letter in tiles_list]
    word_output = ""
    word_output_list = []
    word_output_extras = []
    for letter in word:
        if letter in letter_list:
            word_output_list.append(letter)
            letter_list.pop( letter_list.index(letter) )
        else:
            word_output_list.append('BLANK')
            word_output_extras.append(letter)
            letter_list.pop( letter_list.index('BLANK') )
    
    word_output = ' '.join(word_output_list)
    if word_output_extras:
        word_output += ' (' + ') ('.join(word_output_extras) + ')'
    
    return word_output


def get_remainder_output(word, tiles_list):
    letter_list = [letter for letter in tiles_list]
    remainder_output = ""
    remainder_output_list = []
    for letter in word:
        if letter in letter_list:
            #remainder_output_list.append(letter)
            letter_list.pop( letter_list.index(letter) )
        else:
            #remainder_output_list.append('BLANK')
            letter_list.pop( letter_list.index('BLANK') )
    
    remainder_output = ' '.join(letter_list)
    
    return remainder_output
    

def get_word_points(word, tiles_list):
    point_dict = {'BLANK': 0, 'A': 1, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 3, 'I': 1, 'J': 10, 'K': 5, 'L': 2, 'M': 4, 'N': 2, 'O': 1, 'P': 4, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 5, 'W': 4, 'X': 8, 'Y': 3, 'Z': 10}    
    points = 0
    letter_list = [letter for letter in tiles_list]
    for letter in word:
        if letter in letter_list:
            letter_list.pop( letter_list.index(letter) )
            points += point_dict.get(letter)
    if len(word) == 7:
        points += 35
    return points


def replace_blanks( tiles_list, blanks_tiles_lists ):
    if 'BLANK' in tiles_list:
        tiles_list_this = [val for val in tiles_list]
        tiles_list_this.pop( tiles_list_this.index('BLANK') )
        for alpha_letter in string.uppercase:
            tiles_list_replacement = [val for val in tiles_list_this]
            tiles_list_replacement.append( alpha_letter )
            replace_blanks( tiles_list_replacement, blanks_tiles_lists )
            
            if 'BLANK' not in tiles_list_replacement:
                add_to_list = True
                tiles_list_replacement = sorted(tiles_list_replacement)
                for blanks_tiles_list in blanks_tiles_lists:
                    if cmp( blanks_tiles_list, tiles_list_replacement ) == 0:
                        add_to_list = False
                if add_to_list:
                    blanks_tiles_lists.append( tiles_list_replacement )


def build_words( remaining_letters, word, all_words, dictionary_words, length_limit=0, longest_word=0 ):
    # break out of recursion if a word the size of length_limit has been found
    # Does a pretty good job of (sometimes) reducing processing, particularly when there are BLANKs.
    if length_limit > 0 and longest_word >= length_limit:
        return longest_word
    
    if remaining_letters:
        remaining_letters_iter = [val for val in remaining_letters]
        for letter in remaining_letters_iter:
            
            new_word = word + letter
            
            if(new_word not in all_words and new_word in dictionary_words):
                if(len(new_word) > longest_word):
                    longest_word = len(new_word)
                all_words.append(new_word)
            
            remaining_letters_new = [val for val in remaining_letters_iter]
            remaining_letters_new.pop( remaining_letters_iter.index(letter) )
            longest_word = build_words( remaining_letters_new, new_word, all_words, dictionary_words, length_limit, longest_word )
            
    return longest_word
    

def main():
    # get dictionary and build a set of only words with 7 or less characters
    regex_limit_length = re.compile('.{0,7}(\n)?$', re.I)
    dictionary_file = "/usr/share/dict/words"
    dictionary_words = set(word.strip().upper() for word in open(dictionary_file) if re.match(regex_limit_length, word))
    
    
    # get input tiles
    all_words = []
    tiles = raw_input('Please enter your tiles:')
    tiles_list = tiles.upper().split(' ')
    number_of_tiles = len(tiles_list)
    
    
    # build a list of all valid words from input tiles
    if 'BLANK' in tiles_list:
        blanks_tiles_lists = []
        replace_blanks( tiles_list, blanks_tiles_lists )
        for blanks_tiles_list in blanks_tiles_lists:
            longest_word = build_words( blanks_tiles_list, "", all_words, dictionary_words, number_of_tiles )
            if longest_word >= number_of_tiles:
                break;
    else:
        build_words( tiles_list, "", all_words, dictionary_words, number_of_tiles )
    
    
    # figure out which word has the highest most point value, and print output
    best_word_so_far = ""
    best_points_so_far = 0
    for word in all_words:
        points = get_word_points(word, tiles_list)
        if (points > best_points_so_far) or (points == best_points_so_far and len(word) > len(best_word_so_far)):
            best_word_so_far = word
            best_points_so_far = points
            
    output_word = get_word_output(best_word_so_far, tiles_list)
    output_points = best_points_so_far
    output_remainder = get_remainder_output(best_word_so_far, tiles_list)

    print output_word
    print output_points
    print output_remainder
    

if __name__ == '__main__':
    import string
    import re
        
    main()
