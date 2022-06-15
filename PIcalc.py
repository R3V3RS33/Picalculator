import math
from colorama import init, Fore, Back, Style
import os
from os import system as s
import random
import numpy as np
import time
init(convert=True)

inv = "n"
pi = math.pi

def AUFG():
    UR = random.uniform(1, 10)
    U = round(UR, 2)
    RR = random.uniform(1, 10)
    R = round(RR, 2)
    DR = random.uniform(1, 10)
    D = round(DR, 2)
    AR = random.uniform(1, 10)
    A= round(AR, 2)
    print(Fore.CYAN + f"{U}")
    DDeq = U / pi
    Deq = round(DDeq, 2)
    print(f"D = {Deq}")
    result = float(input("U = "))
    if result == U:
        print("correct")
    else:
        print(f"incorrect the result was {U} (if its close then you had it right anyway)")



    input("")

def Picalc():
    print(Fore.RED + """██████████████████████████████████████████████████████████████████████████████""")
    time.sleep(0.05)
    print(Fore.RED + """█▄─▄▄─█▄─▄█▀▀▀▀▀██─▄▄▄─██▀▄─██▄─▄███─▄▄▄─█▄─██─▄█▄─▄████▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█""")
    time.sleep(0.05)
    print(Fore.RED + """██─▄▄▄██─█████████─███▀██─▀─███─██▀█─███▀██─██─███─██▀██─▀─████─███─██─██─▄─▄█""")
    time.sleep(0.05)
    print(Fore.RED + """▀▄▄▄▀▀▀▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀""")
    time.sleep(0.05)
    print(Fore.RED + """
         ################################
   ##################################
  ###################################
  ####    #####         ####                These are the following options:
 ###      #####        #####
 #        #####        #####                                    [1] : Calculate Circumference (U)
 #        #####        ####                                     [2] : Calculate Radius        (R)
         ####         #####                                     [3] : Calculate Diameter      (D)
        #####         #####                                     [4] : Calculate Area          (Ak)
       ######         #####                                     [5] : Cylinder options
       #####          #####        ##                           [6] : Credits
      #######         ######       ##                           [7] : Formulas
     #######           ##############                           [8] : U Exercises (Rounded to 2 {0.00})
    #######            #############                            [9] : Calculate everything at once
    #######             ###########
    ######               #########
""")
    print(Fore.WHITE + "")
    selection = input("Select an option : ")
    print(Fore.RED + "")
    if selection == "1":
        D = float(input("Diamater : "))
        result_float = pi * D
        result_str = str(result_float)
        print(f"Your Circumference is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        input("Press any key to continue")

    if selection == "2":
        U = float(input("Circumference : "))
        result_float = U / pi
        result_float2 = result_float / 2
        result_str = str(result_float2)
        print(f"Your Radius is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        input("Press any key to continue")

    if selection == "3":
        U = float(input("Circumference : "))
        result_float = U / pi
        result_str = str(result_float)
        print(f"Your Diamater is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        input("Press any key to continue")

    if selection == "4":
        D = float(input("Diamater : "))
        result_float = D / 2
        Double_R_result = result_float * result_float
        result_float2 = pi * Double_R_result
        result_str = str(result_float2)
        print(f"Your Area is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        input("Press any key to continue")

    if selection == "5":
        s("cls")
        PicalcC()

    if selection == "6":
        print("""
        Socials :
        Tiktok : r3v3rs3_
        Insta : r3v3rs3__
        Twitch : r3v3rs3_12203
        Youtube : r3v3rs3

        """)
        input("Press any key to continue")
        s("cls")
    if selection == "7":
        print("""
        U = pi * D

        R = U / pi / 2 == D / 2

        D = U / pi == r * 2

        A = pi * r^2
        """)
        input("Press any key to continue")
    if selection == "8":
        s("cls")
        AUFG()

    if selection == "9":
        U = 0
        R = 0
        D = 0
        A = 0
        print(Fore.CYAN + "")

        try:
            U = float(input("U : "))
        except ValueError:
            U = 0
        try:
            R = float(input("R : "))
        except ValueError:
            A = 0

        try:
            D = float(input("D : "))
        except ValueError:
            A = 0

        try:
            A = float(input("A : "))
        except ValueError:
            A = 0
        print(Fore.RED + "")
        if U == 0:
            if D != 0:
                result_float = pi * D
            else:
                if R != 0:
                    result_float = pi * (R * 2)
                else:
                    result_float = U
        else:
            result_float = U
        result_str = str(result_float)
        print(f"Your Circumference is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        if R == 0:
            if D != 0:
                result_float = D / 2
            else:
                if U != 0:
                    result_float = (U / pi) / 2
                else: result_float = R

        else:
            result_float = R
        result_str = str(result_float)
        print(f"Your Radius is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        if D == 0:
            if R != 0:
                result_float = R * 2
            else:
                if U != 0:
                    result_float = U / pi
                else:
                    result_float = 0




        else:
            result_float = D
        result_str = str(result_float)
        print(f"Your Diamater is " + Fore.GREEN + F"{result_str}" + Fore.RED)
        if A == 0:
            if D != 0:
                result_float = pi * ((D / 2) * (D / 2))
            else:
                if U != 0:
                    result_float = pi * (((U / pi) / 2) * ((U / pi) / 2))
                else:
                    if R != 0:
                        result_float = pi * (R * R)
                    else:
                        result_float = A


        else:
            result_float = A

        result_str = str(result_float)
        print(f"Your Area is : " + Fore.GREEN + F"{result_str}" + Fore.RED)

        input("Press any key to continue")


    s("cls")
    Picalc()

def PicalcC():
    print(Fore.CYAN + """██████████████████████████████████████████████████████████████████""")
    time.sleep(0.05)
    print(Fore.CYAN + """█▄─▄▄─█▄─▄█▀▀▀▀▀██─▄▄▄─█▄─█─▄█▄─▄███▄─▄█▄─▀█▄─▄█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█""")
    time.sleep(0.05)
    print(Fore.CYAN + """██─▄▄▄██─█████████─███▀██▄─▄███─██▀██─███─█▄▀─███─██─██─▄█▀██─▄─▄█""")
    time.sleep(0.05)
    print(Fore.CYAN + """▀▄▄▄▀▀▀▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀""")
    time.sleep(0.05)
    print(Fore.CYAN + """
     ################################
   ##################################
  ###################################
  ####    #####         ####                These are the following options:
 ###      #####        #####
 #        #####        #####                                    [1] : Calculate Volume          (V)
 #        #####        ####                                     [2] : Calculate lateral surface (M)
         ####         #####                                     [3] : Calculate Surface         (O)
        #####         #####                                     [4] : Calculate height          (H)
       ######         #####                                     [5] : Circle options
       #####          #####        ##                           [6] : Credits
      #######         ######       ##                           [7] : Random Rainbow parrot
     #######           ##############
    #######            #############
    #######             ###########
    ######               #########
    """)
    print(Fore.WHITE + "")
    selection = input("Select an option : ")
    print(Fore.RED + "")
    if selection == "1":
        r = float(input("Radius : "))
        h = float(input("Height : "))
        r2 = r * r
        result_float = pi * r2  * h
        print(Fore.GREEN + f"{result_float}" + Fore.RED)


        input("Press any key to continue")

    if selection == "2":
        input()
        O / (2 * pi * r) - r

        input("Press any key to continue")

    if selection == "3":
        r = float(input("Radius : "))
        r2 = r * r
        result_float = pi * r2
        print(f"Your Surface is " + Fore.GREEN + F"{result_float}" + Fore.RED)


        input("Press any key to continue")

    if selection == "4":
        r = float(input("Radius : "))
        V = float(input("Volume : "))
        #result_float = O / (2 * pi * r) - r
        r2 = r * r
        result_float = V / pi * r2
        result_str = str(result_float)
        print(Fore.GREEN + f"{result_str}" + Fore.RED)

        input("Press any key to continue")
    if selection == "5":
        s("cls")
        Picalc()

    if selection == "6":
        print("""
        Socials :
        Tiktok : r3v3rs3_
        Insta : r3v3rs3__
        Twitch : r3v3rs3_12203
        Youtube : r3v3rs3

        """)
        input("Press any key to continue")
        s("cls")
    if selection == "7":
        s("curl parrot.live")
    s("cls")
    PicalcC()

Picalc()
