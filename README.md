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


<details><summary>See feature images</summary>

![Home page](docs/features/home_page.png)
</details>


### Logo & Navigation
- Custom logo for the business
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- displayed on all pages

<details><summary>See feature images</summary>

![Navigation Bar](docs/features/fnav_bar_login.png)
![Navigation Bar](docs/features/nav_bar_bookings.png)
![Navigation Bar](docs/features/nav_bar_hamburger.png)
</details>


### Footer
- Contains social media links and copyright
- displayed across all pages

<details><summary>See feature images</summary>

![Footer](docs/features/footer.png)
</details>


### Sign up / Register
- Allow users to register an acoount
- Username and password is required, email is optional

<details><summary>See feature images</summary>

![Register](docs/features/sign_up.png)
</details>


### Login
- User can login to create a booking, view bookings, edit and delete bookings

<details><summary>See feature images</summary>

![Login](docs/features/sign_in.png)
![Login](docs/features/sign_in_2.png)
</details>


### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>See feature images</summary>

![Logout](docs/features/sign_out.png)
</details>


### Book
- Allows the user to book a table using the booking form
- Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format

<details><summary>See feature images</summary>

![Book](docs/features/reservations.png)
![Book](docs/features/reservations_error.png)
![Book](docs/features/reservations_double_booking.png)
</details>


### My Bookings
- Allows the user to see all their bookings in a paginated layout, 4 per page
- If the booking is older than today it is automatically expired for the user
- Status of the booking is displayed, awaiting confirmation and when approved will then change to confirmed status for the user

<details><summary>See feature images</summary>

![My Bookings](docs/features/my_bookings.png)
</details>


### Edit Booking
- Allows the user to edit their booking to another date, time, guest count and table
<details><summary>See feature images</summary>

![Edit Booking](docs/features/edit_booking.png
![ImaEdit Bookingge](docs/features/edit_booking_error.png)
</details>


### Cancel Booking 
- Allows the user to cancel their booking, asks user are they sure
  
<details><summary>See feature images</summary>

![Cancel Booking](docs/features/fcancel_booking.png)
</details>


### Food Menu
- The food menu displays all available foods on the menu
- Menu is seperated by starters, mains and desserts
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete foods via the admin panel
  
<details><summary>See feature images</summary>

![Food Menu](docs/features/food_menu.png)
</details>


### Drinks Menu
- The drinks menu displays all available foods on the menu
- Menu is seperated by wines, beers and cocktails
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete foods via the admin panel 
  
<details><summary>See feature images</summary>

![Drinks Menu](docs/features/drinks_menu.png)
</details>


<!-- ### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page
  
<details><summary>See feature images</summary>

![Blog](docs/features/feature-blog.PNG)
</details>


### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Registerd user can comment on the blog
  
<details><summary>See feature images</summary>

![Blog Expanded](docs/features/feature-blog2.PNG)
</details>


### Comments
- Comments made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend
  
<details><summary>See feature images</summary>

![Comments](docs/features/feature-comments.PNG)
</details> -->

<!-- ### Likes
- Likes made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can like a blog post
  
<details><summary>See feature images</summary>

![Comments](docs/features/blog_like.png)
</details>  -->


### Contact Us
- Registered users can DM staff via the message box
- Contact info such as, phone, email, and address is displayed
- A Google Map is embedded with the address for users to use
  
<details><summary>See feature images</summary>

![Contact Us](docs/features/contact_message.png)
![Contact Us](docs/features/contact_address.png)
![Contact Us](docs/features/contact_map.png)
</details>


### Social Media Links
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/social_media.png)
</details>


### Pagination
- Pagination is used on the bookings list and the blog page
- Ensures the page is kept tidy as only 4 items are displayed per page
  
<details><summary>See feature images</summary>

![Pagination](docs/features/pagination.png)
</details>
