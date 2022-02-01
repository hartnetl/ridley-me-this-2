# Testing for Ridley Me This site

## Features 

* Information is clear and obvious
    * Expected: Text is easy to read, contrast is high and in short blocks for readability 
    * Works: YES
* Easy to use navbar
    * Expected: All links work to every page, on every page. Same for footer.
    * Works: YES
* Collapsed mobile view navbar
    * Expected: The navbar collapses down for easier viewing on smaller screens
    * Works: YES
* All external links have "target=_blank"
    * Expected: All links which leave the website open in a new tab
    * Works: YES
* A list of all products is visible to shoppers
    * Expected: The products page displays all products to users logged in and out
    * Works: YES
* Details view for turtles 
    * Expected: Clicking on a turtle (or any product) opens product on new page showing all info about that product (or turtle)
    * Works: YES
* Separate sponsored and available turtle sections
    * Expected: Turtles added to site go to 'available' and when someone sponsors them it moves to 'sponsored'
    * Works: YES
* A basket icon in the navbar that holds the current total in your basket
    * Expected: Each time an item is added / taken from the shopping basket the total displayed on the page updates also
    * Works: YES
* Straight forward registration page
    * Expected: Registration page is simple and details are rememembered for furture use
    * Works: YES
* Email registration confirmation Email
    * Expected: After a user registers they are sent an email to confirm that email address
    * Works: YES
* links to sign up or login at checkout
    * Expected: At checkout use is redirected to login/signup if those links are clicked in the checkout and the basket session is saved
    * Works: YES
* Each registered user gets a profile
    * Expected: When a user registers a profile is created with their name on it
    * Works: YES
* Sign in button
    * Expected: There is a sign in button which brings user to login page - visible when logged out and isn't visible when users are logged in 
    * Works: YES
* Logout button
    * Expected: When clicked it takes user to logout page. Visible when logged in, not visible when logged out.
    * Works: YES
* Forgot password link 
    * Expected: When user clicks the forgot password button, an email is sent to their registered email address
    * Works: YES
* Search bar in navbar
    * Expected: When user types in a search term, results are displayed
    * Works: YES
* Search results
    * Expected: User's search term is displayed on the page, as well as how many hits it got
    * Works: YES
* Sort button on product pages
    * Expected: Sort button works in direction selected and by type selected
    * Works: YES
* Products split into turtles, merchandise and donations in navbar
    * Expected: Each link in the lower navbar (turtles, mech, donations) filters all products by the category selected
    * Works: YES
* Non turtle items have a + and - button to change quantity
    * Expected: For merchandise and donations there is a quantity selector on the details and basket pages. 
    * Works: YES
* View the basket 
    * Expected: When users click the basket icon it brings them to their basket, which shows the items they selected in the quantities they selected and the cost.
    * Works: YES
* Merch and donate view has quantity selector, turtles do not
    * Expected: Users can input between 1 and 99 quantity of any merchandise or donation item. Users can only select one turtle.
    * Works: Mostly! Some bugs with users being able to repeatedly add the same turtle to their basket.
* Straightforward checkout
    * Expected: Users only need to input vital information. Card details section is simple and short.
    * Works: YES
* When order is placed successfully, email is sent to the email supplied at checkout with order details
    * Expected: User receives email after successful purchase thanking them for their order and giving some details of it
    * Works: YES
* Order history is displayed on user's profile
    * Expected: Users can see the items they have previously bought on their profile page
    * Works: YES
* Add product form
    * Expected: Admin can add products to the page from the front end
    * Works: YES
* Edit button on products which allows owner to edit the details of the product
    * Expected: The edit button allows owner to edit the items on the page
    * Works: YES
* Admin can delete products from page
    * Expected: Owners can delete products from the page
    * Works: YES
* Admin can use add product form to add turtles
    * Expected: Owner can use the add product form to add turtles to the store
    * Works: YES
* Admin can click the edit button to edit details about each turtle
    * Expected: Clicking edit allows owner to change information about the turtles
    * Works: YES
* Admin can delete any turtle from the website
    * Expected: Admin can remove turtles from the webpage using the delete button
    * Works: YES
* Contact form on page
    * Expected: When user uses contact form their message is sent to the database, they receive a confirmation message to the page and an email is sent to admin to say the contact form was used
    * Works: YES
* Functional newsletter signup
    * Expected: If user enters their email address into the newsletter signup they get a confirmation message displayed on the page and their info added to mailchimp directory. If they try reenter their email they get a message saying they already signed up
    * Works: YES
* Social media links on page - leads to home pages of those sites
    * Expected: Social media link leads to the corresponding home page of that site
    * Works: YES
