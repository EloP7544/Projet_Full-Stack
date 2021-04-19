### 18/04/2021 
  ##### 1. maj_daily.md 
        was added to MAIN branch, this is an update Diray or Todo List for advancement of our project 
  ##### 2. requirements.txt 
        was added, this file contains all pip libs for our project (nlp scrapy, opencv2, sklearn, tf2, etc)
  ##### 3. How to update from git? 
       3.1  "git checkout main"
       3.2  "git pull"
       3.3  "git checkout <yourdevbranch>"
       3.4  "git merge main"
       3.5  here you might have a popup for confirming sure your choice, ignore and close it , if it is nano text editor, just input "^x"
       3.6  if you don't want to keep maj_daily.md in this branch, just delete it and git add . git commit -m "<your message>"
       3.7 git push
  ##### 4. Update Daily Todo
      We will update our dailys notes directly on our web interface of github 
  
  
  
### 19/04/2021
  ##### 1. How to save training history of our model ? (This is for displaying our training graphe with Plotly Dash in our website)
         1.1  history=model.fit(train_X,train_Y,batch_size=8,epochs=100)
         1.2  import pickle

              with open('trainHistoryDict.txt', 'wb') as file_pi:
                  pickle.dump(history.history, file_pi)
                  
         1.3  with open('trainHistoryDict.txt','rb') as file_pi:
                  history=pickle.load(file_pi)
