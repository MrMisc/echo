import re
from ast import Num
import discord
import numpy as np
import numexpr as ne
from sympy import Derivative, Symbol, symbols
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands, tasks
import datetime
import itertools
from datetime import datetime, timezone, date
import matplotlib.pyplot as plt
from matplotlib import colors
from plotly.offline import plot
from matplotlib.ticker import PercentFormatter
import os
import requests
import schedule
import asyncio
import time
import random
import queue
from urllib.request import Request, urlopen
import sched
from bs4 import BeautifulSoup
import numexpr as ne
import pickle

from urllib.request import Request, urlopen
from urllib.error import HTTPError ####
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import Image
import seaborn as sns
import math
import matplotlib as faggot

from threading import Thread



intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 'S', Intents = intents)

Bot = discord.Client(intents=intents)
dick = 0


animalswikia = f'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SGD'
Req = Request(animalswikia)
uClient = urlopen(Req)
soup = BeautifulSoup(uClient.read(), 'html5lib')
txt = soup.find('p',{'class':"result__BigRate-sc-1bsijpp-1 iGrAod"}).text
rate = float(txt.split(' S')[0])   




def pitychaintilldeath(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!!
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    level=1
    string = ' '
    xxxx = [float(x) for x in args]
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    while count < int(faith)+1 and level+lastroll<len(args)+1:
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
        elif level+lastroll>1 and string.split(' ')[-1] == 'False':
            level-=0
            string+='True '
            count+=1
        elif level+lastroll>1:
            level-=1
    return string







def pitychaintilldeath0(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!! 100% false dependent.
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    xxxx = [float(x) for x in args]
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    while countFalses(string) < int(faith) and level+lastroll<len(args)+1:
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
        elif level+lastroll>1 and string.split(' ')[-1] == 'False':
            level-=0
            string+='True '
            count+=1
        elif level+lastroll>1:
            level-=1
    return string







n=[]



async def time_check():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(620593416757182474)    #Pulse channel
        schannel = client.get_channel(620604577288290314)
        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
        json_data = requests.get(rss_address).json()
        magn = float(json_data['features'][0]['properties']['mag'])
        loc = json_data['features'][0]['properties']['place']
        timedispLat = json_data['features'][0]['properties']['updated'] - json_data['features'][0]['properties']['time']
        T = lambda: int(round(time.time() * 1000))
        timeepochmodified = T()/1000
        normaltime = datetime.fromtimestamp(timeepochmodified, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
        timeattainLat = T() - json_data['features'][0]['properties']['time']

        global n
        if (loc not in n):
            n.append(loc)
            # print(n)
            await channel.send(f'``{loc}:{magn}@ {normaltime}\n Processing Delay:{timedispLat//1000}s , API Delay:{timeattainLat//1000}s ``')
            await schannel.send(f'``{loc}:{magn} @ {normaltime}\n Processing Delay:{timedispLat//1000}s , API Delay:{timeattainLat//1000}s ``')


            if len(n)>=10:
                n = n[9:10]


        await asyncio.sleep(5)





client.loop.create_task(time_check())








@client.event
async def on_ready():
    print("Boop!")


@client.command()
@commands.has_role("Duke")
async def stop(ctx):
    await client.logout()


@client.command()
async def react(ctx):
    choices = ["Boop? O3O", '{◕ ◡ ◕} \n beep boop']
    await ctx.send(random.choice(choices))



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()


@client.command()
@commands.has_role("Team Lucid")
async def StarmatrixNB(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    faith = max(len(args),faith)
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    for i in range(int(trials)):
        nall = []
        count = 1
        lasttime = 0
        checkthis = pitychaintilldeath(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis = pitychaintilldeath(lasttime, faith, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')





@client.command(brief = '<Number of pings/samples you want> ', description = "This command pings all the channels in maple. Requires Duke role \n While more samples will give a better average, taking samples above 20 would likely lead you to getting ping behaviour that is rather different for the appx 1/2h or so that you are playing for. Channels are inconsistent. \n Number of pings recommended prior to doing a boss run for instance is probably about 20-30. \n Note also that each ping takes about 4.5 seconds")
@commands.has_role("Duke")
async def _maple_ping(ctx, noofpings, cute_norm = 2):
    schannel = client.get_channel(892205198456533022)
    N_TRIES = min(60**2, int(noofpings))
    await schannel.send(f"``Commencing maple-reboot channel ping analysis for norm of {cute_norm} with {noofpings} pings...``")
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'E:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        print(len(source))
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        try:
            number = min(channels)-1
            for j in channels:
                matr[row][j-1] += PING[number]
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except: pass
    MEAN = [np.median([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))] #changed from 30 to len(source) for longevity
    if int(cute_norm)==2:STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    else:
        MINUS = [np.array(matr[:, channel]) /MEAN[channel] for channel in range(len(source))]
        def norm(array, dyn):
            sum=0
            for thing in array:
                sum+=thing**dyn
            return sum**(1/dyn)
        STD = [norm(error, int(cute_norm)) for error in MINUS]
    #Let us try rearranging the parent matr matrix in order to get sexier plots. We shall use the standard dev values in STD!
    sortedmatrixsortof = [list(np.transpose(matr)[i-1]) for __,i in sorted(zip(STD,channels))]
    new_matr = np.zeros([len(source),N_TRIES])
    for i in range(len(new_matr)):
        for j in range(len(new_matr[i])):
            new_matr[i,j] += sortedmatrixsortof[i][j]
    Channelssorted = [i for __,i in sorted(zip(STD,channels))]
    x_axis = np.arange(1,N_TRIES+1) #####################
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    await schannel.send(f"```{ctx.message.author}'s Request for ping over {N_TRIES} samples with norm of {cute_norm} acquired!```")
    print(type(sortedmatrixsortof))
    # plt.figure(figsize=(4.1*2.5,4.1))
    if int(noofpings)<21:plt.figure(figsize=(15,8))
    else:plt.figure(figsize=(25,10))
    RAND = np.random.uniform(10,20)
    for repeat in range(3):
        plt.clf()
        plt.style.use("seaborn-dark")
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey
        split = 0
        for idx, row in enumerate(np.transpose(np.transpose(new_matr)[:,repeat*10:(repeat+1)*10])): #@@7z. Senpai wish me luck o3o
            plt.grid(color='#2A3459')
            if split <5:
                plt.subplot(1,2,1)
                stringofchannels = ''
                for i in range(5):
                    stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                plt.title(f"Channels {stringofchannels}")
                # plt.subplots_adjust(wspace=3, hspace=3)
            else:
                plt.subplot(1,2,2)
                stringofchannels = ''
                for i in range(5,10):
                    stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                plt.title(f"Channels {stringofchannels}")
                # plt.subplots_adjust(wspace=1, hspace=1)
            number_of_colors = len(source)
            C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
            # print(color)
            MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
            size = 12
            plt.ylabel("NZ ping/ms")
            plt.plot(x_axis, row, label = f" Ch {Channelssorted[repeat*10+idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
            n_lines = 12
            diff_linewidth = 1.02
            alpha_value = 0.02 #0.03
            for n in range(1, n_lines+1):
                plt.plot(x_axis,row,
                        linewidth=2+(diff_linewidth*n),
                        alpha=alpha_value,
                        color=C0L, ms = size)
            leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 22})
            leg.get_frame().set_alpha(0.7)
            plt.xlabel("Ping attempts")

            #Here was the title line
            split+=1
        plt.savefig(fname='plot')
        await schannel.send(file=discord.File('plot.png'))
        os.remove('plot.png') ############
    STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    L10 = [norm(error, 10) for error in MINUS]
    await schannel.send(f'``The lowest mean server is Channel {MEAN.index(min(MEAN))+1}: with sd {STD[MEAN.index(min(MEAN))]}``')
    mean = np.copy(MEAN)
    await schannel.send(f'``Alternatives would be Channel {MEAN.index(sorted(mean)[1])+1}, {MEAN.index(sorted(mean)[2])+1}, or {MEAN.index(sorted(mean)[3])+1}``')
    await schannel.send(f'``The least variant server is Channel {STD.index(min(STD))+1}: {MEAN[STD.index(min(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(min(STD))]}``')
    std = np.copy(STD)
    await schannel.send(f'``Alternatives would be Channel {STD.index(sorted(std)[1])+1}, {STD.index(sorted(std)[2])+1}, or {STD.index(sorted(std)[3])+1}``')
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    await schannel.send(f'``Fun fact: the channel with the highest ping is Channel {MEAN.index(max(MEAN))+1}: {MEAN[MEAN.index(max(MEAN))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[MEAN.index(max(MEAN))]}``')
    await schannel.send(f'``The channel with the most variant ping is Channel {STD.index(max(STD))+1}: {MEAN[STD.index(max(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(max(STD))]}``')
    source_copy = np.copy(source)
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > 2]
    var = 2
    if len(UNS) >27:
        var = .75*(max(L10) - min(L10)) + min(L10)
        UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > var]
    uns = " "
    for i in UNS: uns+=i + ", "
    ORDER_OF_CHAOS = [channel for _,channel in sorted(zip(L10, source_copy))]
    await schannel.send(f'**Warning**: ``Detecting severe relative instabilities in  {ORDER_OF_CHAOS[-1]}, {ORDER_OF_CHAOS[-2]}, or {ORDER_OF_CHAOS[-3]}!! \n List of Channels with >{var} L10 norm : {uns}``  ')
    await schannel.send(f'``Instead, consider these if anything else -  {ORDER_OF_CHAOS[0]}, {ORDER_OF_CHAOS[1]}, {ORDER_OF_CHAOS[2]}, or {ORDER_OF_CHAOS[3]}.``  ')




#Command to add regular entry to watch price of
@client.command()
@commands.has_role("Duke")
async def removesearchterm_etsy(ctx,URL,price=None):
    searchterms = open('E:\\My_Favourite_Whale\\pricewatch','rb')
    whattosearch = [x for x in pickle.load(searchterms)]
    searchterms.close()    
    stringo="```"
    for i in range(len(whattosearch)):
        stringo+=f"[{i}]."+i[0]+'\n'
    await ctx.send(stringo+"```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)    
    no = 0
    while True:
        try:
            no=int(float(morecontent.content))
            break
        except:pass
    del whattosearch[no]
    print(whattosearch)
    uwupickle = open('pricewatch','wb')
    pickle.dump(whattosearch,uwupickle)
    uwupickle.close()   
    await ctx.send("Pricewatch list has been updated :>")      
    

#Command to add regular entry to watch price of
@client.command()
@commands.has_role("Duke")
async def addsearchterm_etsy(ctx,URL,price=None):
    searchterms = open('E:\\My_Favourite_Whale\\pricewatch','rb')
    whattosearch = [x for x in pickle.load(searchterms)]
    searchterms.close()
    listinsidelist = []
    listinsidelist.append(URL)
    if price!=None:
        while True:
            try:
                cost = float(price)
                listinsidelist.append(cost)
                break
            except:pass
    else:
        Req = Request(URL)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        trim = re.compile(r'[^\d.,]+')
        mystring = soup.find('p',{'class':'wt-text-title-03'}).find_all('span')[-1].text
        result = trim.sub('', mystring)        
        listinsidelist.append(float(result))
    print(listinsidelist)
    whattosearch.append(listinsidelist)
    searchterms1 = open('E:\\My_Favourite_Whale\\pricewatch','wb')
    pickle.dump(whattosearch,searchterms1)
    searchterms1.close()    
    await ctx.send("Entry has been added :>")


#Command to search database of etsy saved for SA keycaps
@client.command()
@commands.has_role("Duke")
async def SA(ctx):
    importedpickle = open('E:\\My_Favourite_Whale\\n1','rb')
    NEW_ = pickle.load(importedpickle)
    importedpickle.close()    
    colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
    count=0
    print(count)
    stringo=''
    for x in NEW_:
        Sections = x.split('\n')
        count=count
        stringo+='\n'+f"[{count}.]"
        emb_message = discord.Embed(title = f"{Sections[0].split(':')[1]}", color = random.choice(colours))
        for i in Sections[0].split(':')[1].split(' ')[:4]:
            stringo+=i+' '
        stringo+=' '*(50-len(stringo.split('\n')[-1])) 
        if Sections[1][10].isdigit():
            emb_message.add_field(name = 'Price', value = f"{float(Sections[1][10:].split(' ')[0])*rate} SGD" )
            stringo+=f"{float(Sections[1][10:].split(' ')[0])*rate} SGD"
        else:
            # print(Sections[1][21:].split(' ')[0])
            emb_message.add_field(name = 'Price', value = f"{float(Sections[1][21:].split(' ')[0])*rate} SGD" )
            stringo+=f"{float(Sections[1][21:].split(' ')[0])*rate:.2f} SGD"
        #Extracting link
        stringo+='     '
        if len(Sections[2].split('|')[1])<2000:
            try:emb_message.add_field(name = 'Link', value = f"{Sections[2].split('|')[1]}" )
            except:pass
        # stringo+=Sections[2].split('|')[1]+'        '
        stringo+='\n'
        emb_message.set_author(name = "Etsy", icon_url = "https://th.bing.com/th/id/OIP.fMDcFM0oJwZgykDHz6CTogHaHa?pid=ImgDet&rs=1")
        if len(NEW_)<6:await ctx.send(content = None, embed = emb_message)
        count+=1
    if len(stringo)>2000:
        for i in range(0,len(stringo),1900):
            await ctx.send('```'+stringo[i:i+1900]+'```')
    else:
        await ctx.send('```'+stringo+'```')    



@client.command()
@commands.has_role("Team Lucid")
async def ImpStarmatrixNB(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    for i in range(int(trials)):
        nall = []
        count = 1
        lasttime = 0
        checkthis = pitychaintilldeath0(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis = pitychaintilldeath0(lasttime, faith, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

  


@client.command()
@commands.has_role("Team Lucid")
async def Starhist(ctx, trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    trials = int(trials)
    plt.clf()
    faith = abs(int(faith))
    faith = max(len(args),faith)
    await ctx.send(f"```Do you want an impulsive, fail averse approach? Please state <Yes/No/Both> <Amount of fails you are willing to tolerate before abandoning attempt>```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    impulsive = False
    FailCapacity = 0
    try:
        listo = str(morecontent.content).split(' ')
        if listo[0] != 'No':
            impuslive = True
            FailCapacity = int(listo[1])
        else:
            pass
    except:
        pass
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    for i in range(int(trials)):
        count = 1
        lasttime = 0
        if impulsive: checkthis = pitychaintilldeath0(lasttime, faith, *args) #first run
        else : checkthis = pitychaintilldeath(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            if impulsive: checkthis = pitychaintilldeath0(lasttime, faith, *args)
            else : checkthis = pitychaintilldeath(lasttime, faith, *args)
            #print(checkthis)
        data.append(count)
    legend = ['distribution']
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success")
    # Creating histogram
    fig, axs = plt.subplots(1, 1,
                            figsize =(20, 10),
                            tight_layout = True, alpha = 0.3)
     
     
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        axs.spines[s].set_visible(False)
     
    # Remove x, y ticks
    axs.xaxis.set_ticks_position('none')
    axs.yaxis.set_ticks_position('none')
       
    # Add padding between axes and labels
    axs.xaxis.set_tick_params(pad = 5)
    axs.yaxis.set_tick_params(pad = 10)
     
    # Add x, y gridlines
    axs.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5)
     
    # Add Text watermark
    fig.text(0.9, 0.15, 'Viridis colour palette corresponds to first simulation \n plasma colour set corresponds to second simulation',
             fontsize = 12,
             color ='red',
             ha ='right',
             va ='bottom',
             alpha = 0.7)
     
    # Creating histogram
    N, bins, patches = axs.hist(data, bins = int(trials**0.7), alpha = 0.6)
     
    # Setting color
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
     
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.winter(norm(thisfrac))
        thispatch.set_facecolor(color)
     
    # Adding extra features   
    plt.xlabel("X-axis")
    plt.ylabel("y-axis")
    plt.legend(legend)
    plt.title('Customized histogram')
    #plt.savefig(fname='plot2')
    #await ctx.send(file=discord.File('plot2.png'))
    await ctx.send(f"```Again. Are we conducting an impulsive, fail averse approach this time? Please state <Yes/No/Both> <Amount of fails you are willing to tolerate before abandoning attempt>```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    impulsive = False
    FailCapacity = 0
    try:
        listo = str(morecontent.content).split(' ')
        if listo[0] != 'No':
            impuslive = True
            FailCapacity = int(listo[1])
        else:
            pass
    except:
        pass
    await ctx.send(f"```Provide the second simulation parameters : <Number of trials> <Number of attempts*> <prob1> <prob2> ...```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    trials = int(str(morecontent.content).split(' ')[0])
    faith = int(str(morecontent.content).split(' ')[1])
    args = str(morecontent.content).split(' ')[2:]
    ARGS = [float(x) for x in args]
    data = []  #Number of tries it took until we got a success and stopped the trial
    for i in range(int(trials)):
        count = 1
        lasttime = 0
        if impulsive: checkthis = pitychaintilldeath0(lasttime, faith, *ARGS) #first run
        else : checkthis = pitychaintilldeath(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            if impulsive: checkthis = pitychaintilldeath0(lasttime, faith, *args)
            else : checkthis = pitychaintilldeath(lasttime, faith, *args)
            #print(checkthis)
        data.append(count)
    legend = ['distribution']
    x = np.linspace(1,int(trials),int(trials))    
    N, bins, patches = axs.hist(data, bins = int(trials**0.7))
     
    # Setting color
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
     
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.copper(norm(thisfrac))
        thispatch.set_facecolor(color)
    plt.legend()
    plt.savefig(fname='plot2')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')  






@client.command()
@commands.has_role("Team Lucid")
async def Starhist2(ctx, trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    c1 = trials+' ' + faith
    trials = int(trials)
    plt.clf()
    faith = abs(int(faith))
    faith = max(len(args),faith)
    await ctx.send(f"```Do you want an impulsive, fail averse approach? Please state <Yes/No/Both> <Amount of fails you are willing to tolerate before abandoning attempt>```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    imp1 = morecontent.content
    impulsive = False
    FailCapacity = 0
    try:
        listo = str(morecontent.content).split(' ')
        if listo[0].lower() != 'no':
            impuslive = True
            FailCapacity = int(listo[1])
        else:
            pass
    except:
        pass
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    tapdata = []
    for i in range(int(trials)):
        count = 1
        taps = 0
        lasttime = 0
        if impulsive: 
            checkthis = pitychaintilldeath0(lasttime, faith, *args) #first run
            taps += len(checkthis.split(' '))
        else : 
            checkthis = pitychaintilldeath(lasttime, faith, *args) #first run
            taps += len(checkthis.split(' '))
        print(checkthis) #print the string of results for the first batch of runs
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            print(checkthis) #just to double check that the checkthis from outside is being recognised at the start and being updated accorindgly
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            if impulsive: 
                checkthis = pitychaintilldeath0(lasttime, faith, *args)
                taps += len(checkthis.split(' '))
            else : 
                checkthis = pitychaintilldeath(lasttime, faith, *args)
                taps += len(checkthis.split(' '))
            #print(checkthis)
        data.append(count)
        tapdata.append(taps)
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    alphaamt = max(data)
    bins = np.linspace(0, alphaamt, int(alphaamt**.7))
    await ctx.send(f"```Again. Are we conducting an impulsive, fail averse approach this time? Please state <Yes/No/Both> <Amount of fails you are willing to tolerate before abandoning attempt>```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    impulsive = False
    FailCapacity = 0
    try:
        listo = str(morecontent.content).split(' ')
        if listo[0].lower() != 'no':
            impuslive = True
            FailCapacity = int(listo[1])
        else:
            pass
    except:
        pass
    await ctx.send(f"```Provide the second simulation parameters : <Number of trials> <Number of attempts*> <prob1> <prob2> ...```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    c2 = morecontent.content
    trials = int(str(morecontent.content).split(' ')[0])
    print(f"Number of trials is {trials}")
    faith = int(str(morecontent.content).split(' ')[1])
    args = str(morecontent.content).split(' ')[2:]
    ARGS = [float(x) for x in args]
    print(ARGS)
    data2 = []  #Number of tries it took until we got a success and stopped the trial
    tapdata2 = []
    check2 = ""
    for i in range(int(trials)):
        SUCCESSWEWANT = len(ARGS)
        count = 1
        lasttime = 0
        taps = 0
        if impulsive: 
            check2 = pitychaintilldeath0(lasttime, faith, *ARGS) #first run
            taps += len(check2.split(' '))
        else : 
            check2 = pitychaintilldeath(lasttime, faith, *ARGS) #first run
            taps += len(check2.split(' '))
        while TrueCount(check2, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in check2.split(' ') if x == 'True']) - len([x for x in check2.split(' ') if x == 'False'])  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            #additional checks
            print(*ARGS)
            print(pitychaintilldeath0(lasttime, faith, *ARGS))
            if impulsive: 
                print("Doing other process")
                print(*ARGS)
                check2 = pitychaintilldeath0(lasttime, faith, *ARGS)
                print(pitychaintilldeath(lasttime, faith, *ARGS))
                print("Trying to print check2 below this line")                
                print(check2)
                taps += len(check2.split(' '))
            else : 
                print("Doing the normal version")
                print(*ARGS)
                print(TrueCount)
                check2 = pitychaintilldeath(lasttime, faith, *ARGS)
                print(pitychaintilldeath(lasttime, faith, *ARGS))
                print("Trying to print check2 below this line")
                print(check2)
                taps += len(check2.split(' '))
            print("----")
            print(check2)
            print("Chicken")
        data2.append(count)
        tapdata2.append(taps)
    alphaamt = max(alphaamt,max(data2))
    bins = np.linspace(0, alphaamt,int(alphaamt**.7))
    plt.hist([data, data2], bins, alpha=0.5, label=[f'First simulation for {str(c1).split(" ")[1] } attempts per session', f'Second simulation for {str(c2).split(" ")[1] } attempts per session']) 
    plt.xlabel("Number of attempts taken to success")
    plt.ylabel("Frequency")
    plt.title("Number of successes every couple of sessions of rolls/Bernoulli trials per simulation")
    plt.legend(loc='upper right')
    plt.savefig(fname='plot2')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')  
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    alphaamt = max(tapdata)
    # bins = np.linspace(0, alphaamt, alphaamt)    
    alphaamt = max(alphaamt,max(tapdata2))
    maxatt = max(int(c1.split(" ")[1]), int(c2.split(" ")[1]))
    minatt = min(int(c1.split(" ")[1]), int(c2.split(" ")[1]))
    if alphaamt>60:bins = np.linspace(0, alphaamt,int(alphaamt/maxatt)) #first wrt to the smaller attempt pool
    else:bins = np.linspace(0, alphaamt,int(alphaamt/5))
    bins = np.array(bins)
    plt.hist([tapdata, tapdata2], bins, alpha=0.5, label=[f'First simulation for {str(c1).split(" ")[1] } attempts per session', f'Second simulation for {str(c2).split(" ")[1] } attempts per session']) 
    plt.xlabel("Number of Bernoulli trials taken to success")
    plt.ylabel("Frequency")
    plt.gca().set_xscale("log")
    plt.title("Number of successes every {maxatt} rolls/Bernoulli trials")
    plt.legend(loc='upper right')
    plt.savefig(fname='plot2')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')    
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    alphaamt = max(tapdata)
    # bins = np.linspace(0, alphaamt, alphaamt)    
    alphaamt = max(alphaamt,max(tapdata2))
    if alphaamt>60:bins = np.linspace(0, alphaamt,int(alphaamt/minatt))
    else:bins = np.linspace(0, alphaamt,int(alphaamt/5))
    bins = np.array(bins)
    plt.hist([tapdata, tapdata2], bins, alpha=0.5, label=[f'First simulation for {str(c1).split(" ")[1] } attempts per session', f'Second simulation for {str(c2).split(" ")[1] } attempts per session']) 
    plt.xlabel("Number of Bernoulli trials taken to success")
    plt.ylabel("Frequency")
    plt.gca().set_xscale("log")
    plt.title("Number of successes every {minatt} rolls/Bernoulli trials")
    plt.legend(loc='upper right')
    plt.savefig(fname='plot2')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')              







@client.command()
async def chain(ctx, *args):
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False

    string = ''
    for i in args:
        print(i)
        sampleMassDist = (float(i),1-float(i))
        string += str(roll(sampleMassDist))+' '
    await ctx.send(string)    


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return


    if client.user.mentioned_in(message):
        if message.content.lower().__contains__('hi'):
            await message.channel.send(f"{message.author.mention}``, boop boop?``")
            time.sleep(1)
            await message.channel.send("``:>``")


    if message.content.lower().__contains__('fuck pulse'):
        await message.channel.send(f"``that say you would why now, {message.author.mention}? o3o``")

    if 'o3o' in message.content.lower():
        choices = [ '(∥◯Δ◯)', 'Ｖ(=￣▽￣=)', 'ｖ(^ー^)', 'v(○ﾟε＾○)', '(;◎_◎)?', '7(⊙.☉)']
        if np.random.normal()>-.8:await channel.send(random.choice(choices))

    await client.process_commands(message)


    if message.content.lower().__contains__('fuck pulse'):
        await message.channel.send(f"``{message.author.mention}, now why would you say that? o3o``")


    if message.content.startswith('etymonline'):
        userinput = message.content[11:]
        print(userinput)
        animalswikia = f'https://www.etymonline.com/search?q={userinput}'

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        # print(soup.find('div',{'class':'ant-col-xs-24 ant-col-sm-24 ant-col-md-24 ant-col-lg-17'}))
        listofoutputs = soup.find('div',{'class':'ant-col-xs-24 ant-col-sm-24 ant-col-md-24 ant-col-lg-17'}).find_all('div',{'class':'word--C9UPa word_4pc--2SZw8'})
        listofnames = [x.find('a').text for x in listofoutputs]
        listofoutputs = [x.a['href'] for x in listofoutputs]
        stringtoprint=''
        for i in range(len(listofnames)):
            stringtoprint += f"{i}.{listofnames[i]}"+'\n'
        await channel.send(f"```{stringtoprint}```")
        # soup.find_all('a',{ "class", "result-link"})[3]['href']

        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        link = 'https://www.etymonline.com'+listofoutputs[(int(ans))]
        # print(link)
        Req = Request(link)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')

        # soup.find('div',{'class style':'position:relative'})
        await channel.send(f"```{soup.find('h1').text}```")
        await channel.send(f"```{soup.find('div',{'style':'position:relative'}).find('section',{'class':'word__defination--2q7ZH'}).p.text}```")


    if message.content.startswith('wf.wikia'):
        ctx = message.content[9:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://warframe.fandom.com/wiki/Special:Search?query={ctx}'

        print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        soup.find_all('a',{ "class", "result-link"})[3]['href']
        if len(soup.find_all('a',{ "class", "result-link"})) >= 10:
            length = 10
        else:
            length = len(soup.find_all('a',{ "class", "result-link"}))

        list = []
        for i in range(length):
            list.append(soup.find_all('a',{ "class", "result-link"})[i]['href'])
            alpha = soup.find_all('li', {'class', 'result'})[i].a.text
            print(i,alpha)
            await channel.send(f'```{alpha}```')

        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        eligible = []
        for i in range(len(soup.find_all('a',{ "class", "result-link"}))):
            eligible.append(i)


#Going into the link perhaps
        if ans in eligible:
            await channel.send((soup.find_all('li', {'class', 'result'})[ans].a['href']))   #Post link for now
            animalswikia = soup.find_all('li', {'class', 'result'})[ans].a['href']
            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

            isthereatable = len(soup.find_all('aside'))
            if isthereatable == 1:
                img = soup.aside.a['href']
                try:
                    for i in range(len(soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'}))):
                        thing = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].div.text
                        Stat = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].find_all('a')[-1].text
                        await channel.send(f'```{Stat} \n {thing} ```')
                except:
                    pass

    if 'o3o' in message.content.lower():
        choices = [ '(◯Δ◯∥)', '∑(ΦдΦlll', '（∂△∂；）', '(;Ⅲ□Ⅲ;)', '(=￣▽￣=)Ｖ', '(^ー^)ｖ', '(○ﾟε＾○)v', ':thumbsup:', 'ಠ‸ಠ', '(◎_◎;)?', '(⊙.☉)7', 'סּ_סּ' ]
        if np.random.normal()>-.8:await channel.send(random.choice(choices))


    if message.content.lower().__contains__('spank'):
        if (message.author.bot  == False ):
            await channel.send('https://tenor.com/view/cats-funny-spank-slap-gif-15308590')


    # if len([x for x in [message.content.lower().__contains__(i) for i in shock] if x==True])>.1:
    #     choices = ['ಠ‸ಠ', 'ಠnಠ', '( ಠ ಠ )', '༼ ಠل͟ಠ༽', '(╯°Д°）╯︵/(.□ . \)', '┌∩┐(ಠ_ಠ)┌∩┐', '┌─┐\n┴─┴\nಠ_ರೃ' ]
    #     await channel.send(random.choice(choices))

    if 'potato' in message.content.lower():
        if np.random.normal()>.6:
            await channel.send('https://cdn.discordapp.com/attachments/400673288768192524/855288890650001488/potato.gif')

    if len([x for x in [message.content.lower().__contains__(i) for i in ["can't stop me", "cant stop me"]] if x==True])>.1:
        if np.random.normal()>0.01:
            await channel.send('https://cdn.discordapp.com/attachments/891562421221732363/941219411203850270/temptation.JPG')

    if 'hi pulse' in message.content.lower() or 'Pulse' in message.content:
        choices = ['乁( ◔ ౪◔)ㄏ' ,'◔‿◔', '୧༼ಠ益ಠ༽୨', 'つ◕ل͜◕)つ', '☜(ಠ_ಠ☜)' ,  '( =￣+∇￣=)v']
        await channel.send(random.choice(choices))

    if 'sugoi' in message.content.lower() or 'wow' in message.content.lower():
        await channel.send('https://cdn.discordapp.com/attachments/400673288768192524/855288876888490014/jesus.gif')

    if 'sad' in message.content.lower():
        choices = ['◉︵◉', '(◕︵◕)', '༼இɷஇ༽']
        if np.random.normal()>0.2:await channel.send(random.choice(choices))

    if message.content.lower() in ['impossible', 'not possible', 'not possible', 'how?', 'not scientifically possible', 'shut yo mouth', 'shut your mouth']:
        await channel.send('https://cdn.discordapp.com/attachments/83566743976411136/858594186516758538/external-content.duckduckgo.com.gif')

    if 'facebook' in message.content.lower():
        await channel.send('(╯°□°)╯︵ ʞooqǝɔɐℲ')

    if message.content.startswith('anima.wikia'):
        def x202(thingie):
            thing = thingie.replace('\n', '')
            thing = thing.replace('\t', '')
            news = thing.encode('ascii', 'ignore')
            encoding = 'utf-8'
            news = news.decode(encoding)
            return(news)
        ctx = message.content[12:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://animals.fandom.com/wiki/Special:Search?query={ctx}'

        print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        if len(soup.find_all('li', {'class', 'unified-search__result'})) >= 10:
            length = 10
        else:
            length = len(soup.find_all('li', {'class', 'unified-search__result'}))

        list = []
        stringo = ''
        for i in range(length):
            list.append(soup.find_all('li', {'class' : 'unified-search__result'})[i].find('h1').a['href'])  #Title links
            alpha = x202(soup.find_all('li', {'class' : 'unified-search__result'})[i].find('h1').text)                 #Title names
            # await channel.send(f'```[{i}]. {alpha}```')                                #Titles with numbers now!!
            stringo+=f'[{i}]. {alpha}' + ' \n'
        await channel.send(f"```{stringo}```")

        def check(m):
            return m.content == m.content and m.channel == message.channel
        count = 0
        while(count<10000):
            try:
                await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = int(float(morecontent.content))
                break
            except:
                if ans.lower().__contains__('stop'):break
                print("Float to int conversion failed!")
                count+=1
        print(ans)
        eligible = []
        for i in range(length):
            eligible.append(i)


        if ans in eligible:                                                     #After feedback has been given to expand on selected section of entry
            animalswikia = soup.find_all('li', {'class' : 'unified-search__result'})[ans].find('h1').a['href']

            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')


            try:
                list = []
                for element in soup.tbody.find_all('tr'):
                    if element.th != None:
                        pass
                    elif element.td.has_attr('colspan'):
                        pass
                    elif element.td.text == '\n':
                        pass
                    else:
                        list.append(element)

                categories = []
                categorienames = []
                for element in list:
                    categories.append(element.b.text)
                    categorienames.append(x202(element.text.replace(f'{element.b.text}', "")))

                colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]      #Listofcoloursforembed anima wikia output
                emb = discord.Embed(title = f"Animal Wikia for {message.content[12:]}", color = random.choice(colours))
                for j in range(len(categories)):
                    emb.add_field(name = f'{categories[j]}', value = f'{categorienames[j]}' )

                for i in range(1,len(soup.find_all('img'))):
                    if soup.find_all('img')[i]['height'] == '75':              #To remove the first image in every anima wikia page. Best way to remove for now instead of identifying it with some other
                        pass
                    else:
                        image = soup.find_all('img')[i]['src']
                        if image.startswith('https'):
                            break
                        else:
                            pass

                titles = ''
                listformytitles = []
                soup.find_all("span", {"class", "mw-headline"})
                n = 0
                nlist = [0]
                for thing in soup.find_all("span", {"class", "mw-headline"}):                     #Listoftitles at end of output apparently
                    titles += f'[{n}]'+ '.' + str(thing['id']) + '.   '
                    listformytitles.append(thing['id'])
                    n += 1
                    nlist.append(n)                                                               #We have made 2 separate lists to try to make 2 optins for user to choose section to expand

                emb.set_image(url = f'{image}')

                await channel.send(content = None, embed = emb)
                try:
                    #Starter text from animal fandom
                    start = soup.find("div", {"class", "mw-content-ltr mw-content-text"}).table.next_sibling
                    end = soup.find("nav", {"class", "toc"}).previous
                    x = start
                    comp = [start]
                    while x != end:
                        x = x.next
                        comp.append(x)

                    print(type(str(comp[2])))
                    sr = ''
                    for part in comp:
                        if type(part) != bs4.element.NavigableString:
                            pass
                        else:
                            sr += str(part)


                    await channel.send(f'``{sr} ``')
                    await channel.send(f'```  {titles} ```')
                    print(f'{titles}')
                except:
                    pass
                    await channel.send(f'```  {titles}  ```')
                    print(f'{titles}')


# We have now the bot to go ahead and wait for user to ask to expand any sections below



                def check(m):
                    return m.content == m.content and m.channel == message.channel
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = (morecontent.content)


                if ans in listformytitles:
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-content-ltr mw-content-text"}).find_all('p'):
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')




# We use numbers to call titles out as well


                elif int(ans) in nlist:
                    ans = listformytitles[int(ans)]
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-parser-output"}).find_all('p'):     #All paragraphs presumably
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')








            except:
                await channel.send('``Page format does not include table or some other standard wikia format. Initiating alternative procedure...``')
                titles = ''
                listformytitles = []
                soup.find_all("span", {"class", "mw-headline"})
                for thing in soup.find_all("span", {"class", "mw-headline"}):
                    titles += str(thing['id']) + '.'
                    listformytitles.append(thing['id'])

                try:
                    #Starter text from animal fandom
                    start = soup.find("div", {"class", "mw-content-ltr mw-content-text"}).table.next_sibling
                    end = soup.find("nav", {"class", "toc"}).previous
                    x = start
                    comp = [start]
                    while x != end:
                        x = x.next
                        comp.append(x)

                    print(type(str(comp[2])))
                    sr = ''
                    for part in comp:
                        if type(part) != bs4.element.NavigableString:
                            pass
                        else:
                            sr += str(part)


                    await channel.send(f'``{sr} ``')
                    await channel.send(f'```  {titles} ```')
                    print(f'{titles}')
                except:
                    pass
                    await channel.send(f'```  {titles}  ```')
                    print(f'{titles}')


                def check(m):
                    return m.content == m.content and m.channel == message.channel
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = (morecontent.content)


                if ans in listformytitles:
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-parser-output"}).find_all('p'):
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')

    elif message.content.startswith('etsy'):
        client_search_term = message.content[5:]
        print(client_search_term)
        pageno = 1
        rarity = 0
        link_template = f"https://www.etsy.com/market/{client_search_term.lower().replace(' ','_')}?ref=pagination&page={pageno}"   #But this is the search results ordered by time
        print(link_template)
        Req = Request(link_template)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        LINKS = [x.find('a')['href'] for x in soup.find(id="search-results").find_all('li')]
        Products_ = [x.find('div',{'class':'v2-listing-card__info'}).h2.text for x in soup.find(id='search-results').find_all('li')]
        Prices1 = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-value'})] for x in soup.find(id='search-results').find_all('li')]
        PriceSymbols = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-symbol'})] for x in soup.find(id='search-results').find_all('li')]
        Price = [[value+' '+currency for value,currency in zip(values,currencies)] for values,currencies in zip(Prices1,PriceSymbols)]
        print("Checkllist for Products_")
        for i in Products_:print(i)
        Products_ = [x.split('\n')[1] for x in Products_]
        Products = []     
        for s in Products_:
            for i,x in enumerate(s):
                if x.isalpha():         #True if its a letter
                    pos = i                   #first letter position
                    break
            new_str = s[pos:]
            Products.append(new_str)        
        print("Check for Products")
        for i in Products:print(i)
        Concat_prices = []
        for price_list in Price:
            if len(price_list)==2:
                Concat_prices.append("Sale Price:"+price_list[0]+" Original Price:"+price_list[1])
            else:
                buffet = ''
                for i in price_list:
                    buffet+=i
                Concat_prices.append(buffet)      
        animalswikia = f'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SGD'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        txt = soup.find('p',{'class':"result__BigRate-sc-1bsijpp-1 iGrAod"}).text
        rate = float(txt.split(' S')[0])
        print(f"1 USD is currently {rate} SGD")
        await channel.send("``Please name your keyword(s) or state No/None:``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check)     
        NEW=[i for i in range(len(Products))]
        Products_=Products
        Price_=Price
        LINKS_=LINKS        
        if morecontent.content.lower().startswith('no'):pass
        else:
            NEW = [i for i in range(len(Products)) if all(word in Products[i].lower() for word in morecontent.content.lower().split(' '))]  #One line to check if a string has a LIST of keywords | RMB THIS
            Products_ = [Products[x] for x in range(len(Products)) if x in NEW]
            Price_    = [Price[x] for x in range(len(Price)) if x in NEW]       
            LINKS_    = [LINKS[x] for x in range(len(LINKS)) if x in NEW] 
            Products = Products_
            Price = Price_
            LINKS = LINKS_
        while len(NEW)<10 and pageno<31:
            #Redo for more entries....
            try:
                pageno+=1
                link_template = f"https://www.etsy.com/market/{client_search_term.lower().replace(' ','_')}?ref=pagination&page={pageno}"   #But this is the search results ordered by time
                print(link_template)
                Req = Request(link_template)
                uClient = urlopen(Req)
                soup = BeautifulSoup(uClient.read(), 'html5lib')
                LINKStoadd = [x.find('a')['href'] for x in soup.find(id="search-results").find_all('li')]
                Products_toadd = [x.find('div',{'class':'v2-listing-card__info'}).h2.text for x in soup.find(id='search-results').find_all('li')]
                Prices1toadd = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-value'})] for x in soup.find(id='search-results').find_all('li')]
                PriceSymbolstoadd = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-symbol'})] for x in soup.find(id='search-results').find_all('li')]
                Pricetoadd = [[value+' '+currency for value,currency in zip(values,currencies)] for values,currencies in zip(Prices1toadd,PriceSymbolstoadd)]
                print("Checkllist for Products_")
                for i in Products_toadd:print(i)
                Products_toadd = [x.split('\n')[1] for x in Products_toadd]
                Productstoadd = []     
                for s in Products_toadd:
                    for i,x in enumerate(s):
                        if x.isalpha():         #True if its a letter
                            pos = i                   #first letter position
                            break
                    new_str = s[pos:]
                    Productstoadd.append(new_str)        
                print("Check for Products")
                for i in Productstoadd:print(i)
                Concat_pricestoadd = []
                for price_list in Pricetoadd:
                    if len(price_list)==2:
                        Concat_pricestoadd.append("Sale Price:"+price_list[0]+" Original Price:"+price_list[1])
                    else:
                        buffet = ''
                        for i in price_list:
                            buffet+=i
                        Concat_pricestoadd.append(buffet) 
                if morecontent.content.lower().startswith('no'):
                    for i in range(len(Productstoadd)):
                        NEW.append(NEWtoadd[i])
                        Products.append(Productstoadd[i])
                        Price.append(Pricetoadd[i])
                        LINKS.append(LINKStoadd[i])     
                else:                                  
                    NEWtoadd = [i for i in range(len(Productstoadd)) if all(word in Productstoadd[i].lower() for word in morecontent.content.lower().split(' '))]  #One line to check if a string has a LIST of keywords | RMB THIS
                    Products_toadd = [Productstoadd[x] for x in range(len(Productstoadd)) if x in NEWtoadd]
                    Price_toadd    = [Pricetoadd[x] for x in range(len(Pricetoadd)) if x in NEWtoadd]       
                    LINKS_toadd    = [LINKStoadd[x] for x in range(len(LINKStoadd)) if x in NEWtoadd] 
                    Productstoadd = Products_toadd
                    Pricetoadd = Price_toadd
                    LINKStoadd = LINKS_toadd
                    for i in range(len(Productstoadd)):
                        NEW.append(NEWtoadd[i])
                        Products.append(Productstoadd[i])
                        Price.append(Pricetoadd[i])
                        LINKS.append(LINKStoadd[i])
            except:pass
        stringo = ''
        for i in range(len(Products)):
            stringo+='\n'+f"[{i}.]"+' '
            for j in Products[i].split(' ')[:4]:
                stringo+=j+' '
            stringo+=' '*(50-len(stringo.split('\n')[-1]))
            print("Price given is")
            print(Price[i][0].split(' $')[0])
            pp = Price[i][0].split(' $')[0]
            if pp.__contains__(','):
                newstring = ''
                for i in pp.split(','):
                    newstring+=i
                pp = newstring
            stringo+=f"{float(pp)*rate:.2f} SGD\n"   #Going to assume that with this urllib method, etsy will always post currency in ' $'
        # stringo+='```'
        if len(stringo)>2000:
            for i in range(0,len(stringo),1900):
                await channel.send('```'+stringo[i:i+1900]+'```')
        else:
            await channel.send('```'+stringo+'```')
        await channel.send("``Please select one of the entries with the associated title numbers: 0,1,2 etc:")
        for i in range(13):
            morecontent = await client.wait_for('message',check = check)    
            while True:
                try:
                    NUM = int(float(morecontent.content))
                    break
                except:
                    pass
            link_template = LINKS[NUM]
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome('E:/chromedriver.exe', options=options)
            driver.get(link_template)
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
            except TimeoutException:
                print('Page timed out after 1 secs.')
            soup = BeautifulSoup(driver.page_source, 'html5lib')
            driver.quit() 
            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"{soup.find('h1').text}", color = random.choice(colours))              
            try:emb.add_field(name = "Price", value = soup.find('div',{'class':'wt-mb-xs-3'}).p.text.split('Price:')[1] )
            except:emb.add_field(name = "Price", value = soup.find('div',{'class':'wt-mb-xs-3'}).p.text)
            emb.add_field(name = "Link", value = link_template )
            IMG = [x.img for x in soup.find('div',{'class':'image-carousel-container'}).ul.find_all('li')]
            IMG_ = []
            for i in IMG:
                try:
                    IMG_.append(i['data-src-zoom-image'])
                except:
                    pass
            emb.set_author(name = "Etsy search result", icon_url = IMG_[0])
            if len(IMG_)>1:emb.set_image(url = IMG_[1])
            if len(IMG_)>2:emb.set_thumbnail(url = IMG_[2])
            try:emb.add_field(name = "Number of Sales by Seller", value = soup.find(id='listing-page-cart').div.find('div',{'class':'wt-display-inline-flex-xs'}).find('span',{'class':'wt-text-caption'}).text )
            except:pass
            reviews = [x for x in soup.find_all('div') if x.has_attr('data-reviews')][0]
            if len(reviews.find_all('button',{'id':'same-listing-reviews-tab'}))>0:
                stringo = ''
                for i in range(4):
                    try:
                        stringo+="\n"+soup.find(id = 'same-listing-reviews-panel').find(id = f'review-preview-toggle-{i}').text+'\n\n'
                    except:pass
                emb.add_field(name = "Reviews for Product", value = stringo[:1000] )
            else:
                emb.add_field(name = "Reviews for Product", value = "No reviews available for this product" )
            await channel.send(content = None, embed = emb)
            




    elif message.content.startswith('anc.wikia'):

        def generalise(string):
            name = ''
            for i in string.h1.text.split('\n'):   #It finds the h1 title name and makes it into a text itself
                if i != '':
                    for j in i.split('\t'):
                        if j != '':
                            name+=j + ' '
            return name


        ctx = message.content[10:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://ancient-animals.fandom.com/wiki/Special:Search?query={ctx}'
        dinowikia = f'https://dinopedia.fandom.com/wiki/Special:Search?query={ctx}'
        # print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')

        Req = Request(dinowikia)
        uClient = urlopen(Req)
        soup2 = BeautifulSoup(uClient.read(), 'html5lib')

        length = 0   #To find the titles and the length of the list of all of these titles from each of the 2 websites
        if len(soup.find_all('li', {'class', 'unified-search__result'})) >= 5:
            length += 5
        else:
            length += len(soup.find_all('li', {'class', 'unified-search__result'}))

        length2 = 0
        if len(soup2.find_all('li', {'class', 'unified-search__result'})) >= 15:
            length += 15
            length2 += 15
        else:
            length += len(soup2.find_all('li', {'class', 'unified-search__result'}))
            length2 += len(soup2.find_all('li', {'class', 'unified-search__result'}))

        # print(length, length2)
        list = []
        for i in range(length - length2):
            #list.append(soup.find_all('a',{ "class", "result-link"})[int(2*i)]['href'])
            list.append(soup.find_all('li', {'class', 'unified-search__result'})[i].a['href'])
            alpha = generalise(soup.find_all('li', {'class', 'unified-search__result'})[i])
            await channel.send(f'```[{i}]. {alpha}```')                                #Titles with numbers now!!

        for i in range(length2):
            list.append(soup2.find_all('li', {'class', 'unified-search__result'})[i].a['href'])
            alpha = generalise(soup2.find_all('li', {'class', 'unified-search__result'})[i])
            await channel.send(f'```[{i+length - length2}]. {alpha}```')                                #Titles with numbers now!!



        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")


        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        eligible = []
        eligible2 = []
        for i in range(length - length2):
            eligible.append(i)
        for i in range(length - length2, length):
            eligible2.append(i)



        if ans in eligible:
            animalswikia = soup.find_all("li", {"class":"unified-search__result"})[ans].a['href']
            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

            if len(soup.find_all('table', {'class':'wikia-infobox'})) != 0:
                Classification = []
                Ans = []
                Titles = []
                nt = 0
                no = 0
                nolist = []
                yet = 0
                for element in soup.find_all('table', {'class':'wikia-infobox'}):
                    for part in element.find_all('tr'):
                        if len(part.find_all('th')) != 0:
                            if len(part.find_all('td')) != 0:
                                if part.th.has_attr('class') == False:
                                    if part.td.has_attr('class') == False:
                                        if part.div == None:
                                            Classification.append(part.th.text)
                                            Ans.append(part.td.text)
                                            no += 1
                            elif part.th.has_attr('class'):
                                if part.th['class'] == ['wikia-infobox-header']:
                                    if yet != 0:
                                        Titles.append(part.text)
                                        nt+=1
                                        nolist.append(no)
                                        no = 0
                                        yet += 1
                                    else:
                                        Titles.append(part.text)
                                        nt+=1
                                        no = 0
                                        yet += 1
                nolist.append(no)

                #Recursive way to export out the table values
                add = 0
                n = 0
                for ii in nolist:
                    prev = add
                    add += ii
                    # print('NEWLISTODESU')
                    colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
                    emb = discord.Embed(title = f"{Titles[n]} wikia findings...", color = random.choice(colours))
                    for element in range(prev, add):
                        emb.add_field(name = f'{Classification[element]}', value = f'{Ans[element]}' )
                    emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
                    await channel.send(content = None, embed = emb)
                    n += 1



        elif ans in eligible2:
            def filtern(string):
                list = string.split('\n')
                for thing in list:
                    if thing == '':
                        list.remove(thing)

                for element in list:
                    list = element.split(' ')
                    for thing in list:
                        if thing == '':
                            list.remove(thing)
                return list

            def filtern2(string):
                list = string.split('\n')
                for thing in list:
                    if thing == '':
                        list.remove(thing)

                for element in list:
                    list = element.split(' ')
                    for thing in list:
                        if thing == '':
                            list.remove(thing)

                str = ''
                for i in list:
                    str += f'{i}' + ' '
                return str

            def green(ele):   #On 'tr' results
                return len(ele.find_all('th'))

            def greenno():    #I think this calculated the number of table elements
                no = 0
                for i in soup.find_all('tr'):
                    if green(i) != 0:
                        no+= 1

                return no

            def Tits():
                list = []
                begin = 0
                n = 0
                if len(soup.find_all('table',{'class':'infobox'})) >= 1:
                    for i in soup.find_all('tr'):
                        n+=1
                        if filtern2(i.text) == 'Scientific classification ':
                            list.append(f'Scientific classification ' + '/' + f'{n-1}')
                            begin += 1
                            break

                if begin!=0:
                    for i in range(n, len(soup.find_all('tr'))):
                        if len(list) <= greenno() -2:
                            if green(soup.find_all('tr')[i]) != 0:
                                str = filtern2(soup.find_all('tr')[i].text)
                                newstr = str + '/' + f'{i}'
                                list.append(newstr)
                                # print((soup.find_all('tr')[i].text))
                                # print(list)


                return list



            print(length2)
            print(length)
            print(ans)
            animalswikia = soup2.find_all("li", {"class":"unified-search__result"})[ans-length+length2].a['href']
            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

###

            Class = []
            Ans = []
            for element in soup.find('table', {'class':'infobox'}).find_all('tr'):
                if len(element.find_all('td')) == 2:
                    Class.append(element.find_all('td')[0].text.split('\n')[0])
                    Ans.append(element.find_all('td')[1].text)

            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"{soup.find('h1').text} wikia findings...", color = random.choice(colours))
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            for element in range(len(Class)):
                emb.add_field(name = f'{Class[element]}', value = f'{Ans[element]}' )


            imgcount = 0
            img = []
            row = 0
            for element in soup.find('table', {'class':'infobox'}).find_all('tr'):
                row += 1
                if len(element.find_all('a')) >= 0.1:
                    for thing in element.find_all('a'):
                        if thing.has_attr('title') == False:
                            imgcount += len(element.find_all('a'))
                            img.append(thing['href'])
                    if imgcount >= 1.1:
                        print(f'There are {imgcount} images in the table section for the {row}th row.')

            emb.set_thumbnail(url = f'{img[0]}')

            conditionforsynonym = 0
            for i in range(len(soup.find_all('tr'))):
                if filtern2(soup.find_all('tr')[i].text) == 'Synonyms ':
                    conditionforsynonym += i

            if conditionforsynonym != 0:
                if len(soup.find_all('tr')[conditionforsynonym+1].find_all('p')) >= 1:
                    left = []
                    right = []
                    for i in range(len(soup.find_all('tr')[conditionforsynonym+1].find_all('p'))):
                        left.append(soup.find_all('tr')[conditionforsynonym+1].find_all('p')[i].text)
                        try:
                            right.append(soup.find_all('tr')[conditionforsynonym+1].find_all('ul')[i].text)
                        except:
                            right.append('Nil')

                    for i in range(len(left)):
                        emb.add_field(name = f'{left[i]}', value = f'{right[i]}' )


            await channel.send(content = None, embed = emb)


#     elif message.content.startswith('anc.tax'):
#         def x202(thingie):
#             thing = thingie.replace('\n', ' ')
#             news = thing.encode('ascii', 'ignore')
#             encoding = 'utf-8'
#             news = news.decode(encoding)
#             return(news)

#         # await channel.send(f'{message.content[8]}')
#         # await channel.send(f'{message.content[8:]}')
#         animalswikia = f'http://www.prehistoric-wildlife.com/species/{message.content[8]}/{message.content[8:]}.html'
#         Req = Request(animalswikia)
#         uClient = urlopen(Req)
#         soup = BeautifulSoup(uClient.read(), 'html5lib')

#         #Table results : Universal
#         c = 0
#         Tibble = []
#         TibbleRes = []
#         while c!= 1:
#             for item in soup.find_all('b'):
#                 Tibble.append(item.text)
#                 if item.next_sibling == ' ':
#                     # print(item.text, item.next_sibling.next_sibling.text, 'method0')
#                     TibbleRes.append(item.next_sibling.next_sibling.text)
#                 else:
#                     try:
#                         # print(item.text, x202(item.next_sibling.text), 'method1')
#                         TibbleRes.append(x202(item.next_sibling.text))
#                     except:
#                         # print(item.text, x202(item.next_sibling), 'method3')
#                         TibbleRes.append(x202(item.next_sibling))
#                 if item.text == 'Fossil representation:':
#                     c += 1
#                     break

#         #Diagnostics: 0 images, 1 image, multiple images +/- multiple paragraphs?
#         n = len(soup.find_all('img'))-3
#         list = soup.find_all('img')
#         for i in range(len(soup.find_all('img'))):
#             string = soup.find_all('img')[i]['src']
#             listofwords = string.split('/')
#             if 'r_nav_link_images' in listofwords:
#                 n -= 1
#                 list.remove(soup.find_all('img')[i])
#         # n = number of bodyline images, including the center top image, list is later to be made into finallist of full links below
#         finallist = []
#         for i in range(3, len(list)):
#             eg = list[i]
#             egg = eg['src']
#             link = 'http://www.prehistoric-wildlife.com/images' + egg.split('images')[-1]
#             finallist.append(link)

#         def chunks(s, n):                                        #To split long paragraphs of information into chunks of 1980 chars down in "for chunk in chunks(text, __)"
#             for start in range(0, len(s), n):
#                 yield s[start:start+n]

#         def Title(x):                                                       #Finding title by finding the bold text within the left aligned paras
#             ptit = soup.find_all('p', {'align':'left'})[x].b
#             if ptit != None:
#                 thingie = ptit.text
#                 thing = thingie.replace('\n', ' ')
#                 news = thing.encode('ascii', 'ignore')
#                 encoding = 'utf-8'
#                 news = news.decode(encoding)

#                 return news
#             else:
#                 return "There is no title for this paragraph"

#         ntitles = -1                                                         #How many multiple titles are there in the body of text?
#         for i in range(1, len(soup.find_all('p', {'align':'left'}))):
#             if Title(i) != 'There is no title for this paragraph':
#                 ntitles+=1
#             else:
#                 pass

#         if n <= .9:
#             print('No images found')

#             colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
#             emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
#             for element in range(len(Tibble)):
#                 emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
#             emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
#             await channel.send(content = None, embed = emb)
#             #In the case that we have 1 paragraph in entire article : Most common
#             listofps = soup.find_all('p')
#             for i in range(len(listofps)):
#                 if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
#                     # print(soup.find_all('p')[i].text)
#                     TT = soup.find_all('p')[i].text
#                     TT = TT.replace('\n', ' ')
#                     TT = TT.replace('\xa0', '')
#                     for chunk in chunks(TT, 1980):
#                         await channel.send(f'``{chunk}``')
#                     # print(TT)
#                 else:
#                     pass


# #This is to cover cases whereby there is at least 1 image BUT there are not multiple subtitles within the subtext
#         elif ntitles <= 0:
#             print(n)
#             colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
#             emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
#             for element in range(len(Tibble)):
#                 emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
#             emb.set_thumbnail(url = f'{finallist[0]}')
#             emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
#             if n == 1:
#                 await channel.send(content = None, embed = emb)
#             elif n == 2:
#                 emb.set_image(url = finallist[1])
#                 await channel.send(content = None, embed = emb)
#             elif n >= 2:
#                 emb.set_image(url = finallist[1])
#                 await channel.send(content = None, embed = emb)
#                 for i in range(2, n):
#                     await channel.send(finallist[i])
#             listofps = soup.find_all('p')
#             for i in range(len(listofps)):
#                 if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
#                     # print(soup.find_all('p')[i].text)
#                     TT = soup.find_all('p')[i].text
#                     TT = TT.replace('\n', ' ')
#                     TT = TT.replace('\xa0', '')
#                     for chunk in chunks(TT, 1980):
#                         await channel.send(f'``{chunk}``')
#                     # print(TT)
#                 else:
#                     pass




#         else:
#             print('fag')
#             print(n)
#             print(ntitles)
#             colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
#             emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
#             for element in range(len(Tibble)):
#                 emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
#             emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
#             emb.set_thumbnail(url = f'{finallist[0]}')
#             if n == 1:
#                 await channel.send(content = None, embed = emb)
#             elif n == 2:
#                 emb.set_image(url = finallist[1])
#                 await channel.send(content = None, embed = emb)
#             elif n >= 2:
#                 emb.set_image(url = finallist[1])
#                 await channel.send(content = None, embed = emb)
#                 for i in range(2, n):
#                     await channel.send(finallist[i])

# #THe paragraphs associated with each TItle
#             arbitrary = 1
#             yet = 0
#             listofpara = []
#             listoftits = []
#             for i in range(1, len(soup.find_all('p', {'align':'left'}))):
#                 if Title(i) != 'There is no title for this paragraph':
#                     yet += 1
#                     listoftits.append(Title(i))
#                     textie = soup.find_all('p', {'align':'left'})[i].text
#                     listofpara.append(x202(textie.split(soup.find_all('p', {'align':'left'})[i].next.text)[-1]))
#                 elif yet == 0:
#                     listofpara.append(x202(soup.find_all('p', {'align':'left'})[i].text) + '\n')
#                     arbitrary = 0
#                 else:
#                     listofpara[-1] += '\n' + x202(soup.find_all('p', {'align':'left'})[i].text)

#             if arbitrary == 0:
#                 for chunk in chunks(listofpara[0], 1980):
#                     await channel.send(f'``{chunk}``')
#                 del listofpara[0]


#             await channel.send(f'There appear to be {ntitles} within this library that you can expand')



#             read = ''
#             para = []
#             for i in range(len(listoftits)-1):
#                 read += f'[{i}]. ' + listoftits[i] + '\n'
#                 para.append(i)

#             await channel.send(f'```{read}```')
#             def check(m):
#                 return m.content == m.content and m.channel == message.channel
#             morecontent = await client.wait_for('message',check = check, timeout = 40.0)
#             ans = (morecontent.content)

#             if int(ans) in para:
#                 send = int(ans)
#                 await channel.send(f'**{listoftits[send]}**')
#                 text = listofpara[send]
#                 if len(text) >= 2000:
#                     for chunk in chunks(text, 1980):
#                         await channel.send(f'``{chunk}``')
#                 else:
#                     await channel.send(f'``{text}``')
    elif message.content.startswith('wiki'):
        await channel.send("Locating...")
        userinput=message.content[5:]    
        print(userinput)
        link_template = f"https://en.wikipedia.org/w/index.php?search={userinput.replace(' ','_')}&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome('E:/chromedriver.exe', options=options)
        driver.get(link_template)
        try:
            WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print('Page timed out after 0.5 secs.')

        soup = BeautifulSoup(driver.page_source, 'html5lib')
        # print(soup)
        driver.quit()
        searches = [[x.find('div',{'class':'mw-search-result-heading'}),x.find('div',{'class':'searchresult'}),x.find('div',{'class':'mw-search-result-data'})] for x in soup.find('ul',{'class':'mw-search-results'}).find_all('li',{'class':'mw-search-result'})]
        links = [x.find('div',{'class':'mw-search-result-heading'}).a['href'] for x in soup.find('ul',{'class':'mw-search-results'}).find_all('li',{'class':'mw-search-result'})]

        installwiki = "https://en.wikipedia.org"
        for n in range(0,max(len(searches),5),5):
            count = n
            searchstring = '```'
            for i in searches[n:min(len(searches),n+5)]:            
                searchstring+= f"[{count}.]Search Title:{i[0].text} \n Description:{i[1].text} \n Metadata : {i[2].text} \n\n"
                count+=1
            searchstring+="```"
            await channel.send(searchstring)
        await channel.send("Please tell me with a number, which wiki entry you would like to enter :>")
        while True:
            Moreinfo = await client.wait_for('message', timeout = 200.0, check = lambda message: message.author == message.author)
            try:
                userinput = int(float(Moreinfo.content))
                break
            except:pass
        link_template = installwiki+links[userinput]
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome('E:/chromedriver.exe', options=options)
        driver.get(link_template)
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print('Page timed out after 2 secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        img = [x for x in soup.find_all('img') if x['src'].lower().__contains__("footer")==False if x['src'].lower().__contains__("svg")==False if x['src'].lower().__contains__("icon")==False if x['src'].lower().__contains__("logo")==False if x['src'].lower().__contains__("wikimedia_wordmark")==False][0]['src'] 
        imgs = [x['src'] for x in soup.find_all('img') if x['src'] != "//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/50px-Question_book-new.svg.png" if x['src']!="//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png" if x['src'].lower().__contains__("wikimedia-button")==False if x['src'].lower().__contains__("footer")==False if x['src'].lower().__contains__("svg")==False if x['src'].lower().__contains__("icon")==False if x['src'].lower().__contains__("logo")==False if x['src'].lower().__contains__("wikimedia_wordmark")==False] 
        titlenames = [x.text for x in soup.find_all("h2") if x.text.lower().__contains__("see also")==False if x.text.lower().__contains__("references")==False if x.text.lower().__contains__("notes")==False if x.text.lower().__contains__("navigation menu")==False if x.text.lower().__contains__("external links")==False if x.text.lower().__contains__("contents")==False]
        print(len(titlenames))
        titles = [x for x in soup.find_all("h2") if x.text.lower().__contains__("see also")==False if x.text.lower().__contains__("references")==False if x.text.lower().__contains__("notes")==False if x.text.lower().__contains__("navigation menu")==False if x.text.lower().__contains__("external links")==False if x.text.lower().__contains__("contents")==False]

        try:endpoint = [x.text for x in soup.find_all("h2")][[x for x in soup.find_all("h2")].index(titles[-1])+1] 
        except:
            try:endpoint=[x.text for x in soup.find_all("h2")][[x for x in soup.find_all("h2")].index(titles[-1])]
            except:endpoint=''
        titlenames.append(endpoint) #Add that title to titles list
        GOLD = [soup.text.split(titlenames[i])[1].split(titlenames[i+1])[0] for i in range(len(titlenames)-1)]
        titlenames=titlenames[:-1]
        # try:
        #     tabletext = soup.find('tbody').text
        #     STARTER = soup.find('div',{'class':'mw-parser-output'}).text.split(tabletext)[1].split(titlenames[0])[0]
        # except:STARTER = soup.find('div',{'class':'mw-parser-output'}).text.split(titlenames[0])[0]
        STARTER = [x.text+'\n' for x in soup.find_all('p')]
        stringn = ''
        for i in STARTER:stringn+=i
        TITLE = soup.find('h1').text
        emb = discord.Embed(title = f"{TITLE}", color = 0x594F4F)
        emb2 = discord.Embed(title = f"{TITLE}", color = 0x594F4F)
        if len(imgs)>1:
            if imgs[1].lower().startswith("https"):
                emb.set_author(name = "Wikipedia", icon_url = imgs[1])
                emb2.set_author(name = "Wikipedia", icon_url = imgs[1])
            else:
                emb.set_author(name = "Wikipedia", icon_url = 'https:'+imgs[1])
                emb2.set_author(name = "Wikipedia", icon_url = 'https:'+imgs[1])
        else:
            emb.set_author(name = "Wikipedia")
            emb2.set_author(name = "Wikipedia")
        try:
            if img.lower().startswith("https"):emb.set_image(url = f'{img}')
            else:emb.set_image(url = f'https:{img}')
        except:pass
        # print(STARTER)
        emb.add_field(name = '**Synopsis**', value = stringn[:min(1000,len(stringn))] )
        emb2.add_field(name = 'Source', value = link_template )
        #Search for table
        if len(soup.find_all('tbody'))>0:
            for i in [[[z.text for z in y.find_all('td')] for y in x.find_all('tr') if len(y.find_all('td'))==2] for x in soup.find_all('tbody') ]:
                if i!=[]:
                    for j in i:
                        if len(j[0])!=2 and j[1]!='' and j[0]!='':  #To get rid of the u202 chars that are read as empty fields in discord
                            emb2.add_field(name = j[0], value = j[1])        
                            print(j)
        footer=''
        for i in range(len(titlenames)):footer+=f"[{i}.]"+titlenames[i]
        emb2.set_footer(text = footer)
        await channel.send(content = None, embed = emb)
        await channel.send(content = None, embed = emb2)
        Moreinfo = await client.wait_for('message', check = lambda message: message.author == message.author)
        try:Which = int(float(Moreinfo.content))
        except:Which = Moreinfo.content
        if Which in range(len(titlenames)):
            x = 1990
            stringo = GOLD[Which]
            for i in range(0,len(stringo),x):
                await channel.send(f"`` {stringo[i:i+x]} ``")
        elif Which.lower().__contains__("img") and len(imgs)>1:
            if len(imgs)<=10:
                for i in imgs[:min(len(imgs),10)]:
                    if i.lower().startswith("https"):await channel.send(i)
                    else:await channel.send("https:"+i)
            else:
                guild = message.guild
                stringthing = f"All images from {TITLE}"
                existing_channel = await guild.categories[1].create_text_channel(stringthing)
                # existing_channel = discord.utils.get(guild.categories[1].get_all_channels(), name=stringthing)
                # iden = existing_channel.id
                # schannel = client.get_channel(iden)
                await existing_channel.send(message.author.mention)
                for i in imgs:
                    if i.lower().startswith("https"):await existing_channel.send(i)
                    else:await existing_channel.send("https:"+i)
                time.sleep(240)
                await existing_channel.delete()

    
    if message.content.startswith('prehistory'):
        def x202(thingie):
            thing = thingie.replace('\n', ' ')
            news = thing.encode('ascii', 'ignore')
            encoding = 'utf-8'
            news = news.decode(encoding)
            return(news)

        # await channel.send(f'{message.content[8]}')
        # await channel.send(f'{message.content[8:]}')
        animalswikia = f'http://www.prehistoric-wildlife.com/species/{message.content[11]}/{message.content[11:]}.html'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')

        #Table results : Universal
        c = 0
        Tibble = []
        TibbleRes = []
        while c!= 1:
            for item in soup.find_all('b'):
                Tibble.append(item.text)
                if item.next_sibling == ' ':
                    # print(item.text, item.next_sibling.next_sibling.text, 'method0')
                    TibbleRes.append(item.next_sibling.next_sibling.text)
                else:
                    try:
                        # print(item.text, x202(item.next_sibling.text), 'method1')
                        TibbleRes.append(x202(item.next_sibling.text))
                    except:
                        # print(item.text, x202(item.next_sibling), 'method3')
                        TibbleRes.append(x202(item.next_sibling))
                if item.text == 'Fossil representation:':
                    c += 1
                    break

        #Diagnostics: 0 images, 1 image, multiple images +/- multiple paragraphs?
        n = len(soup.find_all('img'))-3
        list = soup.find_all('img')
        for i in range(len(soup.find_all('img'))):
            string = soup.find_all('img')[i]['src']
            listofwords = string.split('/')
            if 'r_nav_link_images' in listofwords:
                n -= 1
                list.remove(soup.find_all('img')[i])
        # n = number of bodyline images, including the center top image, list is later to be made into finallist of full links below
        finallist = []
        for i in range(3, len(list)):
            eg = list[i]
            egg = eg['src']
            link = 'http://www.prehistoric-wildlife.com/images' + egg.split('images')[-1]
            finallist.append(link)

        def chunks(s, n):                                        #To split long paragraphs of information into chunks of 1980 chars down in "for chunk in chunks(text, __)"
            for start in range(0, len(s), n):
                yield s[start:start+n]

        def Title(x):                                                       #Finding title by finding the bold text within the left aligned paras
            ptit = soup.find_all('p', {'align':'left'})[x].b
            if ptit != None:
                thingie = ptit.text
                thing = thingie.replace('\n', ' ')
                news = thing.encode('ascii', 'ignore')
                encoding = 'utf-8'
                news = news.decode(encoding)

                return news
            else:
                return "There is no title for this paragraph"

        ntitles = -1                                                         #How many multiple titles are there in the body of text?
        for i in range(1, len(soup.find_all('p', {'align':'left'}))):
            if Title(i) != 'There is no title for this paragraph':
                ntitles+=1
            else:
                pass

        if n <= .9:
            print('No images found')

            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            await channel.send(content = None, embed = emb)
            #In the case that we have 1 paragraph in entire article : Most common
            listofps = soup.find_all('p')
            for i in range(len(listofps)):
                if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
                    # print(soup.find_all('p')[i].text)
                    TT = soup.find_all('p')[i].text
                    TT = TT.replace('\n', ' ')
                    TT = TT.replace('\xa0', '')
                    for chunk in chunks(TT, 1980):
                        await channel.send(f'``{chunk}``')
                    # print(TT)
                else:
                    pass


#This is to cover cases whereby there is at least 1 image BUT there are not multiple subtitles within the subtext
        elif ntitles <= 0:
            print(n)
            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_thumbnail(url = f'{finallist[0]}')
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            if n == 1:
                await channel.send(content = None, embed = emb)
            elif n == 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
            elif n >= 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
                for i in range(2, n):
                    await channel.send(finallist[i])
            listofps = soup.find_all('p')
            for i in range(len(listofps)):
                if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
                    # print(soup.find_all('p')[i].text)
                    TT = soup.find_all('p')[i].text
                    TT = TT.replace('\n', ' ')
                    TT = TT.replace('\xa0', '')
                    for chunk in chunks(TT, 1980):
                        await channel.send(f'``{chunk}``')
                    # print(TT)
                else:
                    pass




        else:
            print('fag')
            print(n)
            print(ntitles)
            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            emb.set_thumbnail(url = f'{finallist[0]}')
            if n == 1:
                await channel.send(content = None, embed = emb)
            elif n == 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
            elif n >= 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
                for i in range(2, n):
                    await channel.send(finallist[i])

#THe paragraphs associated with each TItle
            arbitrary = 1
            yet = 0
            listofpara = []
            listoftits = []
            for i in range(1, len(soup.find_all('p', {'align':'left'}))):
                if Title(i) != 'There is no title for this paragraph':
                    yet += 1
                    listoftits.append(Title(i))
                    textie = soup.find_all('p', {'align':'left'})[i].text
                    listofpara.append(x202(textie.split(soup.find_all('p', {'align':'left'})[i].next.text)[-1]))
                elif yet == 0:
                    listofpara.append(x202(soup.find_all('p', {'align':'left'})[i].text) + '\n')
                    arbitrary = 0
                else:
                    listofpara[-1] += '\n' + x202(soup.find_all('p', {'align':'left'})[i].text)

            if arbitrary == 0:
                for chunk in chunks(listofpara[0], 1980):
                    await channel.send(f'``{chunk}``')
                del listofpara[0]


            await channel.send(f'There appear to be {ntitles} within this library that you can expand')



            read = ''
            para = []
            for i in range(len(listoftits)-1):
                read += f'[{i}]. ' + listoftits[i] + '\n'
                para.append(i)

            await channel.send(f'```{read}```')
            def check(m):
                return m.content == m.content and m.channel == message.channel
            morecontent = await client.wait_for('message',check = check, timeout = 40.0)
            ans = (morecontent.content)

            if int(ans) in para:
                send = int(ans)
                await channel.send(f'**{listoftits[send]}**')
                text = listofpara[send]
                if len(text) >= 2000:
                    for chunk in chunks(text, 1980):
                        await channel.send(f'``{chunk}``')
                else:
                    await channel.send(f'``{text}``')



    elif message.content.startswith('IUCN'):
        await channel.send("Locating...")
        userinput=message.content[5:]
        #str has to be scientific name preferably in order to get a proper result. Genius and Species

        link_template = f"https://www.iucnredlist.org/search?query={userinput.replace(' ','%20')}&searchType=species"



        # def p8(x):
        #     y = (x.encode("utf-8"))
        #     print(y)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome('E:/chromedriver.exe', options=options)
        driver.get(link_template)
        try:
            WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print('Page timed out after 1.5 secs.')

        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        try:
            print(soup.find('a', {'class':'link--faux'})['href'])
            await channel.send(f"I found something {message.author.name}, my good sir!")
        except:await channel.send(f"Sorry, {message.author.mention}! There does not appear to be any entry regarding {userinput} :c Try something else!")
        print("Located webpage...")
        tag = soup.find('a', {'class':'link--faux'})['href']
        print(tag)


        #INTO THE NEIGHBOURHOOD WE GO!
        result_page = f'https://www.iucnredlist.org{tag}'


        driver = webdriver.Chrome('E:/chromedriver.exe', options = options)
        driver.set_window_size(1650, 650)
        driver.get(result_page)
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(3)
        driver.save_screenshot('E:/IUCNimage.png')
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "panel__data panel__data--std panel__data--accent")))
        except TimeoutException:
            print('Page timed out after 5 secs.')

        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()

        #embed
        colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
        emb = discord.Embed(title = f"{soup.find('h1').text} | {soup.find(id='taxonomy-details').find('div',{'class':'layout-card--split__minor'}).p.text} ", color = 0x594F4F)
        emb2 = discord.Embed(title = f"{soup.find('h1').text} | {soup.find(id='taxonomy-details').find('div',{'class':'layout-card--split__minor'}).p.text} ", color = 0x594F4F)
        thing1 = soup.find('div', {"class", "panel panel--orphan panel--ruled"}).p.text
        whenlastassessed = soup.find('div', {"class", "panel panel--orphan panel--ruled"}).p.next_sibling.text
        # emb.add_field(name = f'**{thing1}**', value = f'{whenlastassessed}' )
        #We want emb2 message to be sent first
        emb2.set_author(name = "IUCN Redlist Taxonomy and Distribution", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650605859017195530/IUCN.png")
        emb.set_author(name = "IUCN Threats and Assessment", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650605859017195530/IUCN.png")
        try:
            imaging = soup.find('a', {"class":"featherlight__gallery__image featherlight__gallery__image--trigger"})['href']
            emb2.set_image(url = f'{imaging}')
        except:
            pass

        #scope
        thing2 = soup.find('div', {"class", "panel panel--orphan"}).p.text
        thing2thing2 = soup.find('div', {"class", "panel panel--orphan"}).p.next_sibling.text
        emb2.add_field(name = f'**{thing2}**', value = f'{thing2thing2}' )


        #Population trend

        thing3 = soup.find('div', {"class", "panel panel--dark bg-brand"}).p.text
        thingthing3 = soup.find('div', {"class", "panel panel--dark bg-brand"}).p.next_sibling.text
        emb2.add_field(name = f'**{thing3}**', value = f'{thingthing3}' )


        # await channel.send(soup.find('div', {"class", "panel panel--dark bg-brand"}).p.text)
        # await channel.send(soup.find('div', {"class", "panel panel--dark bg-brand"}).p.next_sibling.text)



        #number of mature individuals

        thing4 = soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-5"}).p.text
        thingthing4 = soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-5"}).p.next_sibling.text
        if thingthing4 == '':
            emb2.add_field(name = f'**{thing4}**', value = '{<Unknown>}' )
        else:
            emb2.add_field(name = f'**{thing4}**', value = f'{thingthing4}' )


        thing5 = soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-4"}).p.text
        thingthing5 = soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-4"}).p.next_sibling.text
        emb.add_field(name = f'**{thing5}**', value = f'{thingthing5}' )
        # await channel.send(soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-4"}).p.text)
        # await channel.send(soup.find('div', {"class", "panel panel--dark panel--grow bg-grey-a-4"}).p.next_sibling.text)


        #Threattitles being embed

        Threat = [x.text for x in soup.find(id="threats").find_all('h3',{'class':'card__data card__data--std card__data--accent'})]
        Reasons=[[y.text for y in x.find_all('li',{'class':'list-bulleted__item'})] for x in soup.find(id="threats").find_all('div',{'class':'text-body'}) if len(x.find_all('h4'))==0]
        # Reasons = []
        # for i in range(len(soup.find('div', {"class", "layout-panels__1-3rds"}).find_all('div', {"class", "text-body"}))):
        #     stroke = []
        #     Reasons.append(stroke)
        #     for j in range(len(soup.find('div', {"class", "layout-panels__1-3rds"}).find_all('div', {"class", "text-body"})[i].find_all('li'))):
        #         # print(soup.find('div', {"class", "layout-panels__1-3rds"}).find_all('div', {"class", "text-body"})[i].find_all('li')[j].text, i)
        #         add = soup.find('div', {"class", "layout-panels__1-3rds"}).find_all('div', {"class", "text-body"})[i].find_all('li')[j].text
        #         stroke.append(add)

        


        for i in range(len(Threat)):
            finalstr = Reasons[i][0]
            for j in range(1, len(Reasons[i])):
                finalstr += '\n'
                finalstr += Reasons[i][j]
            emb.add_field(name = f'**{Threat[i]}**', value = f'{finalstr}')

        #Footer - text Summary titles
        textsum = [x.text for x in soup.find_all('h2') if x.text.lower().__contains__("site navigation")==False]
        string = ''
        for i in range(len(textsum)):
            string += f"{[i]}"+textsum[i] + '.'
        emb.set_footer(text = f"{string}")

        #For later use, we store the titles in a list we can navigate.
        IUCNlisttitles = []
        for title in textsum:
            IUCNlisttitles.append(title)

        # Assessment keep at final

        Assessment_card = soup.find(id = "assessment-information")
        Assessments = [x.text for x in Assessment_card.find_all('h3')]
        Assessments_answers = [x.text for x in Assessment_card.find_all('p',{'class':'card__data card__data--key card__data--accent'})]
        for i in range(len(Assessments)):
            emb.add_field(name = f'{Assessments[i]}', value = f'**{Assessments_answers[i]}**')

        # emb2.set_author(name = "IUCN Redlist Risk Assessment", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650605859017195530/IUCN.png")

        #Let us try to append geographic and taxonomic information for emb2 first

        Taxo_Titles = [x.h3.text for x in soup.find(id="taxonomy").find_all('div',{'class':'layout-card--thirds__third'})]
        Taxo = [x.p.text for x in soup.find(id="taxonomy").find_all('div',{'class':'layout-card--thirds__third'})]
        for i in range(len(Taxo_Titles)):emb2.add_field(name=f"{Taxo_Titles[i]}", value=f"{Taxo[i]}")

        #Geographic range
        Geo = [[[y.h4.text,y.p.text] for y in x.find_all('div',{'class':'u--margin-top-sm'})] for x in soup.find(id="geographic-range").find_all('div',{'class':'layout-card--split geographic-locations'})]
        Geo_shape1 = len(Geo)
        Geo_shape2 = len(Geo[0])
        #Geo2 has titles but Geo above title is the first word only
        Geo2 = [[x.h3.text,x.p.text] for x in soup.find(id="geographic-range").find('div',{'class':'layout-card--split'}).find_all('h3') if len(x.find_all('p'))!=0]
        for i in Geo:
            for j in i:
                fag = j[1].replace(";","\n")
                fagg = j[1]
                emb2.add_field(name = f'{j[0]}', value = f'{fagg[:1020]}')
                locale_fields = []
        locale_field_ans = [x.text for x in soup.find(id="geographic-range").find_all('p',{'class':'card__data card__data--key card__data--accent'})]
        locale_fields_ans = []  #copying into this one to 'remove' empty entries 
        for i in range(len(locale_field_ans)):
            if locale_field_ans[i]!='':
                locale_fields.append([x.text for x in soup.find(id="geographic-range").find_all('h3',{'class':'heading'}) if x.text.lower().__contains__("native")==False if x.text != ''][i])
                locale_fields_ans.append(locale_field_ans[i])
        for i in range(len(locale_fields_ans)):
            emb2.add_field(name = f'{locale_fields[i]}', value = f'{locale_fields_ans[i]}')

        await channel.send(content = None, embed = emb2)
        await channel.send(content = None, embed = emb)
        await channel.send(file=discord.File('E:/IUCNimage.png'))

        Moreinfo = await client.wait_for('message', timeout = 300.0, check = lambda message: message.author == message.author)
        Which = int(float(Moreinfo.content))
        # for i in range(len(IUCNlisttitles)):
        #     if Which in IUCNlisttitles[i]:
        #         text = textsum.find_all('h4')[i].next_sibling.text
        #         await channel.send(f'{IUCNlisttitles[i]}')
        #         if f'{text}' == '':
        #             await channel.send('No information on that sorry :c')
        #         else:
        #             if len(text) <= 2000:
        #                 await channel.send(text)
        #             else:
        #                 def chunks(s, n):                                        #To split long paragraphs of information into chunks of 1980 chars down in "for chunk in chunks(text, __)"
        #                     for start in range(0, len(s), n):
        #                         yield s[start:start+n]
        #                 for chunk in chunks(text, 1980):
        #                     await channel.send(f'``{chunk}``')
        #     elif f'{i}' in Which:
        #         text = textsum.find_all('h4')[i].next_sibling.text
        #         await channel.send(f'{IUCNlisttitles[i]}')
        #         if f'{text}' == '':
        #             await channel.send('No information on that sorry :c')
        #         else:
        #             await channel.send(text)
        if Which in range(len(IUCNlisttitles)):
            x = 1990
            stringo = [x.text for x in soup.find_all('div',{'class':'card__details details'})][Which]
            for i in range(0,len(stringo),x):
                await channel.send(f"`` {stringo[i:i+x]} ``")

        for i in range(3):
            # await channel.send(content = None, embed = emb)

            Moreinfo = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == message.author)
            Which = int(float(Moreinfo.content))
            if Which in range(len(IUCNlisttitles)):
                x = 1990
                stringo = [x.text for x in soup.find_all('div',{'class':'card__details details'})][Which]
                for i in range(0,len(stringo),x):
                    await channel.send(f"`` {stringo[i:i+x]} ``")


    await client.process_commands(message)

client.run('####YOUR TOKEN HERE#####')