# Jim's Bar & Grill

![Am I Responsive](docs/amiresponsive.png)

**Developer: James Lynch**

💻 [Visit live website](https://jims-bar-and-grill.herokuapp.com/)

## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Jim's Bar & Grill is a fictional business where users can create an account, book a table, read a blog and view the food and drinks menu.
<hr>

### User Goals

- To create a table booking
- To be able to view edit and cancel bookings
- To view menus, a blog and contact info

### Site Owner Goals

- To provide a solution to allow users to book a table online
- To attract more business with a well crafted site
- Provide a modern application with an easy navigation
- Fully responsive and accessible

<hr>

## User Experience

### Target Audience

- Users that wish to book a table for a meal or a party with family and friends
- Past and new customers for the business
- Tourists visiting the area that are looking for a meal or a drink or both
- Fans visiting the area for a sports event or a music concert
- People employed in the area to eat and drink after work

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>

## User Stories

### As a website user: 

1. I want a site in which I can view a contact us page to get in touch with the business (Required)
2. I want a site in which i can view view blog posts so i can read articles and get a better sense of the restaurant (Should have)
3. I want a site in which i can like a blog post so I  can interact with the restaurant (Should have)
4. I want a site I can view comments the restaurant's blog posts so I can see what other people thinks about about the posts (Should have)
5. I want a site I can create and register an account which stores my details for faster bookings (Required)
6. I want a site I can create a comment for a blog so I can converse with the restaurant and its community (Should have)
7. I Want a site I can view the amount of likes on a blog post so i can see if the post is highly rated (Should have)
8. I want a site I can navigate through easily and have all features accessible (Required)
9. I want a site in which I have full use of all navbar, body, footer and icon features so that I can navigate the site views, forms, access requests, and access socials (Required)
10. I want a site I can view paginated blog posts so the there's not too much information being shown (Should have)
11. I want a site i can provide a contact us page so that users can reach out to the business (Required)
12. I want a site I can not double book a table as it would be invalid (Required)
13.	I want a site that I can view the opening hours, contact details, an address along with a map so that I know where the business is located and when the business is open along with how to contact them via email, phone and socials (Required)
14. I want a site I can view a menu option so that I can decide wether to eat at the business (Required)
15. I want a site in which i am unable to book a table in the past as i would be invalid (Required)
16. I want a site in which i can view a notifaction so that I know if my action of creation, edit, or deletion of a booking has been confirmed (Required)
17.	I want a site I can delete my booking so that I can cancel my table reservation (Required)
18.  I want a site where i can view all my booking requests with the date and time (Required)
19.	I want a site I can request a booking by selecting a time and date so that I can reserve a table (Required)
20.	I want a site I can update my booking so that I can choose another available date and time (Required)
21.	I want a site I can create a booking so that I reserve a table (Required)
22. I want a site I can view a confirmation of my booking (Required)

### Admin / Authorised User

1. As an Admin / Authorised User I can acces the backend of the site by logging in (Required)
2. As an Admin / Authorised User I can manually manage all blog content on site (Required)
3. As an Admin / Authorised User I can review bookings as to check if any double bookings were registered (Required)
4. As an Admin / Authorised User I can access the back end of the site to create, edit and delete any of the menu options (Required)
5. As an Admin / Authorised User I can search through reservations and menu items should i require that information (Should have)
6. As an Admin / Authorised User I can view filtered bookings based on the name, email and date (Should have)
7. As an Admin / Authorised User I can manually create, edit or delete a reservation should a customer request (Should have)

### Site Owner  

1. As a Site Owner I want to provide a easy to use site with all relevent information displayed while being fully responsive (Required)
2. As a Site Owner I want a site were all data entered is validated catalogued correctly without any errors (Required)

### Kanban, Epics & User Stories

- GitHub Kanban boards were used to visualize project progress
- The label feature in github was used to create Epics
- Todo, In Progress and Done labels were used in the kanban

</details>

<details><summary>User Stories</summary>

![User stories](docs/features/user-stories-1.png)
![User stories](docs/features/user-stories-2.png)
![User stories](docs/features/user-stories-3.png)

</details>

<details><summary>Kanban</summary>

![Kanban](docs/features/kanban-1.png)
![Kanban](docs/features/kanban-2.png)
![Kanban](docs/features/kanban-3.png)
![Kanban](docs/features/kanban-4.png)


</details>

<hr>

##### Back to [top](#table-of-contents)<hr>

## Design

### Design Choices

My goal is to create a simple and efficent website so all features are easily accessible. In order to achieve this, all pages are responive and labeled. All content is made easy to read with links to features clearly visible without being excessive.

### Colour
The colour sheme was chosen as a dark red and black theme in which i was aided by Adobe Color by using their Split Complementary Color feature. A light grey and simple white was used to give it contrast which was selected also through adobe color. A slighly dark grey was selected for certain elements in the events page.
<br>
 
![Colour scheme](docs/color-palette.png)


### Fonts
Kanit was used for the logo, heading and sub-heading's. 
<br>
Martel Sans was used for smaller body elements and navbar . 
<br>
The fonts chosen because of the contrast between them with Kanit's loopless lettering matching Martel Sans' fluidity. The match for this font was made through fontjoy.
<br>
San-serif was used as my backup.

### Structure
The home page is designed to have all relevanet information easily accessible with all relevent navigation clearly visible. The logo is postioned on the left, navigation on the right and this is shown on all pages in the same layout. The design is created also to be responsive on all viewports while maintaing all relevant information: 
- Homepage with a hero image with login details/bookings anchor. Cards are also used with details and links to other pages of the site.
- Food menu has the current list of all available foods from the database sorted by different sections of the menu
- Drinks menu has the current list of all available drinks from the database sorted by different sections of the menu
- Blog page has a paginated list of blogs posted by an admin or authorised user, 6 per page
- Blog expanded displays a blog the user has selected so they can read the blog, if they are logged in they can also leave a comment or like the comment which will then need to be approved before it is displayed.
- Reservations page allows registered users to book a table , date requested, time requested and guest count
- My bookings displays all confirmed reservations for the user that they have made
- My bookings page aloso lets users edit or cancel any confirmed reservations made
- Cancel booking allows the user to cancel the booking which will then delete it from the database
- A contacts page with a message section, the address and a map should the user need to contact the restaurant
- Login / Logout allows users to login to make bookings, view, edit, and delete bookings
- Register section allows to have their details stored for easier access to interact with sections of the site
- 404 page is displayed when a 404 error is raised

### Wireframes

<details><summary>Home</summary>
<img src="docs/wireframes/home.png">
(docs/features/kanban-1.png)
</details>
<details><summary>Menu</summary>
<img src="docs/wireframes/menu.png">
</details>
<details><summary>Blog</summary>
<img src="docs/wireframes/blog.png">
</details>
<details><summary>Reservations</summary>
<img src="docs/wireframes/reservations.png">
</details>
<details><summary>Contact</summary>
<img src="docs/wireframes/contact.png">
</details>
<details><summary>Register</summary>
<img src="docs/wireframes/register.png">
</details>
<details><summary>Log In/Details</summary>
<img src="docs/wireframes/log_in_details.png">
</details>
<details><summary>404</summary>
<img src="docs/wireframes/page_404.png">
</details>

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Two database model shows all the fields stored in the database

##### User Model
The User Model contains the following:
- username
- first_name
- last_name
- email
- password
- groups
- user_permissions
- is_staff
- is_active
- is_superuser
- last_login
- date_joined

##### FoodItem Model
The FoodItem Model contains the following:
- food_id
- food_name
- description
- price
- food_type
- available

##### DrinkItem Model
The DrinkItem Model contains the following:
- drink_id
- drink_name
- description
- price
- drink_type
- available

##### Booking Model
The Booking Model contains the following:
- booking_id (PrimaryKey)
- created_date
- requested_date
- requested_time
- guest (ForeignKey)
- email
- phone
- status
- seats
- guest_count

##### Post Model
The Post Model contains the following:
- title
- slug
- author (ForeignKey)
- featured_image
- post_id (PrimaryKey)
- excerpt
- updated_date
- content
- created_date
- status
- likes

##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- name
- email
- message
- created_on
- approved

##### Contact Model
The Contact Model contains the following:
- message_id (PrimaryKey)
- created_date
- user (ForeignKey) 
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- message

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Bootstrap 5
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.3](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)

