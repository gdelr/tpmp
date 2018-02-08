import socket
from Mock_input import PressKey, ReleaseKey
import time
 
### Options (Don't edit)
SERVER = "irc.twitch.tv"  # server
PORT = 6667  # port
### Options (Edit this)
PASS = "oauth:61typskxa4tkrdoy1zypux508ie00r"  # bot password can be found on https://twitchapps.com/tmi/
BOT = "pig_bot"  # Bot's name [NO CAPITALS]
CHANNEL = "iampigss"  # Channal name [NO CAPITALS]
OWNER = "gabe"  # Owner's name [NO CAPITALS]
 
### Functions
 
def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())
 
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user
def getMessage(line):
    global message
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message
def joinchat():
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loadingCompleted(line)
    sendMessage(s, "Chat room joined!")
    print("Bot has joined " + CHANNEL + " Channel!")
 
def loadingCompleted(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
### Code runs
s_prep = socket.socket()
s_prep.connect((SERVER, PORT))
s_prep.send(("PASS " + PASS + "\r\n").encode())
s_prep.send(("NICK " + BOT + "\r\n").encode())
s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
s = s_prep
joinchat()
readbuffer = ""
 
def Console(line):
    # gets if it is a user or twitch server
    if "PRIVMSG" in line:
        return False
    else:
        return True
 
 
while True:
        try:
            readbuffer = s.recv(1024)
            readbuffer = readbuffer.decode()
            temp = readbuffer.split("\n")
            readbuffer = readbuffer.encode()
            readbuffer = temp.pop()
        except:
            temp = ""
        for line in temp:
            if line == "":
                break
            # So twitch doesn't timeout the bot.
            if "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                s.send(msgg)
                print(msgg)
                break
            # get user
            user = getUser(line)
            # get message send by user
            message = getMessage(line)
            # for you to see the chat from CMD
            print(user + " > " + message)
            # sends private msg to the user (start line)
            PMSG = "/w " + user + " "
 
            if "Up" in message or "up" in message: #w
                PressKey(0x57)
                time.sleep(1/7)
                ReleaseKey(0x57)
                break
            elif "Left" in message or "left" in message: #a
                PressKey(0x41)
                time.sleep(1/7)
                ReleaseKey(0x41)
                break
            elif "Down" in message or "down" in message: #s
                PressKey(0x53)
                time.sleep(1/7)
                ReleaseKey(0x53)
                break
            elif "Right" in message or "right" in message: #d
                PressKey(0x44)
                time.sleep(1/7)
                ReleaseKey(0x44)
                break
            elif "A" in  message: #f
                PressKey(0x46)
                time.sleep(1/7)
                ReleaseKey(0x46)
                break
            elif "B" in message or "b" in message:  #shift
                PressKey(0x10)
                time.sleep(1/7)
                ReleaseKey(0x10)
                break
            elif "Start" in message or "start" in message: #space
                PressKey(0x58)
                time.sleep(1/7)
                ReleaseKey(0x58)
                break
