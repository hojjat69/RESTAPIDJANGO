# RESTAPIDJANGO
The purpose of this project is to build a REST API with abilities of post,get, put, patch and delete method as well as user creation, login and search. 
Moreover each user is able to put status and update it and view or search others'. The localhost/8080/api has three sub-roots:

localhost/8080/api/profile/ >> to view users, search (by name and email), create and update (if authenticated) user profile

localhost/8080/api/feed/ >> to create a status or update, search and view (if authenticated) others' 

localhost:8000/api/hello-viewset/ to test API viewset and viewset methods like  post,get, put, patch and delete method 

to check update and its authentication ability>> localhost/8080/api/feed/<feed_id>/






1. You need to install Python on your computer to visualize the web. 


 
2. Now open cmd and set your dir to project folder and run the manage.py by python as follow:
   `python manage.py runserver`
   
   
3. Create a user in 'localhost/8080/api/profile/' by post method



4. You need to create migration by writing the following command in cmd:
   `python manage.py makemigrations`
   
   
   
5. The last stem is migration by writing the following command in the cmd:
   `python manage.py migrate`
   
   

6. Install ModHeader extention for google chrome



7. Then login with created users in localhost/8080/api/profile/login and check the API abilities


8. Copy the token provided by API and use it in ModHeader as Authorization 


  
6. Open your browser and browse `http://127.0.0.1:8000/`


  
Enjoy your browsning ;)  
 

