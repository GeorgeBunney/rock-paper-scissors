def rock_paper_scissors():
    import random 
    import cv2
    from tensorflow.keras.models import load_model
    import numpy as np
    n=50
    model = load_model('keras_model5.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    outcomes={"0rock":["drew","dessiné"],"1rock":["lost","perdu"],"2rock":["won","gagné"],"0paper":["won","gagné"],"1paper":["drew","dessiné"],"2paper":["lost","perdu"],"0scissors":["lost","perdu"],"1scissors":["won","gagné"],"2scissors":["drew","dessiné"]}
    computer_choice={"0":["rock","le rock"],"1":["paper","le papier"],"2":["scissors","les ciseaux"]}
    win_lose={"won": 0, "lost": 0, "drew": 0}
    numbers={0:3,10:2,20:1}
    while 1==1:
            language=input("English: 0 Francais:1 ")
            if language=="0" or language=="1":
                break
    language=int(language)
    while 1==1:
            rounds=input(["what score should the game be played to? ","combien de fois le jeu doit-il être joué? "][language])
            if rounds.isnumeric():
                break
    rounds=int(rounds)
    while win_lose["won"]<rounds and win_lose["lost"]<rounds:
        computer_in=str(random.randint(0,2))
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        if n%50==0 or n%50==20 or n%50==20:
            print(numbers[n%50])
        if n%50==30:
            if prediction[0,0]>prediction[0,1] and prediction[0,0]>prediction[0,2]:
                player_in="rock"
            if prediction[0,1]>prediction[0,0] and prediction[0,1]>prediction[0,2]:
                player_in="paper"
            if prediction[0,2]>prediction[0,0] and prediction[0,2]>prediction[0,1]:
                player_in="scissors"
            print(["the computer chose " + computer_choice[computer_in][language] + ", you " + outcomes[computer_in+player_in][language] + "!", "l'ordinateur a choisi " + computer_choice[computer_in][language] + " tu as " + outcomes[computer_in+player_in][language]][language])
            win_lose[outcomes[computer_in+player_in][0]] +=1
            print(["you:" + str(win_lose["won"]) + " computer: " + str(win_lose["lost"]), "toi: " + str(win_lose["won"]) + " l'ordinateur: " + str(win_lose["lost"])][language])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        n=n+1    
    print(["the score limit has been reached you " + outcomes[computer_in+player_in][language], "la limite de score a été atteinte vous avez " + outcomes[computer_in+player_in][language]][language])
    cap.release()
    cv2.destroyAllWindows()

rock_paper_scissors()










