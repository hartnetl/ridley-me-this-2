# Ridley Me this

[Live Site]( https://ridley-me-this-app.herokuapp.com/)


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

## Introduction

***

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


#### User stories 

| As a:       | I can:         | So that:  |
| ------------- |:-------------:| -----:|
|    |  |  |
|    |  |  |
|    |  |  |
|    |  |  |
|    |  |  |
|    |  |  |
|    |  |  |


#### Wireframes

<details>
<summary>Show wireframes</summary>
</details>


#### UI design

**Fonts**
* The logo font used is 
* The main text font used is 
* The main heading font is 

## Data Structure

The database used locally is sql and by heroku is postgres.  
AWS is used to house media and static files for this project.  

Talk about the models

<details>
<summary>Custom data models used:</summary>
Show the model schema:
![datamodels used](#)
</details>

<br>

## Web Marketing

### Business Model

Ridley Me This is a not-for-profit e-commerce site. It allows users to sponsor turtles for a year, purchase merchandise and give monetary donations. 100% of cost is a profit which goes straight towards the conservation of the turtles. The delivery cost of the certificate and gift is covered by the user. There is a small profit made off of the merchandise, which goes straight towards conserving the turtles. Once again the delivery cost is covered by the user. There is nothing delivered when users make a donation, but by taking a 'delivery fee' for these transactions all processing fees are covered.


### Facebook Campaign

As Facebook tends to remove pages it believes to not be a functional business page, I opted to create a mock up of a would be Facebook page.


## Technologies Used

***

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
    

## Features


#### SCREENSHOTS of site


### Future features 

* Integrate google maps API to generate random location for sponsored turtles instead of a single uploaded image
* Add banner which tells users how much money has been donated to date
* Collate sponsorship details about the turtles for the management to reveal how much profit has been raised for the turtles, which turtles have been sponsored by who etc
* Allow users to name the turtle when purchasing, instead of having to contact the site admin to do it manually
* Add JavaScript to hide the turtle info section when admin is adding a product unless it is a turtle they are uploading

## Testing 

***

### Manual Testing

The manual testing file is [here](#)


### Validation

html: [W3C markup validator](https://validator.w3.org/)   
Each page url was ran through the validator and any errors or warnings that appeared were corrected, and the url was ran through the validator again.  
<details>
<summary></summary>

![w3c html validator results for home page](#)
</details>
<details>
<summary></summary>

</details>  
<br>

CSS: [W3C validator](https://jigsaw.w3.org/css-validator/)  
CSS file was copied into the validator
<details>
<summary>View clear validator</summary>

![css validator with no warnings](#)
</details>   

<br>

Python: [pep8](http://pep8online.com/)  

<details>
<summary></summary>

</details>


JS: [JSHint](https://jshint.com/)  
JS script was ran through jshint 
<details><summary>View jshint result</summary>

![screenshot of jshint results](#)
</details>


Links: [w3c link validator](https://validator.w3.org/checklink)
<details>
<summary>View report here</summary>

![links report](#)
</details>


## Bugs


## Credits


## Deployment


## Acknowledgements


