class WordleGame:
  def __init__(self):
    self.guess = ''
    self.target = ''

    
def set_target(self, target):
  if len(target) != 5:
    raise ValueError("Target must be 5 letters")
  self.target = target

def set_guess(self, guess):
  if len(guess) != 5:
    raise ValueError("Guess must be 5 letters")
  self.guess = guess
  
  def check_guess(self):
    result = ""
    for i in range(5):
      if self.target[i] == self.guess[i]:
        result += "2"  
      elif self.target.find(self.guess[i]) != -1:
        result += "1"
      else:
        result += "0"
    return result
  
  def play(self):
    while self.target != self.guess:
      self.guess = input("Enter your guess: ")
      result = self.check_guess()
      print(result)
      if result == "22222":
        print("You win!")
        break
      elif result == "00000":
        print("You lose!")
        break
      else:
        print("Keep trying!")
        
        game = WordleGame()
        game.set_target("hello")
        game.set_guess("hello")
        game.play()
        print(game.target)
        print(game.guess)
        print(game.check_guess())
        print(game.play())
        print(game.target)
        print(game.guess)
        
        

                          


