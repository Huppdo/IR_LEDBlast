from flask import Flask, request, make_response, render_template, redirect, url_for, jsonify
import os
import json

app = Flask(__name__)

cueList = ["init_init","fade_orange", "fade_red", "dim_blue", "fade_orange", "fade_red","fade_orange","fade_blue","instant_orange"]
currentPosition = 0

@app.route("/")
def mainPage():
    return make_response(render_template('index.html'))

@app.route("/trigger", methods=["POST"])
def singleAction():
    for i in range(4):
        cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(request.args.get("cmd")))
        os.system(cmdStr)
    return "Okay!"

def full():
    for i in range(10):
        os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_UP")
    cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(request.args.get("cmd")))
    for i in range(5):
        os.system(cmdStr)

@app.route("/fade", methods=["POST"])
def fadeAction():
    for i in range(10):
        os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_DOWN")
    cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(request.args.get("cmd")))
    for i in range(5):
        os.system(cmdStr)
    for i in range(10):
        os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_UP")
    return "Okay!"

@app.route("/cues", methods=["GET"])
def showCues():
    display = ""
    for element in range(len(cueList)):
        if element == currentPosition:
            display += "<b>" + cueList[element] + "</b><br>"
        else:
            display += "" + cueList[element] + "<br>"
    return make_response(render_template('cues.html', visibleCues=display))

@app.route("/next", methods=["POST"])
def nextCue():
    global currentPosition
    currentPosition += 1
    try:
        actionStr = cueList[currentPosition]
        actionList = actionStr.split("_")
        print(actionList)
    except:
        print("Out of cues or error")
        return "Out of cues or error"
    if actionList[0] == "instant":
        for i in range(4):
            cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
            os.system(cmdStr)
    elif actionList[0] == "fade":
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_DOWN")
        cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
        for i in range(5):
            os.system(cmdStr)
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_UP")
    elif actionList[0] == "dim":
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_DOWN")
        cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
        for i in range(5):
            os.system(cmdStr)
    return str(actionList) + " completed"

@app.route("/prev", methods=["POST"])
def prevCue():
    global currentPosition
    currentPosition -= 1
    try:
        actionStr = cueList[currentPosition]
        actionList = actionStr.split("_")
        print(actionList)
    except:
        print("Out of cues or error")
        return "Out of cues or error"
    if actionList[0] == "instant":
        for i in range(4):
            cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
            os.system(cmdStr)
    elif actionList[0] == "fade":
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_DOWN")
        cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
        for i in range(5):
            os.system(cmdStr)
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_UP")
    elif actionList[0] == "dim":
        for i in range(10):
            os.system("irsend SEND_ONCE LED_44_KEY BRIGHT_DOWN")
        cmdStr = str("irsend SEND_ONCE LED_44_KEY " + str(actionList[1]).upper())
        for i in range(5):
            os.system(cmdStr)
    return str(actionList) + " completed"

if __name__ == "__main__":  # starts the whole program
    print("started")
    app.run(host='0.0.0.0', port=5001)