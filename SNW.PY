import random

def check_win(computer, player):
  """
  Checks if the computer or the player has won the game.

  Args:
    computer: The computer's choice.
    player: The player's choice.

  Returns:
    1 if the computer wins, 2 if the player wins, and 0 if there is a tie.
  """

  if computer == 0:
    if player == 1:
      return 1
    elif player == 2:
      return 2
    else:
      return 0
  elif computer == 1:
    if player == 0:
      return 2
    elif player == 2:
      return 1
    else:
      return 0
  else:
    if player == 0:
      return 2
    elif player == 1:
      return 1
    else:
      return 0

def play_game():
  """
  Plays one game of Snake Water Gun.

  Returns:
    1 if the computer wins, 2 if the player wins, and 0 if there is a tie.
  """

  computer = random.randint(0, 2)
  player = input("Enter S for snake, W for water, or G for gun: ").lower()

  return check_win(computer, player)

def main():
  """
  Plays multiple games of Snake Water Gun until the user quits.
  """

  while True:
    result = play_game()

    if result == 1:
      print("Computer wins!")
    elif result == 2:
      print("Player wins!")
    else:
      print("Tie!")

    play_again = input("Play again? (Y/N): ").lower()
    if play_again != "y":
      break

if __name__ == "__main__":
  main()