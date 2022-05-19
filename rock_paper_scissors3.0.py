from pickle import TRUE
import random
import string 
import cv2
import numpy as np

from tensorflow.keras.models import load_model
from time import time
from time import sleep

class rock_paper_scissors():
    def __init__(self):
        
        self.model = load_model('/home/george/Documents/AiCore/Computer_vision/keras_model5.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.outcomes=[[["drew","dessiné"],["lost","perdu"],["won","gagné"]],[["won","gagné"],["drew","dessiné"],["lost","perdu"]],[["lost","perdu"],["won","gagné"],["drew","dessiné"]]]
        self.computer_choice=[["rock","le rock"],["paper","le papier"],["scissors","les ciseaux"]]
        self.win_lose={"won": 0, "lost": 0, "drew": 0}

        self.main()
    
    def main(self):
        
        language=self.select_language()
        rounds=self.select_winning_score(language)
        start_time=time()
        self.display_data=[0, 0, "", "", "",["", ""]]
        self.set_display_data(language)
        n=1

        while TRUE:
            self.video_display()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break    

            if n>200:
                break
            
            if (self.win_lose["won"]>=rounds or self.win_lose["lost"]>=rounds):
                if rounds != 0:
                    print(["the score limit has been reached you " + self.outcomes[self.player_in][self.computer_in][language] + "!", "la limite de score a été atteinte vous avez " + self.outcomes[self.player_in][self.computer_in][language] + "!"] [language] )
                    self.display_data[5]=[["the score limit has been reached,", "you " + self.outcomes[self.player_in][self.computer_in][language] + " the game!"],[ "la limite de score a été atteinte", "vous avez " + self.outcomes[self.player_in][self.computer_in][language] + "la partie!"]][language]
                rounds=0
                n=n+1
                continue
                
            self.decide_stage(start_time, language)

        self.cap.release()
        cv2.destroyAllWindows()

    def video_display(self):
        ret, frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image

        
        cv2.putText(frame, str(self.display_data[self.display_data[0]]), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, self.display_data[2], (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, self.display_data[3], (410, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, self.display_data[5][0], (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(frame, self.display_data[5][1], (10, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.imshow('frame', frame)

    def set_display_data(self, language):
        self.display_data[2] = ["you:" + str(self.win_lose["won"]), "toi: " + str(self.win_lose["won"])][language]
        self.display_data[3] = [" computer: " + str(self.win_lose["lost"]), " l'ordinateur: " + str(self.win_lose["lost"])][language]

    def select_language(self):
        while 1==1:
            language=int(input("English: 0 Francais:1 "))
            if language==0 or language==1:
                break
        return language

    def select_winning_score(self, language):
        while 1==1:
            rounds=input(["what score should the game be played to? ","combien de fois le jeu doit-il être joué? "][language])
            if rounds.isnumeric():
                break
        return int(rounds)
    
    def decide_winner(self,language):
        
        prediction = self.model.predict(self.data)
        if prediction[0,0]>prediction[0,1] and prediction[0,0]>prediction[0,2]:
            player_in=0
        if prediction[0,1]>prediction[0,0] and prediction[0,1]>prediction[0,2]:
            player_in=1
        if prediction[0,2]>prediction[0,0] and prediction[0,2]>prediction[0,1]:
            player_in=2
        print(["the computer chose " + self.computer_choice[self.computer_in][language] + ", you " + self.outcomes[player_in][self.computer_in][language] + "!", "l'ordinateur a choisi " + self.computer_choice[self.computer_in][language] + " tu as " + self.outcomes[player_in][self.computer_in][language]][language])
        self.win_lose[self.outcomes[player_in][self.computer_in][0]] +=1
        print(["you:" + str(self.win_lose["won"]) + " computer: " + str(self.win_lose["lost"]), "toi: " + str(self.win_lose["won"]) + " l'ordinateur: " + str(self.win_lose["lost"])][language])
        self.set_display_data(language)
        self.player_in = player_in
        return ["the computer chose " + self.computer_choice[self.computer_in][language] + ", you " + self.outcomes[player_in][self.computer_in][language] + "!", "l'ordinateur a choisi " + self.computer_choice[self.computer_in][language] + " tu as " + self.outcomes[player_in][self.computer_in][language]][language]

    def decide_stage(self, start_time, language):
        elapsed_time=time()-start_time
        if (elapsed_time%8)<2 and self.display_data[1] != 3:
            print(30)
            self.display_data[0]=1
            self.display_data[1] = 3
        if 2<=(elapsed_time%8)<4 and self.display_data[1] != 2:
            print(20)
            self.display_data[1] = 2
        if 4<=(elapsed_time%8)<6 and self.display_data[1] != 1:           
            print(10)
            self.display_data[1] = 1
        if 6<=((time()-start_time)%8)<8 and self.display_data[0] != 4:        
            self.computer_in=random.randint(0,2)
            self.display_data[0]=4
            self.display_data[4] = self.decide_winner(language)


rock_paper_scissors()