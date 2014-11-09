class hand:
    beats = ""
    
    def beats():
        return self.beats
    


class rock(hand):
    beats = 'scissors'
    
class paper(hand):
    beats = 'rock'

class scissors(hand):
    beats = 'rock'



class game:
    def __init__(self):
        self.set_out_of()
        self.play()

    def set_out_of(self):
        
        try:
            self.out_of = int(raw_input('Best out of:'))
        except TypeError:
            self.out_of = 0
            
        while self.out_of % 2 == 0:
            print('Must be an odd number!')
            try:
                self.out_of = int(raw_input('Best out of:'))
            except TypeError:
                self.out_of = 0
    
    def play(self):
        
        while !self.
    



def main():

    game()
    
    #new_rock = getattr(sys.modules[__name__], 'rock')




if __name__ == '__main__':
    import sys

    main()