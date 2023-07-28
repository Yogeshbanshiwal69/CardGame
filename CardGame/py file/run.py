import random
cards_H={'HA':13,'HK':12,'HQ':11,'HJ':10,'HT':9,'H9':8,'H8':7,'H7':6,'H6':6,'H5':4,'H4':3,'H3':2,'H2':1}
cards_C={'CA':13,'CK':12,'CQ':11,'CJ':10,'CT':9,'C9':8,'C8':7,'C7':6,'C6':6,'C5':4,'C4':3,'C3':2,'C2':1}
cards_D={'DA':13,'DK':12,'DQ':11,'DJ':10,'DT':9,'D9':8,'D8':7,'D7':6,'D6':6,'D5':4,'D4':3,'D3':2,'D2':1}
cards_S={'SA':13,'SK':12,'SQ':11,'SJ':10,'ST':9,'S9':8,'S8':7,'S7':6,'S6':6,'S5':4,'S4':3,'S3':2,'S2':1}

BOT1={'name':'BOT1','curr_cards':[],'call':0,'turns':[],'victory':0,'score':0,'final_score':0}
BOT2={'name':'BOT2','curr_cards':[],'call':0,'turns':[],'victory':0,'score':0,'final_score':0}
BOT3={'name':'BOT3','curr_cards':[],'call':0,'turns':[],'victory':0,'score':0,'final_score':0}
player={'name':'player','curr_cards':[],'call':0,'turns':[],'victory':0,'score':0,'final_score':0}

all_cards= ['HA','HK','HQ','HJ','HT','H9','H8','H7','H6','H5','H4','H3','H2']
all_cards+=['CA','CK','CQ','CJ','CT','C9','C8','C7','C6','C5','C4','C3','C2']
all_cards+=['DA','DK','DQ','DJ','DT','D9','D8','D7','D6','D5','D4','D3','D2']
all_cards+=['SA','SK','SQ','SJ','ST','S9','S8','S7','S6','S5','S4','S3','S2']


def calculating_calls(x):
    set_a={'HA','HK','HQ','HJ','CA','CK','CQ','CJ','DA','DK','DQ','DJ','SA','SK','SQ','SJ'}
    set_b=set(x['curr_cards'])
    x['call']=len(set_a.intersection(set_b))

def bot_movement(bot):
    assigned__=0
    first_card_of_this_round=list_of_players[0]['turns'][-1]
    list_of_cards=[cards_H,cards_C,cards_D,cards_S]
    #print(f"Current cards for {bot['name']} is {bot['curr_cards']} ")
    for i in list_of_cards:
        if first_card_of_this_round in i:
            for z in i.keys():
                if z!=first_card_of_this_round:
                    if z in bot['curr_cards']:
                        bot['turns'].append(z)
                        bot['curr_cards'].remove(z)
                        print(f"{bot['name']} : {z}")
                        assigned__=1
                        break
                else:
                    break
            if assigned__==0:
                for y in reversed(i.keys()):
                    if y in bot['curr_cards']:
                        bot['turns'].append(y)
                        bot['curr_cards'].remove(y)
                        print(f"{bot['name']} : {y}")
                        assigned__=1
                        break
    if assigned__==0:
        priority_order=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        for i in reversed(priority_order):
            if assigned__==1:
                break
            for q in bot['curr_cards']:
                if q[1]==i:
                    bot['turns'].append(q)
                    bot['curr_cards'].remove(q)
                    print(f"{bot['name']} : {q}")
                    assigned__=1
                    break

def one_round(players):
    if players[0]==player:                          #if the round is started by the player
        curr_cards=players[0]['curr_cards']
        print("It is player\'s turn.\n Your cards are: ",curr_cards)
        turn_number=int(input(f"Choose a card to play. (e.g. to select {curr_cards[0]}, press 1) \nEnter a number: "))-1
        print("You chose: ",curr_cards[turn_number])
        players[0]['turns'].append(curr_cards[turn_number])
        curr_cards.remove(curr_cards[turn_number])
        bot_movement(players[1])
        bot_movement(players[2])
        bot_movement(players[3])
    
    else:
        priority_order=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        x=0
        for i in priority_order:
            for q in players[0]['curr_cards']:
                if q[1]==i:
                    players[0]['turns'].append(q)
                    players[0]['curr_cards'].remove(q)
                    print(f"{players[0]['name']} : {q}")
                    x=1
                    break
            if x==1:
                break
        if players[1]==player:                          
            curr_cards=players[1]['curr_cards']
            print("It is player\'s turn.\n Your cards are: ",curr_cards)
            turn_number=int(input(f"Choose a card to play. (e.g. to select {curr_cards[0]}, press 1) \nEnter a number: "))-1
            print("You chose: ",curr_cards[turn_number])
            players[1]['turns'].append(curr_cards[turn_number])
            curr_cards.remove(curr_cards[turn_number])
        else:
            bot_movement(players[1])

        if players[2]==player:                          
            curr_cards=players[2]['curr_cards']
            print("It is player\'s turn.\n Your cards are: ",curr_cards)
            turn_number=int(input(f"Choose a card to play. (e.g. to select {curr_cards[0]}, press 1) \nEnter a number: "))-1
            print("You chose: ",curr_cards[turn_number])
            players[2]['turns'].append(curr_cards[turn_number])
            curr_cards.remove(curr_cards[turn_number])
        else:
            bot_movement(players[2])

        if players[3]==player:                          
            curr_cards=players[3]['curr_cards']
            print("It is player\'s turn.\n Your cards are: ",curr_cards)
            turn_number=int(input(f"Choose a card to play. (e.g. to select {curr_cards[0]}, press 1) \nEnter a number: "))-1
            print("You chose: ",curr_cards[turn_number])
            players[3]['turns'].append(curr_cards[turn_number])
            curr_cards.remove(curr_cards[turn_number])
        else:
            bot_movement(players[3])

