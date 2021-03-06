# CERU - AUTHENTIC AMERICAN DINER

<img width="977" alt="responsive-app" src="https://user-images.githubusercontent.com/82375381/157510961-1f9b70d1-6980-4699-9196-c7417c2ca87a.png">

## Author

Gabriel Alves

You can visit my GitHub page [here](https://github.com/gabriel-alves-p).

# Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
  * [Languages](#languages)
  * [Libraries & Frameworks](#libraries---frameworks)
  * [Django Extensions](#django-extensions)
  * [Database](#database)
  * [Deployment, Repository & Media](#deployment--repository---media)
- [UX](#ux)
  * [Project Goals / Strategy Plane](#project-goals---strategy-plane)
  * [Scope Plane](#scope-plane)
    + [Home Page](#home-page)
    + [Menus Page](#menus-page)
    + [Sign Up Page](#sign-up-page)
    + [Login Page](#login-page)
    + [Logout Page](#logout-page)
    + [Edit Account Page](#edit-account-page)
    + [Delete Account Page](#delete-account-page)
    + [Change Password Page](#change-password-page)
    + [Make a Booking Page](#make-a-booking-page)
    + [View Bookings Page](#view-bookings-page)
    + [Edit a Booking Page](#edit-a-booking-page)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
    + [Balsamiq Wireframes](#balsamiq-wireframes)
  * [Colors](#colors)
  * [Typography](#typography)
  * [Images](#images)
  * [Animations and Transitions](#animations-and-transitions)
  * [Custom Styles](#custom-styles)
  * [Custom Javascript](#custom-javascript)
- [Agile Process](#agile-process)
  * [User Stories](#user-stories)
  * [Epics](#epics)
  * [Development / Iterations](#development---iterations)
    + [Week 1 Milestone - Project inception & planning.](#week-1-milestone---project-inception---planning)
    + [Week 2 Milestone - Create repository & deploy.](#week-2-milestone---create-repository---deploy)
    + [Week 3 Milestone - Set up basics & find images online for content](#week-3-milestone---set-up-basics---find-images-online-for-content)
    + [Week 4 Milestone - Write basic templates, views and urls](#week-4-milestone---write-basic-templates--views-and-urls)
    + [Week 5 Milestone - Write functionality & style](#week-5-milestone---write-functionality---style)
    + [Week 6 Milestone - Polish off and README.md](#week-6-milestone---polish-off-and-readmemd)
- [Information Architecture](#information-architecture)
  * [Database Choice](#database-choice)
  * [Data Models](#data-models)
  * [CRUD Diagrams](#crud-diagrams)
- [Features](#features)
  * [Implemented Features](#implemented-features)
  * [Future Features](#future-features)
- [Testing](#testing)
  * [Validation Testing](#validation-testing)
  * [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  * [Manual Testing](#manual-testing)
- [Defects](#defects)
- [Lighthouse Audits](#lighthouse-audits)
- [Deployment](#deployment)
  * [Requirements](#requirements)
  * [GitHub](#github)
  * [In your IDE](#in-your-ide)
  * [Heroku](#heroku)
- [Credits](#credits)
- [Media / Content](#media---content)
- [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Project Overview

This project was incepted with the goal of creating a 'hassle-free' booking system for a Diner to increase their revenue. It achieves this goal by means of two models; a "user", and a "booking" system.
The user can very easily sign-up for an account, which only then grants them access to the booking form. Users are also allowed the freedom to view, edit, and cancel their bookings as well as their own personal accounts with the Diner if they wish to do so, following the C.R.U.D. Operations (Create, Read, Update, Delete).

The app also aims to reflect the diner itself in its color pallette and vintage feel, friendly and straight out of the 70s.

You can view this web application [here](https://ceru-restaurant.herokuapp.com/).

This is my fourth Portfolio project for my Software Development course with Code Institute.

Inception: 29/01/2022

Submission date: 13/03/2022

Deadline: 13/03/2022

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

### User Stories

I followed Agile process and used GitHub issues to store my User Stories. They were created from the Epics above and were prioritized and ordered from "Must have", and "Should have", to "Could have", according to the Agile Process taught in one of the Code Institute lessons.

You can view my User Stories [here](https://github.com/gabriel-alves-p/ceru-restaurant/projects/1) or by clicking on 'Projects' and then 'User Stories' on this repository on GitHub.

All of my templates (User Stories and Bug Report) can be viewed [here](https://github.com/gabriel-alves-p/ceru-restaurant/issues/new/choose) or by clicking on 'Issues' and then 'New Issue' on this repository on GitHub.

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

### Development / Iterations

#### Week 1 Milestone - Project inception & planning.
- Decide to follow Code Institute's project idea 1 to create a restaurant's booking system.

<img width="576" alt="code-institute-idea" src="https://user-images.githubusercontent.com/82375381/157700816-b26f06c2-c67d-4bd2-ae91-a6adb6f8660a.png">

- Meet with mentor Malia Havlicek to speak about my ideas and hear her suggestions.

- Begin planning project (notes).
<img width="524" alt="notes1" src="https://user-images.githubusercontent.com/82375381/157701219-4d812bfa-52c0-48a6-b6dd-da6b977467d0.png">

<img width="512" alt="notes2" src="https://user-images.githubusercontent.com/82375381/157701238-01d25b1d-9516-47ac-ba6c-d103dc99d4e2.png">

- Planning of models for the app.

<img width="523" alt="data-models" src="https://user-images.githubusercontent.com/82375381/157699276-dff9db71-2040-4965-9bbd-73a64430bc38.png">

<img width="525" alt="data-models2" src="https://user-images.githubusercontent.com/82375381/157699285-b38adae4-cade-4edf-ae0b-0570c5bb9fee.png">

- Loosely plan workflow chart.

<img width="1073" alt="workflow" src="https://user-images.githubusercontent.com/82375381/157702146-9711110f-3221-4303-adb4-075d7a19fe6a.png">

- Create Epics.
- Create User Stories that inherit from Epics.
- Plan milestones from now until submission.

#### Week 2 Milestone - Create repository & deploy.
- Create GitHub repository using Code Institute's gitpod template.

<img width="395" alt="Screenshot 2022-03-10 at 16 07 43" src="https://user-images.githubusercontent.com/82375381/157736752-488b3b7e-0f08-466e-a228-4a25f5e6efeb.png">

- Install frameworks & libraries.
- Freeze dependencies.

<img width="543" alt="step1 png" src="https://user-images.githubusercontent.com/82375381/157737821-293c37d3-ea55-479a-b7bd-b778b623bee7.png">

<img width="574" alt="step2 png" src="https://user-images.githubusercontent.com/82375381/157737830-67d97844-90b7-44a5-bfb1-eddf3b2b5ebe.png">

<img width="560" alt="step3 png" src="https://user-images.githubusercontent.com/82375381/157737902-bc253d2a-6f64-48d1-8f96-d170ba3879ab.png">

<img width="582" alt="step4 png" src="https://user-images.githubusercontent.com/82375381/157737942-d0f276fb-7a09-443c-8a3e-db19493a3008.png">

- Start Django app.

<img width="613" alt="step5 png" src="https://user-images.githubusercontent.com/82375381/157738013-f48f3b61-1747-47f8-bf03-722e2151b486.png">

<img width="529" alt="step6 png" src="https://user-images.githubusercontent.com/82375381/157738042-4018c1c4-58a8-4cf9-bd43-73307def0514.png">

<img width="490" alt="step7 png" src="https://user-images.githubusercontent.com/82375381/157738080-8ffe84d7-bc45-47f3-bdf9-16b80995b792.png">

- Configure settings.py

- Import env.py if the file exists in the current directory.

<img width="274" alt="step18 png" src="https://user-images.githubusercontent.com/82375381/157738713-afd8bec6-d5fc-4dd8-a9fe-2cbd6d301385.png">

- Add intalled apps to the same section on settings.py

<img width="302" alt="step26 png" src="https://user-images.githubusercontent.com/82375381/157738701-ebea6db4-caf1-4a3b-bc6e-32caca8286ec.png">

- Set security key to get from env.py

<img width="536" alt="step19 png" src="https://user-images.githubusercontent.com/82375381/157739387-8b555ecc-9881-4c6e-98fa-862704108102.png">

- Set database to collect from env.py

<img width="562" alt="step20 png" src="https://user-images.githubusercontent.com/82375381/157739738-55095aa6-c4cb-4d94-af9f-65265373ef7c.png">

- Direct Django where to find template files.

<img width="517" alt="step29 png" src="https://user-images.githubusercontent.com/82375381/157739973-22be773d-8c5c-427f-986a-62c256f67a38.png">

- Set allowed hosts.

<img width="509" alt="step30 png" src="https://user-images.githubusercontent.com/82375381/157740036-d4f61ec1-b5cf-4810-be20-11e3bfc110f5.png">

- Configure env.py file.

<img width="810" alt="step16 png" src="https://user-images.githubusercontent.com/82375381/157740100-a4950cbf-3a65-443e-8b5a-1f05bd7a7322.png">

- Create and configure Procfile for heroku.

<img width="332" alt="step31 png" src="https://user-images.githubusercontent.com/82375381/157740193-bfbd31fa-b1ec-4d61-9107-bc2be20b1061.png">

FURTHER STEPS OF DEPLOYMENT FOLLOWED BEYOND THIS STAGE CAN BE FOUND BELOW IN THE **DEPLOYMENT** SECTION.

- Save, commit & push changes to GitHub.

<img width="527" alt="step32 png" src="https://user-images.githubusercontent.com/82375381/157740427-a232677c-a596-45ce-9c07-ef130bac6123.png">

<img width="369" alt="step33 png" src="https://user-images.githubusercontent.com/82375381/157740431-6d23979a-008a-4b37-8a4a-032eba15a1fb.png">

#### Week 3 Milestone - Set up basics & find images online for content
- Turn Data models above into code in models.py

<img width="1200" alt="Screenshot 2022-03-10 at 17 18 20" src="https://user-images.githubusercontent.com/82375381/157747610-523df3be-2e5e-4cee-9eb6-0fe475a134d8.png">

- Migrate changes.
<img width="490" alt="step7 png" src="https://user-images.githubusercontent.com/82375381/157749463-62c0ec71-970a-41ae-b7fa-0899fd566e98.png">

- Search online and come up with content to begin writing templates.

#### Week 4 Milestone - Write basic templates, views and urls
- Create templates directory.

- Install Django Allauth for authentication.

<img width="305" alt="Screenshot 2022-03-10 at 18 09 26" src="https://user-images.githubusercontent.com/82375381/157755080-30c1357f-0a03-4a2c-8aab-72a67ada338a.png">

- Add allauth urls to urls.py in ceru_restaurant directory.

<img width="488" alt="Screenshot 2022-03-10 at 18 08 44" src="https://user-images.githubusercontent.com/82375381/157754989-1d2f9d82-fe20-4953-902c-03a1a2291b4c.png">

- Create template files for all pages (base.html, index.html, booking_form.html, dashboard.html, edit_booking.html, edit_password.html, edit_profile.html, delete_account.html, menus.html)

<img width="383" alt="Screenshot 2022-03-10 at 18 05 44" src="https://user-images.githubusercontent.com/82375381/157754586-9a2eab24-521f-4b6f-84bd-8ec71302464e.png">

- Create basic views (one for each page) in views.py.

<img width="573" alt="Screenshot 2022-03-10 at 18 14 55" src="https://user-images.githubusercontent.com/82375381/157755989-bf37e7d6-e12f-4bc5-83f6-92a59d62313d.png">

- Create urls (one for each page) in urls.py in ceru directory.

<img width="912" alt="Screenshot 2022-03-10 at 18 14 06" src="https://user-images.githubusercontent.com/82375381/157755888-045c99db-d5dd-4d4c-86f6-c339a8b146cf.png">

#### Week 5 Milestone - Write functionality & style
- Write HTML, CSS, JavaScript and use Bootstrap for responsiveness on all templates.
- Once styles and responsiveness are in place, begin writing functionality in forms.py and views.py.
- Follow same iteration format from Structure plane to work on each page: write template, style it, write functionality, implement functionality.

#### Week 6 Milestone - Polish off and README.md
- Set up Django mail to work in settings.py

<img width="521" alt="Screenshot 2022-03-11 at 00 32 10" src="https://user-images.githubusercontent.com/82375381/157797156-dad4ae91-6997-4eb1-a9e5-14c99508853d.png">

- Set up environmental variables for mail settings in env.py

<img width="448" alt="Screenshot 2022-03-11 at 00 32 35" src="https://user-images.githubusercontent.com/82375381/157797184-a71edeaa-a936-4e97-ae9f-f11731b285a3.png">

- Work on README.md file (this documentation).

- Review all code written.

- Ensure all class and function docstrings are well written, clear and concise.

## Information Architecture 

### Database Choice

PostgreSQL was my database of choice for the deployed application, for the data is relational and Heroku (used for deployment) serves this up realitvely easily, and with no cost.

### Data Models
Profile model created from Django User model.
<img width="523" alt="data-models" src="https://user-images.githubusercontent.com/82375381/157699276-dff9db71-2040-4965-9bbd-73a64430bc38.png">

Booking model created from Django User model.
<img width="525" alt="data-models2" src="https://user-images.githubusercontent.com/82375381/157699285-b38adae4-cade-4edf-ae0b-0570c5bb9fee.png">

### CRUD Diagrams

- CRUD diagram for User model below.

<img width="828" alt="crud-diagram-user-model" src="https://user-images.githubusercontent.com/82375381/157767090-311bd67f-21db-48c4-a2ec-9c94e4b1227c.png">

- CRUD diagram for Booking model below.

<img width="825" alt="Screenshot 2022-03-10 at 19 49 43" src="https://user-images.githubusercontent.com/82375381/157768100-3dc24a52-cdf7-4c31-aa25-2e30368302a3.png">


## Features

### Implemented Features

- Navigation bar shows different links depending on whether the user is logged in or not.
- EPIC: Home

<img width="866" alt="Screenshot 2022-03-12 at 17 31 10" src="https://user-images.githubusercontent.com/82375381/158034014-2eb0cdf7-0304-458a-a7bf-1e87f3cf0bfb.png">
<img width="976" alt="Screenshot 2022-03-12 at 17 30 58" src="https://user-images.githubusercontent.com/82375381/158034017-f9d14e39-dc25-4ee9-90cc-50fc55d3b1ff.png">

- Booking button leads to booking form if user is logged in, or to signup form if user is not logged in.
- EPIC: Home

<img width="665" alt="Screenshot 2022-03-12 at 17 32 29" src="https://user-images.githubusercontent.com/82375381/158034046-10057e72-a9d3-47f5-85a9-1607595de90b.png">

- About us section informs user of restaurants history.
- EPIC: Home

<img width="1440" alt="Screenshot 2022-03-12 at 17 33 34" src="https://user-images.githubusercontent.com/82375381/158034054-a5080f98-1326-4ab8-9d4a-8118bada429d.png">

- Menus section provides user with menus. 
- EPIC: Home

<img width="1440" alt="Screenshot 2022-03-12 at 17 37 02" src="https://user-images.githubusercontent.com/82375381/158034160-13b3d739-a38d-4c6d-bd62-9924d5134792.png">

- Find us section and contact us sections provide user with easy access to our location and any queries they might have. Admin set up in env.py receives email.
- EPIC: Home

<img width="1440" alt="Screenshot 2022-03-12 at 17 38 35" src="https://user-images.githubusercontent.com/82375381/158034259-81d21b02-8b5d-4072-882d-cae9a1c1ab1e.png">
<img width="498" alt="Screenshot 2022-03-12 at 18 13 12" src="https://user-images.githubusercontent.com/82375381/158035191-6670c157-b340-4901-9f9d-e5551469a4c7.png">

- Footer provides general information about the diner, and is intuitive for the user.
- EPIC: Home

<img width="784" alt="Screenshot 2022-03-12 at 17 39 56" src="https://user-images.githubusercontent.com/82375381/158034255-8f2c5741-6d85-4c58-99ed-deb3d7ea8e75.png">

- Menus are available to all users, whether logged in or not, so they can decide whether they want to book or not.
- EPIC: Menus

<img width="1440" alt="Screenshot 2022-03-12 at 17 54 35" src="https://user-images.githubusercontent.com/82375381/158034661-2cf8cde2-edc9-4e0c-bf58-97199d74015e.png">

- Sign up form, easy and intuitive.
- EPIC: Accounts
<img width="597" alt="Screenshot 2022-03-12 at 17 56 00" src="https://user-images.githubusercontent.com/82375381/158034694-bf3c79c6-eac2-42fa-98d4-0d32b9892847.png">

- Log in form, easy and intuitive.
- EPIC: Accounts

<img width="626" alt="Screenshot 2022-03-12 at 17 56 45" src="https://user-images.githubusercontent.com/82375381/158034723-5b699c5c-b586-4ff0-ae8b-288263cc929a.png">

- Booking form, logging in redirects here straight away to maximize revenue.
- EPIC: Booking

<img width="954" alt="Screenshot 2022-03-12 at 17 59 17" src="https://user-images.githubusercontent.com/82375381/158034778-111ab2a4-4098-4af2-a9bd-ea216fa4f9b4.png">

- Dashboard so user sees their bookings. Admin sees and can manage all bookings. Users can only see and manage their own bookings.
- Pop up message pops up confirming deletion.
- EPIC: Booking

<img width="985" alt="Screenshot 2022-03-12 at 18 00 20" src="https://user-images.githubusercontent.com/82375381/158034804-06e76321-ba6c-4727-9304-8640cb3134fc.png">
<img width="446" alt="Screenshot 2022-03-12 at 18 01 25" src="https://user-images.githubusercontent.com/82375381/158034839-d63bf7fe-4244-4093-afa6-4020712b49a6.png">
<img width="273" alt="Screenshot 2022-03-12 at 18 01 56" src="https://user-images.githubusercontent.com/82375381/158034853-6263ba49-51d5-4af0-984a-c43e8a15e288.png">

- User can edit their own bookings. Form is pre-populated with their booking details. I purposely left the 'date' field out, fearing it might be giving the user too much freedom. User can cancel their current booking and book a new table if they wish to change the date.
- EPIC: Booking

<img width="959" alt="Screenshot 2022-03-12 at 18 02 14" src="https://user-images.githubusercontent.com/82375381/158034868-8d25db28-6ccd-4b54-a708-f6ff53c9da8b.png">

- User is able to edit their account details or delete their accounts if they wish to do so. Form is pre-populated with their account details.
- EPIC: Accounts

<img width="967" alt="Screenshot 2022-03-12 at 18 03 57" src="https://user-images.githubusercontent.com/82375381/158034917-07a37bc4-3d80-4267-b66a-73fc7e4ef8b7.png">
<img width="913" alt="Screenshot 2022-03-12 at 18 05 19" src="https://user-images.githubusercontent.com/82375381/158034956-9269fbaa-42f9-4f94-ae6f-ba68ec06d78b.png">
<img width="774" alt="Screenshot 2022-03-12 at 18 06 57" src="https://user-images.githubusercontent.com/82375381/158035033-ed5643c5-d92b-4d0e-863e-92dd428257e0.png">

### Future Features

In the future, I would like to implement the following features onto this web application:
- Table capping for Admin at 40 guests for any given time.
- Table plan for the User to choose their table, and see what tables are taken.
- Reward accumulation for every table booked.
- Booking automatically disappears once date and time are past.
- Forgot my password and forgot my username emails sent to user.

## Testing

### Validation Testing

Python validation was done using [PEP8 Validator](http://pep8online.com/) on all python files in the app.

- settings.py

<img width="987" alt="settings" src="https://user-images.githubusercontent.com/82375381/157996389-431c6fab-a804-4034-8c51-7825e70c1700.png">

- urls.py (ceru_restaurant directory)

<img width="980" alt="urls1" src="https://user-images.githubusercontent.com/82375381/157996404-9deee6d4-883c-442d-8080-92dfe9e3ec1d.png">

- wsgi.py

<img width="999" alt="wsgi" src="https://user-images.githubusercontent.com/82375381/157996410-a22f2841-5434-43e8-a8d2-6a25f65c659a.png">

- admin.py

<img width="945" alt="admin" src="https://user-images.githubusercontent.com/82375381/157996423-251a2f80-0d0f-46a6-9290-29708831b419.png">

- apps.py

<img width="958" alt="apps" src="https://user-images.githubusercontent.com/82375381/157996435-4bd024a2-a3f9-4a78-83eb-cd463fc7d17a.png">

- forms.py

<img width="967" alt="forms" src="https://user-images.githubusercontent.com/82375381/157996451-54ddbd0e-f011-4d1c-821a-15012cda9024.png">

- models.py

<img width="983" alt="models" src="https://user-images.githubusercontent.com/82375381/157996460-a7ada14a-b86a-466f-bc61-8b0b5092feb1.png">

- signals.py

<img width="969" alt="signals" src="https://user-images.githubusercontent.com/82375381/157996470-4300c31f-cc45-46aa-9ad0-b2ec1ae429b4.png">

- urls.py (ceru directory)

<img width="964" alt="urls2" src="https://user-images.githubusercontent.com/82375381/157996487-0977a282-5ca8-4814-8534-fa8dec3ab9cc.png">

- views.py

<img width="964" alt="views" src="https://user-images.githubusercontent.com/82375381/157996497-8bf71472-1807-4a3e-8742-159a09c26c8e.png">

- env.py

<img width="989" alt="env" src="https://user-images.githubusercontent.com/82375381/157996504-fd0957f2-d7b8-49b3-ad83-11e84b2a7081.png">

- manage.py

<img width="987" alt="manage" src="https://user-images.githubusercontent.com/82375381/157996512-555ee4c1-7b9d-4d69-bcde-484e02263812.png">

CSS validation was done using [CSS Validator](https://jigsaw.w3.org/css-validator/) on all css files in the app.

- style.css

<img width="656" alt="style" src="https://user-images.githubusercontent.com/82375381/157996522-d045e94c-bac1-40ea-819a-1d5506589ebc.png">

- media-queries.css

<img width="651" alt="media-queries" src="https://user-images.githubusercontent.com/82375381/157996536-fb359111-f686-4d89-a579-180f1b1e3724.png">

- edit_profile.css

<img width="654" alt="edit-profile" src="https://user-images.githubusercontent.com/82375381/157996551-a3ad39b2-3be6-4e21-a3ef-898e110cc935.png">


JavaScript validation was done using [JavaScript Validation](https://jshint.com) on all js files in the app.

- script.js

<img width="1060" alt="js" src="https://user-images.githubusercontent.com/82375381/157996558-7e2b87a6-ace8-454b-b7a9-96feaaf138ac.png">

HTML validation was done using [HTML Validator](https://validator.w3.org/) on all html files in the app.

- index.html

<img width="469" alt="index" src="https://user-images.githubusercontent.com/82375381/158030224-7a0cb53b-2fdf-4a4c-be86-30d865e1dafa.png">

- menus.html

<img width="485" alt="menus" src="https://user-images.githubusercontent.com/82375381/158030229-bf0c2a4b-cfb5-4236-bf7c-b05850b096e2.png">

- signup.html

<img width="477" alt="signup" src="https://user-images.githubusercontent.com/82375381/158030232-16609b77-e2ab-44a8-855f-a69de398cffa.png">

- login.html

<img width="480" alt="login" src="https://user-images.githubusercontent.com/82375381/158030237-c0b7597c-7674-4a6b-9ec5-2a5588526ea3.png">

- booking_form.html

<img width="476" alt="bookingform" src="https://user-images.githubusercontent.com/82375381/158030241-933a97eb-e167-463d-9171-54ec9b371143.png">

- dashboard.html

<img width="479" alt="dashboard" src="https://user-images.githubusercontent.com/82375381/158030245-6358d141-4628-481c-97e8-a8f0c8fa9f04.png">

- edit-booking.html

<img width="474" alt="edit-booking" src="https://user-images.githubusercontent.com/82375381/158030251-a29cc8bf-c39a-4731-936b-93241a51de81.png">

- delete-account.html

<img width="500" alt="account-deletion" src="https://user-images.githubusercontent.com/82375381/158030256-b8ee8cef-d7e2-4963-876c-f59a84da0992.png">

- edit-password.html
- Errors found within Django's own HTML form, I rendered the form with {% form | crispy %}, but this extension seems to have the HTML error below.

<img width="1080" alt="edit-password" src="https://user-images.githubusercontent.com/82375381/158030259-7f43a15b-9e73-4fae-a2ca-43b24f850976.png">

- Here is the documentation snippet for this Django class.
<img width="694" alt="Screenshot 2022-03-12 at 15 52 38" src="https://user-images.githubusercontent.com/82375381/158031041-274c5afe-b7fb-43ac-bb51-6bab6fb9acc5.png">

- edit-profile.html

<img width="469" alt="edit-profile" src="https://user-images.githubusercontent.com/82375381/158030824-39274e1f-b02e-411b-b771-7351980d3f5c.png">

- 404.html

<img width="475" alt="404" src="https://user-images.githubusercontent.com/82375381/158030266-63d5d683-a9a2-443c-973a-34e39b2fee66.png">

- 500.html

<img width="477" alt="500" src="https://user-images.githubusercontent.com/82375381/158030270-185ec1e7-28d6-49ad-b4ef-7d3a7885be0e.png">

### Cross Browser and Cross Device Testing

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| Real Phone: iPhone XS Max     | Safari      | iOs.       | S/M 414 x 896 |
| Real Phone: iPhone 12.        | Chrome      | iOs        | S  390 x 844  |
| Real Computer: MacBook Pro    | Firefox     | Big Sur    | L  1240 x 768 |
| Chrome DevTools: Surface Duo  | Chrome      | Android    | M  540 x 720  |
| Safari DevTools: iPad         | Safari      | iOs        | M 768 x 1024  |
| Chrome DevTools: iPad mini    | Chrome      | iOs        | M 768 x 1024  |
| Firefox DevTools: iPad Pro    | Firefox     | Android    | L 1024 x 1366 |
| Firefox DevTools: iPad Pro Hz | Firefox     | iOs        | L 1366 x 1024 |
| Real Computer: MacBook Pro XL | Safari      | Big Sur    | XL 1752 x 960 |

### Manual Testing

- If user tries creating an account that already exists:

<img width="268" alt="Screenshot 2022-03-12 at 18 33 48" src="https://user-images.githubusercontent.com/82375381/158035984-3c5c353d-50cc-4a92-ac5b-82020b2e4643.png">

- If user's passwords do not match:

<img width="254" alt="Screenshot 2022-03-12 at 18 34 23" src="https://user-images.githubusercontent.com/82375381/158036001-ba6be75f-271c-4f12-9262-f4fc2aa1b33f.png">

- If when logging in, user's details are wrong:

<img width="330" alt="Screenshot 2022-03-12 at 18 35 28" src="https://user-images.githubusercontent.com/82375381/158036007-270b3bea-3008-4427-95fa-d61ae5862a71.png">

- If any of the required booking form fields are left blank:

<img width="664" alt="Screenshot 2022-03-12 at 18 36 02" src="https://user-images.githubusercontent.com/82375381/158036023-fab10b5b-b7be-4a65-bdc7-d6f390678606.png">
<img width="662" alt="Screenshot 2022-03-12 at 18 36 19" src="https://user-images.githubusercontent.com/82375381/158036033-b4c97588-dc6f-422d-96ef-b49716848148.png">
<img width="686" alt="Screenshot 2022-03-12 at 18 36 55" src="https://user-images.githubusercontent.com/82375381/158036205-e1b3bef8-e531-4fce-a359-9f423773fb16.png">
<img width="676" alt="Screenshot 2022-03-12 at 18 37 05" src="https://user-images.githubusercontent.com/82375381/158036208-abfbffb1-d935-47a8-97cb-2b88604851e7.png">

- User cannot choose a date in the past to book a table:

<img width="237" alt="Screenshot 2022-03-12 at 18 36 32" src="https://user-images.githubusercontent.com/82375381/158036198-0a9912e7-5a08-4039-83f0-763fe52efb76.png">

- User only sees their own bookings, unless admin:

<img width="963" alt="Screenshot 2022-03-12 at 18 39 30" src="https://user-images.githubusercontent.com/82375381/158036227-f8f2e3d4-50a3-4f31-8cf3-503621fdd522.png">
<img width="720" alt="Screenshot 2022-03-12 at 18 46 56" src="https://user-images.githubusercontent.com/82375381/158036254-959ca8ea-b239-40c3-8e86-926db086e3b6.png">

- Confirmation pops up before deletion of booking:

<img width="448" alt="Screenshot 2022-03-12 at 18 47 03" src="https://user-images.githubusercontent.com/82375381/158036259-9c7df859-5b3a-4d60-bc2d-be450add13c8.png">

- Account deletion form requires confirmation by user:

<img width="627" alt="Screenshot 2022-03-12 at 18 39 13" src="https://user-images.githubusercontent.com/82375381/158036274-47cfadaf-edb4-489e-ad03-8b3212538638.png">

- If wrong old password is given when updating password:

<img width="509" alt="Screenshot 2022-03-12 at 18 39 55" src="https://user-images.githubusercontent.com/82375381/158036302-79bf365b-575e-431d-b4d4-1ddb7bb3472c.png">

- If both new passwords don't match when updating password:

<img width="299" alt="Screenshot 2022-03-12 at 18 40 11" src="https://user-images.githubusercontent.com/82375381/158036312-984e342c-d2e9-4bdf-a03e-4f0034fb7a2c.png">

## Defects

I kept track of my bugs in real time. You can view them and their details [here](https://github.com/gabriel-alves-p/ceru-restaurant/projects/2) or by clicking on the 'Projects' and then 'Bug Report' on this repository on GitHub.

- I accidentally leaked my env.py file to GitHub. In the process of fixing it, I accidentally cloned all of my commits, so there are two of every commit.
- In the end, I managed to delete all history of my env.py on GitHub, and as a safety caution, I changed all of my keys and created a new env.py file.
I used the following urls to solve this issue (as well as the help of my lovely mentor Malia Havlicek):
- https://careerkarma.com/blog/git-remove-remote/#:~:text=The%20git%20remote%20remove%20command%20removes%20a%20remote%20from%20a,rm%20
- https://stackoverflow.com/questions/32056324/there-is-no-tracking-information-for-the-current-branch
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/delete-remote-Git-branches-github-gitlab-bitbucket-tracking-local
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository#using-git-filter-repo

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

## Media / Content

- https://docs.djangoproject.com/en/4.0/topics/auth/default/
- https://stackoverflow.com/questions/41653346/remove-user-in-django
- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
- https://www.rubys.com/
- https://www.camdendiner.com/
- https://www.shutterstock.com/
- https://unsplash.com/
- https://icons.getbootstrap.com/
- https://fontawesome.com/

## Acknowledgments

- Malia Havlicek (Code Institute mentor) for getting me out of some pickles, and being supportive and caring towards my project.
- Code Institute for providing me with a project idea and the content from which I learned these skills from.
- [Bootstrap](https://getbootstrap.com/) documentation for being super easy to follow.
- [Django](https://docs.djangoproject.com/en/4.0/) documentation for teaching me so much.
- [Codemy.com](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw) youtube channel for teaching me lessons that were extremely valuable to this project.
- [freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) youtube channel for teaching me lots too.
