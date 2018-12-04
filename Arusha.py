import discord
import asyncio
import pymysql
import statistics 
import datetime
from discord.ext import commands
#Connections is a file that stores personal details that will not be shared.  
from db_connect import * 

#client = discord.Client()
description = "A bot to help you out with GBF betting!"
client = commands.Bot(command_prefix="!gw ",description= description)

curr_day = 1
curr_GW = 40
curr_ele = "Fire"

#creates a connection to the database under db. Details imported from Connections.py 
db = pymysql.connect(host,username,password,db_name)
#Creates a cursor object
cursor = db.cursor()
#Stores a query into the cursor object

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(description="Retrieves the latest scores for each team",pass_context=True)
async def scores(ctx):
    global curr_GW
    global curr_day
    try:
        cursor.execute("SELECT * FROM Scores WHERE Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
        if cursor.rowcount == 0 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW) + ",day " + str(curr_day))
        else:
            rows = 4
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            message = ""
            for x in range(rows):
                data = cursor.fetchone()
                message += data[2] + ": " + str(data[0]) + " \n"
            else:
                await client.send_message(ctx.message.channel, message)
    except Exception as e:
        await client.send_message(ctx.message.channel, "Something went wrong, please try again!")

@client.command(description="Retrieves the latest 4 scores for North and gives the mean change", pass_context=True)
async def north(ctx):
    global curr_GW
    global curr_day
    try:
        cursor.execute("SELECT * FROM Scores WHERE Team_Name ='North' AND Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
        if cursor.rowcount < 2 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW) + ", day " + str(curr_day))
        else:
            rows = 4
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            message = ""
            scores = []
            for x in range(rows):
                data = cursor.fetchone()
                scores.append(data[0])
                message += data[2] + ": " + str(data[0]) + " \n"
            differences = []
            for x in range(len(scores)-1) :
                differences.append(scores[x+1]-scores[x])
            message = "Recent mean change per hour: " + str(abs(statistics.mean(differences))) + "\n" + message 
            await client.send_message(ctx.message.channel, message)     
    except Exception as e:
        await client.send_message(ctx.message.channel, "Something went wrong, please try again!")

@client.command(description="Retrieves the latest 4 scores for West and gives the mean change", pass_context=True)
async def west(ctx):
    global curr_GW
    global curr_day
    try:
        cursor.execute("SELECT * FROM Scores WHERE Team_Name ='West' AND Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
        rows = 4
        if cursor.rowcount < 2 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW) + ", day " + str(curr_day))
        else:
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            message = ""
            scores = []
            for x in range(rows):
                data = cursor.fetchone()
                scores.append(data[0])
                message += data[2] + ": " + str(data[0]) + " \n"
            differences = []
            for x in range(len(scores)-1) :
                differences.append(scores[x+1]-scores[x])
            message = "Recent mean change per hour: " + str(abs(statistics.mean(differences))) + "\n" + message 
            await client.send_message(ctx.message.channel, message) 
    except Exception as e:
        await client.send_message(ctx.message.channel, "Something went wrong, please try again!")

@client.command(description="Retrieves the latest 4 scores for East and gives the mean change", pass_context=True)
async def east(ctx):
    global curr_GW
    global curr_day
    try:
        cursor.execute("SELECT * FROM Scores WHERE Team_Name ='East' AND Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
        rows = 4
        if cursor.rowcount < 2 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW) + ", day " + str(curr_day))
        else:
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            message = ""
            scores = []
            for x in range(rows):
                data = cursor.fetchone()
                scores.append(data[0])
                message += data[2] + ": " + str(data[0]) + " \n"
            differences = []
            for x in range(len(scores)-1) :
                differences.append(scores[x+1]-scores[x])
            message = "Recent mean change per hour: " + str(abs(statistics.mean(differences))) + "\n" + message 
            await client.send_message(ctx.message.channel, message) 
    except Exception as e:
        await client.send_message(ctx.message.channel, "Something went wrong, please try again!")

@client.command(description="Retrieves the latest 4 scores for South and gives the mean change", pass_context=True)
async def south(ctx):
    global curr_GW
    global curr_day
    try:
        cursor.execute("SELECT * FROM Scores WHERE Team_Name ='South' AND Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
        rows = 4
        if cursor.rowcount < 2 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW) + ", day " + str(curr_day))
        else:
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            message = ""
            scores = []
            for x in range(rows):
                data = cursor.fetchone()
                scores.append(data[0])
                message += data[2] + ": " + str(data[0]) + " \n"
            differences = []
            for x in range(len(scores)-1) :
                differences.append(scores[x+1]-scores[x])
            message = "Recent mean change per hour: " + str(abs(statistics.mean(differences))) + "\n" + message 
            await client.send_message(ctx.message.channel, message) 
    except Exception as e:

        await client.send_message(ctx.message.channel, "Something went wrong, please try again!") 

@client.command(description="Just says hello for testing purposes",pass_context=True)
async def hello(ctx):
    await client.send_message(ctx.message.channel, "hello 2!")

@client.command(description="Shuts down all running instances of the bot. Owner use only",pass_context=True)
async def shutdown(ctx):
    #this ends up just crashing the bot, but it still achives the purpose of closing all instances of the bot that may be up so I cant complain
    if ctx.message.author.id == ownerID : 
        await client.send_message(ctx.message.channel,"See you later!")
        print ("closing")
        exit()
    else :
        await client.send_message(ctx.message.channel,"You dont have permission to use this command")

@client.command(description="Sets the day to use",pass_context=True)
async def set_day(ctx, new_day : str):
    global curr_day
    try:
        new_day = int(new_day)
        curr_day = new_day
        message = "Day set to " + str(curr_day)
        await client.send_message(ctx.message.channel,message)
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel,"That is not a valid input for this command.")

