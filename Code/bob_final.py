import tkinter
from tkinter import Tk,Canvas,Frame,Button,LEFT,RIGHT,messagebox,CURRENT
from random import randint
from socket import *
from time import ctime
import threading


HOST = '127.0.0.1'
PORT = 30009
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

root=Tk()
root.title('BOB')
canvas=Canvas(root,width=680,height=250)

moves=[]


def create_pile():
	global pieces,board,piece_name
	pieces=[7,5,3]
	board=[[1,1,1,1,1,1,1],[1,1,1,1,1],[1,1,1]]
	piece_name="NEW_GAME"
	circle_size=50
	linecolour="black"
	fillcolour="yellow"
	#Group A is on the left,it is a group of 7
	A1x=50
	A1y=50
	A2x=110
	A2y=50
	A3x=20
	A3y=105
	A4x=80
	A4y=105
	A5x=140
	A5y=105
	A6x=50
	A6y=160
	A7x=110
	A7y=160

	canvas.create_oval(A1x,A1y,A1x+circle_size,A1y+circle_size,outline=linecolour,fill=fillcolour,tags="A1")
	canvas.create_oval(A2x,A2y,A2x+circle_size,A2y+circle_size,outline=linecolour,fill=fillcolour,tags="A2")
	canvas.create_oval(A3x,A3y,A3x+circle_size,A3y+circle_size,outline=linecolour,fill=fillcolour,tags="A3")
	canvas.create_oval(A4x,A4y,A4x+circle_size,A4y+circle_size,outline=linecolour,fill=fillcolour,tags="A4")
	canvas.create_oval(A5x,A5y,A5x+circle_size,A5y+circle_size,outline=linecolour,fill=fillcolour,tags="A5")
	canvas.create_oval(A6x,A6y,A6x+circle_size,A6y+circle_size,outline=linecolour,fill=fillcolour,tags="A6")
	canvas.create_oval(A7x,A7y,A7x+circle_size,A7y+circle_size,outline=linecolour,fill=fillcolour,tags="A7")

	B1x=330
	B1y=65
	B2x=280
	B2y=105
	B3x=380
	B3y=105
	B4x=300
	B4y=160
	B5x=360
	B5y=160
	canvas.create_oval(B1x,B1y,B1x+circle_size,B1y+circle_size,outline=linecolour,fill=fillcolour,tags="B1")
	canvas.create_oval(B2x,B2y,B2x+circle_size,B2y+circle_size,outline=linecolour,fill=fillcolour,tags="B2")
	canvas.create_oval(B3x,B3y,B3x+circle_size,B3y+circle_size,outline=linecolour,fill=fillcolour,tags="B3")
	canvas.create_oval(B4x,B4y,B4x+circle_size,B4y+circle_size,outline=linecolour,fill=fillcolour,tags="B4")
	canvas.create_oval(B5x,B5y,B5x+circle_size,B5y+circle_size,outline=linecolour,fill=fillcolour,tags="B5")

	C1x=570
	C1y=105
	C2x=540
	C2y=160
	C3x=600
	C3y=160
	canvas.create_oval(C1x,C1y,C1x+circle_size,C1y+circle_size,outline=linecolour,fill=fillcolour,tags="C1")
	canvas.create_oval(C2x,C2y,C2x+circle_size,C2y+circle_size,outline=linecolour,fill=fillcolour,tags="C2")
	canvas.create_oval(C3x,C3y,C3x+circle_size,C3y+circle_size,outline=linecolour,fill=fillcolour,tags="C3")

def create_DONE_button():
	canvas.create_rectangle(500,1,680,70, outline="black",fill="gray80",tags="DONE")
	canvas.create_text(580,30,text="I'm done",font="Purisa",tags="DONE")

def create_operation_buttons():
	operation_frame=Frame()
	operation_frame.pack(fill="both",expand=True)
	Start=Button(operation_frame,text='Click here to start a new game',height=2,command=start_game,bg='white',fg='navy')
	Start.pack(fill="both",expand=True,side=LEFT)
	Rules=Button(operation_frame,text='Click here to see the rules',command=show_rules,height=2,bg='navy',fg='white')
	Rules.pack(fill="both",expand=True,side=RIGHT)


def start_game():
	#this turna all the ovals into buttons to be activated by a mouse click.
	create_pile()
	create_DONE_button()
	canvas.delete('win')
	canvas.delete("BC")
	canvas.delete("AC")
	Bob_to_play()
	canvas.bind("<Button-1>",func=on_click)
def show_rules():
		rules_intro = 'Welcome to Nim, a game with more strategy than may first appear!\n'
		game_play = 'Playing Nim involves each player taking pieces from the game screen in turns.\n'
		rule1 = 'Your goal is to pick up the last piece .\n'
		rule2 = 'You may only take from one pile each turn.\n'
		rule3 = 'You can take as many pieces as you want each turn.\n\n'
		operation = 'When you are done with your turn, please click the button in the top right corner to let the opponent know that he/she can play.'
		rule_message = rules_intro+game_play+rule1+rule2+rule3+operation
		messagebox.showinfo("How to play Nim", rule_message)


def get_data():
	data=tcpCliSock.recv(BUFSIZ)
	return data.decode('utf-8')
def send_data(h):
	tcpCliSock.send(bytes(x),'utf-8')