def winner(players):
    global winner_
    last_plays=[]
    last_plays.append(players[0]['turns'][-1])
    last_plays.append(players[1]['turns'][-1])
    last_plays.append(players[2]['turns'][-1])
    last_plays.append(players[3]['turns'][-1])
    list_of_cards=[cards_H,cards_C,cards_D,cards_S]
    index_=0
    for i in list_of_cards:
        if last_plays[0] in i:
            curr_card=i
            break
    for x in curr_card:
        if x!=last_plays[0]:
            if x in last_plays:
                index_=last_plays.index(x)
                break
        else:
            break
    winner_=players[index_]
    winner_['victory']+=1

def score(players):
    print("Scores:\n")
    scores=[]
    for player in players:
        if player['call']>player['victory']:
            player['score']=(-10)*player['call']
            print(f"{player['name']}: -10*{player['call']} = {player['score']}")
            player['final_score']+=player['score']
            scores.append(player['score'])
        else:
            player['score']=9*player['call']+player['victory']
            print(f"{player['name']}: 10*{player['call']}+({player['victory']}-{player['call']}) = {player['score']} ")
            player['final_score']+=player['score']
            scores.append(player['score'])
    scores.sort()
    for player in players:
        if scores[-1]==player['score']:
            print("Winner of this round is: ",player['name'])
    

print("\n\n\n_______Card Game________\n\n")
print('loading...\n')
name=input("Type your username: ")
player['name']=name
print("creating user...")
print("Your username is: ",player['name'])
input("Press any key to start the game.")

list_of_players=[player,BOT1,BOT2,BOT3]

while True:

    print("Do you want the card distribution to be\n1. random or \n2. via a txt file")
    msg=input("Press 1 or 2: ")
    if msg=='1':
        print("Assigning random cards to each players...")
        random.shuffle(all_cards)                                            #shuffling for random distribution
        BOT1['curr_cards']=all_cards[:13]
        BOT2['curr_cards']=all_cards[13:26]
        BOT3['curr_cards']=all_cards[26:39]
        player['curr_cards']=all_cards[39:53]
    else:
        with open('cards_dist.txt','r') as fileobject:
            data=fileobject.readlines()
            BOT1['curr_cards']=data[0].split(',')
            BOT2['curr_cards']=data[1].split(',')
            BOT3['curr_cards']=data[2].split(',')
            player['curr_cards']=data[3].split(',')
            order=data[4].split(',')

            BOT1['curr_cards'][-1]=BOT1['curr_cards'][-1][0:2]
            BOT2['curr_cards'][-1]=BOT2['curr_cards'][-1][0:2]
            BOT3['curr_cards'][-1]=BOT3['curr_cards'][-1][0:2]
            player['curr_cards'][-1]=player['curr_cards'][-1][0:2]
            order[-1]=order[-1][0]

            list_of_players[0],list_of_players[1],list_of_players[2],list_of_players[3]=list_of_players[int(order[0])],list_of_players[int(order[1])],list_of_players[int(order[2])],list_of_players[int(order[3])]

    print("The cards are successfully distributed.")
    calculating_calls(BOT1)
    calculating_calls(BOT2)
    calculating_calls(BOT3)
    call=int(input("Define your call for this round: "))
    player['call']=call
    BOT1['victory']=0
    BOT2['victory']=0
    BOT3['victory']=0
    player['victory']=0

    while list_of_players[0]['curr_cards']:
        '''
        print("victory: ")
        print(list_of_players[0]['name']," : ",list_of_players[0]['victory'])
        print(list_of_players[1]['name']," : ",list_of_players[1]['victory'])
        print(list_of_players[2]['name']," : ",list_of_players[2]['victory'])
        print(list_of_players[3]['name']," : ",list_of_players[3]['victory'])
        '''
        print("\n\n\n")
        print(f"The order of playing is '{list_of_players[0]['name']}' -> '{list_of_players[1]['name']}' -> '{list_of_players[2]['name']}' -> '{list_of_players[3]['name']}'")
        one_round(list_of_players)
        winner(list_of_players)
        while list_of_players[0]!=winner_:
            temp=list_of_players.pop(0)
            list_of_players.append(temp)
        print(f"\n{winner_['name']} wins")
    
    print('\n\n\n')
    score(list_of_players)
    msg=input("\nDo you want to continue (y/n): ")
    print('\n')
    if msg=='n':
        final_scores=[]
        print("Final score")
        for i in list_of_players:
            print(f" {i['name']}: {i['final_score']} ")
            final_scores.append(i['final_score'])
        final_scores.sort()
        for i in list_of_players:
            if i['final_score']==final_scores[-1]:
                print("\n\n\nCongratulations!!!!!!\n\nWinner of this series is ",i['name'],"\n\n!!!!!!!!!!!!!!!!")
                break
        break