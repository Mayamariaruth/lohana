
# Testing 

## Table of Contents:
1. [**Manual testing**](#manual-testing)
    * [***User stories***](#user-stories)
1. [**Validator testing**](#validator-testing)
1. [**Lighthouse testing**](#lighthouse-testing)
    * [***Landing page***](#landing-page)
    * [***Menu***](#menu)
    * [***Booking form***](#booking-form)
    * [***Booking success***](#booking-success)
    * [***Profile***](#profile)
    * [***Edit account details***](#edit-account-details)
    * [***Delete account***](#delete-account)
    * [***Edit booking***](#edit-booking)
    * [***Delete booking***](#delete-booking)
1. [**Wave accessibility evaluation**](#wave-accessibility-evaluation)
1. [**Bugs**](#bugs)
    * [***Unfixed Bugs***](#unfixed-bugs)

## Manual testing
I manually tested this site in multiple ways highlighted below:
* I tested every feature and its functionality as highlighted below in the [user stories](#user-stories).
* I deployed the site in an early stage on Heroku to make sure everything was working as intended. 
* I received invaluable feedback from my mentor David, students in my community, family members and friends working in the industry.
* I tested the site for cross-compatibility in the two most used browsers, Chrome and Safari.
* I used DevTools to easily move between different screen sizes, simulating sizes between 390px to 4000px (but it is also functional on even larger screens given the max-width setting on the Body element to keep the content compact instead of stretched).

### User stories

#### EPIC - View Products

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| List of all products on the Products page
|&check;| Navigation to Products from navigation bar
|&check;| Navigation to Products from landing page
|&check;| Products displayed with name, price, image, category and introduction
|&check;| Able to click on products to get to the Product Details page
|&check;| Back to top button exists to simplify page scrolling
|&check;| Number of products displayed on the page is highlighted


|passed | **View all categories of products so that I can purchase specific items based on my needs**
|:---:|:---|
|&check;| All categories highlighted in navigation bar
|&check;| All categories highlighted on Products page under title
|&check;| Every category button/link displays the list of products in that category
|&check;| Each product has a category tag
|&check;| The category tag displays the list of products in that category


|passed | **View every products details on a separate page so that I can find more information and select them to purchase**
|:---:|:---|
|&check;| Click on a product from Products page to get to Product Details page
|&check;| The page contains all details, price, image, name, introduction, category tag and description
|&check;| Can select quantity between 1-99 of product to add to shopping bag
|&check;| Error displays if value is incorrect
|&check;| Add to bag button adds product to the shopping bag
|&check;| Success message displays shopping bag summary with added products and details
|&check;| Continue Shopping button directs back to Products page


|passed | **Add a review on the products so that I can share my opinions about the products**
|:---:|:---|
|&check;| Any shopper/site user can submit a review on the Product Details page
|&check;| Review displays after submitting with name, review and time 
|&check;| Overflow property sets the review container to scroll
|&check;| Review count updates correctly after each added review (as well as after being deleted in the admin panel)


#### EPIC - Register and User profile

|passed | **Create an account so that I can have a personal account on the site**
|:---:|:---|
|&check;| Register page highlighted in the navigation bar
|&check;| Functioning Allauth authorization page (with error messages if incorrect values are added)
|&check;| Receive email confirmation through Gmail to verify the email
|&check;| Functioning Confirm email link and page
|&check;| Personal user profile is created and accessible from the navigation bar


|passed | **Sign In/Sign Out out of my account so that I can access my account**
|:---:|:---|
|&check;| Sign In/Sign Out pages highlighted in the navigation bar
|&check;| Functioning Allauth authorization pages (with error messages if incorrect values are added)
|&check;| Recover password works and a link to reset password is on the sign in page
|&check;| Access to personal user profile with my details from the navigation bar when logged in


    * List of user orders and link to order confirmation

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| Access to Profile from navigation bar
|&check;| Error message if admin tries to access the profile and redirect to sign in page if non-logged in user tries
|&check;| Functioning tabs for each profile section
|&check;| User's delivery details are correctly displayed (or set to None if they haven't added them yet)
|&check;| Update delivery details form works and updates the details properly after submitting
|&check;| Delivery details saved from the checkout displays properly
|&check;| Order history tab contains all user's orders
|&check;| Correctly displays the user order details
|&check;| Order number links back to the order confirmation (checkout success)
|&check;| Displays 'You have no orders' if no orders have been made
|&check;| Continue shopping button directs to Products page


As a site user I can save products to my wishlist on my profile so that I can save products that I would like to buy

- Acceptance Criteria
    * Able to save a product from the products list

    * Access the wishlist on my profile

    * List of the products I have saved


|passed | **Save products to my wishlist on my profile so that I can save products that I would like to buy**
|:---:|:---|
|&check;| Button to Save to Wishlist displays with logged in users (and not admin)
|&check;| Save to Wishlist button on the Products page under each product
|&check;| With each click, product is either added or removed from the user's wishlist and JSON success response message displays
|&check;| If any issues, JSON response displays an error message
|&check;| Access to Wishlist on the user profile
|&check;| Products displayed as on the Products page (with price, name, introduction and category tag)
|&check;| Sort box to sort products by name, price and category
|&check;| Remove from wishlist button under each product that removes the product
|&check;| Product count functioning and updates with addition or removal from wishlist 
|&check;| Link to All Products


#### EPIC - Search and sort 

|passed | **Search for products so that I can easily find what I'm looking for**
|:---:|:---|
|&check;| Search option in navigation bar
|&check;| Search based on name, description or category
|&check;| Displays list of products that match
|&check;| Product count displayed with the search term used
|&check;| All Products link
|&check;| Sort box to sort by name, price and category


As a shopper I can sort the products so that I can quickly identify what I'm looking for

- Acceptance Criteria
    * Sorting option on products page

    * Sort based on name, price, rating and category

    * See how many products are available


|passed | **Sort the products so that I can quickly identify what I'm looking for**
|:---:|:---|
|&check;| Sort box displayed on all pages with products (Products page, Category pages, Wishlist)
|&check;| Sort products based on name, price and category
|&check;| Displays product count and all products link


#### EPIC - Shopping bag and checkout

|passed | **View shopping bag so that I can ensure I make the correct order**
|:---:|:---|
|&check;| View shopping bag icon in navigation bar
|&check;| See total price of the items selected on icon
|&check;| Shopping bag preview displays in success message after adding product to bag
|&check;| Secure checkout button in preview to go to shopping page
|&check;| If order total is below $100, a banner highlights amount left until free delivery
|&check;| Click shopping bag to be directed to shopping bag page


|passed | **Edit/delete my order in the shopping bag so that I can purchase what I want**
|:---:|:---|
|&check;| View all items in my shopping bag with name, image, SKU, quantity and subtotal
|&check;| Quantity buttons disabled at number 1 and 99
|&check;| Remove button removes the product from the shopping bag
|&check;| Update button updates the quantity when changed
|&check;| Bag total, delivery total and grand total displays correctly
|&check;| Continue shopping button directs to all products
|&check;| Secure checkout button directs to checkout page 


As a shopper I can make an order purchase so that I can buy the items I want safely

- Acceptance Criteria
    * Checkout by entering my personal details, payment information and billing details

    * See delivery information (free delivery or delivery fee)

    * Make a card transaction

    * My personal and payment information is safe and secure

|passed | **Make an order purchase so that I can buy the items I want safely**
|:---:|:---|
|&check;| Order summary displayed on checkout page with shopping bag details
|&check;| 
|&check;| 
|&check;| 

As a shopper I can receive an order confirmation after checkout so that I know my order has been processed

- Acceptance Criteria
    * View an order confirmation with all my order details after checkout

    * Receive an email of my order confirmation

    * Able to contact the store if something is not correct with my order

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| List of all products on the site
|&check;| 
|&check;| 
|&check;| 

#### EPIC - Admin management

As an admin I can edit/delete products from the site so that I have control over the store inventory

- Acceptance Criteria
    * Access product information

    * Edit product information

    * Delete products

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| List of all products on the site
|&check;| 
|&check;| 
|&check;| 

As an admin I can add products to the site so that I can add relevant inventory

- Acceptance Criteria
    * Admin access to site with admin profile

    * Add more products to the site

    * Input images, price, description and necessary product information

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| List of all products on the site
|&check;| 
|&check;| 
|&check;| 

#### EPIC - Contact

As a shopper I can contact the store so that I can communicate with the store about orders, products or whatever I might need to make a purchase

- Acceptance Criteria
    * Contact form on the website

    * Input details and message for the store

    * Form submission to admin panel

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| List of all products on the site
|&check;| 
|&check;| 
|&check;| 

### Footer 

|passed | **View all site products so that I can purchase them**
|:---:|:---|
|&check;| 
|&check;| 
|&check;| 
|&check;| 

## Validator testing 

- HTML
  - There were no errors present when passing through the official W3C validator ![W3C validator](docs/validation/html.png)

- CSS
  - There were no errors present when passing through the official Jigsaw validator with direct input ![(Jigsaw) validator](docs/validation/css.png)

- PEP8
  - There were no errors present when passing through the PEP8 CI Python linter ![PEP8](docs/validation/linter.png)

## Lighthouse testing 

This testing was done in an incognito window in Chrome to make sure the results were not influenced by browser extensions.

The lower scores were for two main reasons:
- The cdn imports from bootstrap, Google fonts and Font Awesome.
- Hero image and background image, which were compressed and even resized multiple times without a change in score. It was not possible to edit them further without a bigger change in quality.

### **Landing page**
- Desktop version:

![Desktop landing page](docs/images/lighthouse/land-desk.png)

- Mobile version:

![Mobile landing page](docs/images/lighthouse/land-mob.png)

### **Menu**

- Desktop version:

![Desktop menu](docs/images/lighthouse/menu-desk.png)

- Mobile version:

![Mobile menu](docs/images/lighthouse/menu-mob.png)

### **Booking form**

- Desktop version:

![Desktop booking form](docs/images/lighthouse/form-desk.png)

- Mobile version:

![Mobile booking form](docs/images/lighthouse/form-mob.png)

### **Booking success**

- Desktop version:

![Desktop booking success](docs/images/lighthouse/success-desk.png)

- Mobile version:

![Mobile booking success](docs/images/lighthouse/success-mob.png)

### **Profile**

- Desktop version:

![Desktop profile](docs/images/lighthouse/prof-desk.png)

- Mobile version:

![Mobile profile](docs/images/lighthouse/prof-mob.png)

### **Edit account details**

- Desktop version:

![Desktop edit account details](docs/images/lighthouse/edit-acc-desk.png)

- Mobile version:

![Mobile edit account details](docs/images/lighthouse/edit-acc-mob.png)

### **Delete account**

- Desktop version:

![Desktop delete account](docs/images/lighthouse/del-acc-desk.png)

- Mobile version:

![Mobile delete account](docs/images/lighthouse/del-acc-mob.png)

### **Edit booking**

- Desktop version:

![Desktop edit booking](docs/images/lighthouse/edit-book-desk.png)

- Mobile version:

![Mobile edit booking](docs/images/lighthouse/edit-book-mob.png)

### **Delete booking**

- Desktop version:

![Desktop delete booking](docs/images/lighthouse/del-book-desk.png)

- Mobile version:

![Mobile delete booking](docs/images/lighthouse/del-book-mob.png)

## Wave accessibility evaluation

I also used the Wave evaluation tool to make sure I covered all my bases. 
The evaluation is free from errors on all pages.

![Wave evaluation]()

## Bugs

- 
    - 

- Summernote description field is not updating after set up /// Update ProductAdmin function from admin.ModelAdmin to SummernoteModelAdmin and add summernote_fields there
- Summernote field text is displaying as raw HTML content /// Add “|safe” to the HTML tag 
- After adding title tag for products page, when clicking all products it says necklaces /// add If statement to check if the length of the categories selected match the count of the Category model (template tag includes all categories)
- Category sorting not working with sorting box on products page /// change elif statement from “order_by(‘category’)” to “order_by(‘category__name’)”
- toasts disappears after 1 second // add autohide attribute in JS
- grand total not displaying correctly in admin panel on created orders /// update the model method to calculate the grand_total as the sum of the delivery cost and order total
- migration fail after changing the Country model field to Django Countries (Error: value too long for type character varying(2)) /// Migration file stored the Country field as Max_length=2 so I updated the max_length to 255 in the file and migrated again
- User profile tab content being pushed down by Delivery details tab content /// The d-flex class on the Delivery Details content pushed the other content down. Added JS code to add/remove the d-flex class depending on the tab
- Profile delivery details not displaying users delivery details /// problem with the user profile connection to the order. 
- After adding a product to the site with Admin Management profile and then removing the product from the admin panel, the whole site errored saying “Page not found (404) No Product matches the given query.” On every site /// Added if statement in bag_contents context processor to only query the Product model when necessary **(with help of ChatGPT)**
- Error when trying to submit new update in edit_products.template after adding summer note (clean() got an unexpected keyword argument 'styles’) // download Bleach ([Django Summernote clean\(\) got an unexpected keyword argument 'styles' in DjangoForms](https://stackoverflow.com/questions/73789407/django-summernote-clean-got-an-unexpected-keyword-argument-styles-in-djangof))
- Heorku deployment error when setting up Django-storages (An error occurred (403) when calling the HeadObject operation: Forbidden) /// removed AWS and went with white noise and cloudinary for easier storage
- register/login error with new users (SMTP.starttls() got an unexpected keyword argument 'keyfile’) /// update to Django 4.2.7 and allauth0.61.0 https://stackoverflow.com/questions/77482831/smtp-starttls-got-an-unexpected-keyword-argument-keyfile
- error with add_to_wishlist view when using Ajax (AttributeError: 'WSGIRequest' object has no attribute 'is_ajax’) // change is_ajax to **request.headers.get('x-requested-with') == 'XMLHttpRequest'** [AttributeError: 'WSGIRequest' object has no attribute 'is_ajax'](https://stackoverflow.com/questions/70419441/attributeerror-wsgirequest-object-has-no-attribute-is-ajax)
- NameError when checking out with Stripe (payment.intent.succeeded = 500 server error) // import stripe at the top of web hooks, OOPS!
- Superuser can access user profile // add if statement in profile view to handle superuser access
- Emails not sending on heroku, only in local environment /// had set ‘DEVELOPMENT’ variable in heroku config var to False, removed it and everything was fine
- in shopping bag, can update number of quantity to over 99 or under 1 // 

### Unfixed Bugs
- This might be more of an unfixed feature but when the logged in user adds a product to their wishlist, a JSON response message pops up instead of a toast message. I tried adding the toast messages too but they did not display properly so given the time constraint of the deadline, I decided to remove them completely and keep the JSON messages for now.
This would of course be one of the first things I would change with more time, so as to keep the messages cohesive across the site.

- The reset functionality on the sorting box when clicking 'Sort By' was not working properly so I had to abandon that last minute but I plan on fixing it when coming back to the project as well.

- When going to the Products page directly from the [URL](https://lohana-df1411a79e72.herokuapp.com/products/) and not one of the buttons on the page, the page displays without the categories under the title (and without the categories in the URL). This was noticed in the final moments before the deadline of course...