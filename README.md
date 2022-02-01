# Ridley Me this

Link to the live site:  
[Ridley Me This]( https://ridley-me-this-app.herokuapp.com/)  

![am-i-responsive](readmefiles/amiresponsive.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Data Structure](#data-structure)
3. [Web Marketing](#web-marketing)
4. [Technologies used](#technologies-used)
5. [Features](#features)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Credits](#credits)
9. [Deployment](#deployment)
10. [Acknowledgements](#acknowledgements)

<hr>

## Introduction
<hr>

Welcome to **Ridley Me This**  
This project is set up as a turtle sponsorship website, with the additional option to buy merchandise, give monetary donations or read up on turtle and eco living.  
The 7 species of sea turtle have different levels of endangerment. We need to ensure none of these worsen, and hopefully get them all to not endangered status.  
Users who sponsor a turtle do so for a year, and even get to give it a nickname for a year which is displayed on the website. A certificate of sponsorship and a special turtle themed gift is sent to each sponsor. The proceeds are then put towards the conservation effort to protect turtles.  

### Project Planning

#### Agile Development

The agile development process helps to keep a team organised and on track. It does this through monitoring the progress of the project and rating each feature and associated tasks by importance (from ones that are needed, ones that the project should have, and those that would be nice to have but not needed).  
An attempt was made to implement in this project, though admittedly because this was a solo project there was a tendency to track progress by handwiting to do lists etc over the github project setup.  That said, all issues were created based on user stories for the project requirements. These were broken into 6 different themes represented as 6 different project boards. Each project had 3 boards - to do, in progress and done. As the project progressed each issue card was moved between boards as its status changed. Issues were also given labels to declare an order of important - need, should and want labels.

By using this agile system it enables the team (or individual) to create the best functional application in the shortest possible time, as the project is frequently reassessed and completed in set time bouts. This ensures time isn't wasted on nice to have features while ignoring the features that are definitely required.

#### User Goals

As a site user I want to be able to:  

* View all products available on the shop to see what is available
* See a clear price so I know how much I'll spend
* Make a profile to keep track of previous orders and save personal information for speedy future checkouts
* Easily navigate around the site, and easily find the information / products I'm looking for 
* Purchase the items I can see on the site
* Know that the purchase was successful


As a site owner I want to be able to:

* Provide an aesthetically pleasing and easy to use website for users
* Offer a wide range of products to attract more customers
* Allow users to easily purchase my products, without the need to create an account
* Add, edit and delete products on the site as required
* Delete testimonials left by users, in the case of inappropriate content being posted.


#### Wireframes

<details>
<summary>Show wireframes as images</summary>

![wireframes for desktop and mobile](readmefiles/wireframe-images/ABOUT-PAGE.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/CART.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/CHECKOUT-LOGGED-OUT.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/CHECKOUT.png)    <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/CONTACT.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/home-page-logged-in.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/home-page-logged-out.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/PROFILE.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/SHOP-PAGE.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/SPONSOR-PAGE-DETAIL.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/SPONSOR-PAGE.png)  <br><br>
![wireframes for desktop and mobile](readmefiles/wireframe-images/TRACKING.png)  <br><br>

</details>

<br> 
View wireframes as pdf:  

[wireframe link](readmefiles/wireframes.pdf)


#### UI design

The colour scheme used is 'cool and fresh' found [here](https://visme.co/blog/website-color-schemes/)  
<details>
<summary>See the colour scheme here</summary>

![colour scheme](readmefiles/colour-scheme.png)

</details>


<hr>

## Data Structure
<hr>

The database used locally is sql and by heroku is postgres.  
AWS is used to house media and static files for this project.  

Talk about the models

<details>
<summary>Custom data models used:</summary>
Show the model schema:
![datamodels used](#)
</details>

<br>

<hr>

## Web Marketing
<hr>

### Business Model

Ridley Me This is a not-for-profit e-commerce site. It allows users to sponsor turtles for a year, purchase merchandise and give monetary donations. 100% of cost is a profit which goes straight towards the conservation of the turtles. The delivery cost of the certificate and gift is covered by the user. There is a small profit made off of the merchandise, which goes straight towards conserving the turtles. Once again the delivery cost is covered by the user. There is nothing delivered when users make a donation, but by taking a 'delivery fee' for these transactions all processing fees are covered.


### Facebook Campaign

As Facebook tends to remove pages it believes to not be a functional business page, I opted to create a mock up of a would be Facebook page.


<hr>

## Technologies Used
<hr>

Languages  
* [Python3](https://www.python.org/about/) 
* [Javascript](https://www.tutorialspoint.com/javascript/javascript_overview.htm#:~:text=JavaScript%20is%20a%20dynamic%20computer,language%20with%20object%2Doriented%20capabilities.) 
* [html5](https://developer.mozilla.org/en-US/docs/Web/HTML) 
* [css](https://developer.mozilla.org/en-US/docs/Web/CSS)

<br>

Libraries and other technologies used
* [Django 3](https://www.djangoproject.com/start/overview/)
* [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Google fonts](https://fonts.google.com/)
* [Fontawesome](https://fontawesome.com/)
* [Postgresql](https://www.postgresql.org/)
* [aws](https://aws.amazon.com/)

Other tools
* [Gitpod](https://www.gitpod.io/docs/) as the IDE for development 
* [Git](https://git-scm.com/about) for version control 
* [Github](https://github.com/about) to host the project code 
* [Heroku](https://www.heroku.com/about) to deploy the project
* W3C for validating [html](https://validator.w3.org/), [css](https://jigsaw.w3.org/css-validator/) and [links](https://validator.w3.org/checklink) 
* [jshint](https://jshint.com/about/) to validate javascript
* [pep8 online](http://pep8online.com/about) to validate python code
* [lighthouse](https://developers.google.com/web/tools/lighthouse) to test accessibilility and performance 
* [github projects](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards) to create kanban boards 
* [balsamiq](https://balsamiq.com/) for wireframes
* [tinypng](https://tinypng.com/) to compress image file sizes
* [logomaker](https://www.logomaker.com/ ) to create the logo
    

<hr>

## Features
<hr>

### Linking user stories to features  


#### User stories 

EPIC: Navigating webpage  

USER STORIES:  

* As a site user or shopper I want the purpose of each page to be clear and intuitive so that I don’t waste time searching or with irrelevant information
    * Feature: Information is clear and obvious
* As a site user or shopper I want to be able to quickly navigate between pages to find what I need
    * Feature: Easy to use navbar
            <details>
        <summary>NavBar</summary>

        ![navbar image](readmefiles/navbar.png)

        </details>

* As a site user or shopper I want to be able to use the website on my mobile phone so I can shop or browse on the go
    * Feature: Collapsed mobile view navbar
            <details>
        <summary>Mobile NavBar</summary>
        
        ![mobile navbar image](readmefiles/mobile-navbar.png)

        </details>
* As a site user or shopper I want to be able to open relevant links in new tabs so I can get that extra information without having to repeatedly hit the back button to find where I was
    * Feature: All external links have "target=_blank"

EPIC: Viewing products  

* As a site user or shopper I want to be able to see all available products so that I can buy them 
    * Feature: A list of all products is visible to shoppers  
            <details>
        <summary>All Product View</summary>
        
        ![All products image](readmefiles/all-products.png)

        </details>
* As a site user or shopper I want to be able to view products/turtles in more detail so I can decide which product/turtle I want
    * Feature: Details view for turtles  
            <details>
        <summary>detail view</summary>
        
        Turtle Detail View  
        ![Turtles detail view image](readmefiles/turtle-detail.png)  

        Donate Detail View  
        ![Donate detail view](readmefiles/donate-detail.png)  

        </details>

* As a shopper I want to be able to see what turtles have already been sponsored so that I know there will be more available for sponsorship at a later date
    * Feature: Separate sponsored and available turtle sections  

        <details>
        <summary>Turtle categories </summary>

        ![Sponsored and available turtles](readmefiles/turtle-cat.png)  

        </details>

* As a shopper I want to be able to see an updated spend total of my cart so that I am fully aware of how much I’m spending
    * Feature: A basket icon in the navbar that holds the current total in your basket

        <details>

        <summary>Basket total </summary>

        ![basket total](readmefiles/basket.png)

        </details>

* As a site user I want to be able to easily register for an account so that I don’t waste time with complicated sign ups and get my own profile
    * Feature: Straight forward registration page

        <details>

        <summary>Signup Form </summary>

        ![Signup page](readmefiles/signup.png)

        ![Signup button](readmefiles/signup-button.png)

        </details>

* As a site user I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful
    * Feature: Email registration confirmation email 

        <details>

        <summary>Confirmation email </summary>

        ![email confirmation](readmefiles/email-confirmation.png)

        </details>

* As a shopper I want to be able to create an account when making a purchase to save me time and avoid repeating my details
    * Feature: links to sign up or login at checkout 

        <details>

        <summary>Account at checkout</summary>

        ![account at checkout](readmefiles/checkout-account.png)

        </details>

* As a site user I want to be able to have a personalized user profile so that I can view my sponsored turtle, previous order history and my saved details 
    * Feature: Each registered user gets a profile

        <details>

        <summary>Prfile page</summary>

        ![Profile page](readmefiles/profile-image.png)

        </details>

* As a site user I want to be able to easily log on to my profile so that I can easily keep track of my turtle and get info on my purchases
    * Feature: Sign in button
* As a site user I want to be able to easily log out of my account so that I can keep my account and personal information secure 
    * Feature: Logout button
* As a site user I want to be able to easily recover my password if I forget it so that I can recover access to my account
    * Feature: Forgot password link 

THEME: Finding products  

EPIC: Product searching  

* As a shopper I want to be able to search for products on all pages so that I can quickly find what I’m looking for
    * Search bar in navbar
* As a shopper I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available 
    * Search results
* As a shopper I want to be able to search for a specific product so that I can find a specific product I'd like to get
    * Filtered search bar

EPIC: Product filtering and sorting  

* As a shopper I want to be able to sort the products so that I can arrange products by price and rating
    * Sort button on product pages
* As a shopper I want products filtered by type so that I can save time only looking through what I need
    * Products split into turtles, merchandise and donations in navbar

THEME: Making a purchase  

EPIC: Choosing items  

* As a shopper I want to be able to easily select the quantity of a product so that I don't accidentally select the wrong product, quantity or option
    * Feature: Non turtle items have a + and - button to change quantity


EPIC: Checkout  

* As a shopper I want to be able to view items in my bag to be purchased so that I can see how much I’m about to spend and what I’m getting for that 
money    
  * Feature: View the basket 

     <details>

    <summary>Basket page</summary>

    ![Basket page](readmefiles/shopping-basket.png)

    </details>

* As a shopper I want to be able to adjust the quantity of each item in my bag so that I can easily make changes to my purchase before checkout
    * Feature: Merch and donate view has quantity selector, turtles do not
* As a shopper I want to be able to easily enter my payment information so that I can checkout quickly and with no unnecessary difficulty
    * Feature: Straightforward checkout

        <details>

        <summary>Payment</summary>

        ![Payment](readmefiles/payment-info.png)

        </details>



EPIC: Post payment  

* As a  shopper  I want to be able to  view an order confirmation after checkout  so that I can  verify that I haven't made any mistakes 
    * Feature: When order is placed successfully, email is sent to the email supplied at checkout with order details
* As a  shopper  I want to be able to  receive an email confirmation after checking out  so that I can  keep confirmation of what I’ve purchased for my records.  
    * Feature: When order is placed successfully, email is sent to the email supplied at checkout with order details
* As a shopper with a registered account I want to be able to see my order added to my profile after confirmation so I know the order has been confirmed for my account
    * Feature: Order history is displayed on user's profile

THEME: Admin and Store Management  

EPIC: Product management  

* As a  store owner  I want to be able to  add a product  so that I can  add new items to my store 
    * Feature: Add product form
* As a  store owner  I want to be able to  edit/update a product  so that I can  change product prices, descriptions, images and other product information.  
    * Feature: Edit button on products which allows owner to edit the details of the product
* As a  store owner  I want to be able to  delete a product  so that I can  remove items that are no longer for sale
    * Feature: Admin can delete products from page

EPIC: Turtle Management  

* As a store owner I want to be able to add new turtles so that they can be sponsored
    * Feature: Admin can use add product form to add turtles
* As a store owner I want to be able to edit the information given about each turtle so that sponsors are kept up to date with any new info on all our turtles
    * Feature: Admin can click the edit button to edit details about each turtle
* As a store owner I want to be able to remove turtles from the site so they are no longer displayed on the site when they aren’t available for sponsorship anymore
    * Feature: Admin can delete any turtle from the website

THEME: Communication  

EPIC: Contact site owners  

* As a site user I want to be able to have a way to send the site owners a message so that I can have any feedback, questions or concerns addressed
    * Feature: Contact form on page

EPIC: Join community  

* As a site user I’d like to be able to receive a newsletter so that I can stay up to date with the ongoings of the website
    * Feature: Functional newsletter signup 
* As a site user I’d like to follow the website’s social media pages so I can be surrounded by like minded people  
    * Feature: Social media links on page - leads to home pages of those sites


### Future features 

* Integrate google maps API to generate random location for sponsored turtles instead of a single uploaded image
* Add banner which tells users how much money has been donated to date
* Collate sponsorship details about the turtles for the management to reveal how much profit has been raised for the turtles, which turtles have been sponsored by who etc
* Allow users to name the turtle when purchasing, instead of having to contact the site admin to do it manually
* Add JavaScript to hide the turtle info section when admin is adding a product unless it is a turtle they are uploading


<hr>

## Testing 
<hr>

### Manual Testing

The manual testing file is [here](Testing.md)


### Validation

html: [W3C markup validator](https://validator.w3.org/)   
Each page of the site was run through the validator. If errors were found the required changes were made until they could be removed.  
Unfortunately 2 warnings remain.  

<details>
<summary>Products Error</summary>

![products error](readmefiles/product-err.png)  

This error displays on the turtle and donations category page, but not the all products or merchandise donation page.  
I tried to find a solution where all 3 categories and the regular product page didn't have this error but ran out of time.  
</details>

<details>
<summary>Feedback Error</summary>

![feedback error](readmefiles/testimonial-err.png)  

This error displays on the testimonials page, despite the p tag being there. Couldn't find a solution for this.  

![feedback code](readmefiles/testimonial-err-1.png)  

</details>

<br>

CSS: [W3C validator](https://jigsaw.w3.org/css-validator/)  
All css was copied directly into the validator. No errors were found.  
<details>
<summary>View clear validator</summary>

![css validator with no warnings](readmefiles/css-val.png)
</details>   

<br>

Python: [pep8](http://pep8online.com/)  
All python files were validated by pasting the code directly. All errors found that could be removed were removed.
<details>
<summary>PEP-8 results</summary>

![pep8 no errors](readmefiles/pep-8.png)  

After going through the entire app to reduce the line lengths, some threw django errors afer satisfying pep8 requirements.  
Therefore it was better to revert to the longer line lengths and have some longer than usual lines.

![Error 501 - long lines](readmefiles/pep-8-err.png)  
Examples:  
* widgets.py - line 13 - template

</details>
<br>

JS: [JSHint](https://jshint.com/)  
All JS script was ran through jshint and fixes applied until no errors were found.  
<br>

Links: [w3c link validator](https://validator.w3.org/checklink)  
All pages were ran through the link validator. No errors were returned, but there was mention of the linkedin social link.
<details>
<summary>View results here</summary>

![links report](readmefiles/link-val.png)
</details>


<hr>

## Bugs
<hr>

### Fixed 

* Error when deploying  
Tried to migrate after swapping database, got error during migration:  
    django.db.utils.DataError: value too long for type character varying(2)  

Searched stackoverflow and found it's to do with model length   
Checked models, all good  
Check slack, a previous version of country field was max 2  
Edited migration file in error  
Migrate then worked  

* Creating formset - this was missing a line of code  

Error:  

        IntegrityError at /products/add/
        null value in column "price" of relation "orders_product" violates not-null constraint
        DETAIL:  Failing row contains (8, , , null, , null, null, , , null).
        Request Method:	POST
        Request URL:	http://localhost:8000/products/add/
        Django Version:	3.2
        Exception Type:	IntegrityError
        Exception Value:	
        null value in column "price" of relation "orders_product" violates not-null constraint
        DETAIL:  Failing row contains (8, , , null, , null, null, , , null).
        Exception Location:	/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py, line 84, in _execute
        Python Executable:	/home/gitpod/.pyenv/versions/3.8.11/bin/python3
        Python Version:	3.8.11
        Python Path:	
        ['/workspace/ridley-me-this-2',
        '/home/gitpod/.pyenv/versions/3.8.11/lib/python38.zip',
        '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8',
        '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/lib-dynload',
        '/workspace/.pip-modules/lib/python3.8/site-packages',
        '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages']

* Order items not displaying on order history or email  
I deleted a line of code by accident for saving the line items when adding in the change turtle status and didn't notice.  
Adding it back in made this work again   


### Remaining

* The turtle sponsorship dates are linked to the date the product is added, not the date a user sponsors the turtle  
* Even though users can't add more than one turtle at a time, they can repeatedly add the same one to basket - I started trying to fix this but ran out of time before I could fully erase bug  


<hr>

## Credits
<hr>

### Code

* Rolling back migrations  
https://www.delftstack.com/howto/django/django-rollback-migration/


### Media  

* turtle icon   
<a href="https://www.flaticon.com/free-icons/turtle" title="turtle icons">Turtle icons created by Hery Mery - Flaticon</a>  

* leatherback  
<a href="https://commons.wikimedia.org/wiki/File:Leatherback_Sea_Turtle_(17665415746).jpg">Leatherback image - wiki</a>

* Green turtle   
<a href="https://commons.wikimedia.org/wiki/File:Green_Sea_Turtle_grazing_seagrass.jpg">Green sea turtles</a>

* Loggerhead   
<a href="https://commons.wikimedia.org/wiki/File:Loggerhead_Turtle.jpg">Loggerhead turtle</a>

* olive ridley  
<a href="https://commons.wikimedia.org/wiki/File:Turtle_Olive_Ridley.jpg">Olive Ridley</a>

* Kemps ridley  
<a href="https://commons.wikimedia.org/wiki/File:A_Kemp%27s_ridley_sea_turtle_crawling_back_into_the_ocean_after_nesting_along_the_sandbag_dunes_on_Ocracoke_(51305938487).jpg">Kemp's ridley</a>

* Flatback  
<a href="https://commons.wikimedia.org/wiki/File:Flatback_hatchling.jpg">Flatback</a>
 
* hawksbill   
<a href="https://commons.wikimedia.org/wiki/File:Hawksbill_Turtle.jpg">Hawksbill</a>

* scarf  
<a href="https://www.pinterest.com/pin/258182991110068408/">Scarf</a>

* necklace  
<a href="https://images1.novica.net/pictures/27/p391807_2_400.jpg">Necklace</a>

<hr>

## Deployment
<hr>

<hr>

## Acknowledgements
<hr>


