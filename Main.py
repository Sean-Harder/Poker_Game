import tkinter as tk
import time
import random
from tkinter import font
import os

HEIGHT = 500
WIDTH = 850


def poker_script():
  global all_cards
  all_cards = [
  1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
  
  def poker_cards():
    #--Players Cards--
    global player_first_card
    player_first_card = random.choice(all_cards)
    all_cards.remove(player_first_card)
    
    global player_second_card
    player_second_card = random.choice(all_cards)
    all_cards.remove(player_second_card)
    
    global player_third_card
    player_third_card = random.choice(all_cards)
    all_cards.remove(player_third_card)

    global player_fourth_card
    player_fourth_card = random.choice(all_cards)
    all_cards.remove(player_fourth_card)

    global player_fifth_card
    player_fifth_card = random.choice(all_cards)
    all_cards.remove(player_fifth_card)

    #--Player Total--
    global players_total
    players_total = player_first_card + player_second_card

    #--Computer Cards--
    global computers_first_card
    computers_first_card = random.choice(all_cards)
    all_cards.remove(computers_first_card)

    global computers_second_card
    computers_second_card = random.choice(all_cards)
    all_cards.remove(computers_second_card)

    global computers_third_card
    computers_third_card = random.choice(all_cards)
    all_cards.remove(computers_third_card)

    global computers_fourth_card
    computers_fourth_card = random.choice(all_cards)
    all_cards.remove(computers_fourth_card)

    global computers_fifth_card
    computers_fifth_card = random.choice(all_cards)
    all_cards.remove(computers_fifth_card)

    #--Computer Total--
    global computers_total
    computers_total = computers_first_card + computers_second_card

    #prints all of the cards to the console
    print("Debug Purposes")
    print("Player's Cards: {}, {}, {}, {}, {}".format(player_first_card, player_second_card, player_third_card, player_fourth_card, player_fifth_card))

    print("Computer's Cards: {}, {}, {}, {}, {}".format(computers_first_card, computers_second_card, computers_third_card, computers_fourth_card, computers_fifth_card))

  poker_cards()
  
import Players_Balance
#to use "Balance" from players_balance use Player_Balance.Balance


global player_won
def player_won():
  if Last_Bet_Count == 0:
    Bet = Players_Balance.Last_Bet
    global Winnings
    Winnings = Bet * 2
    Balance = Players_Balance.Balance + Winnings
    print(Balance)
    with open('Players_Balance.py', 'w') as f:
      f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Players_Balance.Last_Bet))
  else:
    Bet = Bet_Entry.get()
    Winnings = Bet * 2
    Balance = Players_Balance.Balance + Winnings
    with open('Players_Balance.py', 'w') as f:
      f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Bet_Entry.get()))

global player_lost
def player_lost():
  global Bet
  if Last_Bet_Count == 0:
    Balance = Players_Balance.Balance - Bet
    with open('Players_Balance.py', "w") as f:
      f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Players_Balance.Last_Bet))
  else:
    Balance = Players_Balance.Balance - Bet
    with open('Players_Balance.py', "w") as f:
      f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Bet_Entry.get()))

global player_tied
def player_tied():
  if Last_Bet_Count == 0:
    Balance = Players_Balance.Balance
    with open('Players_Balance.py', "w") as f:
      f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Players_Balance.Last_Bet))
  else:
      Balance = Players_Balance.Balance
      with open('Players_Balance.py', "w") as f:
        f.write("Balance = {}".format(Balance)+"\nLast_Bet = {}".format(Bet_Entry.get()))



    
