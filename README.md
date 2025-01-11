![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

------



# Health Store


## Introduction

Health Store is a web application for a fictional online shop that sells vitamins and supplements, healthy cooking ingredients and foods, natural beauty products, and eco-friendly home items to health-conscious customers.

This is the fifth and last Portfolio Project for the Code Institute's Diploma Course in Full Stack Software Development (E-commerce Applications). The application is built in Django using Python, HTML, CSS, and JavaScript. It provides role-based permissions for users to interact with data in a PostgreSQL database. It includes user authentication, email validation, and CRUD functionality. The application is connected to Stripe in order to simulate online payments. An AWS account is used to store media and static files, and there is also a newsletter signup form connected to a MailChimp account.

[View the live website here](https://health-store-ff0f909bba3d.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![Screenshot of the application on multiple devices](link)


## Table of Contents



## UX

### The Strategy Plane

Health Store is a web application for a fictional online store selling products related to health and wellness, such as: vitamins and supplements, healthy foods, natural cosmetics, essential oils, eco-friendly candles, and other similar items.

Any user can access the most important parts of the website - the shop, product detail pages, the homepage, basket page (if there are any items in a user's basket), checkout page, and checkout confirmation page. Additionally, the application includes a blog where users can find articles and recipes supporting their healthy lifestyle, related to the items sold in the store. There is also a page displaying upcoming online events - free monthly webinars on health- and well-being-related topics with guest speakers. Any user can submit their details through a newsletter signup form in the footer to receive a discount code and gain access to exclusive special offers; since creating an email campaign exceeds the scope of this project, the newsletter itself is not included.

Any user can sign up for an account, and once they have verified their email and logged in, they are granted access to additional functionalities on the website. An authenticated user can "like" their favourite products, adding them to their wishlist in the user account for easy access. They can also bookmark any articles and recipes they like, save their personal and address details for a faster checkout, and register for an online event. In their account, they can also find all their past orders and see each order's details.

A staff user logged into their staff account has access to further functionalities, such as creating and editing an article/recipe for the blog.

An admin logged into their superuser account can additionally manage products, the homepage carousel, online events, articles/recipes on the blog, and product reviews waiting for approval.


#### The Site's Ideal User
- People who are health-conscious
- People who are interested in alternative medicine (herbalism, aromatherapy etc.)
- Vegetarians and vegans
- People with chronic health and well-being issues who want to supplement certain vitamins and minerals
- People who want to support environmentally-friendly businesses
- People with sensitive skin/skin issues who need gentle, natural products


#### Site Goals
- To carry and sell a range of high-quality, natural, and health-supporting products
- To provide an easy way for users to buy any products they might like
- To educate health-conscious users through the blog (articles) and online events
- To inspire and encourage users to keep taking care of their health (blog articles and recipes)
- To create a community of like-minded people through free monthly webinars
- To give users the opportunity to sign up to a newsletter and benefit from exclusive special offers
- To provide users with the opportunity to create a personal profile and use additional functionalities of the application for ease and convenience (faster checkout, a wishlist for favourite products, past orders, bookmarked articles and recipes)


#### Iterations (GitHub Milestones)
Since the project was created using the Agile approach, both planning and prioritizing accordingly was essential.

The work on this project has been divided into 3 iterations, where the 1st and 3rd iteration lasted for close to 4 weeks, and the 2nd iteration exactly 3 weeks. This made the entire process easier to manage and helped track progress as well as decide on the priorities at each stage.

- Iteration 1 - ended on Dec 1, 2024
- Iteration 2 - ended on Dec 22, 2024
- Iteration 3 - ended on Jan 12, 2025

You can see the iterations with their details, including User Stories that were finished in each iteration, [here](https://github.com/Agnieszka-21/health-store/milestones).


#### Epics
This project is based on the following 13 epics:
- [#1 Initial setup in Django](https://github.com/Agnieszka-21/health-store/issues/1)
- [#2 User profile](https://github.com/Agnieszka-21/health-store/issues/2)
- [#3 View products](https://github.com/Agnieszka-21/health-store/issues/3)
- [#4 "Favourite" products](https://github.com/Agnieszka-21/health-store/issues/4)
- [#5 Shopping basket](https://github.com/Agnieszka-21/health-store/issues/5)
- [#6 Checkout](https://github.com/Agnieszka-21/health-store/issues/6)
- [#72 Product reviews](https://github.com/Agnieszka-21/health-store/issues/72)
- [#52 Product management](https://github.com/Agnieszka-21/health-store/issues/52)
- [#9 Blog and webinars](https://github.com/Agnieszka-21/health-store/issues/9)
- [#56 Blog and webinar management](https://github.com/Agnieszka-21/health-store/issues/56)
- [#67 Homepage management](https://github.com/Agnieszka-21/health-store/issues/67)
- [#7 Web marketing](https://github.com/Agnieszka-21/namaste-django/issues/7)
- [#8 SEO](https://github.com/Agnieszka-21/namaste-django/issues/8)


These epics were split into User Stories to help manage the work on this project. All these and more details can be found in the project's [kanban board](https://github.com/users/Agnieszka-21/projects/3/views/1?sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Labels).


#### User Stories
Here are the User Stories resulting from the 13 epics

1. Initial setup in Django
- [#10 Create a new Django project](https://github.com/Agnieszka-21/health-store/issues/10)
- [#11 Install required packages](https://github.com/Agnieszka-21/health-store/issues/11)
- [#12 Create the first app](https://github.com/Agnieszka-21/health-store/issues/12)
- [#14 Deploy the project to Heroku](https://github.com/Agnieszka-21/health-store/issues/14)


2. User profile
- [#15 Create a user account (sign up)](https://github.com/Agnieszka-21/health-store/issues/15)
- [#16 Log into the user profile/account](https://github.com/Agnieszka-21/health-store/issues/16)
- [#17 Log out of the user profile/account](https://github.com/Agnieszka-21/health-store/issues/17)
- [#19 View a user profile/account](https://github.com/Agnieszka-21/health-store/issues/19)
- [#18 Edit the user profile/account](https://github.com/Agnieszka-21/health-store/issues/18)
- [#20 Delete a user profile/account](https://github.com/Agnieszka-21/health-store/issues/20) - see [Future Enhancements](#future-enhancements)
- [#21 SIgn in to the user profile/account using a social media login](https://github.com/Agnieszka-21/health-store/issues/21) - see [Future Enhancements](#future-enhancements)


3. View products
- [#22 View all products](https://github.com/Agnieszka-21/health-store/issues/22)
- [#23 Filter products based on category](https://github.com/Agnieszka-21/health-store/issues/23)
- [#24 Sort products based on specific criteria](https://github.com/Agnieszka-21/health-store/issues/24)
- [#25 Search for a specific product](https://github.com/Agnieszka-21/health-store/issues/25)
- [#26 View a specific product with a high level of detail](https://github.com/Agnieszka-21/health-store/issues/26)
- [#64 Optimize user experience on the shop page (pagination, back-to-top link)](https://github.com/Agnieszka-21/health-store/issues/64)

4. Favourite products
- [#27 Mark and save a product as "favourite"](https://github.com/Agnieszka-21/health-store/issues/27)
- [#28 View your wishlist/"favourites"](https://github.com/Agnieszka-21/health-store/issues/28) 
- [#29 Remove a product/products from your wishlist](https://github.com/Agnieszka-21/health-store/issues/29)

5. Shopping basket
- [#30 Add a product/products to the basket](https://github.com/Agnieszka-21/namaste-django/issues/30)
- [#31 View the basket](https://github.com/Agnieszka-21/namaste-django/issues/31)
- [#32 Remove a product/products from the basket](https://github.com/Agnieszka-21/namaste-django/issues/32)
- [#33 Adjust the quantity of a product/products in the basket](https://github.com/Agnieszka-21/namaste-django/issues/33)
- [#34 Save the shopping basket for later](https://github.com/Agnieszka-21/namaste-django/issues/34) - see [Future Enhancements](#future-enhancements)
- [#35 Proceed to checkout](https://github.com/Agnieszka-21/namaste-django/issues/35)
- [#63 Keep the existing basket when logging in](https://github.com/Agnieszka-21/namaste-django/issues/63) - see [Future Enhancements](#future-enhancements)

6. Checkout
- [#36 Create a user account during a checkout process](https://github.com/Agnieszka-21/namaste-django/issues/36) - [Future Enhancements](#future-enhancements)
- [#37 Provide personal details needed in the checkout process](https://github.com/Agnieszka-21/health-store/issues/37)
- [#38 Pay for the items in the shopping basket](https://github.com/Agnieszka-21/health-store/issues/38)
- [#39 Receive an order confirmation](https://github.com/Agnieszka-21/health-store/issues/39)

7. Product reviews
- [#73 View reviews](https://github.com/Agnieszka-21/health-store/issues/73)
- [#74 Create a product review](https://github.com/Agnieszka-21/health-store/issues/74)
- [#75 Edit a review](https://github.com/Agnieszka-21/health-store/issues/75)
- [#76 Delete a review](https://github.com/Agnieszka-21/health-store/issues/76)
- [#77 Manage reviews awaiting approval](https://github.com/Agnieszka-21/health-store/issues/77)

8. Product management
- [#53 Add products](https://github.com/Agnieszka-21/health-store/issues/53)
- [#54 Edit a product](https://github.com/Agnieszka-21/health-store/issues/54)
- [#55 Delete a product](https://github.com/Agnieszka-21/health-store/issues/55)

9. Blog and webinars
- [#48 View/read a blog with articles and healthy recipes](https://github.com/Agnieszka-21/health-store/issues/48)
- [#49 Save an article/recipe to a user profile](https://github.com/Agnieszka-21/health-store/issues/49)
- [#50 Sign up to a webinar on health- and wellness-related topics](https://github.com/Agnieszka-21/health-store/issues/50)
- [#51 Copy the URL of an article/recipe with one click for easy sharing](https://github.com/Agnieszka-21/health-store/issues/51)

10. Blog and webinar management
- [#57 Add a blog article/recipe](https://github.com/Agnieszka-21/health-store/issues/57)
- [#58 Update a blog article/recipe](https://github.com/Agnieszka-21/health-store/issues/58)
- [#59 Unpublish an article/recipe on the blog](https://github.com/Agnieszka-21/health-store/issues/59)
- [#60 Add an online event(webinar)](https://github.com/Agnieszka-21/health-store/issues/60)
- [#61 Edit an online event (webinar)](https://github.com/Agnieszka-21/health-store/issues/61)
- [#62 Delete a webinar](https://github.com/Agnieszka-21/health-store/issues/62)
- [#65 Cancel an upcomming webinar](https://github.com/Agnieszka-21/health-store/issues/65)

11. Homepage management
- [#68 Create a new carousel](https://github.com/Agnieszka-21/health-store/issues/68)
- [#69 Edit a carousel](https://github.com/Agnieszka-21/health-store/issues/69)
- [#70 Delete a carousel](https://github.com/Agnieszka-21/health-store/issues/70)
- [#71 Activate a carousel so that it is displayed on the homepage](https://github.com/Agnieszka-21/health-store/issues/71)

12. Web marketing
- [#40 Sign up for the newsletter](https://github.com/Agnieszka-21/health-store/issues/40)
- [#41 Unsubscribe from the newsletter](https://github.com/Agnieszka-21/health-store/issues/41) - [Future Enhancements](#future-enhancements)
- [#42 Re-subscribe to the newsletter](https://github.com/Agnieszka-21/health-store/issues/42) - [Future Enhancements](#future-enhancements)
- [#78 Create a business Faceboook page](https://github.com/Agnieszka-21/health-store/issues/78)

13. SEO
- [#43 Create a sitemap](https://github.com/Agnieszka-21/health-store/issues/43)
- [#44 Create a robots.txt file](https://github.com/Agnieszka-21/health-store/issues/44)
- [#45 Research and apply suitable keywords](https://github.com/Agnieszka-21/health-store/issues/45)
- [#46 Link pages internally](https://github.com/Agnieszka-21/health-store/issues/46)
- [#47 Use external links to other established businesses](https://github.com/Agnieszka-21/health-store/issues/47)
- [#66 Customize the keywords meta tag for blog pages](https://github.com/Agnieszka-21/health-store/issues/66)


#### Story Points
Each User Story was given two labels:
- one that that specifies story points used to estimate how much time is needed to complete it,
- and one that marks its type according to MoSCoW prioritization.

Story points are based on a predictive comparison of User Stories' complexity and the expected workload required to complete them. The simplest User Stories were given just 1 story point, the ones that needed a little more attention 2 story points, then 4 points for the ones that required even more time to be completed, and 8 for the most complex features and functionalities.

Altogether, user stories mapped out for this project take up 180 story points. This number includes the user stories that have not been handled, labelled "won't-have" (potential future enhancements), which take up 22 story points. User Stories marked with the label "must-have" have a total of 104 points, which is close to 58%, so below 60% as recommended. The remaining User Stories, all of which have been completed, are marked with a "should-have" or "could-have" label.

#### MoSCoW Prioritization

Each User Story has been marked with one of the following labels:
- must-have,
- should-have,
- could-have,
- won't have.

Using these labels allowed for a clear understanding of what needs to be prioritized in terms of necessary features, and what is simply optional or can be added later as a nice-to-have functionality. User Stories marked with the "must-have" label make up less than 60% of all story points.


### The Scope Plane

__Features planned include:__
- Viewing all products or a subset of products (filtered by category)
- Sorting products by price, rating, name
- Searching for a product by typing a keyword in a search bar
- Viewing each product with a high level of detail
- Viewing any existing product reviews
- Adding products to a shopping basket in a desired quantity
- Going to a checkout page and completing the checkout process, including payment
- Logging in to a user account
- Logging out of a user account
- Resetting password to a user account
- User profile - create, read, update, delete
- Viewing blog posts and recipes
- Viewing upcoming online events (webinars)

__Users need to be logged in__ to use previously saved details (personal and address) during checkout, add a product to their wishlist, bookmark a blog article/recipe, manage their wishlist and bookmarked articles/recipes, view all their past orders, register for an online event, and add a product review.

__Staff users__ need to be logged into their staff account in order to create/edit blog articles and recipes.

__Admins__ need to be logged into their superuser account in order to access the Admin Panel page in the Account dropdown menu and have permission to: create/edit/delete a product, approve/delete a review, create/edit/unpublish an article or recipe, create/edit/delete/cancel an online event, create/edit/delete/activate a homepage carousel.


### The Structure Plane

---

#### View ....

[User story #2:  ](link)
As a User (Client), I would like to view the studio's class schedule, so that I can check if I am interested in and able to attend any classes offered.

__Acceptance Criteria__
- Given that I am a User (Client), when I navigate to the studio's schedule page, then I can see the current schedule without having to register or log in.

__Implementation__
- Create models YogaStyle, StyleDescription, and GroupClass
- In the admin panel, set up data related to these models as needed to create GroupClass objects
- Create a view which lists all group classes, and a template for Schedule page which extends base.html

---

---

#### Opportunities arising from User Stories

| Opportunity | Importance | Viability/Feasibility |
| :---------- | :--------- | :------------- |
| Provide users the ability to access the website on any device | 5 | 5 |
| Provide users the ability to access the main part of the application (shop) without having to log in/register | 5 | 5 |
| Provide users the ability to view each product in detail | 4 | 4 |
| Provide users the ability to view product reviews without having to log in | 5 | 5 |
| Provide users the ability to add products to their shopping basket in a desired quantity without having to log in | 5 | 5 |
| Provide users the ability to proceed to checkout and adjust their order if needed | 5 | 5 |
| Provide users the ability to pay for their items and place the order without having to log in | 5 | 5 |
| Provide users the ability to access the blog and events page without having to log in | 5 | 4 |
| Provide users the ability to create an account | 5 | 5 |
| Provide users the ability to view their profile when logged in | 5 | 5 |
| Provide users the ability to update their profile details when logged in | 5  | 5 |
| Provide users the ability to manage data in their account when logged in | 5 | 5 |
| Provide users the ability to view their past orders when logged in | 5 | 5 |
| Provide users the ability to view and manage their wishlist when logged in | 4 | 4 |
| Provide users the ability to view and manage their bookmarked articles/recipes when logged in | 3 | 3 |
| Provide users the ability to register for an upcoming online event when logged in | 5 | 5 |
| Provide users the ability to submit a product review when logged in | 5 | 5 |
| Provide users the ability to see the store's Privacy Policy | 5 | 4 |
| Provide users the ability to sign up for a newsletter | 4 | 4 |


### The Skeleton Plane

#### Wireframe mock-ups

__Home page__

The home page provides the user with a clear picture as to the purpose of the site. Under the hero carousel of images showcasing typical products that Health Store sells, there is a clear call to action for the user to go to the shop, with a large button in the center of the page that links directly to the Shop page. At the very top, there is a mimimalistic banner that encourages users to sign up to the newsletter in order to get a discount code for their first purchase - the words "sign up" are a link to the form, present in the footer. There is also a navigation bar at the top of the page with the menu and a search bar, and a footer including social media links, a link to the Privacy Policy page, and a newsletter sign-up form - these elements are visible on all pages.

![Wireframe of the Home page - large screen]()

__Shop page__

The Shop page contains the title ("Products"), 2 dropdowns ("Filter", "Sort"), and a list of all products offered by the store. Each listed product is shown as a card, presenting the most important information like product image, its name, price, category, and average rating. Both the image and the title of each product are clickable links that lead to a detail page for that specific product, should the user be interested in checking out more details. At the bottom of each card, there is also an "Add" button (or "Add to basket" on larger screens) for users who do not need any additional information. The Shop page uses pagination to display 8 products at a time.

![Wireframe of the Shop page - large screen]()

__Product Detail pages__

Each product listed on the Shop page leads to its own page where user can find the product's name and price, a detailed description, its ingredients (if applicable), its category, and brand. There is also an average product rating shown, if present, and a field where user can choose the quantity of the product, should they choose to add it to their basket by clicking the "Add to basket" button below. Underneath all that, there is a section displaying any existing reviews for the product, and a button with a call to action: "Log in to leave a review". For logged in users, instead of the button there is a review form they can fill to submit their rating and an optional comment.

![Wireframe of the Product Detail page - large screen]()

__Basket__

This page is accessible to all users. It lists all items currently present in a user's basket (if there are any), including each product's basic information and details regarding quantities, which can be adjusted and updated. Any of the listed products can also be removed completely. Underneath, the basket total, delivery fee, and grand total payable amount are displayed, alongside with the information on how much more one needs to spend to qualify for free delivery. 2 buttons at the bottom of the page let the user decide whether they want to keep shopping, or proceed to checkout.

![Wireframe of the Basket page - large screen]()

__Checkout__

This page is also accessible to all users. It displays a checkout form that has to be filled with personal details (name and email), delivery details (address) and payment details that are processed by Stripe. There is also a list of all items that the user is about to buy and a summary of the order (order total, delivery feel, grand total).

For logged in users, there is also a checkbox under the delivery section of the form that can be checked if the user wishes to save their information to the profile. If they saved their personal and address data in the past, the checkout form is pre-filled.

![Wireframe of the Checkout page - large screen]()

__Checkout Success page__

This page, visible to any user upon placing their order successfully, displays any order details, including order number, basket items, and payment information. This is a confirmation that the order has been processed. Below all the order details, there is a button leading the customer back to the store.

![Wireframe of the Checkout Success page - large screen]()

__Account__

This page can be accessed only if user is logged in. Each user can see here a form for their personal and address details, which are used to simplify and speed up the checkout process. If any data has already been saved during a previous checkout (customer can choose this option), the form is pre-filled with the saved data. The data in the form can be updated anytime by changing the desired details in the form and clicking the "Update information" button below.

There are also 3 cards on this page: one for "Order history", one for "Wishlist", and one for "Bookmarked articles/recipes". These cards link user to further pages where they can see a table with their past orders, further leading them to each order's confirmation details, access and manage the list of their favourite items, as well as access and manage their lists of saved articles and recipes.

![Wireframe of the Account page - large screen]()

__Blog__

This page can be accessed by all users and shows 2 options to choose from: one is a link leading to the page listing all blog articles, and the other is a link leading to the page listing recipes. 2 large images are used as backgrounds for these 2 options.

![Wireframe of the Blog page - large screen]()

__Articles page, Recipes page__

These 2 pages are very similar to one another and they display a list of all published articles/recipes, with a thumbnail image and a title as a link to the detail page for each blog post.

![Wireframe of the Articles page - large screen]()

__Article Detail, Recipe Detail__

These 2 pages display a particular article or recipe. 

For an __article__, there is a title (heading), information on when the post was published, a link icon for copying the URL with one click, and - for loged in users - a bookmark icon that allows user to save the article to their account. Underneath, a banner image for the post is displayed, followed by the article's content. At the bottom of the page, there is a section showcasing related products from the store, if such information has been added to the article. Each product is displayed as an image and a name, both of which are clickable links leading user to this product's detail page. In the bottom right corner, there is also a button that can take user back to the page listing all published articles.

For a __recipe__, the structure of the detail page is only slightly different. Instead of one block of content, the text for each recipe is divided up into an intro, an ingredients section, and a method section. Apart from that, everything else is the same.

![Wireframe of the Article detail page - large screen]()
![Wireframe of the Recipe detail page - large screen]()

__Events__

This page can be accessed by all users and shows a list of all upcoming events. Past events are not shown by default. Each event is a card displaying the event's title, information on when it takes place, who the guest speaker is, and a short description. For unauthenticated users, a "Log in to register" button is shown for each event, and for logged-in users, a "Register" button. By clicking the "Register" button, user is taken to a new page with the particular event's details where they are asked to either confirm their decision with "Register" or to cancel, which sends them back to the Events page. If the user registers for an event, a confirmation email is sent to them.

![Wireframe of the Events page - large screen]()


__Wireframes for mobile devices__

Wireframes were also produced for each major page for mobile devices since the intention was to make the site fully responsive so that it displays correctly regardless of the user's screen size. These wireframes were created before the ones for large screens (because of the mobile-first approach to design) and therefore depict an earlier version of the project, which evolved with time as the development process was progressing.

See the mobile wireframes below:

| Homepage | Shop page | Product detail page |
| :------------------- | :--------------- | :------------- |
| ![Homepage mobile wireframe]() | ![Shop page mobile wireframe]() | ![Product detail mobile wireframe]() |

| Schedule detail | User profile page | My bookings page |
| :------------------- | :--------------- | :--------------- |
| ![Blog mobile wireframe]() | ![Recipe detail mobile wireframe]() | ![Article detail mobile wireframe]() |

| Schedule detail | User profile page | My bookings page |
| :------------------- | :--------------- | :--------------- |
| ![Basket mobile wireframe]() | ![Account mobile wireframe]() | ![Events mobile wireframe]() |


#### Database schema

A few custom models were predicted to be required when building the site. Built-in Django AllAuth with its User model was applied for the user authentication system, removing the need to build a custom User model. However, a custom Profile model was required in order to gather and maintain additional information like a profile image uploaded by the user, as well as information on their date of birth and recent or chronic injuries - if they wished to add these. These 2 models were used throughout the User Profiles app.

In the Schedule app, there are more custom models, some of them linked to the User model. The Yoga Styles and Style Description are simple models which define options to choose from for the Group Class model that stores information on the weekly group classes. The "title" column uses the Yoga Style model as its Foreign Key, while the "description" column has the same relationship to the Style Description model. Further details are declared as choices for a CharField or an IntField, or as a direct input in a form or within the admin panel (e.g. for the datetime field - "first class" column, or the "image" column - CloudinaryField upload).

The next two models, Repeated Event and Event Occurrence, are a result of using the Django-Eventtools library, which was applied to create specific datetimes for each weekly class, needed for the Booking model and the Specific Group Class model.

The Booking model utilises Group Class and User models as its Foreign Keys (for the "chosen class" column, and the "client" column). It gathers and maintains information regarding each specific booking, including whether or not it was cancelled, and storing a cancellation reason based on how the booking was cancelled.

The Specific Group Class model is directly connected only to the User model (many-to-many relationship to store a list of participants' names for each specific class). However, through the use of suitable logic in views, it "inherits" indirectly information regarding the "specific title" column from the Group Class, and for the "specific datetime" column from the Django-Eventtools models (datetime chosen by user on the book class page).

You can see the models and the relationships between them in the following database schema, created using the [drawSQL app](https://drawsql.app/).

![Database schema]()


### The Surface Plane

#### Design
The design of the website is simple, minimalistic, and coherent. It is supposed to convey ease, simplicity, and make the end-user feel both grounded and welcome.

The color palatte is based on earthy and neutral tones.

The main color - walnut brown - has been used throughout the page in the navbar and footer, and also on hover/select for elements like buttons and links to emphasise their active state. It is a neutral shade often associated with earth and nature, which can convey the message of the studio: we are here to help you feel calm, relaxed, and grounded.

The main background color of the page is an off-white color #f7f7f7. Since most of the text is pure black (#000), it provides a good contrast while being gentler on the eyes and matching the natural theme of the color palette.

There is also pure white color (#fff) used as background for cards on the Schedule page and My bookings page, so that the cards are clearly discernible from the off-white background but without creating too much contrast, which could result in distraction and overwhelm.

Elements that are links or made to look like links use the eye-catching "office-green" color (#008000), and the font-weight is bold to ensure plenty of contrast with the background since these are elements that the end-user will interact with.

The following table created with [Contrast Grid](https://contrast-grid.eightshapes.com/) shows the color palette utilised in this project.

![Contrast Grid color palette]()


#### Typography
Two types of Google fonts have been used in this project.
For the brand name shown in the top left corner of each page, "Namaste", the Nova Mono font was used to provide an eye-catching design. Since this is a monospace font, monospace was also declared as a fallback font-family in style.css.

Lato font-family was used for all remaining text, in various weights ranging from 400 to 800. This is a sans-serif font, easily readable, light and simple, which matches the website's overall feel of being easy to navigate, minimalistic, and accessible for anyone. 


#### Images
Images of yoga classes used on this website are free-licence images from Pexels. Most of them come from the same suite of images by Yan Krukau, providing a coherent feel and look, and conveying to the end-user the real character of the yoga studio, giving them insights into the environment and the community of yoga practicioners. The hero image was also the starting point for creating the color palette for the website, with the walnut brown found directly in the image through a color picker tool.


## Features

### Homepage

__Navigation bar__

The navigation bar is shown in 2 versions, depending on whether the user is logged in or not. For a user who is not logged in, it lists Home, Schedule, Sign up, and Log in.

![Navbar - user not logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/navbar_not_logged_in.png)

For a logged in user, it shows the following options: Home, Schedule, My profile, My bookings, and Log out.

![Navbar - user logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/navbar_logged_in.png)

__Hero section__

The hero section consists of a responsive full-width background image, a black semi-transparent overlay for optimal contrast, and white text "Welcome to the friendliest yoga studio in Dublin" followed by a button with the call to action "See our class schedule", which redirects the user to the Schedule page. This way the purpose of the page is clear right away - to invite user to check out the offer of yoga classes so they can book the ones that they find interesting.

![Hero section](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/home_hero.png)

__Embedded Google maps__

Underneath the hero section, the user can find general information about the studio, including an embedded Google map with a pin showing the exact location of the studio.

![Google maps, address, and opening hours](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/home_map_info.png)

__Address and opening hours__

Next to the map (or below on tablet and phone screens), there is information on the studio's address and its opening hours - easily accessible to anyone visiting the page. See the previous screenshot.

__Footer with social icons__

The footer includes links to social media pages of the studio, which open in a new tab each. It also has a copyright section at the very bottom.

![Footer](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/footer.png)


### Schedule page

__Banner image and call-to-action heading__

An image depicting a group of people practising yoga in a class, and below the heading with a call to action: "Find the perfect class for you!".

![Schedule page banner and heading](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_banner_heading.png)

__List of all weekly classes (cards)__

The classes are listed grouped by weekday, starting with Monday, and ordered according to their start time. A calendar icon from Font Awesome and a short name of each weekday visually divide the list for enhanced user experience and clarity. Each class is shown as a card which presents the most important details, and the class title is a link that leads directly to the detail page for the class. Class titles are also tabbable, ensuring that the entire website is accessible for keyboard users.

![Schedule list](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_list.png)


### Schedule detail pages

__Image__

For added visual interest, there is an image of a yoga class. The images differ depending on the style of yoga taught in the class to give the user an idea of what is done in the class or who it is for. The images can be uploaded to Cloudinary through the admin panel when creating/updating a group class.

![Schedule detail page - user not logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_det_not_logged_in.png)

__Class details__

Title, instructor, description, weekday, start time, and duration are all shown next to the class image. They are visually coherent yet separate from one another to ensure that the user finds the information they need the most without feeling overwhelmed by details (see the previous screenshot).

__Show bio link and modal__

Next to the instructor's name, there is a "Show bio" span that can be selected (by a mouseclick or with Tab key) to open a modal that houses a short bio of the instructor. In the modal, there is also a "close" button - if you click the button (or anywhere outside of the modal), the modal will be closed. To ensure that the page is fully accessible, JavaScript was used to handle the modal functionality, including trapping focus in the modal when it is open.

![Teacher bio modal](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/teacher_bio_modal.png)

__Book now button__

Shown only for logged in users, when selected, it takes the user to the "Book class" page. For users who are not logged in or do not have an account yet, there is a link to the log in page instead.

![Schedule detail page - user logged in](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/schedule_det_logged_in.png)


### Book class page

__User form__

Pre-filled and uneditable. Contains the following details: the logged-in user's first name, last name, and email address.

![Book class page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_page.png)

__Booking form__

Contains a dropdown with available dates - the next 3 available occurrences of the weekly group class to choose from.
It also has a checkbox to "sign" the studio's liability waiver, which is required so that the class can be booked.

![Waiver not signed](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/waiver_signed_required.png)

If the booking is successful, the user is redirected to the Schedule page (to encourage the user to check out other classes) and shown a success message.

![Booking successful](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/booking_success.png)

Should the chosen class be already fully booked, the following message is shown:

![Booking failed - class already full](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_fail_full.png)

In the event when the user tries to book the exact same class that they have already booked (same group class on the same date and time), they are informed that they have already booked a place in this class and prevented from making a duplicate booking (each user is allowed to book a class only for themselves, so they receive exactly one spot in each class they book).

![Booking failed - duplicate exists](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/book_class_already_booked.png)

__"Read the waiver here" link and modal__

Under the checkbox, there is a span "Read the waiver here" that opens a modal with the studio's liability waiver. In the modal, there is also a "close" button - if you click the button (or anywhere outside of the modal), the modal will be closed. To ensure that the page is fully accessible, JavaScript was used to handle the modal functionality, including trapping focus in the modal when it is open.

![Waiver modal](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/waiver_modal.png)


### My profile page

This page shows the following information: a profile image (either one uploaded by the user, or the default image), the user's full name and email address, and then their additional information like date of birth and chronic/recent injuries. There is also a button "Edit profile" that brings the user to the Edit profile page.

![My profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_profile_page.png)


### Edit profile page

![Edit profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_profile_page.png)

This page contains a profile form where the user can update the following details: their date of birth, their information about injuries, and their profile image. All these elements are optional and can be left blank (a default picture is used as a profile image in this case). At the bottom of the form, there are 2 buttons: "Save profile" and "Discard changes". The latter simply redirects the user back to their profile page. The "Save profile" button saves the changes, redirects the user to the profile page, and shows the following success message:

![Edit profile - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_profile_success.png)


### My bookings page

The user can see here a list of their booked classes, but only the ones that are upcoming in the future to ensure that no changes are made to the classes that are in the past or taking place in that exact moment. Each class is shown as a card with 2 buttons - Edit booking, and Cancel booking.

![My bookings page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_bookings.png)

If the user has no upcoming bookings, the page informs them about that and a button with the call to action "Book your next class" is shown that redirects the user to the Schedule page so that they can choose and book their next class easily.

![My bookings page with no upcoming classes](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/my_bookings_page_empty.png)


### Edit booking page

The user can change here the date of their class. A dropdown like the one on the "Book class" page is shown, with the next 3 dates of the weekly class. There are also 2 buttons: "Save changes" which leads to the outcomes described below, and "Discard changes" which simply redirects the user to their "My bookings" page.

![Edit booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_page.png)

If the user could be added to the specific class on the new date they chose, a success message is shown and they are redirected to the "My bookings" page.

![Edit booking - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_success.png)

If the specific class on the new date chosen by the user is already fully booked, they are informed that their booking could not be updated for that reason. The user can still choose a different date from the dropdown and try again.

![Edit booking - class already full](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_fail_full.png)

If the specific class on the new date chosen by the user is already one of that user's booked classes, they are informed about that, redirected to their "My bookings" page, and prevented from creating a duplicate booking.

![Edit booking - class already booked](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/edit_booking_duplicate_found.png)


### Cancel booking page

The user can cancel here their upcoming class. The page re-confirms that the user wants to cancel their booking. There are 2 buttons, similarly to the "Edit booking" page: "Yes, cancel my booking" and "No, I changed my mind". 

![Cancel booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/cancel_booking_page.png)

If the latter is seleted, the user is simply redirected back to their "My bookings" page. If the user does go ahead with the cancellation, they are shown a success message and are redirected to the "My bookings" page.

![Cancel booking - success](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/screenshots/cancel_booking_success.png)


### Sign up page
The Sign Up option in the navigation menu is shown when user is not logged in. This page presents a sign up form, allowing the user to create an account and therefore access further features.

![Sign up page]()


### Log in page
The Log In option in the navigation menu is shown when user is not logged in. This page presents a log-in form, allowing the user to log into their account and access further features.

![Log in page]()
![Log in success]()


### Log out page
The Log Out option in the navigation menu is shown when user is logged in. This page asks for a log-out confirmation, allowing the user to log out of their account and keep their personal data safe.

![Log out page]()
![Log out success]()


## Future Enhancements

While the following User Stories have not been completed as they have been deemed unnecessary for an MVP, they present a wide range of potential enhancements that could be added to the project in the future.

- [#20 Delete a user profile/account](https://github.com/Agnieszka-21/health-store/issues/20) - so that User (Customer) can remove their account if they think they are not going to need it anymore
- [#21 Sign in to the user profile/account using a social media login](https://github.com/Agnieszka-21/health-store/issues/21) - so that users can utilise their existing login credentials for easy authentication
- [#34 Save the shopping basket for later](https://github.com/Agnieszka-21/health-store/issues/34) - so that the basket does not get lost the moment the user closes the tab with their basket
- [#36 Create a user account during checkout](https://github.com/Agnieszka-21/health-store/issues/36) - so that new user can easily and quickly create an account
- [#63 Keep the existing basket when logging in](https://github.com/Agnieszka-21/health-store/issues/63) - so that users with an existing account can log in and benefit from a pre-filled checkout form for convenience
- [#41 Unsubscribe from the newsletter](https://github.com/Agnieszka-21/health-store/issues/63) - so that the email campaign is GDPR compliant (this requires actually creating a newsletter campaign though)
- [#42 Re-subscribe to the newsletter](https://github.com/Agnieszka-21/health-store/issues/63) - similar to the above.

Another possible enhancement could be handling stock data and using that information to automatically update the maximum quantity of a product available for purchase for any one customer.


## Testing

### Testing Overview

Continuous testing was an integral part of the development process. I used numerous print statements, which were removed as specific features reached their desired shape and functionality. The statements helped me follow what is happening, especially in the more complex scenarios where multiple things were affected by just one change (e.g. when booking a class, cancelling, or updating a booking) and where multiple functions worked together, calling one another and handling a wide range of scenarios. 

While there is still a significant potential for further enhancements in a project as complex as this one, I ensured to handle any and all errors that I encountered, and took great care to minimise the risk of any errors occurring on submission of forms. Validation was often handled at the earliest stages while developing the forms, limiting the end-users' access to information that can be handled in the backend, in a more secure way (e.g. date input in the booking and update booking forms, name and email not editable by the end-user after the user signs up for an account, or the "waiver signed" field in the booking form being required and a simple checkbox).

Manual tests were conducted mainly in my development environment, and once results were positive, they were re-checked within the live application after it was deployed to Heroku. 

Automated tests were also written to confirm that each view renders the correct template, to ensure that views restricted to logged-in users only redirect the user to the log in page, and many more.


### Manual Testing

While testing every single functionality as I was creating and refining it was essential to progressing with this project, I also applied a more structured approach to testing once everything seemed to work correctly in order to double-check the code's behavior and ensure that I handled any possible scenarios to avoid any issues. The table below documents this more structured approach, where I tested all possible functionalities as well as likely user inputs in [the live version of the app](https://namaste-yoga-studio-d494d1aeeada.herokuapp.com/).


| Functionality being tested | Expected Outcome | Actual Outcome | Result (pass/fail) |
| :------------------------- | :--------------- | :------------- | :-------------------- |
| Logo "Namaste" | takes the user to the homepage when selected on any page | as expected | pass |
| Navbar link "Sign up" | takes the user to the Sign up page | as expected | pass |
| Navbar link "Log in" | takes the user to the Log in page | as expected | pass |
| Navbar link "Schedule" | takes the user to the Schedule page | as expected | pass |
| Navbar link "My profile" | takes a logged-in user to their profile page | as expected | pass |
| Navbar link "My bookings" | takes a logged-in user to their bookings | as expected | pass |
| Navbar link "Log out" | takes a logged-in user to the log out page | as expected | pass |
| Footer: Facebook icon | opens Facebook in a new tab | as expected | pass |
| Footer: Instagram icon | opens Instagram in a new tab| as expected | pass |
| Footer: YouTube icon | opens YouTube in a new tab | as expected | pass |
| Sign up page: "Sign up" button | creates a user account & profile, sends a verification email, redirects the user to the homepage and shows a suitable message | as expected | pass |
| Sign up page: "log in" link | redirects the user to the Log in page | as expected | pass |
| Log in page: "sign up" link | redirects the user to the Sign up page | as expected | pass |
| Log in page: "Log in" button | logs the user into their account, redirects them to the homepage, shows a success message | as expected | pass |
| Log in page: "Forgot password" link | redirects the user to the Password Reset page | as expected | pass |
| Log out page: "Log out" button | logs the user out of their account, redirects them to the homepage, shows a success message | as expected | pass |
| Home: "See our schedule" button | redirects user to the Schedule page | as expected | pass |
| Schedule: class title links | redirect the user to a Schedule detail page for the chosen class | as expected | pass |
| Schedule detail: "Show bio" underlined text | opens the modal containing a particular instructor's bio | as expected | pass |
| Schedule detail: close icon inside the modal | closes the modal | as expected | pass |
| Schedule detail: "Log in to book the class" link | redirects user to the log in page | as expected | pass |
| Schedule detail: "Book class" button | redirects a logged-in user to the Book class page | as expected | pass |
| Book class page: "Read the waiver here" underlined text | opens the modal containing the studio's liability waiver | as expected | pass |
| Book class page: close icon inside the modal | closes the modal | as expected | pass |
| Book class page: "Available dates" dropdown | shows the next 3 dates for the chosen class | as expected | pass |
| Book class page: "Book class" button | if successful: creates a booking, redirects the user to the Schedule page, shows a success message; if not successful: shows a suitable message | as expected | pass | 
| My bookings: "Book your next class" button (shown only if there are no upcoming bookings) | redirects the user to the Schedule page | as expected | pass |
| My bookings: "Edit booking" | redirects the user to the Edit booking page | as expected | pass |
| My bookings: "Cancel booking" | redirects the user to the Cancel booking page | as expected | pass |
| Edit booking page: "Available dates" dropdown | shows the next 3 dates for the chosen class | as expected | pass |
| Edit booking page: "Save changes" button | if successful: updates the chosen booking, redirects the user to My bookings page, shows a success message; if class full: shows an error message; if class already booked on the new date: redirects to My bookings and shows an info message | as expected | pass |
| Edit booking page: "Discard changes" button | redirects the user to My bookings page | as expected | pass |
| Cancel booking page: "Yes, cancel my booking" button | cancels the chosen booking, redirects the user to My bookings, shows a success message | as expected | pass |
| Cancel booking page: "No, I changed my mind" button | redirects the user to My bookings | as expected | pass |
| My profile: "Edit profile" button | redirects the user to the Edit profile page | as expected | pass |
| Edit profile page: "Choose file" for the "Profile image" field | opens the File Explorer on the user's device | as expected | pass |
| Edit profile page: "Clear" checkbox for the "Profile image" field | when checked, on submission it removed the user's current profile image if they uploaded one earlier | as expected | pass | 
| Edit profile page: "Save profile" button | saves changes, redirects the user to My profile page, shows a success message | as expected | pass |
| Edit profile page: "Discard changes" button | redirects the user to My profile | as expected | pass |


### Validator Testing

__HTML__

The [W3C Markup Validation Service](https://validator.w3.org/) was used to check any html files containing custom code. All files are passed the validation test without errors - you can see relevant screenshots below:
- [home page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_home.png)
- [schedule page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_schedule.png)
- [schedule detail page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_schedule_detail.png)
- [signup page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_signup.png)
- [login page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_login.png)
- [logout page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_logout.png)
- [profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_profile.png)
- [edit profile page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_edit_profile.png)
- [my bookings page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_my_bookings.png)
- [edit booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_edit_booking.png)
- [cancel booking page](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/html_cancel_booking.png)

__CSS__

The style.css file containing custom styling for the application has been checked in the [W3C CSS Validation Service Jigsaw](https://jigsaw.w3.org/css-validator/) and has no errors - see the screenshot below:

![CSS validator test](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/css_no_errors.png)

__JavaScript__

[JSHint](https://jshint.com/) has been used to validate all JavaScript files in the application. The files returned no errors.
- [waiver.js - validattion result](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/js_waiver_validator.png)
- [bio.js - validation result](https://github.com/Agnieszka-21/namaste-django/blob/main/assets/validators/js_bio_validator.png)

__Python__

All Python files containing custom code have been run through the [Code Institute's Python linter](https://pep8ci.herokuapp.com/#) in order to ensure that they meet the PEP8 requirements/recommendations. No errors were found - you can find relevenat screenshots in [this folder]().


### Lighthouse and Webaim Wave Testing

The deployed website has been tested using both Lighthouse and WebaAim WAVE in order to ensure that it performs well and meets accessibility criteria. A vast majority of Lighthouse scores is in the optimal green range. However, it is worth noting that
...
...
using Google maps on the homepage, images uploaded to Cloudinary on other pages, as well as applying Bootstrap and Google Fonts has led to Best Practices scores being slightly lower. From the perspective of a business using this web application it made more sense to keep the map and Cloudinary storage rather than trying to get the best score and missing out on those valuable resources, so the decision was simple. 

In order to keep accessibility scores in the optimal range, I ensured to make the website fully-operational for keyboard users, including trapping focus in each modal while it is open (waiver.js and bio.js files) and adding tabindex to card titles on the Schedule page.

You can find screenshots with relevant results here for [Lighthouse](), amd here for [WebAim WAVE]().


### Responsiveness (tested with Chrome Dev Tools)

| Device tested | Site responsive >=700px |	Site Responsive <699px |Renders as expected |
| :------------ | :---------------------- | :--------------------- | :----------------- |
|Galaxy Fold | N/A | yes | yes |
|iPhone SE | N/A | yes | yes |
|iPhone 12Pro | N/A | yes | yes |
|Samsung Galaxy S8+	| N/A | yes	| yes |
|iPad Air | yes	| N/A | yes |
|Surface Pro 7 | yes | N/A | yes |
|Laptop 1440px | yes | N/A | yes |
|4K - 2560px | yes | N/A | yes |


### Browser compatibility testing

| Browser being tested | Section tested | Intended appearance | Intended responsiveness |
| :------------------- | :------------- | :------------------ | :------------------ |
| Chrome | Promo banner | good | good |
| Chrome | Navbar - unauthenticated user | good | good |
| Chrome | Navbar - authenticated user | good | good |
| Chrome | Navbar - authenticated admin | good | good |
| Chrome | Footer - newsletter form, social icons, Privacy Policy, copyright | good | good |
| Chrome | Home - main content | good | good |
| Chrome | Shop - title and Sort/Filter dropdowns | good | good |
| Chrome | Shop - products - unauthenticated user | good | good |
| Chrome | Shop - products - authenticated user | good | good |
| Chrome | Shop - products - authenticated admin | good | good |
| Chrome | Product detail - product images | good | good |
| Chrome | Product detail - product info - unauthenticated user | good | good |
| Chrome | Product detail - product info - authenticated user | good | good |
| Chrome | Product detail - add to basket form | good | good |
| Chrome | Product detail  - authenticated admin | good | good |
| Chrome | Basket page - list of basket items | good | good |
| Chrome | Basket page - empty basket | good | good |
| Chrome | Checkout page - form - unauthenticated user | good | good |
| Chrome | Checkout page - form - authenticated user | good | good |
| Chrome | Checkout page - basket summary | good | good |
| Chrome | Checkout success page | good | good |
| Chrome | Account page - profile form | good | good |
| Chrome | Account page - links to wishlist/bookmarks/past orders | good | good |
| Chrome | Wishlist - listed items | good | good |
| Chrome | Wishlist - no items | good | good |
| Chrome | Bookmarks - listed articles/recipes | good | good |
| Chrome | Bookmarks - no saved articles/recipes | good | good |
| Chrome | Order history - list of past orders | good | good |
| Chrome | Order history - no past orders | good | good |
| Chrome | Order page (past order confirmation) | good | good |
| Chrome | Blog | good | good |
| Chrome | Articles page | good | good |
| Chrome | Articles page - authenticated staff user | good | good |
| Chrome | Articles page - authenticated admin | good | good |
| Chrome | Article detail page - unauthenticated user | good | good |
| Chrome | Article detail page - authenticated user | good | good |
| Chrome | Article detail page - authenticated staff user | good | good |
| Chrome | Article detail page - authenticated admin | good | good |
| Chrome | Edit article - authenticated staff user | good | good |
| Chrome | Edit article - authenticated admin | good | good |
| Chrome | Create article - authenticated staff user | good | good |
| Chrome | Delete article - authenticated admin | good | good |
| Chrome | Unpublish article - authenticated admin | good | good |
| Chrome | Recipes page | good | good |
| Chrome | Recipes page - authenticated staff user | good | good |
| Chrome | Recipes page - authenticated admin | good | good |
| Chrome | Recipe detail page - unauthenticated user | good | good |
| Chrome | Recipe detail page - authenticated user | good | good |
| Chrome | Recipe detail page - authenticated staff user | good | good |
| Chrome | Recipe detail page - authenticated admin | good | good |
| Chrome | Edit recipe - authenticated staff user | good | good |
| Chrome | Edit recipe - authenticated admin | good | good |
| Chrome | Create recipe - authenticated staff user | good | good |
| Chrome | Delete recipe - authenticated admin | good | good |
| Chrome | Unpublish recipe - authenticated admin | good | good |
| Chrome | Events - unauthenticated user | good | good |
| Chrome | Events - authenticated user | good | good |
| Chrome | Events - authenticated admin | good | good |
| Chrome | Event registration page | good | good |
| Chrome | Create event - authenticated admin | good | good |
| Chrome | Edit event - authenticated admin | good | good |
| Chrome | Delete event - authenticated admin | good | good |
| Chrome | Sign up page | good | good |
| Chrome | Log in page | good | good |
| Chrome | Log out page | good | good |
| Chrome | Forgot password page | good | good |
| Chrome | Admin Panel page - authenticated admin | good | good |
| Chrome | Add product - authenticated admin | good | good |
| Chrome | Create carousel - authenticated admin | good | good |
| Chrome | Choose carousel - authenticated admin | good | good |
| Chrome | Activate carousel - authenticated admin | good | good |
| Chrome | Edit carousel - authenticated admin | good | good |
| Chrome | Delete carousel - authenticated admin | good | good |
| Chrome | Manage reviews - authenticated admin | good | good |
| Firefox | Promo banner | good | good |
| Firefox | Navbar - unauthenticated user | good | good |
| Firefox | Navbar - authenticated user | good | good |
| Firefox | Navbar - authenticated admin | good | good |
| Firefox | Footer - newsletter form, social icons, Privacy Policy, copyright | good | good |
| Firefox | Home - main content | good | good |
| Firefox | Shop - title and Sort/Filter dropdowns | good | good |
| Firefox | Shop - products - unauthenticated user | good | good |
| Firefox | Shop - products - authenticated user | good | good |
| Firefox | Shop - products - authenticated admin | good | good |
| Firefox | Product detail - product images | good | good |
| Firefox | Product detail - product info - unauthenticated user | good | good |
| Firefox | Product detail - product info - authenticated user | good | good |
| Firefox | Product detail - add to basket form | good | good |
| Firefox | Product detail  - authenticated admin | good | good |
| Firefox | Basket page - list of basket items | good | good |
| Firefox | Basket page - empty basket | good | good |
| Firefox | Checkout page - form - unauthenticated user | good | good |
| Firefox | Checkout page - form - authenticated user | good | good |
| Firefox | Checkout page - basket summary | good | good |
| Firefox | Checkout success page | good | good |
| Firefox | Account page - profile form | good | good |
| Firefox | Account page - links to wishlist/bookmarks/past orders | good | good |
| Firefox | Wishlist - listed items | good | good |
| Firefox | Wishlist - no items | good | good |
| Firefox | Bookmarks - listed articles/recipes | good | good |
| Firefox | Bookmarks - no saved articles/recipes | good | good |
| Firefox | Order history - list of past orders | good | good |
| Firefox | Order history - no past orders | good | good |
| Firefox | Order page (past order confirmation) | good | good |
| Firefox | Blog | good | good |
| Firefox | Articles page | good | good |
| Firefox | Articles page - authenticated staff user | good | good |
| Firefox | Articles page - authenticated admin | good | good |
| Firefox | Article detail page - unauthenticated user | good | good |
| Firefox | Article detail page - authenticated user | good | good |
| Firefox | Article detail page - authenticated staff user | good | good |
| Firefox | Article detail page - authenticated admin | good | good |
| Firefox | Edit article - authenticated staff user | good | good |
| Firefox | Edit article - authenticated admin | good | good |
| Firefox | Create article - authenticated staff user | good | good |
| Firefox | Delete article - authenticated admin | good | good |
| Firefox | Unpublish article - authenticated admin | good | good |
| Firefox | Recipes page | good | good |
| Firefox | Recipes page - authenticated staff user | good | good |
| Firefox | Recipes page - authenticated admin | good | good |
| Firefox | Recipe detail page - unauthenticated user | good | good |
| Firefox | Recipe detail page - authenticated user | good | good |
| Firefox | Recipe detail page - authenticated staff user | good | good |
| Firefox | Recipe detail page - authenticated admin | good | good |
| Firefox | Edit recipe - authenticated staff user | good | good |
| Firefox | Edit recipe - authenticated admin | good | good |
| Firefox | Create recipe - authenticated staff user | good | good |
| Firefox | Delete recipe - authenticated admin | good | good |
| Firefox | Unpublish recipe - authenticated admin | good | good |
| Firefox | Events - unauthenticated user | good | good |
| Firefox | Events - authenticated user | good | good |
| Firefox | Events - authenticated admin | good | good |
| Firefox | Event registration page | good | good |
| Firefox | Create event - authenticated admin | good | good |
| Firefox | Edit event - authenticated admin | good | good |
| Firefox | Delete event - authenticated admin | good | good |
| Firefox | Sign up page | good | good |
| Firefox | Log in page | good | good |
| Firefox | Log out page | good | good |
| Firefox | Forgot password page | good | good |
| Firefox | Admin Panel page - authenticated admin | good | good |
| Firefox | Add product - authenticated admin | good | good |
| Firefox | Create carousel - authenticated admin | good | good |
| Firefox | Choose carousel - authenticated admin | good | good |
| Firefox | Activate carousel - authenticated admin | good | good |
| Firefox | Edit carousel - authenticated admin | good | good |
| Firefox | Delete carousel - authenticated admin | good | good |
| Firefox | Manage reviews - authenticated admin | good | good |


### Automated tests

Automated testing was done for the following apps: Blog, Events, Home, Products, and Profiles. In total, 248 tests were made:
- 83 tests for the Blog app,
- 15 tests for the Checkout app,
- 32 tests for the Events app,
- 36 tests for the Home app,
- 57 tests for the Products app,
- and 25 for the Profiles app. 

__Blog app testing__

1. test_models.py

19 tests ran successfully, checking the following:
- max_length of CharFields, 
- default value of a field, 
- ForeignKey relationship between models, 
- string representation of a model, 
- verbose name plural (for the models where it was set explicitly), 
- and ordering (if set in class Meta).

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_blog_models.png)

2. test_forms.py

12 tests ran successfully, checking:
- the presence of expected form fields,
- whether a field has correct help text,
- whether a field widget is a SummernoteWidget or MultipleSelectCheckbox as expected, 
- and whether the correct fields are excluded in the restricted forms (subclasses of other forms)

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_blog_forms.png)

3. test_views.py

52 tests ran successfully, checking among others the following details:
- whether views render correct templates,
- whether views restricted to logged-in users only redirect anyone who is not logged in,
- whether views can be accessed by their name,
- whether generic.ListView views actually show all items they should list,
- whether the url of a view exists at the expected location,
- whether views redirect the user upon a successful interaction (e.g. upon deleting a recipe/article),

![Test results - views](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_blog_views.png)

__Checkout app testing__

1. test_models.py

8 tests ran successfully, checking:
- the maximum length of a CharField, 
- and the maximum number of digits for a DecimalField. 

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_checkout_models.png)

2. test_forms.py

7 tests ran successfully, checking the following criteria:
- whether the correct fields are included,
- field labels,
- field placeholders,
- whether a field has the 'autofocus' attribute
- a field's class.

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_checkout_forms.png)

__Events app testing__

1. test_models.py

6 tests ran successfully, checking the following:
- max_length of CharFields, 
- default value of a field, 
- string representation of a model, 
- and ordering (if set in class Meta).

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_events_models.png)

2. test_forms.py

3 tests ran successfully, checking:
- whether the form is related to the correct model,
- the presence of expected form fields,
- whether a field placeholder is shown as expected.

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_events_forms.png)

3. test_views.py

23 tests ran successfully, checking among others the following details:
- whether views render correct templates,
- whether views restricted to logged-in users only redirect anyone who is not logged in,
- whether views can be accessed by their name,
- whether the url of a view exists at the expected location,
- whether past events are excluded as expected,
- whether users with different permissions have access (or do not have access) to different views as expected,
- whether a confirmation email is sent.

![Test results - views](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_events_views.png)

__Home app testing__

1. test_models.py

16 tests ran successfully, checking the following:
- max_length of CharFields, 
- default value of a field, 
- string representation of a model, 
- and ordering (if set in class Meta).

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_home_models.png)

2. test_forms.py

6 tests ran successfully, checking:
- the presence of expected form fields,
- whether specific fields are required as expected.

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_home_forms.png)

3. test_views.py

14 tests ran successfully, checking among others the following details:
- whether views render correct templates,
- whether correct users have access to correct views based on their permissions
- whether views can be accessed by their name,
- whether the url of a view exists at the expected location,
- whether an admin can delete a carousel successfully.

![Test results - views](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_home_views.png)

__Products app testing__

1. test_models.py

22 tests ran successfully, checking the following:
- field labels,
- max_length of CharFields, 
- default value of a field, 
- string representation of a model, 
- and ordering (if set in class Meta).

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_products_models.png)

2. test_forms.py

9 tests ran successfully, checking:
- whether correct models are used,
- whether the correct fields are included in a form,
- whether some fields are required,
- whether a field help text is correct.

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_products_forms.png)

3. test_views.py

26 tests ran successfully, checking among others the following details:
- whether views render correct templates,
- whether correct users have access to correct views based on their permissions
- whether views can be accessed by their name,
- whether the url of a view exists at the expected location,
- whether correct product/products are present in a view,
- whether an authenticated user can submit a product review,
- whether different users have correct access permissions,
- whether a superuser can create/edit/delete a product as expected,
- whether a superuser can approve/delete an unapproved review with text.

![Test results - views](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_products_views.png)

__Profiles app testing__

1. test_models.py

6 tests ran successfully, checking the following:
- Country field label,
- max_length of CharFields, 
- string representation of the UserProfile model.

![Test results - models](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_profiles_models.png)

2. test_forms.py

3 tests ran successfully, checking:
- whether the correct model is used,
- whether the 'user' field is excluded as expected,
- whether the field 'default_phone_number' has the attribute 'autofocus'.

![Test results - forms](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_profiles_forms.png)

3. test_views.py

16 tests ran successfully, checking among others the following details:
- whether views render correct templates,
- whether correct users have access to correct views based on their permissions,
- whether user can edit their profile.

![Test results - views](https://github.com/Agnieszka-21/health-store/blob/main/assets/django_tests/test_profiles_views.png)


### Notable Bugs

There are currently two minor bugs within the project which do not affect the most important functionalities. The first one is a caching issue. On a product detail page, if a product has more than one image, the primary image is shown as larger, and the next one or two images are thumbnails. The images can switch places on a click for optimal user experience. This works well but there is an added functionality there which allows user to click the main (larger) image so that it is opened in a new tab and shown in an even larger size. At the moment the image in the new tab is always displayed correctly when in Incognito mode, but without it, sometimes only the primary product image is opened in a new tab, regardless of where it is positioned (as main image or as thumbnail). Since this issue was not a problem for all products during testing but only ones that I have opened repeatedly in the past, I decided to leave it as it is.

The second minor bug is related to the maximum quantity of a product allowed. The maximum number is set to 9, and this works well in the form on the product detail page and in the basket. However, user could potentially place an item with its maximum quality in the basket, and then keep shopping, and add more of the same product. Since in real life maximum product quantities would be dictated by how many of those products are in stock rather than an arbitrarily chosen number, I decided to leave it as it is for the time being and ideally add stock-tracking functionalities in the future.


## Technologies Used

The following modules were used in this project:
- asgiref==3.8.1
- boto3==1.35.76
- botocore==1.35.76
- crispy-bootstrap4==2024.10
- dj-database-url==0.5.0
- Django==4.2
- django-allauth==0.50.0
- django-countries==7.6.1
- django-crispy-forms==2.3
- django-storages==1.14.4
- django-summernote==0.8.20.0
- gunicorn==23.0.0
- jmespath==1.0.1
- oauthlib==3.2.2
- pillow==11.0.0
- psycopg2==2.9.10
- PyJWT==2.9.0
- python3-openid==3.2.0
- pytz==2024.2
- requests-oauthlib==2.0.0
- s3transfer==0.10.4
- sqlparse==0.5.2
- stripe==11.3.0

### Django
Django was used as the main framework for this project.

### Django AllAuth
Django Allauth was utilised to handle authentication and authorization and therefore manage user permissions.

### django-cookies
This library was used to get a CSRF cookie in JavaScript files handling the product wishlist as well as bookmarking articles/recipes.

### DTL/Jinja
Jinja/Django templating language was used to insert data from the database into templates and to perform queries on specific datasets.

### Crispy forms
Django-crispy-forms was utilised to improve styling and ensure consistent design in any forms in the project

### Pillow
Pillow was utilised to handle image fields in models.

### Heroku
A cloud-based platform for deploying the site.

### PostgreSQL
PostgreSQL was used as the database for this project during both development and in production.

### JavaScript
JavaScript has been utilised to handle multiple scenarios in the following apps: Blog, Checkout, Products, and Profiles. It is used for handling the following functionalities: Stripe elements, product reviews and star ratings, product images on product detail page, wishlist and bookmarked articles/recipes, product quantities for the basket, filtering and sorting products, copying the URL of an article/recipe with one click for easy sharing, and the country field in the checkout form.

### Bootstrap 5
Bootsrap was utilised for creating a responsive layout.

### Font Awesome
It was used to access the calendar icons on the Schedule page.

### CSS
Multiple CSS files (base.css, blog.css, checkout.css, products.css, profile.css) were created to handle custom styling beyond Bootstrap and introduce media queries for improved responsive design.

### HTML
HTML was utilised to create a template for each page.

### Packages Used

- Gitpod was used to develop the site
- GitHub was utilised for storing the files for this project
- Heroku was used to deploy the site
- An AWS account was used to store media and static files for the project


### Resources Used

- [Favicon generator](https://favicon.io/favicon-generator/) used to create the website's favicons
- [Django secret key generator](https://djecrety.ir/) was utilised for creating a secret key for deployment on Heroku (SECRET_KEY config var)
- [Privacy policy generator](https://www.privacypolicygenerator.info/) was utilised to create and host a privacy policy page
- [MailChimp](https://mailchimp.com/) was used to add to the footer a newsletter signup form
- Balsamiq was used to develop wireframes for the site (both mobile and desktop version)
- [DrawSQL.app](https://drawsql.app/) was utilised to develop the database schema during development
- Free online image converters, compressors, and resizers


## Deployment

The application has been deployed via Heroku and the live page can be found [here](https://health-store-ff0f909bba3d.herokuapp.com/).

This program was developed using [this particular template from Code Institute](https://github.com/Code-Institute-Org/ci-full-template).

In order to deploy the application to Heroku I followed the following steps:
- Sign up or log in to Heroku.
- On the main Heroku dashboard page select "Create new app".
- Give the project a unique name, select a suitable region, and click "Create app". This will create the app in Heroku and bring you to the Deploy tab.
- Switch to the Settings tab. 
- In the "Config Vars" section click the "reveal config vars" button.
- Add the following key: DISABLE_COLLECTSTATIC, with the value 1 to prevent Heroku from uploading static files during the build.This key-value pair must be removed before final deployment.
- In the next KEY input field enter "SECRET_KEY" (all capitals), in the VALUE field next to it enter your secret key - you can create yours using [this Django secret key generator](https://djecrety.ir/). Then click the "Add" button to the right.
- Add another config var, with the KEY "DATABASE_URL" and the VALUE that is your PostgreSQL database's URL. Click "Add".
- To connect the project to your Stripe account, set the following Config Vars:
  - CLIENT_SECRET,
  - STRIPE_PUBLIC_KEY,
  - and STRIPE_WH_SECRET. You can find the suitable values for these config vars in your Stripe account.
- If you plan on using an AWS account to store media and static files, set up your bucket following [AWS documentation](https://docs.aws.amazon.com/quickstarts/) and then add these 3 Config Vars:
  - USE_AWS set to True,
  - AWS_ACCESS_KEY_ID with yout access key id,
  - and AWS_SECRET_ACCESS_KEY with your secret key.
- To handle email authentication, add also these config vars:
  - EMAIL_HOST_PASSWORD, where the value is a 16-digit app password from a Gmail account to which you would like to connect the program - see more detailed information on that [here](https://support.google.com/mail/answer/185833?hl=en).
  - EMAIL_HOST_USER, where the value is the email address of the Gmail account with the app passcode.
- In the section "Buildpacks" click the "Add buildpack" button and select "heroku/python". Confirm by clicking the button "Add buildpack".
- Prepare the code for deployment in your local environment: use  pip install -r requirements.txt to install the libraries and packages needed to run the program (including gunicorn)
- In the Procfile add the following code:
web: gunicorn codestar.wsgi
- Make sure DEBUG = False in the settings.py file
- Also in settings.py, add '.herokuapp.com' to the list of ALLOWED_HOSTS
- Git commit and push the changes to your GitHub repository.
- Go back to your Heroku account, choose the Deploy tab at the top. 
- In the "Deployment Method" section choose the "GitHub" button. Follow the next steps (if any) as prompted to connect your GitHub account. In the "Connect to GitHub" section that appears, choose your account, enter the name of your repository, and select "Search".
-  Once your GitHub repo is connected to the Heroku app, scroll down to the section "Manual deploys".
-  Confirm that the correct branch of the repo is selected in the drop-down box, and select "Deploy Branch".
-  Heroku will now build the app for you. Once the process is completed, you will see the message "Your app was successfully deployed", and a link to the app where you can visit the live site. Afterwards, replace the existing sitemap.xml and robots.txt files with your own - if you switch to "Automatic deploys", your changes will be deployed with the next git push.
  

## Cloning and forking the repository

In order to clone the GitHub repository use the following link:
- [https://github.com/Agnieszka-21/health-store.git](https://github.com/Agnieszka-21/health-store.git)

In order to fork the GitHub repository:
- Go to this [health-store repository](https://github.com/Agnieszka-21/health-store)
- In the menu at the top choose the option "Fork"
- You should now have your own repository inside your GitHub account.


## Credits

The following tutorials, articles, documentation and media were used to create this web application.

### Code

- [Django documentation](https://docs.djangoproject.com/en/4.2/) has been used extensively for this project
- Further helpful documentation was related to the libraries installed:
  - [django-summernote](https://pypi.org/project/django-summernote/) was utilised for text editors in blog article and recipe forms
  - [js-cookie](https://www.jsdelivr.com/package/npm/js-cookie) package was utilised in several JavaScript files in order to obtain a CSRF token (see static files related to marking products as "favourite" and bookmarking articles/recipes)
- [Bootstrap 5 documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used extensively to help create any standard elements like the navigation menu, footer, homepage carousel, card elements, toasts etc.
- Handling star reviews proved to be more complex than initially expected, the following tutorial helped me find working solutions: [https://stackoverflow.com/questions/45845427/styling-an-integerfield-to-make-it-a-star-rating-system](https://stackoverflow.com/questions/45845427/styling-an-integerfield-to-make-it-a-star-rating-system)
- Switching places of product images on product detail pages was developed with the help of this post: [https://craftcms.stackexchange.com/questions/32882/how-to-toggle-main-product-image-from-multiple-images](https://craftcms.stackexchange.com/questions/32882/how-to-toggle-main-product-image-from-multiple-images)
- Mutiple parts of this project are based on two Code Institute's walkthrough projects: [I think therefore I blog](https://github.com/Code-Institute-Solutions/blog/tree/main) and [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/profiles/models.py).
  - The review section on product detail pages has been developed based on the blog walkthrough project and its Comments section.
  - Any parts of the code directly related to Stripe (Checkout and Basket apps) have been copied from Boutique Ado, and adjusted slightly if needed.
  - The automatic creation of a profile when a User object is created was done with Django signals - code was copied from the Code Institute's walkthrough project Boutique Ado.
- Pagination for the Shop page has been created by copying code from [this utils.py file](https://github.com/MattBCoding/druid-pp5/blob/main/products/utils.py) by my Code Institute mentor Matt Bodden and tweaking it in the related view.

Code that has been copied from an external source and left without any changes has been also marked in the program files (comments were added with links to the sources and more exact information where applicable).


### Content

- [Holland & Barrett's website](https://www.hollandandbarrett.ie/) was an inspiration to build a functional, aesthetically pleasing webpage that could be used by a real-world health store. Blog articles, banner images for articles, and event details used in this project have been copied or adapted from existing blog posts and podcast episodes by Holland & Barrett.
- Recipes used on the blog have been copied and adapted (including images) from the [BBC Good Food's](https://www.bbcgoodfood.com/) website.
- [Boots](https://www.boots.ie/) and [H&M](https://www2.hm.com/en_ie/index.html) websites and apps were used to guide decisions regarding layout and styling on various devices so that they meet current standards.
- Product SKU values are based on SKUs from the store [Nourish](https://www.nourish.ie/).
- Product images have been copied from their brand's or vendor's websites. This enabled the use of multiple images per product, which is industry standard. Here is a full list of websites from which product images were copied:
  - [Craft Food Traders](https://craftfoodtraders.ie/)
  - [Dublin Herbalists](https://dublinherbalists.ie/)
  - [The Handmade Soap Company](https://thehandmadesoapcompany.ie/)
  - [Tisserand](https://www.tisserand.com/)
  - [Viridian](https://viridian-nutrition.com/)
  - [Wild Nutrition](https://www.wildnutrition.com/)
- Several free-licence images from [Pexels](https://www.pexels.com/) were used in the project.
- [freepik.com](https://www.freepik.com/) is the source of free-licence SVG files on error pages (404 and 500)
- [Font Awesome](https://docs.fontawesome.com/) was used for several icons used in the navigation menu, in the footer (social media icons), on the Schedule page (calendar icons), and in the modals (close icon)..
- [Google Fonts](https://fonts.google.com/) page was used to access the fonts used throughout the website.
- [AWS](https://aws.amazon.com/) was used to store media and static files used in this project.
- A [MailChimp](https://mailchimp.com/) account was used to embed in the footer a newsletter signup form.


## Acknowledgements

I would like to express my sincere gratitude to my mentor, Matt Bodden, whose suggestions and practical advice have been invaluable. I am also grateful for the help of the team of tutors who supported me when I felt stuck and whose insights and tips ensured I could progress with the project.

