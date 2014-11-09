'''
test = [1, 2, 3, 4]
print test

test2 = [val for val in test]
    


test2.pop()
print test
print test2
'''




'''
i = 0
words = set()
for x in open(filename):
    if re.match(cklength, x):
        words.add(x.strip().upper())

print len(words)
'''





import string
import time


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


start = time.time()

#for alpha_letter in string.uppercase:
#    print alpha_letter
tiles_list = ['BLANK', 'BLANK', 'A', 'B', 'C', 'D']
blanks_tiles_lists = []
replace_blanks( tiles_list, blanks_tiles_lists )

#for blank_tile_index in [i for i, x in enumerate(test) if x == "BLANK"]:
   
'''
print ['A','B','C']
print sorted(['B','A','C'])
print cmp(['A','B','C'], sorted(['B','A','C']))
'''
    
print 'it took %.9f seconds' % (time.time() - start)
