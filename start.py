from flask import Flask,url_for
from flask import request
from chatterbot import ChatBot
from flask_cors import CORS
from chatterbot.utils.read_input import input_function


app = Flask(__name__)
CORS(app)
#import pyaudio
@app.route('/sign_users')
def signUpUser():
    chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        silence_performance_warning='True',
        logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
        ],

        input_adapter="chatterbot.adapters.input.TerminalAdapter",
    #input_adapter="chatterbot_voice.VoiceInput",
    
        output_adapter="chatterbot.adapters.output.TerminalAdapter"
    #output_adapter="chatterbot_voice.VoiceOutput",
        )

    # Train based on the english corpus
    chatbot.train("chatterbot.corpus.oam")
    #print("Type something to begin...")
    
    


    user = request.args.get('name')
    direct="D:/bots/flask"
    file = open(direct+"/testfile.txt","w")
    file.write(user) 
    file.close()
    bot_input = chatbot.get_response(None)
    bot=bot_input
    return bot;          

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5002)