@client.command(description="Sets the GW to use",pass_context=True)
async def set_gw(ctx, new_GW : str):
    global curr_GW
    try:
        new_GW = int(new_GW)
        curr_GW = new_GW
        message = "GW set to " + str(curr_GW)
        await client.send_message(ctx.message.channel,message)
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel,"That is not a valid input for this command.")
@client.command(description="Sets the Element to use",pass_context=True)
async def set_ele(ctx, new_ele : str):
    global curr_ele
    try:
        new_ele = new_ele.lower()
        Elements = {
            "wind": "Wind",
            "earth": "Earth",
            "fire": "Fire",
            "water": "Water",
            "null": "Null"
            }
        if new_ele in Elements :
            curr_ele = Elements[new_ele]
            message = "Element set to " + str(curr_ele)
            await client.send_message(ctx.message.channel,message)  
        else :
          await client.send_message(ctx.message.channel,"That is not a valid element") 
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel,"That is not a valid input")

@client.command(description="Displays the prelims of the selected GW", pass_context = True)
async def prelim(ctx):
    global curr_GW
    try:
        cursor.execute("SELECT * FROM Scores WHERE (Team_Name ='A' OR Team_Name = 'B' OR Team_Name = 'C') AND Day_Number = 0 AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Team_Name")
        if cursor.rowcount == 0 :
            await client.send_message(ctx.message.channel, "There is no data to display for GW " + str(curr_GW))
        else:
            rows = 3
            if cursor.rowcount < 3 :
                rows = cursor.rowcount 
            message = ""
            for x in range(rows):
                data = cursor.fetchone()
                message += data[2] + ": " + str(data[0]) + " \n"
            else:
                message = "The Prelim cutoffs for GW " + str(curr_GW) +"\n" + message
                await client.send_message(ctx.message.channel, message)
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel,"Something went wrong, please try again")

@client.command(description="Inserts new GW scores into the DB", pass_context = True)
async def submit(ctx, nor : str, wes : str, eas : str, sou : str) : 
    try:
        global curr_GW
        global curr_day 
        global curr_ele
        north = int(nor)
        south = int(sou)
        east = int(eas)
        west = int(wes)
        date = datetime.datetime.now()
        #Score / Day / Team / Element / GW num / DateTime
        Starting_sql = "INSERT INTO Scores VALUES "
        n_sql = "( "+str(north)+","+str(curr_day)+","+"'North','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "'),"
        w_sql = "( "+str(west)+","+str(curr_day)+","+"'West','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "'),"
        e_sql = "( "+str(east)+","+str(curr_day)+","+"'East','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "'),"
        s_sql = "( "+str(south)+","+str(curr_day)+","+"'South','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "');"

        cursor.execute(Starting_sql+n_sql+w_sql+e_sql+s_sql)
        db.commit()
        await client.send_message(ctx.message.channel, "Thank you for submitting the current score")
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel, "Invalid input. Please use only numbers.")
@client.command(description="Inserts a new prelim score into the GW", pass_context = True)
async def submit_prelim(ctx, A : str, B : str, C : str) : 
    try:
        global curr_GW
        global curr_day 
        global curr_ele
        pre_A = int(A)
        pre_B = int(B)
        pre_C = int(C)
        date = datetime.datetime.now()
        cursor.execute("SELECT * FROM Scores WHERE (Team_Name ='A' OR Team_Name = 'B' OR Team_Name = 'C') AND Day_Number = 0 AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Team_Name")
        if cursor.rowcount == 0 : 
            #Score / Day / Team / Element / GW num / DateTime
            Starting_sql = "INSERT INTO Scores VALUES "
            A_sql = "( "+str(pre_A)+",0,"+"'A','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "'),"
            B_sql = "( "+str(pre_B)+",0,"+"'B','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "'),"
            C_sql = "( "+str(pre_C)+",0,"+"'C','"+str(curr_ele)+"',"+str(curr_GW)+",'"+str(date) + "');"

            cursor.execute(Starting_sql+A_sql+B_sql+C_sql)
            db.commit()
            await client.send_message(ctx.message.channel, "Thank you for submitting the current score")
        else : 
            await client.send_message(ctx.message.channel, "That GW already has the prelims submitted")
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel, "Invalid input. Please use only numbers.")

@client.command(description="Gives the mean increase per hour for each ",pass_context = True)
async def means(ctx) :
    global curr_day
    global curr_GW

    try:
        teams = ["North","East","South","West"]
        message = "These are the average of each teams past 4 hourly gains \n"
        #iterates through scores to fill each value up one a time
        for x in range(len(teams)) :
            temp = []
            cursor.execute("SELECT * FROM Scores WHERE Team_Name = '" + teams[x] + "' AND Day_Number = " + str(curr_day) + " AND GW_Number = " + str(curr_GW) + " ORDER BY GW_Number DESC, Day_Number DESC, `Time` DESC")
            rows = 4
            if cursor.rowcount < 4 :
                rows = cursor.rowcount 
            #fills up the score[x] array with values to get the mean of later
            for y in range(rows) :
                data = cursor.fetchone()
                temp.append(data[0])
            #finds the differences of each one
            differences = []
            for y in range(len(temp)-1) :
                differences.append(temp[y+1]-temp[y])
            message = message + teams[x] + " : " + str(abs(statistics.mean(differences))) +"\n"
        await client.send_message(ctx.message.channel, message)
    except Exception as e:
        print(e)
        await client.send_message(ctx.message.channel,"Something went wrong, please try again")

client.run(Token)