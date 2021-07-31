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



## Deployment
1. Throughout project development, use of 'git add' and 'git commit' functions within project terminal to save changes and document development process. Each commit message explains and shows changes since the last version and provides information to users viewing the repository.
2. Throughout development regular use of 'git push' function. This function pushes changed/new code to GitHub and ensures the code is safe and protected from potential loss or system/cloud error.
3. Integrated GitHub to Heroku platform. Each new commit and push of changes will now be represented on both GitHub repository and Heroku. This allows for seemless protection of data and a backed up workspace.
3. Once the project completed visit the repository via GitHub @ *https://github.com/GreigBenton/Milestone_project_3*
4. From here visit Settings to find deployment steps.
5. Scroll down to the GitHub pages section.
6. Ensure the master branch is selected and *Save*.
7. Project is now visible and live @ *https://github.com/GreigBenton/Milestone_project_3* **AND** *https://milestone-3-book-database.herokuapp.com/.*

#### Local Cloning
1. After downloading GitHub Desktop user logs into to their GitHub profile
2. Selects the repository and branch they wish to clone
3. Denotes the local path 
4. Clicks 'Clone'