def deal_cards_func():

  def Check_Empty():
    global Bet
    if Bet_Entry.get() and int(Bet_Entry.get()) < Players_Balance.Balance or Last_Bet_Count == 0:

      if Last_Bet_Count == 0:
        Bet = Players_Balance.Last_Bet
        print(Bet)

      else:
        Bet = Bet_Entry.get()
        with open('Players_Balance.py', 'w') as f:
          f.write("Balance = 10000\nLast_Bet = {}".format(Bet_Entry.get()))
        print(Bet)


      root_main_page.destroy()
      poker_script()
      global root_deal_cards
      root_deal_cards=tk.Tk()  
      
      game_canvas = tk.Canvas(root_deal_cards, height=HEIGHT, width=WIDTH)
      game_canvas.pack()
      
      game_frame = tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=11, highlightbackground="black")
      game_frame.place(relheight=1, relwidth=1)
      

      #--Frame for Players Cards--
      global players_cards_frame
      players_cards_frame = tk.Frame(game_frame, bg="#0C5B2E", highlightthickness=2, highlightbackground="red")
      players_cards_frame.place(relheight=.3, relwidth=.35, relx=.35, rely=.62)
          
      #--Players Cards Being Placed
      global players_card_one
      players_card_one = tk.Label(players_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
      players_card_one.place(relheight=.8, relwidth=.3, relx=.22, rely=.09)

      global players_card_two
      players_card_two = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
      players_card_two.place(relheight=.8, relwidth=.3, relx=.41, rely=.14)
            
      #Giving the players cards proper numbers
      players_card_one_number =tk.Label(players_card_one, bg="#D8D8D8", text=player_first_card, fg="black",font=("Times New Roman", 10))
      players_card_one_number.place(relheight=.5, relwidth=.65)
            
      global players_card_two_number
      players_card_two_number = tk.Label(players_card_two, bg="#D8D8D8", text=player_second_card, fg="black",font=("Times New Roman", 10))
      players_card_two_number.place(relheight=.5, relwidth=.66)
            
      #--Frame for Computers Cards--
      global computers_cards_frame
      computers_cards_frame = tk.Frame(game_frame, bg="#0C5B2E", highlightthickness=2, highlightbackground="red")
      computers_cards_frame.place(relheight=.3, relwidth=.35, relx=.35, rely=.0)
          
      #Placing the Computers Cards
      global computers_card_one
      computers_card_one = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
      computers_card_one.place(relheight=.8, relwidth=.3, relx=.22, rely=.09)

      global computers_card_two
      computers_card_two = tk.Label(computers_cards_frame, highlightthickness=3, bg="#0C255B", highlightbackground="#919D2A")
      computers_card_two.place(relheight=.8, relwidth=.3, relx=.4, rely=.14)
            
      #Giving the computers Cards Numbers
      computers_card_one_number =tk.Label(computers_card_one, bg="#D8D8D8", text=computers_first_card, fg="black",font=("Times New Roman", 10))
      computers_card_one_number.place(relheight=.5, relwidth=.6,)
            

      #places the players value
      players_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Player's Total: {}".format(players_total)), font=("Times New Roman", 13))
      players_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.56)


      #Shows the total of computers total
      computer_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: "+ str(computers_first_card)), font=("Times New Roman", 13))
      computer_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

      #End of framing the cards

      #Possible Ending Game Texts
      Player_Busted_Text = "You've Busted With {}, The dealer had {}!".format(players_total,computers_total)
      Computer_Busted_Text = "You Won with {}, The dealer had {}!".format(players_total, computers_total)
      Tie_Game_Text = "Tie Game! You Both Had {},{}".format(players_total,computers_total)
      
      def Quit_Game_Func():
        root_deal_cards.destroy()

      def Restart_Game_Func():
        root_deal_cards.destroy()
        main_page_func()
      
      #checks to end the game before moving on to hit or stand  
      def player_busted_it():
        global player_total
        if players_total >= 22:
          players_card_total.destroy()
          computer_card_total.destroy()

          #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
          Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
          Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

          #This is the frame where all the text is going to be place on who lost, how much, and what both players had
          End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
          End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

          End_Game_Top_Text =tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
          End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

          Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text=Player_Busted_Text, font=("Arial, 13"))
          Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

          Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="(Your new balance is 1000temp text)", font=("Arial, 13"))
          Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

          Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
          Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

          Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
          Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)
          print(Player_Busted_Text)
        global players_card_count
        players_card_count = 2
      player_busted_it()

      #The hit function for when you click the Hit_Button
      def Hit_Button_Func():
        global players_total
        global players_card_count
        
        if players_card_count == 2:

          #Add the third card to the players_total
          players_total = players_total + player_third_card

          #Updates the players total, on the screen
          players_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Player's Total: {}".format(players_total)), font=("Times New Roman", 13))
          players_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.56)
          
          Player_Busted_Text = "You've Busted With {}, The dealer had {}!".format(players_total, computers_total)

          if players_total >= 22:
            players_card_total.destroy()
            computer_card_total.destroy()

            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text =tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text=Player_Busted_Text, font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - int(Bet)), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)


          #Placing third card
          global players_card_three
          players_card_three = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_three.place(relheight=.8, relwidth=.3, relx=.56, rely=.14)

          #placing third card number
          global players_card_three_number
          players_card_three_number = tk.Label(players_card_three, bg="#D8D8D8", text=player_third_card, fg="black",font=("Times New Roman", 10))
          players_card_three_number.place(relheight=.5, relwidth=.66)

        if players_card_count == 3:
          #Add the third card to the players_total
          players_total = players_total + player_fourth_card

          #Updates the players total, on the screen
          players_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Player's Total: {}".format(players_total)), font=("Times New Roman", 13))
          players_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.56)

          Player_Busted_Text = "You've Busted With {}, The dealer had {}!".format(players_total,computers_total)

          if players_total >= 22:
            players_card_total.destroy()
            computer_card_total.destroy()

            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text =tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text=Player_Busted_Text, font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - int(Bet)), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

          #Placing third card
          global players_card_four
          players_card_four = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_four.place(relheight=.8, relwidth=.3, relx=.70, rely=.14)

          #placing third card number
          global players_card_four_number
          players_card_fourth_number = tk.Label(players_card_four, bg="#D8D8D8", text=player_fourth_card, fg="black",font=("Times New Roman", 10))
          players_card_fourth_number.place(relheight=.5, relwidth=.66)

        if players_card_count == 4:
          global players_card_one
          global players_card_two
            
          players_total = players_total + player_fifth_card

          players_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Player's Total: {}".format(players_total)), font=("Times New Roman", 13))
          players_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.56)

          players_card_one.destroy()
          players_card_two.destroy()
          players_card_three.destroy()
          players_card_four.destroy()

          Player_Busted_Text = "You've Busted With {}, The dealer had {}!".format(players_total,computers_total)

          if players_total >= 22:
            players_card_total.destroy()
            computer_card_total.destroy()


            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text=Player_Busted_Text, font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - int(Bet)), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

          #Replacing the players 1st Card
          players_card_one = tk.Label(players_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
          players_card_one.place(relheight=.8, relwidth=.3, relx=.05, rely=.09)

          players_card_one_number =tk.Label(players_card_one, bg="#D8D8D8", text=player_first_card, fg="black",font=("Times New Roman", 10))
          players_card_one_number.place(relheight=.5, relwidth=.65)
                
          #Replacing the Players 2nd Card
          players_card_two = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_two.place(relheight=.8, relwidth=.3, relx=.2, rely=.14)

          players_card_two_number = tk.Label(players_card_two, bg="#D8D8D8", text=player_second_card, fg="black",font=("Times New Roman", 10))
          players_card_two_number.place(relheight=.5, relwidth=.66)

          #replacing the players 3rd Card
          players_card_three = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_three.place(relheight=.8, relwidth=.3, relx=.35, rely=.14)

          players_card_three_number = tk.Label(players_card_three, bg="#D8D8D8", text=player_third_card, fg="black",font=("Times New Roman", 10))
          players_card_three_number.place(relheight=.5, relwidth=.66)

          #replacing the players 4th Card
          players_card_four = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_four.place(relheight=.8, relwidth=.3, relx=.50, rely=.14)

          players_card_fourth_number = tk.Label(players_card_four, bg="#D8D8D8", text=player_fourth_card, fg="black",font=("Times New Roman", 10))
          players_card_fourth_number.place(relheight=.5, relwidth=.66)

          #Adding the 5th card now that its orginized
          players_total = players_total + player_fifth_card

          players_card_five = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
          players_card_five.place(relheight=.8, relwidth=.3, relx=.65, rely=.14)

          #placing third card number
          players_card_five_number = tk.Label(players_card_five, bg="#D8D8D8", text=player_fifth_card, fg="black",font=("Times New Roman", 10))
          players_card_five_number.place(relheight=.5, relwidth=.66)

        print(players_card_count)
        players_card_count = players_card_count + 1
      
      def Stand_Button_Func():
        global computers_card_one
        global computers_card_two
        global computers_card_three
        global computers_card_four
        global computers_card_five
        global computers_total

        computers_card_two = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
        computers_card_two.place(relheight=.8, relwidth=.3, relx=.4, rely=.14)

        computer_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: {}".format(computers_total)), font=("Times New Roman", 13))
        computer_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

        computers_card_two_number =tk.Label(computers_card_two, bg="#D8D8D8", text=computers_second_card, fg="black",font=("Times New Roman", 10))
        computers_card_two_number.place(relheight=.5, relwidth=.6)

        #Gives a card to computer's hand if its total hand is less than 15
        if computers_total <= 15:
          computers_card_three = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
          computers_card_three.place(relheight=.8, relwidth=.3, relx=.55, rely=.14)

          computers_total = computers_total + computers_third_card

          computer_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: {}".format(computers_total)), font=("Times New Roman", 13))
          computer_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

          computers_card_three_number =tk.Label(computers_card_three, bg="#D8D8D8", text=computers_third_card, fg="black",font=("Times New Roman", 10))
          computers_card_three_number.place(relheight=.5, relwidth=.6)

          #Gives a card to computer's hand if its total hand is less than 15
          if computers_total <= 15:
            computers_card_four = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
            computers_card_four.place(relheight=.8, relwidth=.3, relx=.7, rely=.14)

            computers_total = computers_total + computers_fourth_card

            computer_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: {}".format(computers_total)), font=("Times New Roman", 13))
            computer_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

            computers_card_four_number =tk.Label(computers_card_four, bg="#D8D8D8", text=computers_fourth_card, fg="black",font=("Times New Roman", 10))
            computers_card_four_number.place(relheight=.5, relwidth=.6)

            if computers_total <= 15:
              computers_card_one.destroy()
              computers_card_two.destroy()
              computers_card_three.destroy()
              computers_card_four.destroy()
              
              computers_total = computers_total + computers_fifth_card

              computer_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: {}".format(computers_total)), font=("Times New Roman", 13))
              computer_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

              computers_card_one = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
              computers_card_one.place(relheight=.8, relwidth=.3, relx=.05, rely=.09)

              computers_card_one_number =tk.Label(computers_card_one, bg="#D8D8D8", text=computers_first_card, fg="black",font=("Times New Roman", 10))
              computers_card_one_number.place(relheight=.5, relwidth=.6,)

              computers_card_two = tk.Label(computers_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
              computers_card_two.place(relheight=.8, relwidth=.3, relx=.2, rely=.14)
                    
              computers_card_two_number =tk.Label(computers_card_two, bg="#D8D8D8", text=computers_second_card, fg="black",font=("Times New Roman", 10))
              computers_card_two_number.place(relheight=.5, relwidth=.6)

              computers_card_three = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
              computers_card_three.place(relheight=.8, relwidth=.3, relx=.35, rely=.14)

              computers_card_three_number =tk.Label(computers_card_three, bg="#D8D8D8", text=computers_third_card, fg="black",font=("Times New Roman", 10))
              computers_card_three_number.place(relheight=.5, relwidth=.6)
              
              computers_card_four = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
              computers_card_four.place(relheight=.8, relwidth=.3, relx=.50, rely=.14)

              computers_card_four_number =tk.Label(computers_card_four, bg="#D8D8D8", text=computers_fourth_card, fg="black",font=("Times New Roman", 10))
              computers_card_four_number.place(relheight=.5, relwidth=.6)
              
              computers_card_five = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
              computers_card_five.place(relheight=.8, relwidth=.3, relx=.65, rely=.14)

              computers_card_five_number =tk.Label(computers_card_five, bg="#D8D8D8", text=computers_fifth_card, fg="black",font=("Times New Roman", 10))
              computers_card_five_number.place(relheight=.5, relwidth=.6)

              if computers_total >= 22:
                player_won()
                #This is the code if the computer busts after getting the new cards
                print("Computer busted! Line 516")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer busted with {}".format(computers_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

              elif computers_total < players_total:
                player_won()
                print("Player Won! Line 553")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The player won with {}, the computer had {}.".format(players_total, computers_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="(Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

              elif computers_total > players_total:
                player_lost()
                print("Computer Won, Line 420")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer won with {},you had {}".format(computers_total, players_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - Bet), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)
            
              elif players_total == computers_total:
                player_tied()
                print("You and the dealer tied, money back line 503")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="You and the Dealer tied you both had {},{}.".format(computers_total, players_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

            else:
              if computers_total >= 22:
                player_won()
                #This is the code if the computer busts after getting the new cards
                print("Computer busted! Line 416")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer busted with {}".format(computers_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="(Your new balance is {}".format(Players_Balance.Balance), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

              elif computers_total < players_total:
                player_won()
                print("Player Won! Line 418")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The player won with {}, the computer had {}.".format(players_total, computers_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

              elif computers_total > players_total:
                player_lost()
                print("Computer Won, Line 420")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer won with {},you had {}".format(computers_total, players_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - Bet), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)
            
              elif players_total == computers_total:
                player_tied()
                print("You and the dealer tied, money back line 503")
                players_card_total.destroy()
                computer_card_total.destroy()


                #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
                Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
                Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

                #This is the frame where all the text is going to be place on who lost, how much, and what both players had
                End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
                End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

                End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
                End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

                Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="You and the Dealer tied you both had {},{}.".format(computers_total, players_total), font=("Arial, 13"))
                Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

                Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
                Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

                Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
                Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

                Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
                Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)


          
          #need to add ending game code if after the first give card if statment on line 386, the computers total is 15 or more
          elif computers_total > 15:
            print("End Game Code ran on Line 414")
            if computers_total >= 22:
              player_won()
              #This is the code if the computer busts after getting the new cards
              print("Computer busted! Line 416")
              players_card_total.destroy()
              computer_card_total.destroy()


              #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
              Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
              Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

              #This is the frame where all the text is going to be place on who lost, how much, and what both players had
              End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
              End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

              End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
              End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

              Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer busted with {}".format(computers_total), font=("Arial, 13"))
              Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

              Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
              Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

              Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
              Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

              Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
              Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

            elif computers_total < players_total:
              player_won()
              print("Player Won! Line 418")
              players_card_total.destroy()
              computer_card_total.destroy()


              #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
              Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
              Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

              #This is the frame where all the text is going to be place on who lost, how much, and what both players had
              End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
              End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

              End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
              End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

              Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The player won with {}, the computer had {}.".format(players_total, computers_total), font=("Arial, 13"))
              Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

              Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
              Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

              Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
              Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

              Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
              Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

            elif computers_total > players_total and computers_total < 22:
              player_lost()
              print("Computer Won, Line 420")
              players_card_total.destroy()
              computer_card_total.destroy()


              #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
              Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
              Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

              #This is the frame where all the text is going to be place on who lost, how much, and what both players had
              End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
              End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

              End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
              End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

              Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer won with {},you had {}".format(computers_total, players_total), font=("Arial, 13"))
              Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

              Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - Bet), font=("Arial, 13"))
              Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

              Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
              Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

              Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
              Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)
            
            elif players_total == computers_total:
              player_tied()
              print("You and the dealer tied, money back line 503")
              players_card_total.destroy()
              computer_card_total.destroy()


              #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
              Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
              Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

              #This is the frame where all the text is going to be place on who lost, how much, and what both players had
              End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
              End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

              End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
              End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

              Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="You and the Dealer tied you both had {},{}.".format(computers_total, players_total), font=("Arial, 13"))
              Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

              Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
              Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

              Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
              Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

              Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
              Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)
        
        else:
          print("End Game Code ran on Line 883")
          if computers_total >= 22:
            player_won()
            #This is the code if the computer busts after getting the new cards
            print("Computer busted! Line 887")
            players_card_total.destroy()
            computer_card_total.destroy()


            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer busted with {}".format(computers_total), font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

          elif computers_total < players_total:
            player_won()
            print("Player Won! Line 917")
            players_card_total.destroy()
            computer_card_total.destroy()


            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The player won with {}, the computer had {}.".format(players_total, computers_total), font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance + Winnings), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)

          elif computers_total > players_total:
            player_lost()
            print("Computer Won1 Line 429")
            players_card_total.destroy()
            computer_card_total.destroy()


            #This is a frame that is covering the hit and stand button so the game doesnt break after it ends
            Game_Options_Cover=tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=0)
            Game_Options_Cover.place(relheight=.077, relwidth=.35, relx=.35, rely=.905)

            #This is the frame where all the text is going to be place on who lost, how much, and what both players had
            End_Game_Notice_Frame = tk.Label(game_canvas, bg="grey", highlightthickness=3)
            End_Game_Notice_Frame.place(relheight=.305, relwidth=.8, relx=.1, rely=.31)

            End_Game_Top_Text = tk.Label(End_Game_Notice_Frame, bg="grey", text="Game Over!", font=("Arial, 20"))
            End_Game_Top_Text.place(relheight=.25, relwidth=.45, relx=.3, rely=0)

            Player_Busted_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="The computer won with {},you had {}".format(computers_total, players_total), font=("Arial, 13"))
            Player_Busted_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.23)

            Players_Balance_Updated_Label = tk.Label(End_Game_Notice_Frame, bg="grey", text="Your new balance is {}".format(Players_Balance.Balance - Bet), font=("Arial, 13"))
            Players_Balance_Updated_Label.place(relheight=.2, relwidth=.8, relx=.1, rely=.4)

            Game_End_Restart_Button = tk.Button(End_Game_Notice_Frame, bg="Green", text="Restart", command=Restart_Game_Func)
            Game_End_Restart_Button.place(relheight=.4, relwidth=.25, relx=.25, rely=.65)

            Game_End_Quit_Button = tk.Button(End_Game_Notice_Frame, bg="#8B0000", text="Quit", command=Quit_Game_Func)
            Game_End_Quit_Button.place(relheight=.4, relwidth=.25, relx=.5, rely=.65)



      #Framing and inserting the hit and stand button

      #Game Options Frame
      Game_Options_Frame = tk.Frame(game_frame, bg="grey")
      Game_Options_Frame.place(relheight=.08, relwidth=.35, relx=.35, rely=.92)

      #Framing The Hit Button
      Hit_Button = tk.Button(Game_Options_Frame, bg="Green", text="Hit", font="Arial, 15", command=Hit_Button_Func)
      Hit_Button.place(relheight=1, relwidth=.5, relx=0, rely=0)

      Stand_Button = tk.Button(Game_Options_Frame, bg="#8B0000", text="Stand", font="Arial, 15", command=Stand_Button_Func)
      Stand_Button.place(relheight=1, relwidth=.5, relx=.5, rely=0)

      root_deal_cards.mainloop()

    else:
      Hint_Frame = tk.Frame(frame_one, bg="grey")
      Hint_Frame.place(relheight=.1, relwidth=.767, relx=.163, rely=.54)
      
      Hint_Label = tk.Label(Hint_Frame, bg="grey", text="Enter a bet above ^ or click the preset Last Bet at the end.", font=("Arial, 12"))
      Hint_Label.place(relheight=.5, relwidth=.9, relx=0, rely=0)

      Hint_Label_Two = tk.Label(Hint_Frame, bg="grey", text="Make sure the bet is below your balance, which is {}".format(Players_Balance.Balance), font=("Arial, 12"))
      Hint_Label_Two.place(relheight=.5, relwidth=.9, relx=0, rely=.5)

      Arrow_Label = tk.Label(Hint_Frame, bg="grey", text="^", font=("Arial, 15"))
      Arrow_Label.place(relheight=1, relwidth=.1, relx=.9, rely=0)

  Check_Empty()

