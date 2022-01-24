import tkinter as tk
import time
import random
from tkinter import font
import os


HEIGHT = 600
WIDTH = 750


def poker_script():
  global all_cards
  all_cards = [
  1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13
  ]
  

  

  def poker_cards():
    
    global player_first_card
    player_first_card = random.choice(all_cards)
    all_cards.remove(player_first_card)
    
    global comp_first_card
    comp_first_card = random.choice(all_cards)
    all_cards.remove(comp_first_card)
    
    global player_second_card
    player_second_card = random.choice(all_cards)
    all_cards.remove(player_second_card)
    
    global comp_second_card
    comp_second_card = random.choice(all_cards)
    all_cards.remove(comp_second_card)

    global player_third_card
    player_third_card = random.choice(all_cards)
    all_cards.remove(player_third_card)

    global comp_third_card
    comp_third_card = random.choice(all_cards)
    all_cards.remove(comp_third_card)

    global player_fourth_card
    player_fourth_card = random.choice(all_cards)
    all_cards.remove(player_fourth_card)

    global comp_fourth_card
    comp_fourth_card = random.choice(all_cards)
    all_cards.remove(comp_fourth_card)

    global player_fifth_card
    player_fifth_card = random.choice(all_cards)
    all_cards.remove(player_fifth_card)

    global comp_fifth_card
    comp_fifth_card = random.choice(all_cards)
    all_cards.remove(comp_fifth_card)
    
    global players_total
    players_total = player_first_card + player_second_card

    global comps_total
    comps_total = comp_first_card + comp_second_card
    
  poker_cards()
  
    