##### Back to [top](#table-of-contents)


## Features

### Home page
- Home page includes nav bar, main body and a footer
- User stories covered: 


<details><summary>See feature images</summary>

![Home page](docs/features/home_page.png)
</details>


### Logo & Navigation
- Custom logo is displayed
- Fully Responsive layout when viewed on differnt viewports
- Provides a logged in/out status
- Featured on all pages
- User stories covered: 

<details><summary>See feature images</summary>

![Navigation Bar](docs/features/nav_bar_login.png)
![Navigation Bar](docs/features/nav_bar_bookings.png)
![Navigation Bar](docs/features/nav_bar_hamburger.png)
</details>


### Footer
- Featured on all pages
- Consists of all social media links
- User stories covered: 

<details><summary>See feature images</summary>

![Footer](docs/features/footer.png)
</details>


### Sign up / Register
- Allows users to sign up or register an account
- Password and username is required
- User stories covered: 

<details><summary>See feature images</summary>

![Register](docs/features/sign_up.png)
</details>


### Login
- User can login to advantage of a number of features when logged in
- User stories covered: 

<details><summary>See feature images</summary>

![Login](docs/features/sign_in.png)
![Login](docs/features/sign_in_2.png)
</details>


### Logout
- Allows the user to securely log out
- Prompt displays asking user to confirm if they want to log out
- User stories covered: 

