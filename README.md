# Ketogenius

A webstore focussed on providing a user friendly and digestible destination for new comers and seasoned veterans of the much discussed Keto diet. Showcasing multiple niche and specialist products and with aims to grow a vast database of helpful products and Ketogenic information.

---

##UX

*Ketogenius* design and user experience philosophy is all about simplicity and ease of use. The main landing page comprises and displays a large and inviting hero image  with a search bar/function at the very top allowing users to search via product name. User's can then also log in or create an account with ease and navigate the store via the clearly defined and labelled links. A note of products and the total price of the user's basket is displayed at all times to offer transparency and ease of use for a customers journey.

* As a new user I want to know upon viewing the site what options I have in terms of signing up/registering and viewing the sites content. I want this to be presented via a clear and navigatable menu.

* As a user I want to be able to view all products the store currently has in stock and be able to sort these by price and customer rating.

* As a user I want to be able to see a product details page to review and decide on whether or not to purchase an item. I then want to be able to be able to add this item or multiples of this item to my bad ready to purchase.

* As a user I want to be able to purchase these products using a secure and sophisticated payment system.

* As a user I want to be able to search for specific and particular products using keywords to filter through results.

* As a user I want to be able to view my previous orders through my account so I can track my spending and purchasing habits.

* As a store owner I want to be able to edit the product list or product details page and be able to add and remove products with a clear and easy to use form which is accessible to store owners.

## Features

#### Exisiting Features

1. Navigation bar - allows users to navigate between pages easily with identifiable descriptors and an easy to understand structure. Is consistent across the entire platform. The brand logo takes the user's back to the home/landing page as is industry standard and a users current bag is displayed at all times.

2. Account management - Allows users to sign up, verify and manage their account. Including logging in if already registered and to view previous/past orders. Allows users to also safely and securely log out to ensure their security, powered by django allauth.

3. Stripe payments - Allows users to purchase/checkout their currently bagged items securely through a third party payment system. 

4. Product searching - Allows users to search for key terms/words/phrases to filter products and narrow their search. This helps provide a more direct service and good UX

5. Product filtering - Allows users to sort products by price both ascending and descending and also by rating and by name.

#### Future Feature Ideas

1. Internal Keto informational page - This will allow Ketogenius to author and create informational content regarding the Keto diet, factual content, opinion based editorial pieces and testimonials of current and previous users of the site.

2. Interactive Reviews - this feature will allows other users aside from the original creater the option/ability to leave their own reviews of products that are listed for sale. This will provide the community with more varied and a wider range of information and opinions.

3. Keto recipe page - This will allow users to view and recreate Ketogenius' favourite recipes. With dedicated pages/tabs for individuals needs including weight loss, muscle gain, gluten and dairy free etc.

## Technologies Used