def on_click(event):
	#deals with actions from clicks based on the name of the button clicked on
	if canvas.find_withtag(CURRENT):
		global last_piece,piece_name
		piece_name=canvas.gettags(CURRENT)[0]
		group_name=piece_name[0]
		#i.e gettags gives "A1" for eg, group_name will be A,i.e heap 1
		if pieces==[7,5,3]:
			last_piece=None
			#i.e the initial heap is intact
			
		try:
			
			if group_name!=last_piece and last_piece !=None and piece_name!='DONE':
			#when the player is playing and has not yet clicked turn done buttton
				#display illegal move warning for 1.5 secs if the user tries to pick pieces from different piles on the same turn
				canvas.create_text(355,40,text="ILLEGAL MOVE",font="Purisa",tags="ILLEGAL_WARNING", fill="black",command=None)
				canvas.update_idletasks() 
						#does not let the user click done button more than once in a row.	canvas.after(1500)
				canvas.delete("ILLEGAL_WARNING")


			else:
				if piece_name=='DONE' and last_piece!='DONE' and last_piece!=None:
					last_piece=None
					canvas.delete("AC")
					if boardsum(board)==0: #when the nsum of the elements in the heap==0
						end_game('Bob')
					else:					
						canvas.create_text(355,80,text="",font="Purisa",tags="BC",fill="black",command=None)
						Bob_to_play()

				elif piece_name=='DONE' and last_piece==None:
					#does not let the player click the done button more than once in a row
					canvas.create_text(355,40,text="YOU HAVE NOT MADE ANY MOVES",font="Purisa",tags="DOUBLE_DONE",fill="black",command=None)
					canvas.update_idletasks()
					canvas.after(1500)
					canvas.delete("DOUBLE_DONE")
				elif piece_name=='win':
					pass	
				
				else:
					canvas.create_text(355,50,text="",font="Purisa",tags="AC",fill="black",command=None)
					canvas.delete("BC")
					update_board(piece_name)
					moves.append(piece_name)
					canvas.delete(piece_name)
					last_piece=piece_name[0] #i.e getting the heap from where it was removed ,A1[0]=A heap
				
					if boardsum(board)==0: #when the nsum of the elements in the heap==0
						end_game('Bob')
					
		except NameError:
			last_piece=group_name
			if piece_name=='DONE':
				canvas.delete('AC')
				Bob_to_play()
			elif piece_name=='WON_BUTTON':
				pass
			else:
				update_board(piece_name)
				canvas.delete(piece_name)
				last_piece=piece_name[0]
				if boardsum(board)==0:
					end_game('Alice')
		
''
def update_board(piece_names):
	   # the board had two representations, the "pieces" representation is [7,5,3].
    # the "board" representation has all the pieces and looks like [[1,1,1,1,1,1,1],[1,1,1,1,1],[1,1,1]].
	update_board_pieces(piece_names)

def update_board_pieces(piece_name):
    # this part adjusts the mathematical representations of the board, being the [7,5,3] and [[1,1,1,1,1,1,1],[1,1,1,1,1],[1,1,1]] arrays.
    # these arrays are global variables defined when the board is created
	group_name = piece_name[0]
	if group_name == 'A':
		pieces[0]-=1
		
	elif group_name == 'B':
		pieces[1] -= 1
		
	elif group_name == 'C':
		pieces[2] -= 1
		
	if piece_name == 'A1':
		board[0][0] = 0
		
	elif piece_name == 'A2':
		board[0][1] = 0
		
	elif piece_name == 'A3':
		board[0][2] = 0
		
	elif piece_name == 'A4':
		board[0][3] = 0
		
	elif piece_name == 'A5':
		board[0][4] = 0
		
	elif piece_name == 'A6':
		board[0][5] = 0
		
	elif piece_name == 'A7':
		board[0][6] = 0
		
	elif piece_name == 'B1':
		board[1][0] = 0

	elif piece_name == 'B2':
		board[1][1] = 0

	elif piece_name == 'B3':
		board[1][2] = 0

	elif piece_name == 'B4':
		board[1][3] = 0

	elif piece_name == 'B5':
		board[1][4] = 0

	elif piece_name == 'C1':
		board[2][0] = 0

	elif piece_name == 'C2':
		board[2][1] = 0

	elif piece_name == 'C3':
		board[2][2] = 0

#to get board sum
def boardsum(board):
	s=0
	for i in range(len(board)):
		for j in range(len(board[i])):
			s=s+board[i][j]
	return s

def end_game(winner):
	board=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0]]
	p = ['A', 'B', 'C']	
	l = []
	canvas.delete('BC')
	canvas.delete('AC')
	canvas.delete('DONE')
	for i in range(1,8):
		l.append(p[0]+str(i))
	for i in range(1,6):
		l.append(p[1]+str(i))
	for i in range(1,4):
		l.append(p[2]+str(i))
	for i in l:
		canvas.delete(i)
	send_moves(moves)
	canvas.create_text(200, 50, text= winner+" won !!!", font="Purisa", tags="win", fill="black",command=None)

def recv_moves():
    data = tcpCliSock.recv(BUFSIZ)
    print(data)
    inp = (data.decode('utf-8')).split()	
    if (inp[0] == -1):
	    end_game(inp[1])         
    return inp

def send_moves(moves):
    data = " ".join(moves)
    print(data)
    tcpCliSock.send(bytes(str(data), 'utf-8'))
    print(moves)
	

def Bob_to_play():
	global moves
	print(moves)
	send_moves(moves) #send what alice does
	#moves=[]
	x=recv_moves()
	print(board)
	for i in range(len(x)):
		
		update_board_pieces(x[i])
		canvas.delete(x[i])
	moves = []
	if boardsum(board)==0: #when the nsum of the elements in the heap==0
		canvas.delete("DONE")
		canvas.delete("AC")
		canvas.delete("BC")
		end_game('Alice')
	print(board)
	
canvas.pack()
create_pile()
create_operation_buttons()


root.mainloop()
