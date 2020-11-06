# Let's go hiking

## Mission Message

The aim of 'Let’s Go Hiking' is to bring together individuals with a sense of adventure as they complete hiking challenges and gain rewards. 
![Home page](/media/readme/home_page.png)
Let's go hiking will provided inspiration to get into the great outdoors and 
create a online social community who like to hike and who love a challenge. 
![About page - mobile](/media/readme/about_mobile.png)
* This site will provide hiking challenges that the user can purchase.
![Challenges page](/media/readme/challenge_page.png)
* With the
purchase the user will become a member of the site and gain access to the full hiking 
information pack and will received a challenge reward, such as a patch or sticker. 
* These patches will be individually designed and exclusive to purchasing the challenge. 
* The member will then be able to share their adventure with other members through the 
community blog (future feature).
 * This allows a hike to become more of an event and to create long lasting memories.
![Shop page](/media/readme/shop_page.png)
* The user will be also able to purchase more apparel through the 'Let's go hiking' shop. 

## UX


### User Stories

#### User Story 1 - The Adventurer
This user is a adventurer at heart and already hikes a lot. This user is looking for insporations for a new challenge and way to stay inspired and motivated. Let's Go Hiking will provide new and exciting routes for the user who can challenge themsleves and recieve a award as well. This will drive a sense of acheivement and even competition between other users, as the user collects awards for completing challenges. They also will browse the shop for items perhaps as gifts.
#### User Story 2 - The Newbie
This user is new to hiking and not sure of where to go and routes to take. This site will give them a full guide and the user can build themselves up from easy challenges up to the hard challenges collect awards along the way.
#### User Story 3 - The Social Bragger
This user will enjoy completing challenges for the awards and the bragging rights, they will be vocal users of the community blog and will need fresh content and products in the shop, as well as on the social media accounts to keep them engaged.
#### User Story 4 - Site owner
The site owner will want easy access to add new products and add new challenges. The will want a way for users to suggest challenges and to give direct feedback to the site admin.


