'''
----- MINI PROJECT 01-----
Name : D.L.I.Sathsara
Index_No: 17/ENG/099
Course : CO3205 Intelligent Systems
Submission Date : 13/5/2021
'''
#importing libraries and python files
import tkinter as tk
import random
import time
import styles as S
import Stimulatingagent as Ag

#global variables declared
wumpus_cod=[]
pit=[]
Agent=[]
step=0
moves=[]
Gold=[]
pre_dir='up'
original_env=[]
original_agent=[]
Action="<Up>"

#wumpus world game environment creation and run agent program
class WumpusGame(tk.Frame): #declare tk frame to create gui
    def __init__(self):
        tk.Frame.__init__(self) #constructor
        self.grid()
        self.master.title("wumpus world stimulator")
        self.main_grid=tk.Frame(
            self, bg=S.ENVBACKGROUND, bd=3, width=700, height=600 #size of the window
        )
        self.main_grid.grid(pady=(70,0),padx=(0,0)) #leave space to show next move
        self.Agentlogic()# print the description of agent
        self.environment() #wumpus world creation with 5 * 5 grid
        self.wumpus() #call other functions in class
        self.pit()
        self.agent_pos()
        self.gold()
        global moves
        moves=Ag.Agent.agentStart(self) #store the moves done by agent to show in gui later. this is returned by agentstimulation.py
        print("\n Description of Agent in the begining of the console print\n Press spacebar to trigger stimulation step by step")
        self.master.bind("<space>",self.start) #proceed each move when space is pressed
        self.mainloop() #mainloop of the gui

    def environment(self): #create 5*5 grid environment
        self.cells=[]
        for i in range(5):
            row=[]
            for j in range(5):
                cell_frame=tk.Frame(
                    self.main_grid,
                    bg="#ffffff",
                    width=90,
                    height=80
                )
                cell_frame.grid(row=i,column=j,padx=5,pady=5)
                cell_number=tk.Label(self.main_grid,bg="#FFFFFF")
                cell_number.grid(row=i,column=j)
                cell_data={"frame":cell_frame,"number":cell_number}
                row.append(cell_data)
            self.cells.append(row)
        score_frame=tk.Frame(self) #title frame
        score_frame.place(relx=0.5,y=30,anchor="center")
        tk.Label(
            score_frame,
            text="Wumpus World Stimulator",
            font=S.DOUBLE_FONT
        ).grid(row=0)
        self.score_label=tk.Label(score_frame,text="Press Spacebar continuosly to stimulate each step",font=S.DOUBLE_FONT1)
        self.score_label.grid(row=1)

    def wumpus(self): #random position for wumpus
        self.matrix=[['0']*5 for _ in range(5)]
        row=random.randint(0,4)
        col=random.randint(0,4)
        #if random position is conners, initialize again
        while(row==0 and col==0) or (row==4 and col==0) or (row==0 and col==4) or (row==4 and col==4):
            row=random.randint(0,4)
            col=random.randint(0,4)

        self.matrix[row][col]='W' #mark cell as wumpus and put adjacent cells as stink
        if (row-1>=0):
            self.matrix[row-1][col]='S'
        if (col+1<5):
            self.matrix[row][col+1]='S'
        if (row+1<5):
            self.matrix[row+1][col]='S'
        if (col-1>=0):
            self.matrix[row][col-1]='S'

        global wumpus_cod
        wumpus_cod=[row,col] #record wumpus location


    def pit(self): #5 pits initialization
        global pit

        while(sum([i.count('P') + i.count('PS') for i in self.matrix])<5):
            row=random.randint(0,4)
            col=random.randint(0,4)
            if(self.matrix[row][col]!='P') and (self.matrix[row][col]!='W') and (self.matrix[row][col]!='PS'):
                if(self.matrix[row][col]!='S'): #if empty mark pit
                    self.matrix[row][col]='P'

                elif(self.matrix[row][col]=='S'): # if stink put pit and stink both PS
                    self.matrix[row][col]='PS'

                pit.append([row,col])
        #following code is to mark the adjacent cells as Breeze
        for i in range(5):
            row=pit[i][0]
            col=pit[i][1]
            if(row-1>=0):
                if(self.matrix[row-1][col]=='W'):
                    self.matrix[row-1][col]='WB'

                elif(self.matrix[row-1][col]=='S'):
                    self.matrix[row-1][col]='SB'

                elif(self.matrix[row-1][col]=='SB'):
                    self.matrix[row-1][col]='SB'

                elif(self.matrix[row-1][col]=='PS'):
                    self.matrix[row-1][col]='PSB'

                elif(self.matrix[row-1][col]=='PSB'):
                    self.matrix[row-1][col]='PSB'

                elif(self.matrix[row-1][col]=='P'):
                    self.matrix[row-1][col]='PB'

                elif(self.matrix[row-1][col]=='WB'):
                    self.matrix[row-1][col]='WB'

                elif(self.matrix[row-1][col]=='PB'):
                    self.matrix[row-1][col]='PB'

                else:
                    self.matrix[row-1][col]='B'

            if(row+1<5):
                if(self.matrix[row+1][col]=='W'):
                    self.matrix[row+1][col]='WB'

                elif(self.matrix[row+1][col]=='PB'):
                    self.matrix[row+1][col]='PB'

                elif(self.matrix[row+1][col]=='WB'):
                    self.matrix[row+1][col]='WB'

                elif(self.matrix[row+1][col]=='S'):
                    self.matrix[row+1][col]='SB'

                elif(self.matrix[row+1][col]=='SB'):
                    self.matrix[row+1][col]='SB'

                elif(self.matrix[row+1][col]=='PS'):
                    self.matrix[row+1][col]='PSB'

                elif(self.matrix[row+1][col]=='PSB'):
                    self.matrix[row+1][col]='PSB'

                elif(self.matrix[row+1][col]=='P'):
                    self.matrix[row+1][col]='PB'

                else:
                    self.matrix[row+1][col]='B'

            if(col-1>=0):
                if(self.matrix[row][col-1]=='W'):
                    self.matrix[row][col-1]='WB'

                elif(self.matrix[row][col-1]=='PB'):
                    self.matrix[row][col-1]='PB'

                elif(self.matrix[row][col-1]=='WB'):
                    self.matrix[row][col-1]='WB'

                elif(self.matrix[row][col-1]=='S'):
                    self.matrix[row][col-1]='SB'

                elif(self.matrix[row][col-1]=='SB'):
                    self.matrix[row][col-1]='SB'

                elif(self.matrix[row][col-1]=='PS'):
                    self.matrix[row][col-1]='PSB'

                elif(self.matrix[row][col-1]=='PSB'):
                    self.matrix[row][col-1]='PSB'

                elif(self.matrix[row][col-1]=='P'):
                    self.matrix[row][col-1]='PB'

                else:
                    self.matrix[row][col-1]='B'

            if(col+1<5):
                if(self.matrix[row][col+1]=='W'):
                    self.matrix[row][col+1]='WB'

                elif(self.matrix[row][col+1]=='PB'):
                    self.matrix[row][col+1]='PB'

                elif(self.matrix[row][col+1]=='WB'):
                    self.matrix[row][col+1]='WB'

                elif(self.matrix[row][col+1]=='S'):
                    self.matrix[row][col+1]='SB'

                elif(self.matrix[row][col+1]=='SB'):
                    self.matrix[row][col+1]='SB'

                elif(self.matrix[row][col+1]=='PS'):
                    self.matrix[row][col+1]='PSB'

                elif(self.matrix[row][col+1]=='PSB'):
                    self.matrix[row][col+1]='PSB'

                elif(self.matrix[row][col+1]=='P'):
                    self.matrix[row][col+1]='PB'

                else:
                    self.matrix[row][col+1]='B'



    def agent_pos(self): #initialize agent position
        row=random.choice([0,4])
        col=random.choice([0,4])
        #only coners which are empty or breezy pr stinky or both is selected
        while(self.matrix[row][col]=='P') or (self.matrix[row][col]=='PS') or (self.matrix[row][col]=='PB') or (self.matrix[row][col]=='PSB'):
            row=random.choice([0,4])
            col=random.choice([0,4])
        global Agent
        global original_agent
        Agent=[row,col] #save agent location
        original_agent=Agent
        #place agent in map or environment
        if(self.matrix[row][col]=='0'):
            self.matrix[row][col]='A'

        elif(self.matrix[row][col]=='B'):
            self.matrix[row][col]='AB'

        elif(self.matrix[row][col]=='S'):
            self.matrix[row][col]='AS'

        elif(self.matrix[row][col]=='SB'):
            self.matrix[row][col]='ASB'

    def gold(self): #initialize gold
        row=random.choice([0,4])
        col=random.choice([0,4])
        #put gold only in cells which are empty,breezy, stink or both
        while(self.matrix[row][col]=='W' or self.matrix[row][col]=='WB' or self.matrix[row][col]=='A' or self.matrix[row][col]=='AS'
              or self.matrix[row][col]=='AB' or self.matrix[row][col]=='ASB' or self.matrix[row][col]=='P' or self.matrix[row][col]=='PSB' or
              self.matrix[row][col]=='PS' or self.matrix[row][col]=='PB'):
            row=random.choice([0,4])
            col=random.choice([0,4])
        #place in environment
        if(self.matrix[row][col]=='B'):
            self.matrix[row][col]='GB'

        elif(self.matrix[row][col]=='S'):
            self.matrix[row][col]='GS'

        elif(self.matrix[row][col]=='0'):
            self.matrix[row][col]='G'

        elif(self.matrix[row][col]=='SB'):
            self.matrix[row][col]='GSB'


        global original_env
        original_env=self.matrix
        #print original environment in console
        print("\ncreating the environment (Original environement)\n")
        for i in range(5):
            print(original_env[i])
        Ag.Agent.agent_loc(Agent,self.matrix)
        #create the gui settings such as colour, font, text and etc
        self.updateGui()



    def updateGui(self):
        #following code is to give specific colour,font and names to each cell
        for i in range(5):
            for j in range(5):
                cell_value=self.matrix[i][j]
                if cell_value=='0':
                    self.cells[i][j]["frame"].configure(bg="#FFFFFF")
                    self.cells[i][j]["number"].configure(
                        bg="#FFFFFF",
                        text=""
                    )
                elif cell_value=='G':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.GOLD,
                        font=S.DOUBLE_FONT,
                        text="GOLD"
                    )
                elif cell_value=='P':
                    self.cells[i][j]["frame"].configure(bg=S.PIT_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.PIT_BG,
                        fg=S.PIT,
                        font=S.TITLE_FONT,
                        text="P"
                    )
                elif cell_value=='W':
                    self.cells[i][j]["frame"].configure(bg=S.WUMPUS_COLOUR)
                    self.cells[i][j]["number"].configure(
                        bg=S.WUMPUS_COLOUR,
                        fg=S.WUMPUS,
                        font=S.TITLE_FONT,
                        text="W"
                    )
                elif cell_value=='S':
                    self.cells[i][j]["frame"].configure(bg=S.STINK_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.STINK,
                        font=S.STINK_FONT,
                        text="Stink"
                    )
                elif cell_value=='B':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.WIND_BG,
                        fg=S.WIND,
                        font=S.DOUBLE_FONT,
                        text="Strong\n Wind"
                    )
                elif cell_value=='PB':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.WIND_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT1,
                        text="Pit \n Strong\n Wind"
                    )
                elif cell_value=='PS':
                    self.cells[i][j]["frame"].configure(bg=S.STINK_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT,
                        text="P \n Stink"
                    )
                elif cell_value=='PSB':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT2,
                        text="P \n Stink \n Strong Wind"
                    )
                elif cell_value=='WB':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.WIND_BG,
                        fg=S.WUMPUS,
                        font=S.DOUBLE_FONT1,
                        text="W \n Strong\n Wind"
                    )
                elif cell_value=='GB':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.GOLD,
                        font=S.DOUBLE_FONT,
                        text="GOLD \n Strong \n Wind"
                    )
                elif cell_value=='GS':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.GOLD,
                        font=S.DOUBLE_FONT,
                        text="GOLD \n Stink"
                    )
                elif cell_value=='PG':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT,
                        text="PIT \n GOLD"
                    )
                elif cell_value=='GSB':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.GOLD,
                        font=S.DOUBLE_FONT1,
                        text="GOLD \n Stink \n Strong \n Wild"
                    )
                elif cell_value=='PGB':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.GOLD,
                        font=S.DOUBLE_FONT1,
                        text="GOLD \n Pit \n Strong \n Wild"
                    )
                elif cell_value=='GPS':
                    self.cells[i][j]["frame"].configure(bg=S.GOLD_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT1,
                        text="GOLD \n Pit \nStink "
                    )
                elif cell_value=='GPSB':
                    self.cells[i][j]["frame"].configure(bg=S.STINK_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.GOLD_BG,
                        fg=S.PIT,
                        font=S.DOUBLE_FONT1,
                        text="GOLD \n Pit \nStink \nS-Wind "
                    )
                elif cell_value=='A':
                    self.cells[i][j]["frame"].configure(bg=S.AGENT_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.AGENT_BG,
                        fg=S.AGENT,
                        font=S.DOUBLE_FONT,
                        text="AGENT"
                    )
                elif cell_value=='AB':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.WIND_BG,
                        fg=S.AGENT,
                        font=S.DOUBLE_FONT1,
                        text="AGENT\nStrong\n Wind"
                    )
                elif cell_value=='AS':
                    self.cells[i][j]["frame"].configure(bg=S.STINK_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.AGENT,
                        font=S.DOUBLE_FONT1,
                        text="AGENT\nStink"
                    )
                elif cell_value=='ASB':
                    self.cells[i][j]["frame"].configure(bg=S.WIND_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.AGENT,
                        font=S.DOUBLE_FONT1,
                        text="AGENT\n Stink \nStrong\n Wind"
                    )
                elif cell_value=='SB':
                    self.cells[i][j]["frame"].configure(bg=S.STINK_BG),
                    self.cells[i][j]["number"].configure(
                        bg=S.STINK_BG,
                        fg=S.WIND,
                        font=S.DOUBLE_FONT1,
                        text="Stink \n Strong\n Wind"
                    )

    def start(self,event): #if function is triggered when spacebar is pressed during stimulation
        #stimulates the gui with next move
        global moves
        global step
        global Agent
        global original_agent
        global pre_dir
        if(step>=len(moves)): #if moves are over end stimulation
            score_frame=tk.Frame(self)
            score_frame.place(relx=0.5,y=30,anchor="center")
            tk.Label(
                score_frame,
                text="*** E N D   O F   S T I M U L A T I O N ***",
                font=S.DOUBLE_FONT
            ).grid(row=0)
            self.score_label=tk.Label(score_frame,text="T h a n k    y o u ",font=S.DOUBLE_FONT1)
            self.score_label.grid(row=1)

        if step<len(moves): #if moves are left
            if(step>=len(moves)):
                game_over_frame=tk.Frame(self.main_grid,borderwidth=4)
                game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
                tk.Label(
                    game_over_frame,
                    text="E N D   O F   S T I M U L A T I O N",
                    bg="#87cefa"
                ).pack()

            else:
                nxt_move=moves[step] #get next move from list
            row=Agent[0]#current location of agent
            col=Agent[1]
            #for each move there is a set of changes needed in the map to update the gui
            if(nxt_move=='move_up'):#if agent moved up
                if(pre_dir=='up'):#if agents previous facing direction is up then its just move forward
                    display_move=" ** ** **  M o v e   -   f o r w a r d  ** ** ** "
                elif(pre_dir=='left'):#similarly other logic is created
                    display_move="** ** ** Turn  Right  and  Move  Forward ** ** **"
                elif(pre_dir=='right'):
                    display_move=" ** ** ** Turn  Left  and  Move  Forward ** ** **"
                else:
                    display_move=" ** *** Turn Right twice and Move Forward  *** **"
                score_frame=tk.Frame(self)#update frame with the move and agents facing direction
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing upwards ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='up'
                #changing the map to update the gui
                if(self.matrix[row][col]=='A'):
                    self.matrix[row][col]='0'
                elif(self.matrix[row][col]=='AB'):
                    self.matrix[row][col]='B'
                elif(self.matrix[row][col]=='AS'):
                    self.matrix[row][col]='S'
                elif(self.matrix[row][col]=='ASB'):
                    self.matrix[row][col]='SB'
                else:
                    self.matrix[row][col]='0'

                if(self.matrix[row-1][col]=='0'):
                    self.matrix[row-1][col]='A'
                elif(self.matrix[row-1][col]=='B'):
                    self.matrix[row-1][col]='AB'
                elif(self.matrix[row-1][col]=='S'):
                    self.matrix[row-1][col]='AS'
                elif(self.matrix[row-1][col]=='SB'):
                    self.matrix[row-1][col]='ASB'
                else:
                    self.matrix[row-1][col]='A'
                Agent=[]
                Agent=[row-1,col] #new agent location
            elif(nxt_move=='move_down'):#similar as above
                if(pre_dir=='down'):
                    display_move=" ** ** **  M o v e   -   f o r w a r d  ** ** ** "
                elif(pre_dir=='left'):
                    display_move=" ** ** ** Turn  Left  and  Move  Forward ** ** **"
                elif(pre_dir=='right'):
                    display_move="** ** ** Turn  Right  and  Move  Forward ** ** **"
                else:
                    display_move=" ** *** Turn Right twice and Move Forward  *** **"
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing downward ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='down'
                if(self.matrix[row][col]=='A'):
                    self.matrix[row][col]='0'
                elif(self.matrix[row][col]=='AB'):
                    self.matrix[row][col]='B'
                elif(self.matrix[row][col]=='AS'):
                    self.matrix[row][col]='S'
                elif(self.matrix[row][col]=='ASB'):
                    self.matrix[row][col]='SB'
                else:
                    self.matrix[row][col]='0'

                if(self.matrix[row+1][col]=='0'):
                    self.matrix[row+1][col]='A'
                elif(self.matrix[row+1][col]=='B'):
                    self.matrix[row+1][col]='AB'
                elif(self.matrix[row+1][col]=='S'):
                    self.matrix[row+1][col]='AS'
                elif(self.matrix[row+1][col]=='SB'):
                    self.matrix[row+1][col]='ASB'
                else:
                    self.matrix[row+1][col]='A'
                Agent=[]
                Agent=[row+1,col]
            elif(nxt_move=='move_right'):
                if(pre_dir=='right'):
                    display_move=" ** ** **  M o v e   -   f o r w a r d  ** ** ** "
                elif(pre_dir=='down'):
                    display_move=" ** ** ** Turn  Left  and  Move  Forward ** ** **"
                elif(pre_dir=='up'):
                    display_move="** ** ** Turn  Right  and  Move  Forward ** ** **"
                else:
                    display_move=" ** *** Turn Right twice and Move Forward  *** **"
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing right direction ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='right'
                if(self.matrix[row][col]=='A'):
                    self.matrix[row][col]='0'
                elif(self.matrix[row][col]=='AB'):
                    self.matrix[row][col]='B'
                elif(self.matrix[row][col]=='AS'):
                    self.matrix[row][col]='S'
                elif(self.matrix[row][col]=='ASB'):
                    self.matrix[row][col]='SB'
                else:
                    self.matrix[row][col]='0'

                if(self.matrix[row][col+1]=='0'):
                    self.matrix[row][col+1]='A'
                elif(self.matrix[row][col+1]=='B'):
                    self.matrix[row][col+1]='AB'
                elif(self.matrix[row][col+1]=='S'):
                    self.matrix[row][col+1]='AS'
                elif(self.matrix[row][col+1]=='SB'):
                    self.matrix[row][col+1]='ASB'
                else:
                    self.matrix[row][col+1]='A'
                Agent=[]
                Agent=[row,col+1]
            elif(nxt_move=='move_left'):
                if(pre_dir=='left'):
                    display_move=" ** ** **  M o v e   -   f o r w a r d  ** ** ** "
                elif(pre_dir=='up'):
                    display_move=" ** ** ** Turn  Left  and  Move  Forward ** ** **"
                elif(pre_dir=='down'):
                    display_move="** ** ** Turn  Right  and  Move  Forward ** ** **"
                else:
                    display_move=" ** *** Turn Right twice and Move Forward  *** **"
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing left direction ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='left'
                if(self.matrix[row][col]=='A'):
                    self.matrix[row][col]='0'
                elif(self.matrix[row][col]=='AB'):
                    self.matrix[row][col]='B'
                elif(self.matrix[row][col]=='AS'):
                    self.matrix[row][col]='S'
                elif(self.matrix[row][col]=='ASB'):
                    self.matrix[row][col]='SB'
                else:
                    self.matrix[row][col]='0'

                if(self.matrix[row][col-1]=='0'):
                    self.matrix[row][col-1]='A'
                elif(self.matrix[row][col-1]=='B'):
                    self.matrix[row][col-1]='AB'
                elif(self.matrix[row][col-1]=='S'):
                    self.matrix[row][col-1]='AS'
                elif(self.matrix[row][col-1]=='SB'):
                    self.matrix[row][col-1]='ASB'
                else:
                    self.matrix[row][col-1]='A'
                Agent=[]
                Agent=[row,col-1]
            elif(nxt_move=='shoot_left'):#shooting the wumpus to left
                display_move=" ** ** ** ** S H O O T   -   L E F T ** ** ** ** "
                if(self.matrix[row][col-1]=='W'): #if there is a wumpus in left remove it ant update map
                    self.matrix[row][col-1]='0'
                elif(self.matrix[row][col-1]=='WB'):
                    self.matrix[row][col-1]='B'
                else:
                    self.matrix[row][col-1]='0'
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing left direction ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='left'
            elif(nxt_move=='shoot_right'):#shooting the wumpus on right similar as above
                if(self.matrix[row][col+1]=='W'):
                    self.matrix[row][col+1]='0'
                elif(self.matrix[row][col+1]=='WB'):
                    self.matrix[row][col+1]='B'
                else:
                    self.matrix[row][col+1]='0'
                display_move=" **** ** ** S H O O T   -   R I G H T ** ** **** "
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing right direction ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='right'
            elif(nxt_move=='shoot_up'):
                if(self.matrix[row-1][col]=='W'):
                    self.matrix[row-1][col]='0'
                elif(self.matrix[row-1][col]=='WB'):
                    self.matrix[row-1][col]='B'
                else:
                    self.matrix[row-1][col]='0'
                display_move=" **** ** **    S H O O T   -   U P    ** ** **** "
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing upwards ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='up'
            elif(nxt_move=='shoot_down'):
                if(self.matrix[row+1][col]=='W'):
                    self.matrix[row+1][col]='0'
                elif(self.matrix[row+1][col]=='WB'):
                    self.matrix[row+1][col]='B'
                else:
                    self.matrix[row+1][col]='0'
                display_move=" **** ** **  S H O O T   -   D O W N  ** ** **** "
                score_frame=tk.Frame(self)
                score_frame.place(relx=0.5,y=30,anchor="center")
                tk.Label(
                    score_frame,
                    text=display_move,
                    font=S.DOUBLE_FONT
                ).grid(row=0)
                self.score_label=tk.Label(score_frame,text=" Agent now facing downward ",font=S.DOUBLE_FONT1)
                self.score_label.grid(row=1)
                pre_dir='down'
            elif(nxt_move=='game_over_pit'):#fell in put
                if(True):
                    game_over_frame=tk.Frame(self.main_grid,borderwidth=8)
                    game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
                    tk.Label(
                        game_over_frame,
                        text="F E L L   I N   P I T!   Y O U   L O S E",
                        font=S.DOUBLE_FONT1,
                        bg="#FFEBCD"
                    ).pack()
            elif(nxt_move=='game_over_wumpus'):#caught by wumpus
                if(True):
                    game_over_frame=tk.Frame(self.main_grid,borderwidth=4)
                    game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
                    tk.Label(
                        game_over_frame,
                        text="A T T A C K E D   B Y   W U M P U S!   Y O U   L O S E",
                        bg="#7fffd4",
                        font=S.DOUBLE_FONT1
                    ).pack()
            elif(nxt_move=='gold'):#found gold
                if(True):
                    game_over_frame=tk.Frame(self.main_grid,borderwidth=4)
                    game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
                    tk.Label(
                        game_over_frame,
                        text="G O L D   F O U N D!   Y O U   W I N",
                        bg="#b29700",
                        font=S.DOUBLE_FONT1
                    ).pack()
            elif(nxt_move=='crash'):#could find a possible move
                if(True):
                    game_over_frame=tk.Frame(self.main_grid,borderwidth=4)
                    game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
                    tk.Label(
                        game_over_frame,
                        text="S O R R Y   A G E N T   C R A S H E D",
                        font=S.DOUBLE_FONT1,
                        bg="#fed8b1"
                    ).pack()
            self.updateGui() #updated the interface
            step+=1 #get the next move index
    def Agentlogic(self):#just a description
        print(" ------------ AGENT LOGIC OF DETECTING PITS AND WUMPUS LOCATIONS --------------")
        print(" [*] All locations of pits, gold, Agent and wumpus are randomly selected according to necessary instructions\n"
              " [*] First agent gets the sence of the initial cell and its adjacent cells\n"
              " [*] Then intializes its view in a map show in the console as agent map\n"
              " [*] Here the agent uses\n "
              "        -> SF to mark Safe locations\n"
              "        -> PP to mark possible pit\n"
              "        -> PW to mark possible wumpus location\n"
              "        -> P to mark pit \n"
              "        -> W to mark wumpus location when identified by logic \n"
              "        -> V to mark visited locations\n"
              " [*] Agent can't see whether the cell has a pit,gold or wumpus\n"
              " [*] Agent check if each adjacent cell is breezy, stink or both\n"
              " [*] If Breeze, mark their adjacent cells as PP unless its V,SF, A or P\n If its already PP then mark it P\n"
              " [*] Similarly is stink, mark as PW. But is Wumpus is allready identified this is not considered\n"
              " [*] Similarly cells with both stink and breeze is marked as PPW- possible wumpus or pit if wumpus not yet found\n Else its PP\n"
              " [*] After senses are analyzed, Agent check is there is only one PW or PPW, hence its must be the Wumpus so Change it to W\n"
              " [*] And also is wumpus is already found, all remaining PW and PPW are change to SF and PP\n"
              " [*] In getting next move first agent check if has SF cells in surrounding in the order up,right,down left\n If there is any more to that cell and mark it V\n"
              " [*] Else it checks whether there are SF cells that it can reach through a safe path without PP,P,W,PW and PPW\nIf a SF cell is found that agent moves to it\n"
              " [*] Else it checks if the surronding cells have a PP cell so that it will take a risk and travel to it\n"
              " [*] Even if the near cells are not PP at this point, agent checks if it can reach a PP that exists in map through a safe path\n"
              " [*] If all these condition failed, Agent just moves near visited cells to check if it can gain a safe path to SF or PP cell but this triggers a crash treeshold\n"
              " [*] If all these condition fail, agent crashes\n"
              " [*] Agent loses if the selected move has a pit or wumpus\n"
              " [*] Agent wins if Gold is found\n"
              " [*] Agent can shoot to wumpus only once and make that cell safe to travel\n"
              " [*] Agent can crash is no possible moves are found according to its knowledge\n "
              " -------------------------------- ENJOY -----------------------------")


WumpusGame() #run the class
