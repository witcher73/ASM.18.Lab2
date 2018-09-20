import cgi


from .guild import Guild


def main(q,selfurl):
    G=Guild(q,selfurl)
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'action' in q:
        if (q['action'].value=="1"):
            G.input()
            if (q['action'].value=="2"):
                G.output()
        if (q['action'].value=="3"):
            G.delete()
    else:
        G.output()


'''
    
def exit():
    return 1

G = Guild()

MENU =[
       ["Add Character", G.input],
       ["Change Character", G.change],
       ["Delete Character", G.delete],
       ["Display Guildlist", G.output],
       ["Write Guildlist to the file", G.outputfile],
       ["Read Guildlist from the file", G.inputfile],
       ["Clear Guildlistlist", G.clear],
       ["Exit",exit]
       ]


def main():
    while True:
        i=0
        print("------------------------------")
        print("Select")
        for i, item in enumerate(MENU):
            print("{0:2}. {1}".format(i, item[0]))
        print("------------------------------")
        obtained_value = int(input())
        MENU[obtained_value][1]()
        if obtained_value == 7:
            break
'''



if __name__ == "__main__":
    main()



