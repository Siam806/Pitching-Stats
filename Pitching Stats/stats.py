import webbrowser
import plotly.graph_objects as go
from pathlib import Path
print("1 = Program ; 2 = Github Page")
choice = input()
print(choice)
if choice == "1":
        pArray = []
        ipArray = []
        hArray = []
        rArray = []
        erArray = []
        bbArray = []
        kArray = []
        hrArray = []
        print("Current limit of pitchers is 3!")
        repeat = int(input("How many pitchers do you want?: "))
        for x in range(0, repeat):
                P = input("Pitcher name: ")
                IP = input("Inning Pitched (IP) :")
                H = input("Hits (H) :")
                R = input("Runs (R) :")
                ER = input("Earned Runs (ER) :")
                BB = input("Base on balls (BB) :")
                K = input("Strikeouts (K) :")
                HR = input("Homeruns (HR) :")
                pArray.append(P)
                ipArray.append(IP)
                hArray.append(H)
                rArray.append(R)
                erArray.append(ER)
                bbArray.append(BB)
                kArray.append(K)
                hrArray.append(HR)

        if repeat == 1:
                fig = go.Figure(data=[go.Table(header=dict(values=['Pitcher', 'IP', 'H', 'R', 'ER', 'BB', 'K', 'HR']),
                                               cells=dict(values=[[pArray[0]], [ipArray[0]], [hArray[0]], [rArray[0]], [erArray[0]], [bbArray[0]], [kArray[0]], [hrArray[0]]]))
                                      ])
        elif repeat <= 2:
                fig = go.Figure(data=[go.Table(header=dict(values=['Pitcher', 'IP', 'H', 'R', 'ER', 'BB', 'K', 'HR']),
                                               cells=dict(values=[[pArray[0], pArray[1]], [ipArray[0], ipArray[1]], [hArray[0], hArray[1]], [rArray[0], rArray[1]], [erArray[0], erArray[1]], [bbArray[0], bbArray[1]], [kArray[0], kArray[1]], [hrArray[0], hrArray[1]]]))
                                      ])
        elif repeat <= 3:
                fig = go.Figure(data=[go.Table(header=dict(values=['Pitcher', 'IP', 'H', 'R', 'ER', 'BB', 'K', 'HR']),
                                               cells=dict(values=[[pArray[0], pArray[1], pArray[2]], [ipArray[0], ipArray[1], ipArray[2]], [hArray[0], hArray[1], hArray[2]], [rArray[0], rArray[1], rArray[2]], [erArray[0], erArray[1], erArray[2]], [bbArray[0], bbArray[1], bbArray[2]], [kArray[0], kArray[1], kArray[2]], [hrArray[0], hrArray[1], hrArray[2]]]))
                                      ])
        fig.show()
elif choice == "2":
     webbrowser.open("https://github.com/Siam806")   
else:
        print("Error")

input()
