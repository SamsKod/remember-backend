# remember-backend





## Features left to implement
- 


# Testing


# Validator Testing

### HTML
No errors were returned when passing through the official W3C validator.
### CSS
No errors were found when passing through the official (Jigsaw) validator. Although there are still some css issues to handle because different browsers render css in different ways. Chrome works best for this application. 
### Accessibility
The Lighthouse test tool show good result in accesibility
![Screenshot](assets/images/screenshot_lighthouse.png)

# Bugs
 * 
# Deployment
This site is deployed on Heroku cloud service the django-api. A Postgres database on ElephantSQL cloud service is used and static files is handled by cloud service Cloudinary.

Steps för deployment:

* Accounts was setup at Heroku, ElephantSQL and Cloudinary.
* After Django app with Django REST Framework is setup a connection to Cloudinary is configured for storage of media files. Connection to Postgres SQL database att ElephantSQL is setup for database storage.
* Code is commited to Git and then push top Github.
* On Heroku a new app is created and in settings in Heroku config vars is set for connection to the Elephant and Cloudinary, port and secret key is also set.
* Heroku App is connected to github repository remember-backend and then deployed to Heroku.


The live link can be found here - https://remember-backend-ff8df02164f2.herokuapp.com/

# Credits
Example code and design is used from:
- 

# Media
My photos.

