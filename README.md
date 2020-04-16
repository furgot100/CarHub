# Welcome to CarHub
All in one place for car enthusiast to post and sell parts and cars
Meant to connect to remaining enthusiasts together. 
## Getting started
First create your own repo, then create your own project file in your terminal and run
```
git clone https://github.com/furgot100/CarHub
```
Then enter into the the folder which should be
```
cd CarHub
```
From there from your terminal you may need to migrate files with
```
python3 manage.py migrate
```
Make sure that you are in the PROJECT folder and not the app folder.
From there run 
```
python3 manage.py runserver
```
And head to the url "/blog" as the home page's design isn't finished
## Problems
Haven't had static files hosted on the live site for now, will do in the future 
### Live site
https://carhub-ft.herokuapp.com/