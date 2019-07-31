from chatterbot.adapters.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.utils.read_input import input_function
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import Text,pos_tag

class TerminalAdapter(InputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the terminal.
    """
    def meaning_analysis(self,sentence_analysis):
        tokens = word_tokenize(sentence_analysis)
        text = Text(tokens)
        tags = pos_tag(text)
        print (tags)
        nouns = "NN NNP PRP NNS".split()
        verbs = "VB VBD VBP VBG".split()
        if len(tags)==1:
            tag_len=len(tags)+1
        else:
            tag_len=len(tags)
        for i in range(tag_len -1):
            if tags[i][1] in verbs:
                if i+1<len(tags) and (tags[i+1][1] in nouns or tags[i+2][1] in nouns or tags[i+3][1] in nouns or tags[i+4][1] in nouns):
                    print("its a decision")
                else:
                    print("unknown decision")
                #print("yoo1")
                final_str="decision"
                break
            else:
                final_str="question asked"
        return final_str;  
    
    def process_input(self,take_question):
        """
        Read the user's input from the terminal.
        """
         
        file = open("D:/bots/flask/testfile.txt", "r") 
        readf=file.read()
        print("user input is",readf)
        direct="D:/bots/flask"
        file = open(direct+"/questions.log","a")
        file.write(readf+",") 
        file.close()
        if readf=='':
            user_input = "jhjjkjkk"#write some sentence from database whose answer is please ask me something
            
        else:
            temp_var= readf
            stop_words = set(stopwords.words('english'))
            stop_words.remove('what')
            stop_words.remove('i')
            word_tokens = word_tokenize(temp_var)
            filtered_sentence=""
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence=filtered_sentence+" "+w
            sentence_classification=self.meaning_analysis(filtered_sentence)
            #print("yoo3",sentence_classification)
            if sentence_classification=="decision":
                print ('This is operation')
                user_input="operation:"+filtered_sentence#write some sentence from database saying this is operation
            else:
                print('This is question')
                user_input=filtered_sentence
            return Statement(user_input)