* [HTML](https://html.spec.whatwg.org/#is-this-html5?) 
    * Used to write the fundamental content of the project

* [CSS](https://www.w3.org/TR/CSS2/)
    * Used to style the project

* [Bootstrap](https://getbootstrap.com/)
    * Used to style the project and create powerful customisable grid layouts

* [Python](https://www.python.org/)
    * Used to provide vast majority of content and allows for integration of databases and apps such as Django

* [Django](https://www.djangoproject.com/)
    * Used in conjunction with Python to create and integrate apps and features such as allauth

* [JQuery](https://jquery.com/)
    * Used to allow functionality of dropdown menus in conjunction with Materialize framework 

* [Stripe](https://stripe.com/en-gb)
    * Used to process and handle payments

* [AWS](https://aws.amazon.com/)
    * Used to host static files and media files

## Testing

#### Navigation Links/bar
1. **Expected Results**

        - All links should open their associate html file successfully from all pages. 
        - Site logo should navigate user back to index.html page/landing page.
        - Products link should open dropdown to enable option to sort items
2. **Reasons for testing**

        - User performs extensive testing on this feature as this is the user's main port of call for navigating through the site.
        - If links are broken then user is unable to access full content.
3. **Tests performed**

        - To test links are working correctly and are opening appropriate HTML the user visits each link from each HTML page, ensuring that each link opens appropriate file and can navigate the entire site via each page.
        - To test logo is directing users back to index.html the user clicks this logo from each page and ensures that they are redirected back to the landing page.
4. **Testing Results**

        - Each link opened the appropriate page when clicked on from each html page as intended.
        - Clicking logo from each page resulted in the user being directed back to landing page as intended.

#### Sign-Up/Login functionality

1. **Expected Results**

        - Password field should be encrypted and not displayed when entering password.
        - Upon signing up/logging in the user should be rdirected to the correct page asking them to confirm their email using the sent confirmation email
        - Upon signing up, user data including username and hashed password should be inserted into database.
        - Upon logging in the user should be redirected to the Ketogenius home page.
        - Upon logging out the user should asked to confirm if this is correct and if so be directed to home page
2. **Reasons for testing**

        - The ability to create an active and returning customer base is dependent on users being able to sign-up and login to log purchases etc. 
        - If a user has an issue when signing up they are unlikely to return to use the site. This is a bad user experience.
        - If a users password security is compromised this can cause data breaches and potentially break GDPR protocols.
3. **Tests performed**

        - Used dummy accounts to test login/sign-up process using temporary emails from [Generator.Email](https://generator.email/). 
        - Entered username and password field and then left field without entering value data to see if defensive programming would activate.
        - Confirmed email via temporary email address to ensure verification process and emails fired correctly.
        - Checked site for inserted data into correct and relevant fields upon signup.

4. **Testing Results**

        - Upon signing up/logging in. User is redirected to the home page as intended.
        - Upon signing up. New user data is inserted into appropriate database collection as intended.
        - When inputting/entering username/password if incorrect or unsuitable values are entered the form will not let the user continue with process as intended.
        - Upon signing out user was redirected to the appropriate page.
        - Upon signing up, verification email was sent and received. Confirmation link then completed sign-up process

#### Products - Search functionality

1. **Expected Results** 
        
        - When searching and submitting form, user should be presented with any data entries that meets search criteria via product information such as name, description etc. Picking up keywords and displaying the appropriate entries.
        - Upon resetting the search form all data/list entries should appear
        - When searching, if no results are found then a message should appear to show the user that their search hasn't yielded any results.
2. **Reasons for testing** 

        - Search functionality is incredibly important as to be a useful database the userbase needs to be able to filter results based on their desires and tastes. A poorly executed search function or one limited in scope will result in poor UX.
3. **Tests performed**

        - Searched for various terms that may or may not appear within the indexed fields. These varied from names of products to  keywords that may have been included in a product descritpion or name
        - After each successful search hit the products home button to test its functionality.
4. **Testing Results**

        - When searching, each time results/entries which were applicable appeared as intended.
        - Each hit of the products home button correctly cleared the search data and returned the intitally listed entries.
        - When searching for a term that wasn't present or applicable the correct message appeared to inform the user that their search garnered no results as intended. 

#### Products page 

1. **Expected Results** 
        
        - When loading, all products should appear in default arrangement as entered into database
        - All product images should load as intended and if product has no designated image the appropriate noimage.png should load
        - Drop down/sort option should result in correct display and product order depending on method chosen by user e.g. price, rating, name etc.
2. **Reasons for testing** 

        - The products page is the fundamental and most important page in creating and convincing users to become patrons of Ketogenius, without informative and enticing products users will not feel the need to purchase
        - Sort feature will allow users to filter and sort products in their preferred way, this increases user agency and provides superior UX
3. **Tests performed**

        - Loaded page to ensure products including image, price, rating etc loaded correctly
        - Created product with no image to ensure approriate default image loaded
        - Used sort option to sort products using all options both descending and ascending where possible
4. **Testing Results**

        - When loading, all products in database appear in correct order
        - All products load with associated rating, price and product information
        - When sorting by price ascending, products sort so that lowest price item appears first and highest appears last
        - When sorting by price descending, products sort so that lowest price item appears last and highest appears first
        - When sorting by rating ascending, products sort so that lowest rating item appears first and highest appears last
        - When sorting by rating descending, products sort so that lowest rating item appears last and highest appears first

#### Product details + bag page 

1. **Expected Results** 
        
        - When loading, the appropriate product description, price, rating etc should appear
        - User should have ability to change the desired quantity of the product before adding to bag
        - When product is added to bag, bag icon should update to show grand total of users current bag
        - When clicking on bag icon user should be directed to their bag showing all items that has previously added
        - When in bag, message should appear showing how much more is needed to be spent in order to qualify for free shipping
2. **Reasons for testing** 

        - Product details will seal the sale and provides functionality to begin the checkout process and purchase using Ketogenius
        - Users need the option to be able to add multiple items accross storefront to their bag before they decide to check out 
        - Good UX to provide updated and running total that customers can view while browsing storefront
3. **Tests performed**

        - Loaded each product page to ensure products including image, price, rating etc loaded correctly
        - Clicked on add to bag from each product using varying item quantities etc to ensure add to bag function works correctly
        - Checked that bag icon updated with the appropriate and correct total with each subsequent item added to bag
        - Clicked on bag to check that bag contents is accurate 
4. **Testing Results**

        - When loading, appropriate product and item information appears
        - When changing quantity of product and adding to bag, correct number of items is added and bag grand total updates correctly
        - When loading bag, the correct items as previously added with correct quantities and grand total are displayed

#### Checkout

1. **Expected Results** 
        
        - When on checkout page, all appropriate and required fields should be noted and checkout should not be able to be processed without this information
        - When on checkout page, an overview of users order should be displayed showing product image, costs and grand total
        - When on checkout page, user should have option to complete secure chckout using displayed form or go back to their bag contents
        - User should be able to save their address/personal information and if selected this info should be saved for further checkout
        - Once users click checkout they should be redirected to order page which displays a rundown of order and info that was provided
2. **Reasons for testing** 

        - Without a functional checkout page users won't be able to purchase from Ketogenius, given the importance of account and payment security. A bad payment experience or failed payment can result in users not trusting platform
3. **Tests performed**

        - Attempted to checkout with dummy bag of contents without using/inputting required fields
        - After visiting checkout page, went bag to products page and updated bagged contents, then went back to checkout page
        - When inputting checkout info, selected to save information.
        - Visited Stripe upon checking out with test card details to ensure successful payment was processed
        - Visited Stripe dashboard and processed test webhook
4. **Testing Results**

        - When loading, bagged contents appear in a summary showing product images and total cost of order
        - When attempting to check out, if required fields aren't entered then payment did not process as intended
        - Once processed payment, added a new bag contents and checked out again, previously inputted information was loaded for applicable user
        - When visiting stripe dahsboard, successful payment attempt was logged
        - When processing test webhook via Stripe dashboard, a successul webhook was logged

#### Product management

1. **Expected Results** 
        
        - If user is a superuser they should have the option to visit product management page via their profile dropdown
        - Prouct management page should display all neccessary fields in order to create a new product within the Ketogenius store
        - All required fields should be denoted
        - User should have ability to upload an image with their product which can be uploaded from their personal device
        - Once submitted the product should be listed on products page and within Ketogenius database
        - On product page if user is super user they should have ability to delete or edit current products
        - if edited, changes should display on products page and if deleted then product and linked info should be removed from storefront and database
2. **Reasons for testing** 

        - The ability to add, edit and delete products is essential in running a successful online store with the aim to create a lage database of items 
        - This option should only be available for admin and selected members of staff to ensure integrity of storefront and it's database
3. **Tests performed**

        - Created multiple test products using specified data and information, tested required fields by attempting to create new products without entering this data
        - Checked products page and searched using keywords to ensure these new entries and products were logged
        - Checked admin database to make sure data and fields were input into correct database field
        - Visited Products page and deleted/edited newly created products to ensure edits/deletion were processed successfully
        - Logged in using both superuser and non superuser account to ensure that these options were only available to accounts that have been flagged as admin
4. **Testing Results**

        - After creating a new product listing, product appeared on products page and was findable via search function as intended. Information was also logged on admin database
        - When deleting a product the specified changes/deletion were represented on storefront and in database as intended
        - Product management and CRUD functionality of products page only available for admin user as intended


## Deployment
1. Throughout project development, use of 'git add' and 'git commit' functions within project terminal to save changes and document development process. Each commit message explains and shows changes since the last version and provides information to users viewing the repository.
2. Throughout development regular use of 'git push' function. This function pushes changed/new code to GitHub and ensures the code is safe and protected from potential loss or system/cloud error.
3. Integrated GitHub to Heroku platform. Each new commit and push of changes will now be represented on both GitHub repository and Heroku. This allows for seemless protection of data and a backed up workspace.
3. Once the project completed visit the repository via GitHub @ *https://github.com/GreigBenton/Milestone_project_3*
4. From here visit Settings to find deployment steps.
5. Scroll down to the GitHub pages section.
6. Ensure the master branch is selected and *Save*.
7. Project is now visible and live @ *https://github.com/GreigBenton/Milestone_project_3* **AND** *https://milestone-3-book-database.herokuapp.com/.*
8. Create bucket on AWS to host and contain sites static files and media content.
9. Integrate real emails via Googlemail.
10. Include config vars for emails and AWS on Heroku app.

#### Local Cloning
1. After downloading GitHub Desktop user logs into to their GitHub profile
2. Selects the repository and branch they wish to clone
3. Denotes the local path 
4. Clicks 'Clone'

#### Differences deployed and development version
1. No changes in deployed version to note

## Credits

#### Content
- Product information including price/rating and description taken from [Healthline](https://www.healthline.com/nutrition/keto-products#_noHeaderPrefixedContent)

#### Media
- Product images taken from same article as product information to create a seamless product page [Healthline](https://www.healthline.com/nutrition/keto-products#_noHeaderPrefixedContent)

## Inspiration 
- Inspiration was taken from various onlin stores that focus on a particular diet or way of living e.g. vegan or vegetarian. As I have previously suffered from health implications based on dietary needs and this was solved by changing to a largely no carb or Keto diet this site is inspired by my own personal journey over the last few years.

----
