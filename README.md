# remember-backend
This backend functionality is build on Django using Django REST Framework with a Postgres SQL database. The frontend React application uses the React library Axios to connect with the Api.
The live link can be found here - https://remember-backend-ff8df02164f2.herokuapp.com/

# Testing
Profile Api:
List profiles:
Steps | Expected result | Actual Results | Pass / Fail
------------- | ------------- | ------------- | -------------
Connect to https://remember-backend-ff8df02164f2.herokuapp.com/| Site should open with message "Welcome to my drf API!" | As expected | Pass 
Append uri /profiles | List profiles data | As expected| Pass
Append uri /profiles/2| Fetch profile by id | As expected| Pass
Append uri /profiles/66| Error message: "HTTP 404 Not Found" "detail": "Not found."  | As expected| Pass
Login| Django REST framework login page should open | As expected| Pass
Login as Sam| Form to update Sam's own profile should open | As expected| Pass
Logout| Form to update Sam's own profile should not open | As expected| Pass
Append uri /posts | List posts data | As expected| Pass
Append uri /posts/2| Fetch post by id| As expected| Pass
Append uri /comments| Fetch comments | As expected| Pass


# Bugs
 * 
# Deployment
The Django project Remember-backend is deployed on Heroku cloud service from Github repository remember-backend https://github.com/SamsKod/remember-backend/. A Postgres database on ElephantSQL cloud service is used and static files is handled by cloud service Cloudinary.


Steps to deploy:

* First you need to create accounts at Heroku, ElephantSQL and Cloudinary Cloud services.
* Create a new instance in ElephantSQL ( you ca use the free Tiny Turtle plan)
* Copy your ElephantSQL database url in that shows in dashboard.
* Create a new app in Heroku
* Open Heroku app and open settings tab. Click Reveal Config Vars.
  * Add Config Var: DATABASE_URL with Value of your ElephantSQL database url.
  * Add Config Var: CLOUDINARY_URL with Value of your Cloudinary API Enviroment variable you find on the Cloudinary dashboard.
  * Add Config Var: SECRET_KEY with random value you create. 
  * Add Config Var: DISABLE_COLLECTSTATIC with Value 1 .
* In Heroku App settings page you select Deployment Method Github and connect to your Github repository where you have copied the code and deploy by clicking Deploy Branch.



# Credits
Example code and design is used from:
- 

# Media
My photos.

