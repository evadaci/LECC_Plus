# Integration of Coding Into High School Students

The aim of this project is to show High School students the importance of programming, and to motivate them to start coding, as soon as possible. This project supports C and C++ programming languages. Students can learn by lectures that the project offers and also entertain and test their programming skills by playing a game. 

## Description

As explained before, by this project, students can learn, entertain and the supported languages are C and C++. Inspired by this we decided to give our App a name: LECC+. Learn, Entertain, C-programming, CPP-programming. <br/>
**Logo:**  <br/>

![](README_PHOTO%2BGIF/LOGO.png)

This project is written in python programming language. With the help of turtle module, <br/>

``` python
import turtle 
```

we made possible creating one main python file for the lectures part, and 4 other .py files regarding the game created. Four games, because there are: two different coding languages and two different game levels (Beginner, Advanced).  <br/>Lecture part and Game is described in a more detailed way below at **"How to use"** label. <br/>
<br/><br/> 
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Main page for** ***lectures:*** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **How** ***game*** **starts:**<br/>

<img src="README_PHOTO%2BGIF/FRONT.png" height="420"> <img src="README_PHOTO%2BGIF/STARTING_GAME.gif" height="420">   
   
   
<br/>**In total 4 games:**   
Game 1: C-programming (Beginner) <br/>
Game 2: C-programming (Advanced) <br/>
Game 3: CPP-programming (Beginner) <br/>
Game 4: CPP-programming (Advanced) <br/><br/>


### How to use 

**The first part (Lectures)** :bookmark_tabs:<br/>
This part is very easy to use and understand. It contains six main function in the first page, that we can activate by clicking on a particular space (BUTTONS) in the given photo. <br/>This is possible by turtle module using onclick function: <br/>
``` python
turtle.onclick(fun, btn=1, add=None)
```
This way functions are linked with each other, and we are allowed to navigate through lecture pages: <br/><br/>
<img src="README_PHOTO%2BGIF/CLICKON_LECTURES.gif" height="550"> <br/><br/>

**The second part (Game)** :video_game:<br/>
In this game, user plays with objects, in our case turtles, gaining points by catching the black turtle. After playing for 10 seconds, user gets to answer a question. This can help gain points too. Game is time limited: 60 seconds. So, user plays 60 seconds, while giving 5 answers in total. These questions are made regarding what user has learned in the lectures part. <br/>
<br/>***Instructions to move the turtle:*** <br/>
**To move left** -> ‘a’ or ‘left’ arrow. <br/>
**To move right** -> ‘d’ or ‘right’ arrow. <br/>
**To increase speed** -> ‘w’ or ‘up’ arrow. <br/>
**To end the game** -> ‘q’ 

This is made possible using listen and onkey turtle functions. <br/>
``` python
turtle.listen()
```

``` python
turtle.onkey(fun, key)
```


Game is created using turtle module. Inside the game there are two turtles created: Blue turtle (user), black turtle. User in this case is the blue turtle and tries catching the black one. Each time blue turtle catches the black turtle, your total score becomes: **Total score= Question_score+1**, and turtles separate in random positions. <br/><br/>
<img src="README_PHOTO%2BGIF/CATCH_TURTLE.gif" height="550"> <br/><br/>

You might might confuse when reading **Question_score** . <br/>
By a simple explanation, game is divided in two parts, regarding the way Total Score is calculated. The first part is when blue turtle catch the black turtle, and the second part is evaluated regarding to the points user gets from correct answers. <br/>After 10 seconds playing, a question box pops up, and the background changes, where user is asked to answer a question. This question is written in the new background, and the answer must be given inside the question box. If the answer is correct your total score becomes: **Total score= Catch_score+1**. <br/>
<br/>Getting a question box inside the game, is made possible by textinput function in turtle. <br/>
``` python
turtle.textinput(title, prompt)
```
<br/>
<img src="README_PHOTO%2BGIF/QUESTION_BOX.gif" height="550"> <br/><br/>

When time inside the game becomes greater than or equal to 60 seconds, the game ends and the points are displayed. <br/>
**NOTE!!** ***Only total points and the points you got from correct answers will be displayed on the screen***.<br/><br/>

<img src="README_PHOTO%2BGIF/DISPLAYPOINTS_ENDGAME.gif" height="550"> <br/><br/>



## Installing

As mentioned before, this project is a set of python code files. They are not converted in .exe files and the games are not implemented in the main code (Lectures part). So, to run this code you must install Python programming language and an IDE (Integrated Development Environment). This way you can run the code, get the output, and also modify it. <br/>**Recommended IDE:** PyScripter -> [Download PyScripter here!](https://sourceforge.net/projects/pyscripter/)
<br/><br/>
***To get the full project download the files of this repository ->***   [Download Repository!](https://github.com/Epoka-Python-Project/LECC_PLUS) <br/>


It contains the readme file, one folder with all the photos used inside the readme file, and other folder named **FullProject**.
<br/>The **FullProject** folder contains two important folders:
- **Main LECTURES Folder**, that contains the main python code for the lectures, including also all the photos used inside the code -> [Main LECTURES Folder](https://github.com/Epoka-Python-Project/LECC_PLUS/tree/main/FullProject/Main%20LECTURES%20Folder) <br/>

- **GAME Folder LECC+**, that contains 4 .py files for all 4 games created, and all the photos used inside these python code to make them run successfully -> [GAME Folder LECC+](https://github.com/Epoka-Python-Project/LECC_PLUS/tree/main/FullProject/Game%20Folder_LECC%2B) <br/>


 
**Game 1:** -> [C-programming (Beginner)](https://github.com/Epoka-Python-Project/LECC_PLUS/blob/main/FullProject/Game%20Folder_LECC%2B/GAME_C_BEGINNER.py) <br/>
**Game 2:** -> [C-programming (Advanced)](https://github.com/Epoka-Python-Project/LECC_PLUS/blob/main/FullProject/Game%20Folder_LECC%2B/GAME_C_ADVANCED.py) <br/>
**Game 3:** -> [CPP-programming (Beginner)](https://github.com/Epoka-Python-Project/LECC_PLUS/blob/main/FullProject/Game%20Folder_LECC%2B/GAME_C%2B%2B_BEGINNER.py) <br/>
**Game 4:** -> [CPP-programming (Advanced)](https://github.com/Epoka-Python-Project/LECC_PLUS/blob/main/FullProject/Game%20Folder_LECC%2B/GAME_C%2B%2B_ADVANCED.py) <br/>




## Authors

##### - Ensild Bici
##### - Eva Daçi 
##### - Enrieta Hoxha
##### - Klaudia Kasa
##### - Qemal Sinaj 