<details><summary>See feature images</summary>

![Logout](docs/features/sign_out.png)
</details>


### Reservations
- Allows the user to book a table using the reservation form
- A prompt is displayed if incorrect or invalid data is posted
- User stories covered:

<details><summary>See feature images</summary>

![Reservations](docs/features/reservations.png)
![Reservations](docs/features/reservations_error.png)
![Reservations](docs/features/reservations_double_booking.png)
</details>


### My Bookings
- Users can view all valid bookings pagianted in a 6 card layout 
- Bookings are automatically expired when the date and time goes passed the current date
- The staus of the booking is displayed
- User stories covered:



<details><summary>See feature images</summary>

![My Bookings](docs/features/my_bookings.png)
</details>


### Edit Booking
- Users can edit their booking to another date, time and number of guests
- User stories covered:

<details><summary>See feature images</summary>

![Edit Booking](docs/features/edit_booking.png)
![Edit Booking Error](docs/features/edit_booking_error.png)
</details>


### Cancel Booking 
- Users can cancel their booking and gives a prompt to confirm
- User stories covered:
  
<details><summary>See feature images</summary>

![Cancel Booking](docs/features/cancel_booking.png)
</details>


### Food Menu
- All available food items are displayed
- Menu is seperated in sections
- Admin/Authorised users can add, edit and delete items
- User stories covered:
  
<details><summary>See feature images</summary>

![Food Menu](docs/features/food_menu.png)
</details>


### Drinks Menu
- All available drink items are displayed
- Menu is seperated into differnet sections
- Admin/Authorised users can add, edit and delete items
- User stories covered:
  
<details><summary>See feature images</summary>

![Drinks Menu](docs/features/drinks_menu.png)
</details>


<!-- ### Blog
- Blog posts are displayed 
- All blog posts are organised into a pagianted format for every 6 posts
- User stories covered:
  
<details><summary>See feature images</summary>

![Blog](docs/features/feature-blog.PNG)
</details>


### Blog Expanded
- Blog is displayed
- An image is displayed at the top
- If no image is uploaded a default image is then used
- Registerd user can comment on the blog
- Registerd user can like the blog
- User stories covered:
  
<details><summary>See feature images</summary>

![Blog Expanded](docs/features/feature-blog2.PNG)
</details>


### Comments
- Blog comments reuqire approval by admin and will display as pending untill admin review
- Users must be signed in to comment on a post
- Approaval of comments must be done through the admin panal
- User stories covered:
  
<details><summary>See feature images</summary>

![Comments](docs/features/feature-comments.PNG)
</details> -->

<!-- ### Likes
- The number of likes is displayed
- Only registered users can like a blog post
- User stories covered:
  
<details><summary>See feature images</summary>

![Comments](docs/features/blog_like.png)
</details>  -->


### Contact Us
- Users who are signed in can send a message with the message form
- Phone, email, address and opening hours are displayed
- An embedded Google Map is also displayed
- User stories covered:
  
<details><summary>See feature images</summary>

![Contact Us](docs/features/contact_message.png)
![Contact Us](docs/features/contact_address.png)
![Contact Us](docs/features/contact_map.png)
</details>


### Social Media Links
- An icon with a link is used for each social media displayed
- Each link opens in a new tab so the user has access to the website after being redirected
- Featured on all pages
- User stories covered:
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/social_media.png)
</details>


### Pagination
- The blog post displays and the booking list both use pagination
- Ensures a consistant and organised display is shown with only 6 itemsa per page
- User stories covered:
  
<details><summary>See feature images</summary>

![Pagination](docs/features/pagination.png)
</details>

<!-- ### 404 page
- A custom 404 page takes away the confusion of not landing on the page they had intended to land on.
- User stories covered: 

![404 image](docs/features/image_404.png)
</details> -->

### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>

![CSS Validation](docs/validation/css.png)
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>

![CSS Validation](docs/validation/js.png)
</details><hr>

### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle as PEP8online was down

<details><summary>Tool used: Pycodestyle</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle.PNG">
</details>

<hr><summary>Bar & Grill</summary><hr>


<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-views.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bar-and-grill-test-urls.PNG">
</details>


<hr><summary>Bookings</summary><hr>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-views.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-test-urls.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-bookings-forms.PNG">
</details>


<hr><summary>Blog</summary><hr>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-views.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-models.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-test-urls.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-blog-forms.PNG">
</details>


<hr><summary>Contact</summary><hr>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-views.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-test-views.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-contact-test-urls.PNG">
</details>


<hr><summary>Home</summary><hr>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-home-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/validation/pep8-validation-pycodestyle-home-views.PNG">
</details><hr>
