
# OVERVIEW

This template was made as a guide to ensure you cover assessment criteria in your fourth portfolio write up. It is specific to the **PORTFOLIO 4: Full-Stack Toolkit** project. 

## Helpful tools

Markdown's not all that easy so sometimes you may want to use some tools to make tables. 

- [Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
- [markdown table generator](https://www.tablesgenerator.com/markdown_tables) - used to help with documentation table formatting
- [mardown table of contents generator](https://ecotrust-canada.github.io/markdown-toc/) - used to create table of contents (be weary it does have some bugs if you have dashes or trailing spaces in your headers)
- [readme.so](https://readme.so/) - if you don't want to learn markdown, this tool might help you

# Table of Contents
Copy your readme to http://ecotrust-canada.github.io/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.

====================================== The Sections you Fill in are below ==============================


# CERU - AUTHENTIC AMERICAN DINER

<img width="977" alt="responsive-app" src="https://user-images.githubusercontent.com/82375381/157510961-1f9b70d1-6980-4699-9196-c7417c2ca87a.png">

## Author

Gabriel Alves

You can visit my GitHub page [here](https://github.com/gabriel-alves-p).

## Project Overview

This project was incepted with the goal of creating a 'hassle-free' booking system for a Diner to increase their revenue. It achieves this goal by means of two models; a "user", and a "booking" system.
The user can very easily sign-up for an account, which only then grants them access to the booking form. Users are also allowed the freedom to view, edit, and cancel their bookings as well as their own personal accounts with the Diner if they wish to do so, following the C.R.U.D. Operations (Create, Read, Update, Delete).

The app also aims to reflect the diner itself in its color pallette and vintage feel, friendly and straight out of the 70s.

You can view this web application [here](https://ceru-restaurant.herokuapp.com/).

## Technologies

### Languages
- HTML
- CSS
- Python
- JavaScript
- Markdown

### Libraries & Frameworks
- Django
- Bootstrap

### Django Extensions
- Allauth
- Crispy forms
- Summernote

### Database
- PostgreSQL
- SQLite

### Deployment, Repository & Media
- GitHub
- Gitpod / VSCode
- Heroku
- Cloudinary
- Adobe Photoshop

## UX

### Project Goals / Strategy Plane

- The website's target audience are adults both with or without families who are interested in an out of the ordinary experience, or that possibly grew up watching American diners on TV, or that possibly have been to one.
- The website is designed to be easy to read and intuitive, with information about the diner, menu links, contact form (including social media links) and the address all found in the home page.
- The website's perhaps most important goal is to increase revenue and credibility via the implementation of a booking system.
- Dedicated pages for account related tasks (sign up, sign in, sign out, edit details, delete account, etc).
- Dedicated pages for booking related tasks (make a booking, view your bookings, edit booking, delete booking, etc).
- The website is also designed to be nostalgic to users and really highlight the decade in the overall feel of the website.
- The website is fully responsive from the largest desktop viewports (4k) to the smallest phone viewports (320px).

### Scope Plane

Features that, based on the strategy plane above, made it onto the web app include:

#### Home Page
> - Same navigation bar shared across all pages, checks whether user is authenticated or not and displays links accordingly. Has logo on top left corner.
> - Toggle menu icon appears and links hide when under 768px screen width.
> - Hero image on home page.
> - Title and brief welcome message.
> - Booking button highlighted as soon as user lands on page.
> - An about us section with a title and two paragraphs explaining the diner's history.
> - An image to decorate the text.
> - A menus section with a title.
> - Three menu buttons, each leading to a different part of the menu page.
> - A carousel of images that showcase the food and drinks served at the diner.
> - A section with a title containing a Google Maps iframe, so that users can get directions easily.
> - A section with a title containing a Contact Us form (first name, last name, email, mobile phone, and message inputs and a submit button).
> - A footer with opening times, address, social media links. Shared across all pages.

<img width="1424" alt="home-screenshot1" src="https://user-images.githubusercontent.com/82375381/157675982-64a87328-e060-4bb6-9acd-1e1b0cd107ee.png">
<img width="1425" alt="home-screenshot2" src="https://user-images.githubusercontent.com/82375381/157675999-105b85cb-9303-41db-9c49-831bb5882c82.png">
<img width="1426" alt="home-screenshot3" src="https://user-images.githubusercontent.com/82375381/157676014-4c4f9693-4121-48e5-88c5-6449fb9a21ca.png">
<img width="1425" alt="home-screenshot4" src="https://user-images.githubusercontent.com/82375381/157676036-e9e7ad8b-a7be-451c-8050-b19f6c7a6d0a.png">

#### Menus Page
> - Photoshopped menu as HTML image elements.

<img width="1424" alt="menus-screenshot" src="https://user-images.githubusercontent.com/82375381/157676792-68bd8e1e-5ebb-42d3-812b-88a2903f600b.png">

#### Sign Up Page
> - Hero image chosen for all pages account related.
> - A section with a title, two paragraphs explaining the page, a link to take the user to the login page.
> - A sign up form using crispy forms and allauth (email, username, password1 and password2 inputs, and a submit button).

<img width="1425" alt="signup-screenshot" src="https://user-images.githubusercontent.com/82375381/157677751-f20ce567-db60-4399-adf2-3e8dec796764.png">


#### Login Page
> - Hero image chosen for all pages account related.
> - A section with a title, two paragraphs explaining the page, a link to take the user to the sign up page.
> - A login form using crispy forms and allauth (username and password inputs, and a submit button).

<img width="1424" alt="login-screenshot" src="https://user-images.githubusercontent.com/82375381/157677789-c74815fa-1525-4fae-97c0-53875f7eb6e0.png">


#### Logout Page
> - Hero image chosen for all pages account related.
> - A section with a title, text asking the user if they want to log out.
> - A logout button using allauth.

<img width="1423" alt="logout-screenshot" src="https://user-images.githubusercontent.com/82375381/157677897-783f9a10-c9db-4a16-b087-ae2fbb9ac937.png">


#### Edit Account Page
> - Hero image chosen for all pages account related.
> - A section with a title, text explaining the page, and a link to the account deletion page.
> - A form for the user to update their account details using crispy forms (pre filled: email and username, and a submit button)
> - A link to take the user to the change password page.

<img width="1427" alt="edit-profile-screenshot" src="https://user-images.githubusercontent.com/82375381/157677940-309de873-5504-4922-b41f-ba2e22842adb.png">


#### Delete Account Page
> - Hero image chosen for all pages account related.
> - A section with a title, warning text asking the user if they want to delete their account, a link to return home.
> - Delete account form using crispy forms ('Are you sure you want to delete your account?' and a submit button).

<img width="1424" alt="delete-account-screenshot" src="https://user-images.githubusercontent.com/82375381/157677959-62145788-b360-49a7-b87a-7dae380a5e6b.png">


#### Change Password Page
> - Hero image chosen for all pages account related.
> - A section with a title.
> - Change password form using crispy forms (old password, new password1, and new password2 inputs, and a submit button).

<img width="1424" alt="edit-password-screenshot" src="https://user-images.githubusercontent.com/82375381/157677971-8e430903-6123-4d94-ba85-bec313184e52.png">


#### Make a Booking Page
> - Hero image chosen for all pages booking related.
> - A section with a title.
> - A booking form using html (first name, last name, email, mobile phone, date, time, number of guests, and requirements inputs, a reset, and a submit button).

<img width="1424" alt="make-booking-screenshot" src="https://user-images.githubusercontent.com/82375381/157678002-16d0c7b1-6ffd-4c31-9172-7a0b311ae4b3.png">


#### View Bookings Page
> - Hero image chosen for all pages booking related.
> - A section with a title.
> - Cards representing bookings (title, last name, first name, date, time, edit button, cancel button).
> - If no bookings found, button leading to booking form appears.
> - If paginated, pagination appears at the bottom.
> - Confirmation appears before cancelling.

<img width="1426" alt="bookings-screenshot1" src="https://user-images.githubusercontent.com/82375381/157678036-69765a4c-803b-4a02-be4a-68e33f2b1c21.png">
<img width="1425" alt="bookings-screenshot2" src="https://user-images.githubusercontent.com/82375381/157678057-e92b5c17-1f6b-4a3c-98aa-4886607f6b97.png">


#### Edit a Booking Page
> - Hero image chosen for all pages booking related.
> - A section with a title.
> - A pre-filled booking form using crispy forms (first name, last name, email, mobile phone, date, time, number of guests, and requirements inputs, and a submit button).

### Structure Plane

I separated the structure planning into pages and used a format of prioritization as I iterated through the pages:
- Use base.html template to have the same navigation bar and footer across all pages.
- Use Scope plan from each page (above) and organize each item in the page from top to bottom according to priority and user intuitiveness.
- Iterate through this format on each page to define the structure of the web app and ensure all pages look related.

### Skeleton Plane

Decisions regarding how the information would be displayed were made by splitting the pages into 4 categories:
- Home (home page).
- Menus (menus page).
- Accounts (sign up, login, logout, edit account, edit password, and delete account pages).
- Bookings (make a booking, view bookings, and edit booking pages).

I then ensured all pages that shared the same category looked very similar to each other but slightly different to the other categories, whilst ensuring it still looked part of the same website. This process was followed to make styling easier and promote intuitiveness for the user while navigating the pages.

I then created wireframes based on this process followed.

#### Balsamiq Wireframes

All wireframes created in the planning stages of this project can be found [here](https://drive.google.com/file/d/1-mW-y9yUtgK-bjodFbpzW5RcX3XePAsj/view?usp=sharing).

### Colors

Below you can find the colors chosen for this web application.
- #0C5679 Blue Sapphire
- #FFE7BD Peach
- #E5340B Vermilion
- #F28A0F Tangerine
<img width="1150" alt="color-palette" src="https://user-images.githubusercontent.com/82375381/157326869-4be966f8-7250-4436-9a49-a7f4e35db8ba.png">

Below you can find the inspiration for the colors chosen for this web application.

<img width="338" alt="color-palette-inspiration" src="https://user-images.githubusercontent.com/82375381/157326981-784b9502-2381-435a-b9b8-2a33d2bae8dc.png">

I chose these colors and inspiration based on the decade the Diner was built, the 1970s. The inspiration was taken from a popular home wallpaper pattern and colors chosen by families in the United States at the time. These colors are nostalgic and retro, which impacts the target audience, whom would ideally be interested, or have grown up in The Golden Era of the United States.

### Typography

Much like the colors discussed above, my choice of fonts ties well to the nostalgic and retro feel I wanted to convey through the styling of the pages.
Keeping this in mind, I chose to go with the Google Font 'Monoton' for all heading elements. The font can be found [here](https://fonts.google.com/specimen/Monoton).

<img width="232" alt="Screenshot 2022-03-10 at 10 28 16" src="https://user-images.githubusercontent.com/82375381/157671846-abeb3afd-1e6b-48ef-b963-ce295c37398b.png">

<img width="453" alt="Screenshot 2022-03-10 at 10 28 23" src="https://user-images.githubusercontent.com/82375381/157671855-bf14d777-0d74-428d-b4c7-e2e713dfbf24.png">

After looking for fonts that complement 'Monoton' I decided to go with 'Poppins' with a weight of 400 for the text in the web app, purely because it is easy to read and easy on the eyes. I felt compelled to contrast the strong use of the 'Monoton' font with a simple and basic font. You can view the font [here](https://fonts.google.com/specimen/Poppins).

<img width="675" alt="font-screenshot" src="https://user-images.githubusercontent.com/82375381/157675093-c4b9fdb1-4f94-40de-8efb-abb3e1cc9610.png">

<img width="669" alt="font-screenshot2" src="https://user-images.githubusercontent.com/82375381/157675105-30fc19f7-691c-41a0-8a3b-4ebdac0cb543.png">

### Images

I used a photoshopped vintage pin-up girl image as a decorator to contribute to the website's feel. Also... it's just an awesome image.

<img width="471" alt="img-1" src="https://user-images.githubusercontent.com/82375381/157681406-edcc6fa5-c53f-42c0-b744-42535a8b1524.png">

I used a carousel of images to rotate showcasing our most popular menu items. A picture speaks a thousand words.

<img width="713" alt="img-2" src="https://user-images.githubusercontent.com/82375381/157681640-7bfc93ba-b47e-4108-9871-81929d785b15.png">

<img width="712" alt="img-3" src="https://user-images.githubusercontent.com/82375381/157681682-e02a7509-9f5a-4219-86b8-5a540e6ce4da.png">

<img width="711" alt="img-4" src="https://user-images.githubusercontent.com/82375381/157681684-bb8c6451-e958-44a1-81ca-373063106990.png">

I used images as background images according to the categories discussed above, so all pages sharing the same category had the same hero-background.

<img width="620" alt="bg-3" src="https://user-images.githubusercontent.com/82375381/157681182-0c714e66-b1cb-4855-b633-836b60f785f1.png">

<img width="756" alt="bg-2" src="https://user-images.githubusercontent.com/82375381/157681219-680a37f8-ba5c-4655-8033-3a8b44d889cd.png">

<img width="500" alt="bg-1" src="https://user-images.githubusercontent.com/82375381/157681239-3f9f051b-a881-4e92-877f-3079688c6ca7.png">

### Animations and Transitions

Hover effects were kept to a minimal due to simplicity being kept in mind.

- Hover effect on navigation bar links scales up by 1.1 times.

<img width="593" alt="hover-effect1" src="https://user-images.githubusercontent.com/82375381/157679892-3e593537-a6de-4df6-b6d1-c7643a7691db.png">

- Hover effect on all buttons across all pages. Colors reverse, 1 second transition.

<img width="171" alt="hover-effect2" src="https://user-images.githubusercontent.com/82375381/157679950-0dbda81f-f405-4122-9c7b-70a15a24dfe5.png">

### Custom Styles

Most of the web app's styles were created using the Bootstrap framework (CSS and JavaScript). However, some custom CSS stylings were necessary. All of the styling written by me can be found [here](https://github.com/gabriel-alves-p/ceru-restaurant/blob/main/static/css/style.css).

### Custom Javascript

Minimal JavaScript was used for this project. All of the JavaScript code written can be found at "static/js/script.js" and it was implemented on the template files "booking-form.html", and "edit-booking-form.html" to ensure the browser does not allow the user to select a date in the past, only from today onwards.

Below you can find a snippet of the JavaScript code used.

<img width="506" alt="javascript-used" src="https://user-images.githubusercontent.com/82375381/157510418-f6cfab6b-5956-4627-8625-719f7c3ae3f7.png">

## Agile Process

### Epics

<img width="800" alt="epic1-1" src="https://user-images.githubusercontent.com/82375381/157558739-bc676c71-cd9d-42f5-a2c2-0d940229f463.png">
<img width="800" alt="epic1-2" src="https://user-images.githubusercontent.com/82375381/157558761-a1079453-e948-4a55-855e-d9344012335e.png">
<img width="800" alt="epic1-3" src="https://user-images.githubusercontent.com/82375381/157558771-5cb0f10f-52be-4b7b-b89b-27a014e8e446.png">
<img width="800" alt="epic1-4" src="https://user-images.githubusercontent.com/82375381/157558779-3f504af1-ca26-4976-925b-41ac194f8c74.png">
<img width="800" alt="epic1-5" src="https://user-images.githubusercontent.com/82375381/157558783-8ce33d51-e417-429d-9ab0-05842b84d446.png">
<img width="800" alt="epic1-6" src="https://user-images.githubusercontent.com/82375381/157558792-8f89238a-2bac-4a3c-8b10-8b828b0a1e53.png">
<img width="800" alt="epic2-1" src="https://user-images.githubusercontent.com/82375381/157562288-11f33559-5d77-4910-93ae-8073b64f2660.png">
<img width="800" alt="epic2-2" src="https://user-images.githubusercontent.com/82375381/157562290-f98b0a3e-40d7-496c-9ad4-08a9efb3f204.png">
<img width="800" alt="epic2-3" src="https://user-images.githubusercontent.com/82375381/157562303-2eeb3921-da58-474d-8218-b6e27d5cbca7.png">
<img width="800" alt="epic3-1" src="https://user-images.githubusercontent.com/82375381/157566813-b241c306-9e4f-4594-98a1-a947638fc993.png">
<img width="800" alt="epic3-2" src="https://user-images.githubusercontent.com/82375381/157566819-bebcb30b-b2fc-4bdd-b3db-8677b9dee030.png">
<img width="800" alt="epic3-3" src="https://user-images.githubusercontent.com/82375381/157566828-d1e69bc5-3126-46d9-93d7-0c70694aceb2.png">
<img width="800" alt="epic4-1" src="https://user-images.githubusercontent.com/82375381/157570221-69f6dcb2-1015-4e8e-9b81-748e5c4f27fb.png">
<img width="800" alt="epic4-2" src="https://user-images.githubusercontent.com/82375381/157570232-c1a18ddf-0310-430b-82aa-77f597440c35.png">
<img width="800" alt="epic4-3" src="https://user-images.githubusercontent.com/82375381/157570239-749e46be-15d7-4dc4-b1ce-f36d0fe6a527.png">

### User Stories

I followed Agile process and used GitHub issues to store my User Stories. They were created from the Epics above and were prioritized and ordered from "Must have", and "Should have", to "Could have", according to the Agile Process taught in one of the Code Institute lessons.

You can view my User Stories [here](https://github.com/gabriel-alves-p/ceru-restaurant/projects/1) or by clicking on 'Projects' and then 'User Stories' on this repository on GitHub.

All of my templates (User Stories and Bug Report) can be viewed [here](https://github.com/gabriel-alves-p/ceru-restaurant/issues/new/choose) or by clicking on 'Issues' and then 'New Issue' on this repository on GitHub.

### Development

#### Week 1 - Project inception & planning.
- Decide to follow Code Institute's project idea 1 to create a restaurant's booking system.

<img width="576" alt="code-institute-idea" src="https://user-images.githubusercontent.com/82375381/157700816-b26f06c2-c67d-4bd2-ae91-a6adb6f8660a.png">

- Meet with mentor Malia Havlicek.

- Begin planning project (notes).
<img width="524" alt="notes1" src="https://user-images.githubusercontent.com/82375381/157701219-4d812bfa-52c0-48a6-b6dd-da6b977467d0.png">

<img width="512" alt="notes2" src="https://user-images.githubusercontent.com/82375381/157701238-01d25b1d-9516-47ac-ba6c-d103dc99d4e2.png">

- Planning of models for the app.

<img width="523" alt="data-models" src="https://user-images.githubusercontent.com/82375381/157699276-dff9db71-2040-4965-9bbd-73a64430bc38.png">

<img width="525" alt="data-models2" src="https://user-images.githubusercontent.com/82375381/157699285-b38adae4-cade-4edf-ae0b-0570c5bb9fee.png">

- Loosely plan workflow chart.

<img width="1073" alt="workflow" src="https://user-images.githubusercontent.com/82375381/157702146-9711110f-3221-4303-adb4-075d7a19fe6a.png">


#### Week 2

#### Week 3

#### Week 4

#### Week 5

#### Week 6

#### Week 7



## Information Architecture
As part of the requirements for this project you need to have at least 1 original data model.  It's this section that discusses your data and how each piece relates to another and draws out the CRUD functionality you built.

## Entity Relationship Diagram
Wade Williams wrote a great blog about how to add a django extension to auto create an ERD. https://wadewilliams.com/technology-software/generating-erd-for-django-applications/ You can always draw one out by hand or google sheets. You can also draw this up by hand if you want or use a spreadsheet to show your data model. 

## Database Choice

PostgreSQL was my database of choice for the deployed application, for the data is relational and Heroku (used for deployment) serves this up realitvely easily, and with no cost.

## Data Models
Show the accessors you know your data. If you end up using some data models from an example project, call that out and don't be as detailed about writing those up unless you added to them.  

Each data model that you created yourself should have its Fields, Field Type and any validation documented.  You should also cross-reference any code in your repository that relate to CREATE, READ, UPDATE, DELETE operations for these models. 

Below is an example of a write up for an Activies Data Model
### Activities Model
Activities is a table to hold a unique icon image and name values that users have associated with events and places. It helps with sorting events and prevents the need from carrying around two data objects in the larger Events and Places data structures. The purpose of an Activities object is to provide an imagery association to a category.

| DB Key 	| Data Type 	|          Purpose          	| Form Validation                        	| DB processing    	|
|--------	|:---------:	|:-------------------------:	|----------------------------------------	|------------------	|
| _id    	| ObjectId  	| unique identifier         	| None                                   	| n/a              	|
| name   	| String    	| Name of Activity          	| Required<br>Min 1 char<br>Max 50 chars 	| trim<br>to lower 	|
| icon   	| String    	| system path to image file 	| Required                               	|                  	|

Activity entries are used by events, places and filtering.

- [x] Create - An activity is potentially created when a user successfully creates a place, creates an event, updates an event, or updates a place. 
- [x] Read - The Activities table is read when a user is adding an event, updating an event, adding a place or updating a place, to determine if a new value should be created or not. The activities table is queried for using the name and icon pair, if it is found, the ObjectId is passed to the event and places. If no match is found, a new Activity is created and that ObjectID is passed to the the place or event.
- [ ] Update
- [ ] Delete
 
 This table has no deletion or updates associated with it. It's strictly create and read. Eventually, maintenance scripts should be written to delete unused/deprecated entries.

The reading/writing of the activities table is housed in the [what2do2day/activities/views.py](what2do2day/activities/views.py) file.

### CRUD Diagrams
This is if you want to go for distinction.  You can also have CRUD diagrams to show them visually how the model is used in your site. 

I used [draw.io](https://app.diagrams.net/) and hooked it up to my google drive to create the screenshot below

![image](https://user-images.githubusercontent.com/23039742/154406188-c9beb57a-2fd1-4f26-a8ed-bee320e46e3d.png)


# Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so and how they tie into  your user stories.

## Implemented Features

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

It's easiest to break this section down into the header, footer, and each page/layer of your website. Call out any differences for mobile vs desktop presentations, **include a screenshot of the implemented feature** and **at least 2 bullet points of their importance**.

Don't forget your 404 error page.

## Future Features

Use this section to discuss plans for additional features to be implemented in the future:

If you end up not developing some features you hoped to implement, you can include those in this section.

# Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Validation Testing
You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

- [CSS Validator](https://jigsaw.w3.org/css-validator/) Note, any error associated with root: color variables were ignored.
- [HTML Validator](https://validator.w3.org/) NOTE: You may need to view the source of each page and paste that into the validator
- [JS validation](https://jshint.com) for each .js file/ , if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `
- [JSON validation](https://jsonlint.com/) for each .json file 
- [PEP8 Validator](http://pep8online.com/) include a screenshot of results. (you should do this for all .py files in your repo, or note that there are no red errors in gitpod after the file is saved)

## Cross Browser and Cross Device Testing
Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: motog6            | chrome      | android    | XS 360 x 640  |
| browser stack: iPhone5s       | safari      | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | firefox     | android    | SM 411 x 731  |
| browserstack: iPhone 10x      | Chrome      | iOs        | SM 375 x 812  |
| browserstack: nexus 7 - vert  | Chrome      | android    | M 600 x 960   |
| real tablet: ipad mini - vert | safari      | iOs        | M 768 x 1024  |
| browserstack: nexus 7 - horiz | firefox     | android    | LG 960 x 600  |
| chrome emulator: ipad - horiz | safari      | iOs        | LG 1024 x 768 |
| browserstack                  | Chrome      | windows    | XL 1920 x 946 |
| real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
| browserstack                  | IE Edge 88  | windows 10 | XL 1920 x 964 |

## Manual Testing

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 

At this point you really should be using GITHUB's Issues to track these as it helps you with the AGILE process requirement.

Create Custom Issue Template and a milestone in git hub.[Here's a brief overview](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing) I put together on how to do this.

## Automated Testing
If you managed to write jasmine tests or some django tests, note those files out here and how to run them.  I only did this in my last project as I didn't have the time or energy to learn how to write tests. https://github.com/maliahavlicek/ms4_challenger/blob/master/documentation/TESTING.md is my write up about those and how I ran them, but a simple test I'd recommend is authentication and any views you limit to superusers or logged in users

https://github.com/maliahavlicek/ms4_challenger/blob/master/challenges/tests/test_views.py 

## Defects of Note

I kept track of my bugs in real time. You can view them and their details [here](https://github.com/gabriel-alves-p/ceru-restaurant/projects/2) or by clicking on the 'Projects' and then 'Bug Report' on this repository on GitHub.

## Lighthouse Audits

<img width="564" alt="lighthouse-audits" src="https://user-images.githubusercontent.com/82375381/157577857-8ca96d40-33ea-4b1c-8051-22d6bcdbfd48.png">

## Deployment

### Requirements

- [A GitHub account](https://github.com/join).
- [A Heroku account](https://signup.heroku.com/).
- [A Cloudinary account](https://cloudinary.com/users/register/free).

### GitHub

- If you wish to contribute to this project, please **fork it** in your own GitHub account by clicking on the "Fork" button on the top right corner of this repository.
<img width="111" alt="fork" src="https://user-images.githubusercontent.com/82375381/157577894-82529101-1cde-4d0a-acda-d61b0eb76fb3.png">

### In your IDE

- After forking the repository, open it on your IDE of choice, and install all the dependencies necessary by running the following command in your command line interface.
```
pip3 install -r requirements.txt
```

- Create a file in the top directory called 'env.py', and if it isn't in your '.gitignore' file, make sure to include its name there.
<img width="136" alt="Screenshot 2022-03-10 at 00 28 27" src="https://user-images.githubusercontent.com/82375381/157582817-f5f6963c-37dd-47be-bfbc-898b8363c666.png">

### Heroku

- Log into Heroku account, click on 'Create new app'. 
<img width="249" alt="step10 png" src="https://user-images.githubusercontent.com/82375381/157579540-98888c1a-0dd9-45ec-b97a-9caa5c90d95a.png">

- Choose an available name, select your region, and click on 'Create app'.
<img width="695" alt="step11 png" src="https://user-images.githubusercontent.com/82375381/157579987-fdaffe3f-5a69-4176-9241-497a7a6ee659.png">

- Click on 'Resources'.
<img width="584" alt="step" src="https://user-images.githubusercontent.com/82375381/157580367-5073c040-1707-4e23-9991-e7b204d950ee.png">

- Search for 'Heroku Postgres' and select it.
<img width="681" alt="Screenshot 2022-03-10 at 00 03 57" src="https://user-images.githubusercontent.com/82375381/157580448-900dad15-5957-4f6d-9250-1c0bdfcad2df.png">

- Select the free 'Hobby Dev' postgres option and click on 'Submit Order Form'.
<img width="528" alt="step13 png" src="https://user-images.githubusercontent.com/82375381/157580581-3abd0fc4-991c-4bfc-9587-5da399905f6f.png">

- Click on 'Settings'.
<img width="598" alt="step14 png" src="https://user-images.githubusercontent.com/82375381/157580749-5094839e-17df-4866-943c-d700d6c70999.png">

- Click on 'Add buildpack' and choose 'heroku/python'.
<img width="845" alt="Screenshot 2022-03-10 at 00 39 09" src="https://user-images.githubusercontent.com/82375381/157583904-cbdd0892-d8de-4bdf-8564-34675d46c522.png">


- Click on 'Reveal Config Vars' and you should see this.
<img width="799" alt="step15 png" src="https://user-images.githubusercontent.com/82375381/157581018-ad3ab525-0089-43eb-ab30-71d63836e1de.png">

- Below that, add the KEY 'SECRET_KEY' and choose whatever VALUE you wish to be your secret key (I've covered mine, keep yours secret).
<img width="804" alt="step17 png" src="https://user-images.githubusercontent.com/82375381/157581364-771cefa1-6418-4daa-bd0a-9b298e24dbcd.png">

- Log into your Cloudinary account and click on 'Dashboard' on the top left corner.
<img width="337" alt="Screenshot 2022-03-10 at 00 15 09" src="https://user-images.githubusercontent.com/82375381/157581548-e579d72f-d8d6-406b-bfc9-9f1ab1a7aa20.png">

- Copy your 'API Environment variable'.
<img width="562" alt="Screenshot 2022-03-10 at 00 15 42" src="https://user-images.githubusercontent.com/82375381/157581735-b59ef865-946f-48ca-a32d-3e7edeabf68f.png">

- Back on Heroku, add a KEY 'CLOUDINARY_URL' and paste in your Cloudinary 'API Environment variable' as the VALUE (it must begin with 'cloudinary://' you can delete anything before that).
<img width="797" alt="step24 png" src="https://user-images.githubusercontent.com/82375381/157582095-59891b58-3c5e-4d2a-847d-026556bb1098.png">

- Create one last KEY 'DEBUG' and set its VALUE to 'False'.
<img width="717" alt="Screenshot 2022-03-10 at 00 21 53" src="https://user-images.githubusercontent.com/82375381/157582190-0c573f33-a476-43ea-a003-4f9e4254b55d.png">

- Back in your 'env.py' file, write the following code, matching your values here with your Heroku VALUES but in quotes on here! (important to be in quotes)
<img width="810" alt="step16 png" src="https://user-images.githubusercontent.com/82375381/157583277-b24ad188-f7eb-4bf4-a201-4080784ee649.png">

- Back to Heroku, click on 'Deploy'.
<img width="592" alt="step34 png" src="https://user-images.githubusercontent.com/82375381/157583398-436efec5-ac81-4d25-8ce0-0d784c95ab46.png">

- Click on GitHub and connect with your GitHub account details 
<img width="537" alt="step35 png" src="https://user-images.githubusercontent.com/82375381/157583534-81c6ea13-65ee-4939-be30-fffbad772500.png">

- Search for this **forked** repository 'ceru-restaurant' and select it.
<img width="1229" alt="Screenshot 2022-03-10 at 00 37 22" src="https://user-images.githubusercontent.com/82375381/157583648-a33289ba-b202-46b0-8665-7878e42bcb01.png">

- Once it shows as connected, scroll down to 'Manual Deploy', select 'main' and click on Deploy Branch.
<img width="600" alt="step36 png" src="https://user-images.githubusercontent.com/82375381/157583740-7233de24-e76a-4090-b5d1-1fbcec2248c6.png">

- You can optionally Enable Automatic Deploys, which means your app will be deployed automatically every time you push your changes to GitHub through your command line interface (recommended).
<img width="1246" alt="Screenshot 2022-03-10 at 00 42 06" src="https://user-images.githubusercontent.com/82375381/157584128-3061ba4b-a797-4472-9b3e-972a97428f39.png">

## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

## Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

## Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.