def main_page_func():
  global root_main_page
  root_main_page=tk.Tk()
  root_main_page.title(" ")

  main_canvas = tk.Canvas(root_main_page, bg="#000000", height=HEIGHT, width=WIDTH)
  main_canvas.pack()

  global frame_one
  frame_one = tk.Frame(main_canvas, bg="#0C5B2E", highlightthickness=10, highlightbackground="#272727")
  frame_one.place(relheight=.8, relwidth=.9, relx=.05, rely=.1)

  title_frame = tk.Frame(frame_one, bg="#0C5B2E")
  title_frame.place(relheight=.25, relwidth=.8, relx=.1, rely=.05)

  #Blackjack label for the mainpage
  label_one = tk.Label(title_frame, text="BLACKJACK", bg="#515151", fg="black", font=("Times New Roman", 40), highlightthickness=4, highlightbackground="black", bd=2)
  label_one.place(relheight=1, relwidth=1, relx=0, rely=0)

  #The frame for all of the betting buttons
  frame_bet = tk.Frame(frame_one, bg="grey", bd=0)
  frame_bet.place(relheight=.1, relwidth=.85, relx=.08, rely=.4)

  #The entry for where you type in your bet ammount
  global Bet_Entry
  Bet_Entry = tk.Entry(frame_bet, bg="grey", bd=0)
  Bet_Entry.place(relheight=1, relwidth=.8, relx=.097, rely=0)

  Bet_Label = tk.Label(frame_bet, bg="grey", text="Bet")
  Bet_Label.place(relheight=1, relwidth=.097, relx=0, rely=0)

  global Last_Bet_Count
  Last_Bet_Count = 1

  def Last_Bet_Func():
    global Last_Bet_Count
    if Last_Bet_Count == 1:

      global Last_Bet_Frame
      Last_Bet_Frame.destroy()

      Last_Bet_Frame = tk.Button(frame_bet, bg="Green", bd=0, highlightthickness=0, text=Players_Balance.Last_Bet, command=Last_Bet_Func)
      Last_Bet_Frame.place(relheight=1, relwidth=.1, relx=.9, rely=0)

      Last_Bet_Count = Last_Bet_Count - 1
      print("Ran 967 LBC = {}".format(Last_Bet_Count))
    
    elif Last_Bet_Count == 0:
      Last_Bet_Frame = tk.Button(frame_bet, bg="grey", bd=0, highlightthickness=0, text=Players_Balance.Last_Bet, command=Last_Bet_Func)
      Last_Bet_Frame.place(relheight=1, relwidth=.1, relx=.9, rely=0)
      Last_Bet_Count = Last_Bet_Count + 1
      print("Ran 977 LBC = {}".format(Last_Bet_Count))

  #A button for last bet
  global Last_Bet_Frame
  Last_Bet_Frame = tk.Button(frame_bet, bg="grey", bd=0, highlightthickness=0, text=Players_Balance.Last_Bet, command=Last_Bet_Func)
  Last_Bet_Frame.place(relheight=1, relwidth=.1, relx=.9, rely=0)

  #Frame to hold the to options
  frame_answer = tk.Frame(frame_one)
  frame_answer.place(relheight=.2, relwidth=.9, relx=.0525, rely=.7)

  #The deal button to start the game
  deal_cards_button = tk.Button(frame_answer, 
  text="Deal Cards",
  command =  deal_cards_func,
  font=("Times New Roman",14),
  bg="#515151",
  relief="flat",
  activebackground="#707070",
  highlightthickness=2,
  highlightbackground="Black")
  deal_cards_button.place(relheight=1, relwidth=.51, relx=0, rely=0)

  #The quit button to end the code
  quit_button = tk.Button(frame_answer,
  text="Quit",
  command=root_main_page.destroy,
  font=("Times New Roman",14),
  bg="#515151",
  relief="flat",
  activebackground="#707070",
  highlightthickness=2,
  highlightbackground="Black")
  quit_button.place(relheight=1 ,relwidth=.5, relx=.5, rely=0)
  root_main_page.mainloop()

main_page_func()