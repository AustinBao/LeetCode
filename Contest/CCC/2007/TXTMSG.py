
while True:
    user = input("Enter phrase> ")
    dit = {
        "CU" : "see you",
        ":-)": "I'm happy",
        ":-(": "I'm unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Contest",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you're welcome",
        "TTYL": "talk to you later"
    }
    if user == "TTYL":
        print(dit[user])
        break
    print(dit[user])