def deal_cards_func():
  root_main_page.destroy()


    
  global players_card_count
  players_card_count = 2
  poker_script()
  global root_deal_cards
  root_deal_cards=tk.Tk()  
  
  game_canvas = tk.Canvas(root_deal_cards, height=HEIGHT, width=WIDTH)
  game_canvas.pack()
  
  game_frame = tk.Frame(game_canvas, bg="#0C5B2E", highlightthickness=11, highlightbackground="black")
  game_frame.place(relheight=1, relwidth=1)
  
  def players_cards_func():
    global players_cards_frame
    players_cards_frame = tk.Frame(game_frame, bg="#0C5B2E", highlightthickness=2, highlightbackground="red")
    players_cards_frame.place(relheight=.3, relwidth=.35, relx=.35, rely=.62)
    
    def players_cards_labels():
      global players_card_one
      players_card_one = tk.Label(players_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
      players_card_one.place(relheight=.8, relwidth=.3, relx=.22, rely=.09)

      global players_card_two
      players_card_two = tk.Label(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
      players_card_two.place(relheight=.8, relwidth=.3, relx=.41, rely=.14)
      
      #Numbers
      players_card_one_number =tk.Label(players_card_one, bg="#D8D8D8", text=player_first_card, fg="black",font=("Times New Roman", 10))
      players_card_one_number.place(relheight=.5, relwidth=.65)
      
      global players_card_two_number
      players_card_two_number = tk.Label(players_card_two, bg="#D8D8D8", text=player_second_card, fg="black",font=("Times New Roman", 10))
      players_card_two_number.place(relheight=.5, relwidth=.66)
      
      
    players_cards_labels()
  players_cards_func()
  
  def computers_cards_func():
    global computers_cards_frame
    computers_cards_frame = tk.Frame(game_frame, bg="#0C5B2E", highlightthickness=2, highlightbackground="red")
    computers_cards_frame.place(relheight=.3, relwidth=.35, relx=.35, rely=.0)
    
    global computers_card_one
    computers_card_one = tk.Label(computers_cards_frame, bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
    computers_card_one.place(relheight=.8, relwidth=.3, relx=.22, rely=.09)

    global computers_card_two
    computers_card_two = tk.Label(computers_cards_frame, highlightthickness=3, bg="#0C255B", highlightbackground="#919D2A")
    computers_card_two.place(relheight=.8, relwidth=.3, relx=.4, rely=.14)
      
    #Numbers
    computers_card_one_number =tk.Label(computers_card_one, bg="#D8D8D8", text=comp_first_card, fg="black",font=("Times New Roman", 10))
    computers_card_one_number.place(relheight=.5, relwidth=.6,)
      

  computers_cards_func()
  #Shows the total of players cards
  global Players_Total_Func
  def Players_Total_Func():
    players_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Player's Total: "+ str(players_total)), font=("Times New Roman", 13))
    players_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.56)

  #Shows the total of computers total
  global Computers_Total_Func  
  def Computers_Total_Func():
    comps_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: "+ str(comps_total)), font=("Times New Roman", 13))
    comps_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)
  Players_Total_Func()
  
  comps_card_total = tk.Label(game_canvas, highlightthickness=2, bg="grey", highlightbackground="Red", text=("Dealer's Total: "+ str(comp_first_card)), font=("Times New Roman", 13))
  comps_card_total.place(relheight=.06, relwidth=.3, relx=.372, rely=.307)

  if players_total >= 22:
    player_busted = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
    player_busted.place(relwidth=.5, relheight=.3, relx=.25, rely=.31)
    text_busted = "You've busted with " + str(players_total)

    player_busted_text = tk.Label(player_busted, bg="White", text=text_busted, font=("Times New Roman", 15))
    player_busted_text.place(relwidth=.9, relheight=.8, relx=.05, rely=.05)

    global Comp_Restart_Func
    def Player_Restart_Start():
      root_deal_cards.destroy(),
      main_page_func()
    player_busted = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
    player_busted.place(relwidth=.5, relheight=.3, relx=.25, rely=.31)
    text_busted = "you've busted: +"+ str(winning_money)
        
    player_busted_text = tk.Label(player_busted, bg="grey", text=text_busted, font=("Times New Roman", 18))
    player_busted_text.place(relwidth=1, relheight=.2, relx=0, rely=.02)

    Player_And_Comp_Cards = tk.Label(player_busted, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 16))
    Player_And_Comp_Cards.place(relwidth=1, relheight=.2, relx=0, rely=.23)

    computers_card_two = tk.Label(computers_cards_frame,bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
    computers_card_two.place(relheight=.8, relwidth=.3, relx=.4, rely=.14)

    #Computers second cards Numbers
    computers_card_two_number =tk.Label(computers_card_two, bg="#D8D8D8", text=comp_second_card, fg="black",font=("Times New Roman", 10))
    computers_card_two_number.place(relheight=.5, relwidth=.6,)


    quit_button = tk.Button(player_busted, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy)
    quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)

    restart_button = tk.Button(player_busted, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=Player_Restart_Start)
    restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)

  def hit_button_func():
    global players_card_count
    global restart_button_code
    def restart_button_code():
        global hit_stand_buttons
        hit_button = tk.Button(game_canvas, state="disabled", bg="Grey", highlightbackground="black", highlightthickness=2, text="Hit", font=("Times New Roman", 11))

        hit_button.place(relheight=.08, relwidth=.17, relx=.359, rely=.9)
        stand_button = tk.Button(game_canvas, state="disabled", bg="grey", highlightthickness=2, highlightbackground="black", text="Stand", font=("Times New Roman", 11))
        stand_button.place(relheight=.08, relwidth=.17, relx=.52, rely=.9)

        player_busted = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
        player_busted.place(relwidth=.5, relheight=.3, relx=.25, rely=.31)  

        player_busted_text = tk.Label(player_busted, bg="grey", text=text_busted, font=("Times New Roman", 18))
        player_busted_text.place(relwidth=.9, relheight=.2, relx=.05, rely=.02)

        Player_And_Comp_Cards = tk.Label(player_busted, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 16))
        Player_And_Comp_Cards.place(relwidth=1, relheight=.2, relx=0, rely=.23)

        bal_update_lost()

        

        global restart_Button_func
        def restart_player_func():
          root_deal_cards.destroy(),
          main_page_func()

        restart_button = tk.Button(player_busted, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=restart_player_func, font=("Times New Roman", 15))
        restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)

        quit_button = tk.Button(player_busted, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy, font=("Times New Roman", 15))
        quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)
    #shows the players 3rd card
    if players_card_count == 2:
      
      global players_total
      players_total = players_total + player_third_card

      global players_card_third
      players_card_third = tk.Frame(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
      players_card_third.place(relheight=.8, relwidth=.3, relx=.6, rely=.16)

      #Numbers
      player_card_third_number = tk.Label(players_card_third, bg="#D8D8D8", text=player_third_card, fg="black",font=("Times New Roman", 10))
      player_card_third_number.place(relheight=.5, relwidth=.6,)
    
      Players_Total_Func()
      
      if players_total >= 22:
        restart_button_code()


      #Recentering of cards for third card
      players_card_one.place(relheight=.8, relwidth=.3, relx=.2, rely=.12)
      players_card_two.place(relheight=.8, relwidth=.3, relx=.35, rely=.14)
      players_card_third.place(relheight=.8, relwidth=.3, relx=.5, rely=.16)
    #shows the players 4th card
    if players_card_count == 3:
      players_total = players_total + player_fourth_card

      global players_card_fourth
      players_card_fourth = tk.Frame(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
      players_card_fourth.place(relheight=.8, relwidth=.3, relx=.58, rely=.16)

      player_card_fourth_number = tk.Label(players_card_fourth, bg="#D8D8D8", text=player_fourth_card, fg="black",font=("Times New Roman", 10))
      player_card_fourth_number.place(relheight=.5, relwidth=.6,)

      #Recentering of cards for fourth card
      players_card_one.place(relheight=.8, relwidth=.3, relx=.06, rely=.12)
      players_card_two.place(relheight=.8, relwidth=.3, relx=.25, rely=.14)
      players_card_third.place(relheight=.8, relwidth=.3, relx=.45, rely=.16)
      players_card_fourth.place(relheight=.8, relwidth=.3, relx=.6, rely=.18)
      
      
      Players_Total_Func()

      if players_total >= 22:
        global restart_button_func
        restart_button_code()
    #shows the players 5th card
    if players_card_count == 4:
      players_total = players_total + player_fifth_card

      players_card_fifth = tk.Frame(players_cards_frame, highlightthickness=3, bg="#D8D8D8", highlightbackground="#919D2A")
      players_card_fifth.place(relheight=.8, relwidth=.3, relx=.65, rely=.19)

      player_card_fifth_number = tk.Label(players_card_fifth, bg="#D8D8D8", text=player_fifth_card, fg="black",font=("Times New Roman", 10))
      player_card_fifth_number.place(relheight=.5, relwidth=.6,)

      #Recentering of cards for fifth card
      players_card_one.place(relheight=.8, relwidth=.3, relx=.05, rely=.12)
      players_card_two.place(relheight=.8, relwidth=.3, relx=.2, rely=.14)
      players_card_third.place(relheight=.8, relwidth=.3, relx=.35, rely=.16)
      players_card_fourth.place(relheight=.8, relwidth=.3, relx=.5, rely=.18)

      Players_Total_Func()
      
      if players_total >= 22:
        global restart_button_func
        restart_button_code()
      else:
        print("You Win!")

    players_card_count = players_card_count + 1


  
  def stand_button_func():
    global comps_total
    #Flips the second card over
    computers_card_two = tk.Label(computers_cards_frame,bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
    computers_card_two.place(relheight=.8, relwidth=.3, relx=.4, rely=.14)

    #Computers second cards Numbers
    computers_card_two_number =tk.Label(computers_card_two, bg="#D8D8D8", text=comp_second_card, fg="black",font=("Times New Roman", 10))
    computers_card_two_number.place(relheight=.5, relwidth=.6,)
    #updates the total
    Computers_Total_Func()
    #Shows if the comp busted

    if comps_total < 14:
      comps_total = comps_total + comp_third_card
      computers_card_three = tk.Label(computers_cards_frame,bg="#D8D8D8", highlightthickness=3, highlightbackground="#919D2A")
      computers_card_three.place(relheight=.8, relwidth=.3, relx=.55, rely=.16)

      computers_card_three_number =tk.Label(computers_card_three, bg="#D8D8D8", text=comp_third_card, fg="black",font=("Times New Roman", 10))
      computers_card_three_number.place(relheight=.5, relwidth=.6,)
      Computers_Total_Func()

    if comps_total <= 21:
      if players_total > comps_total:
        def Player_Won_Func():
          root_deal_cards.destroy(),
          main_page_func()
        print("Win up bal"+ str(win_up_bal))
        Player_Won = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
        Player_Won.place(relwidth=.5, relheight=.334, relx=.25, rely=.3)
        Player_Won_Text.place(relwidth=1, relheight=.25, relx=0, rely=.01)
        Player_And_Comp_Cards = tk.Label(Player_Won, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 18))
        Player_And_Comp_Cards.place(relwidth=1, relheight=.2, relx=0, rely=.2)

      
        quit_button = tk.Button(Player_Won, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy)
        quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)

        restart_button = tk.Button(Player_Won, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=Player_Won_Func)
        restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)

        bal_update_win()

      elif comps_total > players_total:
        def Comp_Won_Func():
          root_deal_cards.destroy(),
          main_page_func()
        Dealer_Won = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
        Dealer_Won.place(relwidth=.5, relheight=.334, relx=.25, rely=.3)
        Dealer_Won_Text.place(relwidth=1, relheight=.25, relx=0, rely=.01)
        Player_And_Comp_Cards = tk.Label(Dealer_Won, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 18))
        Player_And_Comp_Cards.place(relwidth=1, relheight=.2, relx=0, rely=.2)
      
        quit_button = tk.Button(Dealer_Won, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy)
        quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)

        restart_button = tk.Button(Dealer_Won, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=Comp_Won_Func)
        restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)

        bal_update_lost()

      else:
        def Tie_Func():
          root_deal_cards.destroy(),
          main_page_func()
        Tied = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
        Tied.place(relwidth=.5, relheight=.334, relx=.25, rely=.3)
        Tied_Text.place(relwidth=1, relheight=.25, relx=0, rely=.01)
        Player_And_Comp_Cards = tk.Label(Tied, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 18))
        Player_And_Comp_Cards.place(relwidth=1, relheight=.2, relx=0, rely=.2)

      
        quit_button = tk.Button(Tied, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy)
        quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)

        restart_button = tk.Button(Tied, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=Tie_Func)
        restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)



    else:
      global Comp_Restart_Func
      def Comp_Restart_Func():
        root_deal_cards.destroy(),
        main_page_func()
      comp_busted = tk.Frame(game_canvas, bg="grey", highlightthickness=3, highlightbackground="black")
      comp_busted.place(relwidth=.5, relheight=.3, relx=.25, rely=.31)
        
      comp_busted_text = tk.Label(comp_busted, bg="grey", text=busted_text, font=("Times New Roman", 17))
      comp_busted_text.place(relwidth=1, relheight=.2, relx=0, rely=.02)

      Player_And_Comp_Cards = tk.Label(comp_busted, text="You had ("+ str(players_total)+ "), They had ("+ str(comps_total)+")", bg="grey", font=("Times New Roman", 16))
      Player_And_Comp_Cards.place(relwidth=1, relheight=.25, relx=0, rely=.2)


      quit_button = tk.Button(comp_busted, bg="red", text="Quit", highlightthickness=2, highlightbackground="black", bd=0, command=root_deal_cards.destroy)
      quit_button.place(relheight=.35, relwidth=.4, relx=.5, rely=.65)

      restart_button = tk.Button(comp_busted, bg="green", text="Restart", highlightthickness=2, highlightbackground="black", bd=0, command=Comp_Restart_Func)
      restart_button.place(relheight=.35, relwidth=.4, relx=.1, rely=.65)

      bal_update_win()
      


    hit_button = tk.Button(game_canvas, state="disabled", bg="Grey", highlightbackground="black", highlightthickness=2, text="Hit", font=("Times New Roman", 10))
    hit_button.place(relheight=.08, relwidth=.17, relx=.359, rely=.9)

    stand_button = tk.Button(game_canvas, state="disabled", bg="grey", highlightthickness=2, highlightbackground="black", text="Stand", font=("Times New Roman", 10))
    stand_button.place(relheight=.08, relwidth=.17, relx=.52, rely=.9)
      


  def hit_stand_buttons():
    hit_button = tk.Button(game_canvas, command=hit_button_func, bg="Grey", highlightbackground="black", highlightthickness=2, text="Hit", font=("Times New Roman", 10))
    hit_button.place(relheight=.08, relwidth=.17, relx=.359, rely=.9)
  
    stand_button = tk.Button(game_canvas, command=stand_button_func, bg="grey", highlightthickness=2, highlightbackground="black", text="Stand", font=("Times New Roman", 10))
    stand_button.place(relheight=.08, relwidth=.17, relx=.52, rely=.9)
  hit_stand_buttons()
  
  root_deal_cards.mainloop()

def main_page_func():
  global root_main_page
  root_main_page=tk.Tk()
  root_main_page.title(" ")

  main_canvas = tk.Canvas(root_main_page, bg="#000000", height=HEIGHT, width=WIDTH)
  main_canvas.pack()

  frame_one = tk.Frame(main_canvas, bg="#0C5B2E", highlightthickness=10, highlightbackground="#272727")
  frame_one.place(relheight=.8, relwidth=.9, relx=.05, rely=.1)

  title_frame = tk.Frame(frame_one, bg="#0C5B2E")
  title_frame.place(relheight=.25, relwidth=.8, relx=.1, rely=.05)

  label_one = tk.Label(title_frame, text="BLACKJACK", bg="#515151", fg="black", font=("Times New Roman", 40), highlightthickness=4, highlightbackground="black", bd=2)
  label_one.place(relheight=1, relwidth=1, relx=0, rely=0)



  #Answers
  frame_answer = tk.Frame(frame_one)
  frame_answer.place(relheight=.2, relwidth=.9, relx=.06, rely=.7)

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
#dark #000000
#lighter #515151
#border #272727
#https://docs.replit.com/tutorials/02-managing-files-using-repl-it