### Wireframes
![Landing page wireframe](/media/readme/landing_page_wireframe.png)
![Challenges page wireframe](/media/readme/challenges_wireframe.png)
![Shop wireframe](/media/readme/shop-wireframe.png)
#### Orginal idea - planning stage.
* [Idea overview](https://eb258abd-fe1f-4a1b-99b7-36b61e9f6869.ws-eu01.gitpod.io/files/download/?id=b6ed0fda-0a2f-40cf-9f35-c2f7bb6b2716)
* [Slimmed down Idea Brainstorm](https://eb258abd-fe1f-4a1b-99b7-36b61e9f6869.ws-eu01.gitpod.io/files/download/?id=3d6fe427-68bd-484f-ae0d-abfc5ec0fc2f)
* [Idea Brainstorm](https://eb258abd-fe1f-4a1b-99b7-36b61e9f6869.ws-eu01.gitpod.io/files/download/?id=88b86278-b4d0-4e99-9ac8-32ac644b12e6)
* [Plan of process covering user stories with features](https://eb258abd-fe1f-4a1b-99b7-36b61e9f6869.ws-eu01.gitpod.io/files/download/?id=a6113676-cf9c-4f4d-b4bf-7d6fee7297f3)

## Features

### Home app

The home app has a bold landing page with a hero image showing hikers that transistions into another hero image. With a clear subtitle of find your next challenge the user will be inspired to find their next adventure. For new users there is a clear path to find out more information by using the find out more button, which links to the about page.
#### Navbar
The navbar features the site logo of geometric mountain with a path and a bold font displaying the sites name. With clear navigation links of home, Challenges, Shop and a shooping cart, the user will be able to access what they need with ease. The user also has clear access to log in to the site or to sign up if they are a new user. The log in and sign up buttons direct users to the correct page for them with the option to change on screen if they selected incorrectly. These pages are driven by allauth.
The navbar link to shop has a dropdown menu for quick navigation to the area of teh shop the user requires.
#### Footer
The footer features links to the about page, and contact us pages as well as the sites two social media accounts.
#### About us
The about us page features a quote to inspire the user and a mission statement and a step by step guide of how to use the site. At the bottom there are three buttons for navigation, to go back to home, to check of challenges and to start shopping to pull the user into the site.
#### Contact page
The contact page allow the user to submit a question, a suggestion or any feedback directly to the admin pages of the site. This has a pop up message of success when the message is successfully sent.
### Challenges app
The challenges app displays a card of each challenge displaying a image and information that the user will need in making their descision to purchase such as location and difficulty.
The challenge card has an explantion of what the user receives on purchase and the user has the option to add to cart and to add a certain quantity. After adding to cart the user recieves a success meassage stating their selected challenge has been added to the cart.
### Shop app
The shop app is accessable in shopping by category via the navbar or shopping for everything. The shop has a secondary nav with links to the categories allowing users to easily swtich between categories. 
The shop displays products in cards with a large image, the product name, a brief description and price. The user then can use the add to cart button and the quantity selector. The user recieves a success message that the item was added to their cart.
### Cart app
The cart app is accessed using a fontawesome icon with the additional functionality showing how many items are in the users cart.
The cart when empty will inform the users that their cart is empty and there are buttons to direct users back to shop or challenges.
When the user has added items to the cart the items will be displayed with a image the name, quantity with the option to alter the quantity or remove the item from cart. The user can also see a running subtotal and the grand total including the delivery charge.
At the bottom of the cart there is the options to continue shopping or to proceed to payment.
### Payment app
The payment app has a overview of the users order, and a form to collect the user information and the stripe card element for payment. There is also an option to build a profile if a new user.
(BUG - The payment intents are present on the stripe dashboard showing the correct amount, but no user data is collected and no order number is created)
### Profiles app
The profiles app has a side navbar to allow users to access their profile information and edit it (See Features left to implement). It also has a my challenges page to show the user the full route information for the challenge they have purchased and a my orders page to show the user past purchases. 
The user also has a page to submit a challenge idea which the site owner can access through django admin, the site owner can then decide if the challenge idea should be uploaded to the site.
The site owner also as a superuser once logged in has access to add a challenge and add a product pages via the my account dropdown in the navbar, allowing for easy access to add more features. 


## Features left to implement 

Media queries - I have implemented a substanial amount of media queries yet I know there are elements such as the challenge table that is not reponsive due to time constraints.

Payment app - The payments app has caused a lot of issues. I orginially wanted to use stripe checkout. After following one set of guidence that was not successful, I re-built is with success. Connecting to stripe using checkout. ![Stripe confirmed payment](/media/readme/stripe1.png).
After committing the changes and shutting my laptop down, it never worked again. Being short on time I followed the Code Institutes Boutique tutorial to install Stripe with the payment element. Again, I had a lot of difficulty in getting stripe to work correctly, for a while it blocked the cart even connecting to the payment.html page. 
After debugging to get the payments.html page to render I discovered that the payment intents where arriving on the stripe dashboard but it was throwing this error "$.post is not a function at HTMLFormElement.<anonymous>" ![Stripe payment intents](/media/readme/stripe2.png).![Stripe dev dashboard](/media/readme/stripe3.png).
I re-followed the tutorial and continued to the webhooks to hopefully discover an error or the issue that is causing stripe to gain intent but not produce an order. Because of this the additional functionality for users to see their orders and the specific challenge paid for has not been built.

Profile app - The Profile app renders all profiles when authorised which is not the explectation for the profile app. The views of my orders and my challenges have limited functionality due to this. The Edit profile 


## Future ideas for expansion
* The community blog. This would allow the let's go hiking users to discuss the latest challenge they had completed and share photos.
* More variation of challenges - Such as challenges aimed at children, or beginners with more guidedence on the gear to use and how to be safe on the mountains.
* Newsletter - Emailed to all users to inspire and inform users of new challenges, pruductd or features.
* Interactive maps - The users would have a clear positions of start points and car parks.
* Navigation - A system of navigation using a maps api to give the user access to responsive maps during the challenge to guide the user on their route.
* Multi-locations - The challenges can cover world wide hiking locations allowing a global user group and inpsire travelers to explore areas unknown to them.
* Product growth in shop - To expand the shop product line.


## Technologies Used

- Python
- html
- css3
- javascript
- JSON
- Django
- SQLite
- S3 Amazon Web Services
- Github
- Heroku
- Bootstrap
- Django allauth
- crispy forms



## Guidence/Resourses from

- “Created my free logo at https://www.LogoMakr.com”
- "Additional guidence from Django Docs https://www.djangoproject.com/"
- "Fixes for small queries https://stackoverflow.com/"
- "for guidence on cripsy forms set up https://django-crispy-forms.readthedocs.io/en/latest/index.html"
- "Transitions of images on home page from https://cssreset.com/how-to-create-the-perfect-image-crossfade-with-css3-transitions/"
- "Shopping cart with item counter from https://www.solodev.com/blog/web-design/how-to-show-the-total-number-of-items-in-customer-shopping-carts.stml"
- "Bootstrap toasts https://getbootstrap.com/docs/4.3/components/toasts/"
- "Payment app from Stripe https://testdriven.io/blog/django-stripe-tutorial/"
- "Payment app from https://www.youtube.com/watch?v=JwhEjEqG43M"
- "Payment process guided by Code Institute E commance tutorials"

## Testing



Coverage - Nose

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.



## Deployment

This project with built using gitpod and hosted by heroku.

### Deployment process

1. Starting in gitpod - Django was installed using pip3 
2. The project was started using - django-admin startproject LetsGoHiking .
3. Migrations where then ran using - python3 manage.py makemigrate/migrate
4. A superuser was created 
5. A requirements.txt was created using - local
6. gunicorn was installed using pip3
7. A procfile was added using - web: gunicorn LetsGoHiking.wsgi:application 
8. Using the Heroku CII to login into heroku - heroku login -i
9. The app was in heroku was created in the CII
10. Environment variables was created using touch env.py file to hide secret keys
11. In env.py and os was imported into settings.py - for env - if os.path.exists('env.py'): import env
12. env.py was added to .gitnore with pycache and db.sqlite
13. In the heroku app confog vars - DISABLE_COLLECTSTATIC add and set to 1
14. The SECRET_KEY was added to heroku config vars
15. The heroku app added to ALLOWED_HOSTS = ['claire-roberts-lets-go-hiking.herokuapp.com', 'localhost'] in settings.py
16. This was then push to git and heroku with git push heroku master
17. The App was successfully deployed
18. if 'DATABASE_URL' in os.environ: DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else: DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}} was added to settings.py
19. dj-database-url and psycopg2-binary where install with pip and frooze to requirements.txt dj-dj_database_url was the imported into settings.pycache
20. Migrations where ran to heroku using heroku run python3 manage.py makemigrations
21. Static files and medias files set up to run in local developement and to use AWS on heroku.
22. The bucket was set up on S3 for the static and media files
22. The AWS secret keys added to heroku config vars. 
23. boto and django storages install and added to requirements.txt
24. The AWS secret keys where added to env.py
25. custom_storages.py was created and storages added to installed apps in settings.py
26. DISABLE_COLLECTSTATIC removed from heroku config vars
27. DEBUG set up for in environment using os.environ and adding to to env.py
28. Code pushed to heroku



## Credits

## Guidence/Resourses from

- “Created my free logo at https://www.LogoMakr.com”
- "Additional guidence from Django Docs https://www.djangoproject.com/"
- "Fixes for small queries https://stackoverflow.com/"
- "for guidence on cripsy forms set up https://django-crispy-forms.readthedocs.io/en/latest/index.html"
- "Transitions of images on home page from https://cssreset.com/how-to-create-the-perfect-image-crossfade-with-css3-transitions/"
- "Shopping cart with item counter from https://www.solodev.com/blog/web-design/how-to-show-the-total-number-of-items-in-customer-shopping-carts.stml"
- "Bootstrap toasts https://getbootstrap.com/docs/4.3/components/toasts/"
- "Payment app from Stripe https://testdriven.io/blog/django-stripe-tutorial/"
- "Payment app from https://www.youtube.com/watch?v=JwhEjEqG43M"
- "Payment process guided by Code Institute Boutique tutorials"

### Content
- The text for the challenges was copied from 'Great mountain days in the Lake District by Mark Richards'
- Quotes taken from google.

### Media
- The photos used in this site were obtained from google images
- The two map images for the challenges are taken from 'Great mountain days in the Lake District by Mark Richards'

### Acknowledgements

- I received inspiration for this project from  Code Institute Boutique tutorial.
- The idea for patches was inspired by https://www.conquerlakedistrict.co.uk/
- The orginal idea came from wanting to know the best hikes when traveling and knowing where to park and which route to take. I also like mementos and keepsakes and think a challenge drives you to puch yourself to go further, higher or just to go when its raining. This is idea I will pursue further, once I have more experience to build a site that truely reflects what I am after myself as a user of this site.