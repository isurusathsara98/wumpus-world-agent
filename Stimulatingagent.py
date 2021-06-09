'''
----- MINI PROJECT 01-----
Name : D.L.I.Sathsara
Index_No: 17/ENG/099
Course : CO3205 Intelligent Systems
Submission Date : 13/5/2021
'''
#global variables declared
Agent_loc=[]
Agent_view=[['0']*5 for _ in range(5)]
Environement=[]
percived=[]
mov_check=False
moves=[]
pervious_dir='up'
wumpus_loc=False
shoot=False
shoot_cod=[]
Wumpus=[]
possible_wumpus=[]
safe_loc=[]
possible_pit=[]
up_percive=1
down_percive=1
left_percive=1
right_percive=1
current_percive=1
class Agent():#agent class
    def __init__(self):#constructor
        self.matrix=[['0']*5 for _ in range(5)]


    def getpercive(row,col):#get the senses in surrounding
        global up_percive #all adjacent cells
        global down_percive
        global left_percive
        global right_percive
        global current_percive
        global percived
        current_percive=Environement[row][col]#current one
        print("********* If an adjacent cell is observed earlier, it will not be reobserved as it is in knowledge of agent **********")
        if(current_percive=='B' or current_percive=='AB'):
            print("Agent's Current cell observes Breeze")
        elif current_percive=='S' or current_percive=='AS':
            print("Agent's Current cell observes Stink")
        elif current_percive=='SB' or current_percive=='ASB':
            print("Agent's Current cell observes Breeze and Stink")

        if row-1>=0 and [row-1,col] not in percived: #if such a cell exists, get its sense
            up_percive=Environement[row-1][col]
            if(up_percive=='B'):
                print("Agent's adjacent upper cell ",(row-1,col) ," observes Breeze")
            elif up_percive=='S':
                print("Agent's adjacent upper cell ",(row-1,col) ," observes Stink")
            elif up_percive=='SB':
                print("Agent's adjacent upper cell ",(row-1,col) ," observes Breeze and Stink")
            percived.append([row-1,col])#note that this cell was already analyzed and kept in KB
        if row+1<5 and [row+1,col] not in percived: #similar as above
            down_percive=Environement[row+1][col]
            if(down_percive=='B'):
                print("Agent's adjacent downward cell ",(row+1,col) ," observes Breeze")
            elif down_percive=='S':
                print("Agent's adjacent downward cell ",(row+1,col) ," observes Stink")
            elif down_percive=='SB':
                print("Agent's adjacent downward cell ",(row+1,col) ," observes Breeze and Stink")
            percived.append([row+1,col])
        if col-1>=0 and [row,col-1] not in percived:
            left_percive=Environement[row][col-1]
            if(left_percive=='B'):
                print("Agent's adjacent leftward cell ",(row,col-1) ," observes Breeze")
            elif down_percive=='S':
                print("Agent's adjacent leftward cell ",(row,col-1) ," observes Stink")
            elif down_percive=='SB':
                print("Agent's adjacent leftward cell ",(row,col-1) ," observes Breeze and Stink")
            percived.append([row,col-1])
        if col+1<5 and [row,col+1] not in percived:
            right_percive=Environement[row][col+1]
            if(right_percive=='B'):
                print("Agent's adjacent rightward cell ",(row,col+1) ," observes Breeze")
            elif right_percive=='S':
                print("Agent's adjacent rightward cell ",(row,col+1) ," observes Stink")
            elif right_percive=='SB':
                print("Agent's adjacent rightward cell ",(row,col+1) ," observes Breeze and Stink")
            percived.append([row,col+1])
    def safe(row,col): #mark safe cells(if not breeze or stink)
        global Agent_view
        global safe_loc #allready visited cells, current cell, wumpus cell are ignored
        if row-1>=0 and Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='W' and [row-1,col] not in safe_loc:
            if Agent_view[row-1][col]=='PP':
                possible_pit.remove([row-1,col])
            Agent_view[row-1][col]='SF'
            safe_loc.append([row-1,col])#note the safe cells in another array
        if row+1<5 and Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row-1][col]!='W' and [row+1,col] not in safe_loc:
            if Agent_view[row+1][col]=='PP':
                possible_pit.remove([row+1,col])
            Agent_view[row+1][col]='SF'
            safe_loc.append([row+1,col])
        if col-1>=0 and Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row-1][col]!='W' and [row,col-1] not in safe_loc:
            if Agent_view[row][col-1]=='PP':
                possible_pit.remove([row,col-1])
            Agent_view[row][col-1]='SF'
            safe_loc.append([row,col-1])
        if col+1<5 and Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row-1][col]!='W' and [row,col+1] not in safe_loc:
            if Agent_view[row][col+1]=='PP':
                possible_pit.remove([row,col+1])
            Agent_view[row][col+1]='SF'
            safe_loc.append([row,col+1])


    def OnlyBreezeMarkPit(row,col):#similarly is a cells is breezy, use this to mark pits or possible locations of pits
        global possible_pit
        if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF'):
            if Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='P' or Agent_view[row-1][col]=='PPW':
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='P'
            else:
                Agent_view[row-1][col]='PP'
                possible_pit.append([row-1,col])
        if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF'):
            if Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='P' or Agent_view[row+1][col]=='PPW':
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='P'
            else:
                Agent_view[row+1][col]='PP'
                possible_pit.append([row+1,col])
        if col-1>=0 and (Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF'):
            if Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='P' or Agent_view[row][col-1]=='PPW':
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='P'
            else:
                Agent_view[row][col-1]='PP'
                possible_pit.append([row,col-1])
        if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF'):
            if Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='P' or Agent_view[row][col+1]=='PPW':
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='P'
            else:
                Agent_view[row][col+1]='PP'
                possible_pit.append([row,col+1])
    def OnlyStinkMarkWumpus(row,col):#mark posible wumpus locations or wumpus if stink by this function
        global wumpus_loc
        global Wumpus
        if wumpus_loc==False:
            if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF') and wumpus_loc==False:
                if Agent_view[row-1][col]=='PW' or Agent_view[row-1][col]=='W' or Agent_view[row-1][col]=='PPW':
                    Agent_view[row-1][col]='W'
                    Wumpus.append([row-1,col])
                    wumpus_loc=True
                else:
                    if Agent_view[row-1][col]=='PP':
                        possible_pit.remove([row-1,col])
                    Agent_view[row-1][col]='PW'
            if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF') and wumpus_loc==False:
                if Agent_view[row+1][col]=='PW' or Agent_view[row+1][col]=='W' or Agent_view[row+1][col]=='PPW':
                    Agent_view[row+1][col]='W'
                    Wumpus.append([row+1,col])
                    wumpus_loc=True
                else:
                    if Agent_view[row+1][col]=='PP':
                        possible_pit.remove([row+1,col])
                    Agent_view[row+1][col]='PW'
            if col-1>=0 and (Agent_view[row][col-1]!='V'and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF') and wumpus_loc==False:
                if Agent_view[row][col-1]=='PW' or Agent_view[row][col-1]=='W' or Agent_view[row][col-1]=='PPW':
                    Agent_view[row][col-1]='W'
                    Wumpus.append([row,col-1])
                    wumpus_loc=True
                else:
                    if Agent_view[row][col-1]=='PP':
                        possible_pit.remove([row,col-1])
                    Agent_view[row][col-1]='PW'
            if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF') and wumpus_loc==False:
                if Agent_view[row][col+1]=='PW' or Agent_view[row][col+1]=='W' or Agent_view[row][col+1]=='PPW':
                    Agent_view[row][col+1]='W'
                    Wumpus.append([row,col+1])
                    wumpus_loc=True
                else:
                    if Agent_view[row][col+1]=='PP':
                        possible_pit.remove([row,col+1])
                    Agent_view[row][col+1]='PW'
        else:
            if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF' and Agent_view[row-1][col]!='W'):
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='SF'
            if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF' and Agent_view[row+1][col]!='W'):
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='SF'
            if col-1>=0 and (Agent_view[row][col-1]!='V'and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF' and Agent_view[row][col-1]!='W'):
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='SF'
            if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF' and Agent_view[row][col+1]!='W'):
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='SF'
    def BreezeStink(row,col):#if both stink and breeze use this to mark in agent map to acquire knowledge on surrounding
        global wumpus_loc
        global possible_pit
        global Wumpus
        if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF'):
            if Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='P':
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='P'
            elif Agent_view[row-1][col]=='PW' or Agent_view[row-1][col]=='W' or Agent_view[row-1][col]=='PPW' and wumpus_loc==False:
                Agent_view[row-1][col]='W'
                wumpus_loc=True
                Wumpus.append([row-1,col])
            elif wumpus_loc==False:
                Agent_view[row-1][col]='PPW'
            elif Agent_view[row-1][col]!='W':
                Agent_view[row-1][col]='PP'
                possible_pit.append([row-1,col])
        if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF'):
            if Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='P':
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='P'
            elif Agent_view[row+1][col]=='PW' or Agent_view[row+1][col]=='W' or Agent_view[row+1][col]=='PPW' and wumpus_loc==False:
                Agent_view[row+1][col]='W'
                wumpus_loc=True
                Wumpus.append([row+1,col])
            elif wumpus_loc==False:
                Agent_view[row+1][col]='PPW'
            elif Agent_view[row+1][col]!='W':
                Agent_view[row+1][col]='PP'
                possible_pit.append([row+1,col])
        if col-1>=0 and (Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF'):
            if Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='P':
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='P'
            elif Agent_view[row][col-1]=='PW' or Agent_view[row][col-1]=='W' or Agent_view[row][col-1]=='PPW' and wumpus_loc==False:
                Agent_view[row][col-1]='W'
                wumpus_loc=True
                Wumpus.append([row,col-1])
            elif wumpus_loc==False:
                Agent_view[row][col-1]='PPW'
            elif Agent_view[row][col-1]!='W':
                Agent_view[row][col-1]='PP'
                possible_pit.append([row,col-1])
        if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF'):
            if Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='P':
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='P'
            elif Agent_view[row][col+1]=='PW' or Agent_view[row][col+1]=='W' or Agent_view[row][col+1]=='PPW' and wumpus_loc==False:
                Agent_view[row][col+1]='W'
                wumpus_loc=True
                Wumpus.append([row,col+1])
            elif wumpus_loc==False:
                Agent_view[row][col+1]='PPW'
            elif Agent_view[row][col+1]!='W':
                Agent_view[row][col+1]='PP'
                possible_pit.append([row,col+1])
    def travel_to_safe(row,col,temp_row,temp_col):
        #if there is a safe location far away, then travel to it by first going to specific row and the going to column
        global Agent_view
        global pervious_dir

        if(row>=temp_row):
            while(row>temp_row):
                row-=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='up'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_up')
                pervious_dir='up'
                Agent.printenv(Agent_view)
                Agent_view[row][col]=state
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='left'):
                        print("Move - forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right and Move Forward")
                    moves.append('move_left')
                    pervious_dir='left'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state
            else:
                while(col<temp_col):
                    col+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='right'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Left and Move Forward")
                    moves.append('move_right')
                    pervious_dir='right'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state

        else:
            while(row<temp_row):
                row+=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='down'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Left and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_down')
                pervious_dir='down'
                Agent.printenv(Agent_view)
                Agent_view[row][col]=state
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='left'):
                        print("Move - forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right and Move Forward")
                    moves.append('move_left')
                    pervious_dir='left'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state
            else:
                while(col<temp_col):
                    col+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='right'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Left and Move Forward")
                    moves.append('move_right')
                    pervious_dir='right'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state

    def travel_to_safe_col(row,col,temp_row,temp_col):
        #if first going to row and then going to column does have a safe path, then first go to column number of the safe location and then go to row number to
        #get to the safe location
        global Agent_view
        global pervious_dir

        if(col>=temp_col):
            while(col>temp_col):
                col-=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='left'):
                    print("Move - forward")
                elif(pervious_dir=='right'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right and Move Forward")
                moves.append('move_left')
                pervious_dir='left'

                Agent.printenv(Agent_view)
                Agent_view[row][col]=state
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='up'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_up')
                    pervious_dir='up'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state
            else:
                while(row<temp_row):
                    row+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='down'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Left and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_down')
                    pervious_dir='down'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state

        else:
            while(col<temp_col):
                col+=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='right'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Left and Move Forward")
                moves.append('move_right')
                pervious_dir='right'
                Agent.printenv(Agent_view)
                Agent_view[row][col]=state
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='up'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_up')
                    pervious_dir='up'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state
            else:
                while(row<temp_row):
                    row+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='down'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Left and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_down')
                    pervious_dir='down'
                    Agent.printenv(Agent_view)
                    Agent_view[row][col]=state

    def checkpath(row,col,temp_row,temp_col):
        #check if there is a clear path from to a safe cell in the safe_loc array but travelling first to row and then to column
        global Agent_view
        correct=True
        if(row>=temp_row):
            while(row>temp_row):
                row-=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct=False
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(col<temp_col):
                    col+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        else:
            while(row<temp_row):
                row+=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct= False
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(col<temp_col):
                    col+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
    def colcheckpath(row,col,temp_row,temp_col):
        #check if there is a clear path from to a safe cell in the safe_loc array but travelling first to column and then to row
        global Agent_view
        correct=True
        if(col>=temp_col):
            while(col>temp_col):
                col-=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct=False
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(row<temp_row):
                    row+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        else:
            while(col<temp_col):
                col+=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct= False
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(row<temp_row):
                    row+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
    def unsafe(row,col):
        #if no safe locations are accessible take a risk and select a possible pit or possible wumpus location which can be risky
        global pervious_dir
        global Agent_view
        if row-1>=0 and (Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='PW'):
            row=row-1
            col=col
            print(row,col)
            if(pervious_dir=='up'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Right and Move Forward")
            elif(pervious_dir=='right'):
                print("Turn Left and Move Forward")
            else:
                print("Turn Right twice and Move Forward")
            moves.append('move_up')
            pervious_dir='up'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif col+1<5 and (Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='PW'):
            col=col+1
            row=row
            print(row,col)
            if(pervious_dir=='right'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Right twice and Move Forward")
            elif(pervious_dir=='up'):
                print("Turn Right and Move Forward")
            else:
                print("Turn Left and Move Forward")
            moves.append('move_right')
            pervious_dir='right'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif row+1<5 and (Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='PW'):
            row=row+1
            col=col
            print(row,col)
            if(pervious_dir=='down'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Left and Move Forward")
            elif(pervious_dir=='right'):
                print("Turn Right and Move Forward")
            else:
                print("Turn Right twice and Move Forward")
            moves.append('move_down')
            pervious_dir='down'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif col-1>=0 and (Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='PW'):
            row=row
            col=col-1
            print(row,col)
            if(pervious_dir=='left'):
                print("Move - forward")
            elif(pervious_dir=='right'):
                print("Turn Right twice and Move Forward")
            elif(pervious_dir=='up'):
                print("Turn Left and Move Forward")
            else:
                print("Turn Right and Move Forward")
            moves.append('move_left')
            pervious_dir='left'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]

    def agentStart(self): #main function which stimulates the agent
        counter=0
        temp_row=5
        temp_col=5
        crash_cou=0
        global possible_pit
        global safe_loc
        global pervious_dir
        global Agent_view
        global wumpus_loc
        global moves
        global mov_check
        global shoot
        global shoot_cod
        global up_percive,down_percive,left_percive,right_percive
        row=Agent_loc[0]
        col=Agent_loc[1]
        percived.append([row,col])
        Agent.getpercive(row,col) #from initial location of agent get all senses of adjacent cells
        if(current_percive=='A'): #update agent's map with the acquired senses
            Agent.safe(row,col)
        elif(current_percive=='AB'):
            Agent.OnlyBreezeMarkPit(row,col)
        elif(current_percive=='AS') and wumpus_loc==False:
            Agent.OnlyStinkMarkWumpus(row,col)
        elif(current_percive=='ASB'):
            Agent.BreezeStink(row,col)
        while(current_percive!='G' and current_percive!='GB' and current_percive!='GS' and current_percive!='PG' and current_percive!='GSB'
        and current_percive!='PGB' and current_percive!='GPS' and current_percive!='GPSB' and counter!=30):#if glod is found exit loop
            counter+=1#if 30 steps are reached end the loop
            Agent_view[row][col]='A'
            if(Environement[row][col]=='P' or Environement[row][col]=='PS' or Environement[row][col]=='PB' or Environement[row][col]=='PSB'):
                print("FELL IN TO A PIT ! GAME OVER") #if pit game over
                moves.append("game_over_pit")
                break
            if(Environement[row][col]=='W' and shoot==False):
                print("ATTACKED BY WUMPUS ! GAME OVER") #if wumpus and still not shooted game over
                moves.append("game_over_wumpus")
                break
            elif Environement[row][col]=='W' and [row,col] not in shoot_cod:
                print("ATTACKED BY WUMPUS ! GAME OVER")#if wumpus and shooted to wrong position game over
                moves.append("game_over_wumpus")
                break
            if(up_percive!=1): #check each sense of adjacent cells. if a cells is not accessible(out of range) than it is 1 as initialized
                if(up_percive=='B' or up_percive=='PB' or up_percive=='WB' or up_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row-1,col)#mark all prediction in map using senses
                elif(up_percive=='S' or up_percive=='PS' or up_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row-1,col)
                elif(up_percive=='SB' or up_percive=='PSB' or up_percive=='GSB'):
                    Agent.BreezeStink(row-1,col)
                else:
                    Agent.safe(row-1,col)
            if(down_percive!=1):
                if(down_percive=='B' or down_percive=='PB' or down_percive=='WB' or down_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row+1,col)
                elif(down_percive=='S' or down_percive=='PS' or down_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row+1,col)
                elif(down_percive=='SB' or down_percive=='PSB' or down_percive=='GSB'):
                    Agent.BreezeStink(row+1,col)
                else:
                    Agent.safe(row+1,col)
            if(left_percive!=1):
                if(left_percive=='B' or left_percive=='PB' or left_percive=='WB' or left_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row,col-1)
                elif(left_percive=='S' or left_percive=='PS' or left_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row,col-1)
                elif(left_percive=='SB' or left_percive=='PSB' or left_percive=='GSB'):
                    Agent.BreezeStink(row,col-1)
                else:
                    Agent.safe(row,col-1)
            if(right_percive!=1):
                if(right_percive=='B' or right_percive=='PB' or right_percive=='WB' or right_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row,col+1)
                elif(right_percive=='S' or right_percive=='PS' or right_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row,col+1)
                elif(right_percive=='SB' or right_percive=='PSB' or right_percive=='GSB'):
                    Agent.BreezeStink(row,col+1)
                else:
                    Agent.safe(row,col+1)
            Agent.printenv(Agent_view)

            if(wumpus_loc):#i wumpus discovered
                for i in range(5):
                    for j in range(5):#all other posible wumpus locations are changed to no wumpus
                        if Agent_view[i][j]=='PW':
                            Agent_view[i][j]='SF'
                            safe_loc.append([i,j])
                        elif Agent_view[i][j]=='PPW':
                            Agent_view[i][j]='PP'
                            possible_pit.append([i,j])
            else:
                wump_count=0
                for i in range(5):
                    for j in range(5):
                        if Agent_view[i][j]=='PW' or Agent_view[i][j]=='PPW':
                            wump_count+=1
                if(wump_count==1):#if only one PW or PPW is there then its surely a wumpus. so mark it as W
                    for i in range(5):
                        for j in range(5):
                            if Agent_view[i][j]=='PW' or Agent_view[i][j]=='PPW':
                                Agent_view[i][j]='W'
                                wumpus_loc=True
                                Wumpus.append([i,j])


            if(row-1>=0 and Agent_view[row-1][col]=='W' and shoot==False):#not yet shooted, shoot the umpus
                shoot=True
                shoot_cod.append([row-1,col])
                print("SHOOT THE WUMPUS IN ",(row-1,col)," CELL")
                Agent_view[row-1][col]='SF'
                Agent.printenv(Agent_view)
                moves.append("shoot_up")
                safe_loc.append([row-1,col])
            elif(col+1<5 and Agent_view[row][col+1]=='W' and shoot==False):
                shoot=True
                shoot_cod.append([row,col+1])
                print("SHOOT THE WUMPUS IN ",(row,col+1)," CELL")
                Agent_view[row][col+1]='SF'
                Agent.printenv(Agent_view)
                moves.append("shoot_right")
                safe_loc.append([row,col+1])
            elif(row+1<5 and Agent_view[row+1][col]=='W' and shoot==False):
                shoot=True
                shoot_cod.append([row+1,col])
                print("SHOOT THE WUMPUS IN ",(row+1,col)," CELL")
                Agent_view[row+1][col]='SF'
                Agent.printenv(Agent_view)
                moves.append("shoot_down")
                safe_loc.append([row+1,col])
            elif(col-1>=0 and Agent_view[row][col-1]=='W'):
                shoot=True
                shoot_cod.append([row,col-1])
                print("SHOOT THE WUMPUS IN ",(row,col-1)," CELL")
                Agent_view[row][col-1]='SF'
                Agent.printenv(Agent_view)
                moves.append("shoot_left")
                safe_loc.append([row,col-1])
            Agent_view[row][col]='V' #mark the current position as visited
            if(row-1>=0 and Agent_view[row-1][col]=='SF'):#if there is a safe location in the surrounding agent moves to it
                row=row-1
                col=col
                print(row,col)
                if(pervious_dir=='up'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_up')
                pervious_dir='up'
                mov_check=True#move is found
                safe_loc.remove([row,col])#the moved safe location is removed from list
            elif(col+1<5 and Agent_view[row][col+1]=='SF'):#similar to above
                col=col+1
                row=row
                print(row,col)
                if(pervious_dir=='right'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Left and Move Forward")
                moves.append('move_right')
                pervious_dir='right'
                mov_check=True
                safe_loc.remove([row,col])
            elif(row+1<5 and Agent_view[row+1][col]=='SF'):
                row=row+1
                col=col
                print(row,col)
                if(pervious_dir=='down'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Left and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_down')
                pervious_dir='down'
                mov_check=True
                safe_loc.remove([row,col])
            elif(col-1>=0 and Agent_view[row][col-1]=='SF'):
                row=row
                col=col-1
                print(row,col)
                if(pervious_dir=='left'):
                    print("Move - forward")
                elif(pervious_dir=='right'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right and Move Forward")
                moves.append('move_left')
                pervious_dir='left'
                safe_loc.remove([row,col])
                mov_check=True
            elif len(safe_loc)!=0:#if not safe location adjecant to current cell, see whther agent can reach other safe location through a safe path and record the moves
                i=0
                while i<len(safe_loc):#first find path by going to the row number and then traveling to cell by column number
                    temp_row=safe_loc[i][0]
                    temp_col=safe_loc[i][1]
                    clearpath=Agent.checkpath(row,col,temp_row, temp_col)#if there is a safe path
                    if(clearpath):
                        Agent.travel_to_safe(row,col,temp_row,temp_col)#record the moves and travel to it
                        row=temp_row
                        col=temp_col
                        safe_loc.remove([row,col])#remove that location from safe_loc list
                        mov_check=True
                        break
                    elif i==len(safe_loc)-1:#no safe paths found for all safe locations
                        j=0
                        while j<len(safe_loc):#find path by going to the column number and then traveling to cell by row number
                            temp_row=safe_loc[j][0]
                            temp_col=safe_loc[j][1]
                            clearpath1=Agent.colcheckpath(row,col,temp_row,temp_col)
                            if(clearpath1):#similar
                                Agent.travel_to_safe_col(row,col,temp_row,temp_col)
                                row=temp_row
                                col=temp_col
                                safe_loc.remove([row,col])
                                mov_check=True
                                break
                            elif j==len(safe_loc)-1:#move to nearest PP location which is risky
                                break
                            else:
                                temp_col=5
                                temp_row=5
                                j+=1
                        break
                    else:
                        temp_col=5
                        temp_row=5
                        i+=1
            if (mov_check==False and len(possible_pit)!=0):#if there are Posible pits in KB
                new_loc=Agent.unsafe(row,col)#if there are PP cells near the Agent(adjacent ones)
                if new_loc:
                    row=new_loc[0]
                    col=new_loc[1]
                else:#finding a safe path to PP cells far from agent
                    k=0
                    while k<len(possible_pit):
                        temp_row=possible_pit[k][0]
                        temp_col=possible_pit[k][1]
                        clearpath=Agent.colcheckpath(row,col,temp_row,temp_col)#check if path is safe
                        if(clearpath):
                            Agent.travel_to_safe(row,col,temp_row,temp_col)#record the moves and travel to it
                            row=temp_row
                            col=temp_col
                            print("here row bn",temp_row,temp_col)
                            possible_pit.remove([row,col])#remove that location from possible_pit list
                            break
                        elif k==len(possible_pit)-1:
                            h=0
                            while h<len(possible_pit):#find path by going to the column number and then traveling to cell by row number
                                temp_row=possible_pit[h][0]
                                temp_col=possible_pit[h][1]
                                clearpath1=Agent.colcheckpath(row,col,temp_row,temp_col)
                                if(clearpath1):#similar
                                    Agent.travel_to_safe_col(row,col,temp_row,temp_col)
                                    row=temp_row
                                    col=temp_col
                                    print("here col bn",temp_row,temp_col)
                                    possible_pit.remove([row,col])
                                    break
                                elif h==len(possible_pit)-1:#no path found
                                    if(crash_cou==4):#no possible way to get to gold, agent crashes
                                        #could find ant solution from above logic
                                        print(" Agent unable to locate next move")
                                        moves.append("crash")
                                        counter=30
                                    else:#move to a visited location so that it can generated a new path that is safe for a SF location or PP location
                                        crash_cou+=1#crash counter updated to stop this section from infinitely looping
                                        if(row-1>=0 and Agent_view[row-1][col]=='V'):#if there is a visit location in the surrounding agent moves to it
                                            row=row-1
                                            col=col
                                            print(row,col)
                                            if(pervious_dir=='up'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Right and Move Forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Left and Move Forward")
                                            else:
                                                print("Turn Right twice and Move Forward")
                                            moves.append('move_up')
                                            pervious_dir='up'
                                            mov_check=True
                                        elif(col+1<5 and Agent_view[row][col+1]=='V'):#similar to above
                                            col=col+1
                                            row=row
                                            print(row,col)
                                            if(pervious_dir=='right'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Right twice and Move Forward")
                                            elif(pervious_dir=='up'):
                                                print("Turn Right and Move Forward")
                                            else:
                                                print("Turn Left and Move Forward")
                                            moves.append('move_right')
                                            pervious_dir='right'
                                            mov_check=True
                                        elif(row+1<5 and Agent_view[row+1][col]=='V'):
                                            row=row+1
                                            col=col
                                            print(row,col)
                                            if(pervious_dir=='down'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Left and Move Forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Right and Move Forward")
                                            else:
                                                print("Turn Right twice and Move Forward")
                                            moves.append('move_down')
                                            pervious_dir='down'
                                            mov_check=True
                                        elif(col-1>=0 and Agent_view[row][col-1]=='V'):
                                            row=row
                                            col=col-1
                                            print(row,col)
                                            if(pervious_dir=='left'):
                                                print("Move - forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Right twice and Move Forward")
                                            elif(pervious_dir=='up'):
                                                print("Turn Left and Move Forward")
                                            else:
                                                print("Turn Right and Move Forward")
                                            moves.append('move_left')
                                            pervious_dir='left'
                                            mov_check=True

                                    break
                                else:
                                    temp_col=5
                                    temp_row=5
                                    h+=1
                            break
                        else:
                            temp_col=5
                            temp_row=5
                            k+=1
            elif mov_check==False:#no move is yet found
                print("Agent unable to locate next move")
                moves.append("crash")
                counter=30


            mov_check=False #reset there variables to initialized values
            up_percive=1
            down_percive=1
            right_percive=1
            left_percive=1
            Agent.getpercive(row,col)#get percives

        #if gold in current location
        if(Environement[row][col]=="G" or Environement[row][col]=="GS" or Environement[row][col]=="GB" or Environement[row][col]=="GSB"):
            print("GOLD FOUND!!! AGENT WINS")
            moves.append("gold")
        else:
            print("AGENT LOSE :-[")
        return moves
    def printenv(Agent_view):#print the original environment and agent view in each step
        global Environement
        print("\n    Original Environment              Agent environement \n")
        for i in range(5):
            print(" ",Environement[i] ,"     ", Agent_view[i])

    def agent_loc(agent_loc,original):#initialize data from wumpus world such as agent location
        global Agent_loc
        Agent_loc=agent_loc
        row=Agent_loc[0]
        col=Agent_loc[1]
        Agent_view[row][col]='A'
        global Environement
        Environement=original
        Agent.printenv(Agent_view)




