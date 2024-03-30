![Lohana Logo](static/images/header.png)

## Introduction



Link to the live site here - [Lohana](https://lohana-df1411a79e72.herokuapp.com/)

![Responsive Mockup]()

## Table of Contents:
1. [**Introduction**](#introduction)
1. [**Planning**](#planning)
    * [***User Stories***](#user-stories)
        * [***Dropped***](#dropped)
    * [***Site aims***](#site-aims)
    * [***Scope***](#scope)
        * [***Book table form***](#1-book-table-form)
        * [***User profile***](#2-user-profile)
        * [***Admin panel***](#3-admin-panel)
        * [***Navigation bar***](#4-navigation-bar)
        * [***Footer***](#5-footer)
        * [***Landing page***](#6-landing-page)
        * [***Menu***](#7-menu)
    * [***Wireframes***](#wireframes)
    * [***Database schema***](#database-schema)
    * [***Color scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Agile**](#agile)
1. [**Features**](#Features)
    * [***Navigation***](#navigation)
        * [***Navigation - User***](#navigation---user)
        * [***Navigation - Admin***](#navigation---admin)
    * [***Landing page***](#landing-page)
    * [***Footer***](#footer)
    * [***AllAuth***](#allauth)
        * [***Register***](#register)
        * [***Login***](#login)
        * [***Logout***](#logout)
    * [***Contact form***](#booking-form)
    * [***User***](#user)
        * [***Profile***](#profile)
    * [***Admin***](#admin)
        * [***Add products***](#add-products-pagel)
    * [***Future features***](#future-features)
1. [**Deployment**](#deployment)
    * [***Cloning***](#cloning)
1. [**Testing**](#testing)
1. [**Credits**](#credits)
    * [***Technologies***](#technologies)
    * [***Code***](#code)
    * [***Content***](#content)
    * [***Media***](#media)
    * [***General reference***](#general-reference)

## Planning

### User stories
As a site user, I can navigate the site content from the landing page so that I can access all the content easily and find what I'm looking for

- Acceptance Criteria
    * Have a navigation bar with links to the different pages

    * Have separate sections for each page on the landing page

    * Have buttons in each section to access the different pages


#### Dropped
As an admin user, I can access the menu page so that I can edit/delete menu items

- Acceptance Criteria
    * Admin access to the menu page

    * Edit menu items

    * Delete menu items


### Site aims 


### Scope

The following is a prioritized list outlining the scope of the project. These priorities were determined considering the project's limited time frame and the key features essential for its aim (MVP).

#### 1. 

* 

#### 2. 

* 

#### 3. 

* 


#### 4. 

* 

#### 5. 

* 

#### 6. 

* 

#### 7. 

* 

### Wireframes

All pages on the site, except for the landing page, feature a consistent design style, characterized by a shared background image and a clean white text box containing the content. 
As a result, I'm only displaying the wireframes for the critical pages below. Despite minor differences, the overall appearance turned out pretty identical.

- **Landing page**
---
![Landing page desktop](docs/wireframes/land-desk.png)
![Landing page ipad](docs/wireframes/land-ipad.png)
![Landing page mobile](docs/wireframes/land-mob.png)


- **Booking form**
---
![Booking form desktop](docs/wireframes/form-desk.png)
![Booking form ipad](docs/wireframes/form-ipad.png)
![Booking form mobile](docs/wireframes/form-mob.png)

- **Profile**
---
![Profile desktop](docs/wireframes/prof-desk.png)
![Profile ipad](docs/wireframes/prof-ipad.png)
![Profile mobile](docs/wireframes/prof-mob.png)


- **Menu**
---
![Menu desktop](docs/wireframes/menu-desk.png)
![Menu ipad](docs/wireframes/menu-ipad.png)
![Menu mobile](docs/wireframes/menu-mob.png)


### Database schema
 I used Django's built-in User Model for the user accounts and I created three custom models for reviews, wishlist and a contact form (the rest were based off the walkthrough project Boutique Ado). 
 
 

![ERD]()

### Color scheme
I wanted a simple and elegant color scheme to match the theme of the site. 
I generated the colors from the logo on [Coolors](https://coolors.co/).

I utilized the Contrast grid by Eightshapes to test my color combos so the colors complied with the highest accessibility.

![Color]()

### Typography
I used two different fonts across the page:
 * Noto Serif, for most texts on the site.
 * Montserrat, for the reviews to separate them from the rest of the text on the site.

The fonts were sourced from Google Fonts.

## Agile

Throughout the project, I followed the Agile methodology by using GitHub projects and issues. This allowed me to organize the project's tasks into epics and user stories, making it easy to manage them on the Kanban board. This helped break down the work into smaller parts, making development smoother and more efficient.
By utilizing issues in GitHub and MSCW (MoSCoW Prioritization), I was also able to label and categorize the tasks to stay focused on the MVP. The "Won't Have's" of this project are still present on the Kanban board for future development.

I decided not to use sprints in this project due to it being more of a team logic and it made more sense for me to work in a task-based manner.
Even though I worked on this project alone, using Agile principles helped me track progress effectively and ensure future maintenance.

## Features 

### Navigation
- 

![Navigation bar]()

#### Navigation - User
- 

![Navigation bar]()

#### Navigation - Admin
- 

![Navigation bar]()

### Landing page

#### Hero image
- 

![Hero image]()

### Footer
- 

![Footer]()

### AllAuth

#### Register
![Register]()

#### Login
![Login]()

#### Logout
![Logout]()

### Contact form
- 'POST' contact form for all shoppers to contact the store.
- All messages displayed in the admin panel.

![Contact form]()

### Logged in user
#### Profile
- User profile only accessible by the logged in user.
- Three tabs for each section of the page.
- Delivery details tab with the user's saved delivery details and a form to update the details.
- Order history tab displaying all previous orders and ability to click on the order number to go back to the checkout success page.
- Wishlist tab displaying all the user's saved products (with a link back to 'All products', a product count of all wishlist items and the sort box) and ability to remove them.

- Success/error messages after each action.

![Profile delivery]()
![Profile orders]()
![Profile wishlist]()

### Logged in admin
#### Add products page
- 

![]()

#### Edit products page
- 

![]()

#### Delete products page
- 

![]()

### Future features
- Log in page with social accounts login.
- An About page with more information about the store (admin access to customize the page).
- Edit/delete account on user profile page.
- Profile page for the admin to see all contact messages with the senders details.

## Deployment (UPDATE)!!!!!!!

To deploy the site to Heroku, I went through below steps: 
- Go to [Heroku](https://heroku.com/) and log into your account.
- Click "Create new app" on the front page.
- Give your app a name (every name has to be unique on Heroku so it's ok if you can't name your project the same as on GitHub).
- Choose your region (USA or Europe) and click "Create app".
- You're then taken to the dashboard of your app where you have a navigation bar. Click on the Settings tab and scroll down to "Config Vars".
- Click "Reveal Config Vars" and input any necessary environment variables (such as your database URL or secret key).
- Go back to the navigation bar and select "Deploy".
- Scroll down to the "Connect to GitHub" section and click on the Connect button.
- After allowing Heroku access to GitHub, the "Connect to GitHub" section will allow you to search for the repository you wish to connect.
- Find your repository and click "Connect".
- You can now choose automatic deploys (Heroku deploys your app after every GitHub push you make) or manual deploys.
- After choosing a deployment method, click the deploy button and make sure you deploy from the correct branch.

Live link to the site - [Calima](https://calima-665aec414d74.herokuapp.com/)

### Cloning

I used the cloning method to use the VSCode desktop IDE with GitHub, below are the steps I took:
- Generate a repository and click the Code button in the middle of the screen.
- Go to Local and under Clone, copy the Git repository URL on the HTTPS tab.
- Go to the VSCode IDE front page and click 'Clone Git Repository' under Start or go to the Source Control button on the left-hand side menu bar and click 'Clone Repository'.
- Input the URL in the URL tab at the top of the window and press Enter.
- Select the location/folder where you want to store your repository on your computer through the popup and click the 'Select Repository location' button.
- VSCode will now clone the repository and you can choose to open it in your current window or in a new window.

## Testing

All the testing for this project can be found in a separate document [here](TESTING.md).

## Credits 

### Technologies

- The packages installed for this project can be found in [the requirements.txt](requirements.txt).
- Django was used as the Python framework.
- Django AllAuth was used for the user authentication and register, sign-up and login tasks.
- ElephantSQL was used for the database during development and in deployment.
- Bootstrap 5.3.2 was used to style HTML and CSS.
- Cloudinary was used for media file storage.
- Whitenoise was used to serve static files.

### Code 

- I drew help from the walk-through of the Boutique Ado project. There is directly copied code from the project, as well as similarities in some of the code but I adapted it to fit the aims of this project as much as possible.

Below are links that helped me adapt/build certain features:
- [How To Create a Scroll Back To Top Button](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
- [Navs](https://getbootstrap.com/docs/4.6/components/navs/#tabs)
- [Wishlist](https://www.youtube.com/watch?v=kD2vWOZFFcw&ab_channel=SharmaCoder)
- [Ajax change icon color add/remove wishlist](https://stackoverflow.com/questions/35716745/ajax-change-icon-color-add-remove-wishlist)

### Content 

- The wireframes were created with Balsamiq.
- The ERD diagram was created with [Smartdraw](https://www.smartdraw.com/entity-relationship-diagram/er-diagram-tool.htm).
- Fonts were acquired from [Google Fonts](https://fonts.google.com/).
- The icons were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The products, product images and product details were all taken from [Gorjana](https://www.gorjana.com/).
- The hero image was acquired from [Unsplash](https://unsplash.com/).
- The color palette was generated with the image on [Coolors](https://coolors.co/).
- [Am I Responsive](https://ui.dev/amiresponsive) was used to generate the initial image of the ReadME to showcase how the site looks on different screens.

### General references:
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)