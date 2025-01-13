# Health Store


## Introduction

Health Store is a web application for a fictional online shop that sells vitamins and supplements, healthy cooking ingredients and foods, natural beauty products, and eco-friendly home items to health-conscious customers.

This is the fifth and last Portfolio Project for the Code Institute's Diploma Course in Full Stack Software Development (E-commerce Applications). The application is built in Django using Python, HTML, CSS, and JavaScript. It provides role-based permissions for users to interact with data in a PostgreSQL database. It includes user authentication, email validation, and CRUD functionality. The application is connected to Stripe in order to simulate online payments. An AWS account is used to store media and static files, and there is also a newsletter signup form connected to a MailChimp account.

[View the live website here](https://health-store-ff0f909bba3d.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![Screenshot of the application on multiple devices](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/amiresponsive.png)


## Table of Contents

- [Health Store](#health-store)
   * [Introduction](#introduction)
   * [Table of Contents](#table-of-contents)
   * [UX](#ux)
      + [The Strategy Plane](#the-strategy-plane)
         - [The Site's Ideal User](#the-sites-ideal-user)
         - [Site Goals](#site-goals)
         - [Iterations (GitHub Milestones)](#iterations-github-milestones)
         - [Epics](#epics)
         - [User Stories](#user-stories)
         - [Story Points](#story-points)
         - [MoSCoW Prioritization](#moscow-prioritization)
      + [The Scope Plane](#the-scope-plane)
      + [The Structure Plane](#the-structure-plane)
         - [Create a user account (sign up)](#create-a-user-account-sign-up)
         - [Log into the user profile/account](#log-into-the-user-profileaccount)
         - [Log out of the user profile/account](#log-out-of-the-user-profileaccount)
         - [View a user profile/account](#view-a-user-profileaccount)
         - [Edit the user profile/account](#edit-the-user-profileaccount)
         - [View all products](#view-all-products)
         - [Filter products based on category](#filter-products-based-on-category)
         - [Sort products based on specific criteria](#sort-products-based-on-specific-criteria)
         - [Search for a specific product](#search-for-a-specific-product)
         - [View a specific product with a high level of detail](#view-a-specific-product-with-a-high-level-of-detail)
         - [Optimise user experience on the shop page (pagination, back-to-top link)](#optimise-user-experience-on-the-shop-page-pagination-back-to-top-link)
         - [Add a product to the basket](#add-a-product-to-the-basket)
         - [View the basket](#view-the-basket)
         - [Remove a product from the basket](#remove-a-product-from-the-basket)
         - [Adjust the quantity of a product/products in the basket](#adjust-the-quantity-of-a-productproducts-in-the-basket)
         - [Proceed to checkout](#proceed-to-checkout)
         - [Provide personal details needed in the checkout process](#provide-personal-details-needed-in-the-checkout-process)
         - [Pay for the items in the shopping basket](#pay-for-the-items-in-the-shopping-basket)
         - [Receive an order confirmation](#receive-an-order-confirmation)
         - [View product reviews](#view-product-reviews)
         - [Create a product review](#create-a-product-review)
         - [Edit a review](#edit-a-review)
         - [Delete a review](#delete-a-review)
         - [Mark and save a product as "favourite"](#mark-and-save-a-product-as-favourite)
         - [View your wishlist/"favourites"](#view-your-wishlistfavourites)
         - [Remove a product/products from your wishlist](#remove-a-productproducts-from-your-wishlist)
         - [View/read a blog with articles and healthy recipes](#viewread-a-blog-with-articles-and-healthy-recipes)
         - [Save an article/recipe to a user profile](#save-an-articlerecipe-to-a-user-profile)
         - [Sign up to a webinar on health- an wellness-related topics](#sign-up-to-a-webinar-on-health-an-wellness-related-topics)
         - [Copy the URL of an article/recipe with one click for easy sharing ](#copy-the-url-of-an-articlerecipe-with-one-click-for-easy-sharing)
         - [Sign up to the newsletter](#sign-up-to-the-newsletter)
         - [Opportunities arising from User Stories](#opportunities-arising-from-user-stories)
      + [The Skeleton Plane](#the-skeleton-plane)
         - [Wireframe mock-ups](#wireframe-mock-ups)
         - [Desktop version](#desktop-version)
         - [Database schema](#database-schema)
      + [The Surface Plane](#the-surface-plane)
         - [Design](#design)
         - [Typography](#typography)
         - [Images](#images)
   * [Features](#features)
      + [Homepage](#homepage)
      + [Shop page](#shop-page)
      + [Product detail page](#product-detail-page)
      + [Basket page](#basket-page)
      + [Checkout page](#checkout-page)
      + [Checkout success page](#checkout-success-page)
      + [Account page](#account-page)
      + [Blog](#blog)
      + [Events](#events)
      + [Sign up page](#sign-up-page)
      + [Log in page](#log-in-page)
      + [Log out page](#log-out-page)
      + [Additional screenshots](#additional-screenshots)
   * [Future Enhancements](#future-enhancements)
   * [Testing](#testing)
      + [Testing Overview](#testing-overview)
      + [Manual Testing](#manual-testing)
      + [Validator Testing](#validator-testing)
      + [Lighthouse and Webaim Wave Testing](#lighthouse-and-webaim-wave-testing)
      + [Responsiveness (tested with Chrome Dev Tools)](#responsiveness-tested-with-chrome-dev-tools)
      + [Browser compatibility testing](#browser-compatibility-testing)
      + [Automated tests](#automated-tests)
      + [Notable Bugs](#notable-bugs)
   * [Technologies Used](#technologies-used)
      + [Django](#django)
      + [Django AllAuth](#django-allauth)
      + [django-cookies](#django-cookies)
      + [DTL/Jinja](#dtljinja)
      + [Crispy forms](#crispy-forms)
      + [Pillow](#pillow)
      + [Heroku](#heroku)
      + [PostgreSQL](#postgresql)
      + [JavaScript](#javascript)
      + [Bootstrap 5](#bootstrap-5)
      + [Font Awesome](#font-awesome)
      + [CSS](#css)
      + [HTML](#html)
      + [Packages Used](#packages-used)
      + [Resources Used](#resources-used)
   * [Deployment](#deployment)
   * [Cloning and forking the repository](#cloning-and-forking-the-repository)
   * [Business considerations](#business-considerations)
      + [Business model](#business-model)
      + [SEO](#seo)
      + [Web marketing](#web-marketing)
   * [Credits](#credits)
      + [Code](#code)
      + [Content](#content)
   * [Acknowledgements](#acknowledgements)


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
- [#7 Web marketing](https://github.com/Agnieszka-21/health-store/issues/7)
- [#8 SEO](https://github.com/Agnieszka-21/health-store/issues/8)


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
- [#21 Sign in to the user profile/account using a social media login](https://github.com/Agnieszka-21/health-store/issues/21) - see [Future Enhancements](#future-enhancements)


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
- [#30 Add a product/products to the basket](https://github.com/Agnieszka-21/health-store/issues/30)
- [#31 View the basket](https://github.com/Agnieszka-21/health-store/issues/31)
- [#32 Remove a product/products from the basket](https://github.com/Agnieszka-21/health-store/issues/32)
- [#33 Adjust the quantity of a product/products in the basket](https://github.com/Agnieszka-21/health-store/issues/33)
- [#34 Save the shopping basket for later](https://github.com/Agnieszka-21/health-store/issues/34) - see [Future Enhancements](#future-enhancements)
- [#35 Proceed to checkout](https://github.com/Agnieszka-21/health-store/issues/35)
- [#63 Keep the existing basket when logging in](https://github.com/Agnieszka-21/health-store/issues/63) - see [Future Enhancements](#future-enhancements)

6. Checkout
- [#36 Create a user account during a checkout process](https://github.com/Agnieszka-21/health-store/issues/36) - [Future Enhancements](#future-enhancements)
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

#### Create a user account (sign up)

[User story #15:  ](https://github.com/Agnieszka-21/health-store/issues/15)
As a User (Customer), I would like to create a user profile/account, so that I can save my data for a speedier checkout process, save favourite products and blog and avail of any other functionalities available only to registered users.

__Acceptance Criteria__
- Given that I am an unregistered User (Client), when I choose the "Sign Up" option, then I can create my account with an email address and a password.
- Given that I am an unregistered User (Client), when I choose the "Sign Up" option, then I am sent an email that allows me to verify my email and confirm that I want to sign up for an account.

__Implementation__
- Use Django AllAuth so that the user can create an account.
- Make sure to verify user's email (configuration in settings.py)
- Adjust the verification/confirmation email so that it displays the correct business name instead of example.com

---

#### Log into the user profile/account

[User story #16:  ](https://github.com/Agnieszka-21/health-store/issues/16)
As a User (Customer), I would like to be able to log in to my profile/account, so that I can access the advantages of having an account.

__Acceptance Criteria__
- Given that I am a registered user
When I navigate to the login page
Then I can enter my details to log in to my account
- Given that I am a registered user, when I navigate to the login page and enter my details and I click login, then I am logged into my account and I am able to see a visual confirmation that I am now logged in.
- Given that I am a registered user and I try to log in to my account, when I enter the wrong information, then the site informs me that the information was incorrect and prevents my logging in.
- Given that I am a registered user and I try to log in to my account, when I forget my password, then I can click a "Forgot password" link that takes me to a page that helps me reset my password.

__Implementation__
- Create a Login option in the navigation bar and main menu
- Show the Login option only to a user who is not logged in yet
- Make sure the user can reset their password in case they forget it

---

#### Log out of the user profile/account

[User story #17:  ](https://github.com/Agnieszka-21/health-store/issues/17)
As a User (Customer), I would like to be able to log out of my account, so that I can make sure my personal details are safe.

__Acceptance Criteria__
- Given that I am a logged in user, when I select "log out" in the nav bar and confirm it, then I am redirected to the homepage and a confirmation message is shown

__Implementation__
- Once the User is logged in, give them the option to log out in the main menu and the nav bar
- Defensive programming - when user chooses the log out option, ask for confirmation
- If the user confirms that they want to log out, redirect them to the Homepage with updated navbar (Login/Signup option shown)

---

#### View a user profile/account

[User story #19:  ](https://github.com/Agnieszka-21/health-store/issues/19)
As a User (Customer), I would like to be able to view my profile, so that I can see any information saved there.

__Acceptance Criteria__
- Given that I am a registered user, when I log in to my account, then I can easily navigate to and view my profile/account

__Implementation__
- Create the Profile/Account option in the nav bar, shown only when a user is logged in
- Ensure that this option takes the user to their account with all their saved information

---

#### Edit the user profile/account

[User story #18:  ](https://github.com/Agnieszka-21/health-store/issues/18)
As a User (Customer), I would like to be able to add and edit specific details like address or payment method to my profile, so that they stay up to date and enhance my shopping experience.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to my profile/account, then I can add and edit suitable data.
- Given that I am a logged in user, when I add/edit/delete my profile data, then get a notification that confirms my changes.
- Given that I am a logged in user, when there is an issue with adding/editing/deleting my profile data, then the site informs me what went wrong.

__Implementation__
- Create a way of saving a user's default address, name, email, and phone number in their user account
- Show a suitable notification whenever user makes a change to their profile

---

#### View all products

[User story #22:  ](https://github.com/Agnieszka-21/health-store/issues/22)
As a User (Customer), I would like to be able to view all products in one place, so that I can browse and explore what the shop has to offer.

__Acceptance Criteria__
- Given that I am a user who wants to browse all products carried by the store, when I navigate to the shop page, then I can see all products listed there.
- Given that I am a user who wants to browse all products carried by the store, when I access the shop page, then I can easily access all products by scrolling.
- Given that I am a user who wants to browse all products carried by the store, when I view the shop page, then I can see the right level of detail for each product to be well-informed without feeling overwhelmed.

__Implementation__
- Create a page that shows all products carried by the store with only the most relevant information
- I For each product, show one image and only the most essential information

---

#### Filter products based on category

[User story #23:  ](https://github.com/Agnieszka-21/health-store/issues/23)
As a User (Customer), I would like to be able to filter products available on the shop page, so that I can be more specific in my search for products while still exploring my options.

__Acceptance Criteria__
- Given that I am a user who wants to browse products in a specific category, when I navigate to the shop page, then I can switch on a suitable filter to view only relevant products.

__Implementation__
- Create a filter button and functionality
- Provide the functionality of filtering products by category

---

#### Sort products based on specific criteria

[User story #24:  ](https://github.com/Agnieszka-21/health-store/issues/24)
As a User (Customer), I would like to be able to sort products available on the shop page, so that I can browse products in a specific order (lowest price first/highest price first/highest ratings first).

__Acceptance Criteria__
- Given that I am a user who wants to see products with the highest ratings first, when I navigate to the shop page, then I can switch on a suitable sorting option to view products in the required order.
- Given that I am a user who wants to see products with the lowest price first, when I navigate to the shop page, then I can switch on a suitable sorting option to view products in the required order.
- Given that I am a user who wants to see products with the highest price first, when I navigate to the shop page, then I can switch on a suitable sorting option to view products in the required order.

__Implementation__
-  Create a sort button and functionality
- Provide the following sorting options: by price (low to high), by price (high to low), by rating (high to low), by name (A-Z and Z-A)

---

#### Search for a specific product

[User story #25:  ](https://github.com/Agnieszka-21/health-store/issues/25)
As a User (Customer), I would like to be able to search for a specific product by typing a keyword, so that results show only the products related to my search.

__Acceptance Criteria__
- Given that I am a user who wants to search for a specific product, when I navigate to the shop page, then I can type a keyword into a search bar.
- Given that I am a user who wants to search for a specific product, when I navigate to the shop page, then I can view results of my search that include only products related to my keyword.

__Implementation__
- Create a search bar as part in the header
- Ensure the functionality looks for the keyword in product name/description/ingredients

---

#### View a specific product with a high level of detail

[User story #26:  ](https://github.com/Agnieszka-21/health-store/issues/26)
As a User (Customer), I would like to be able to view any product in more detail, on a separate page, so that I can access all the information I might need to help me decide whether to purchase that product or not.

__Acceptance Criteria__
- Given that I am a user who is interested in specific products, when I navigate to the shop page, then I can select a product to view it in more detail.
- Given that I am a user who is interested in specific products, when I view a product detail page, then I can access a suitable level of information, including multiple photos, ratings, description etc.

__Implementation__
- Create a product detail page that populates with a chosen product's data
- Include all relevant information - product name, description, price, rating, SKU, and multiple images

---

#### Optimise user experience on the shop page (pagination, back-to-top link)

[User story #64:  ](https://github.com/Agnieszka-21/health-store/issues/64)
As a User (Customer), I would like to be able to avoid endless scrolling and get back to the top of the page easily, so that I can enjoy the shopping experience without feeling overwhelmed.

__Acceptance Criteria__
- Given That I am a user, when I scroll through the shop page, then I have the option of going to the next/previous page that loads more products.
- Given That I am a user, when I scroll through the shop page, then I can click the back-to-top button and easily return to the top of the page.

__Implementation__
- Add pagination to the page with all products (shop) to avoid endless scrolling
- Add the "back to the top" option for enhanced user experience

---

#### Add a product to the basket

[User story #30:  ](https://github.com/Agnieszka-21/health-store/issues/30)
As a User (Customer), I would like to be able to add products that I want to buy to my shopping basket, so that I can purchase them.

__Acceptance Criteria__
- Given That I am an unregistered user, when I find a product I want to purchase and I click on "add to basket", then the product is added to my shopping basket.
- Given That I am a registered and logged in user, when I find a product I want to purchase and click "add to basket", then the product is added to my shopping basket.
- Given that I am a user,, when I click add to cart on a product that is already in my basket, then the quantity of that product in my basket increases by the defined amount.

__Implementation__
- Develop a shopping basket functionality to track products the user wants to purchase
- Make the basket functionality accessible for both logged in and not logged in/unregistered users
- Develop a method to check whether a product already exists in the basket – if the product exists, increase quantity as required

---

#### View the basket

[User story #31:  ](https://github.com/Agnieszka-21/health-store/issues/31)
As a User (Customer), I would like to be able to view the contents of my shopping basket, so that I can confirm that it contains all the products I want to buy in correct quantities before proceeding to purchase.

__Acceptance Criteria__
- Given that I am a user, when I click on the shopping basket in the nav bar, then I am taken to a page with the details of all the products I have in my basket.
- Given that I am a user, when I add a product to my cart, then I receive a visual confirmation that the product was added to my basket.

__Implementation__
- Develop a page for viewing the shopping basket
- Develop a temporary preview of the shopping cart to display when adding a product to the cart (on medium and larger screens)
- Display number of products in the basket next to the basket icon in the navbar

---

#### Remove a product from the basket

[User story #32:  ](https://github.com/Agnieszka-21/health-store/issues/32)
As a User (Customer), I would like to be able to remove products from my baseket so that I can purchase exactly the products I want to buy.

__Acceptance Criteria__
- Given that I am a user and I have added products to my shopping basket, when I view the basket, then I can remove each specific product listed there.

__Implementation__
- Develop the ability to remove a product from the shopping basket
- Update the total price of all items in the basket when a product is removed

---

#### Adjust the quantity of a product/products in the basket

[User story #33:  ](https://github.com/Agnieszka-21/health-store/issues/33)
As a User (Customer), I would like to be able to adjust the quantity of each product in my baseket so that I can purchase exactly the right quantity of each chosen product.

__Acceptance Criteria__
- Given that I am a user and I have added products to my shopping basket, when I view the basket, then I can adjust the quantity of each product.
- Given that I am a user and I have added products to my shopping basket, when I change the quantity of a product in my shopping basket, then I the total price for all products is adjusted accordingly.

__Implementation__
- Develop the ability to adjust the item quantity in the shopping basket
- Update the total price of all items in the basket when product quantity is changed

---

#### Proceed to checkout

[User story #35:  ](https://github.com/Agnieszka-21/health-store/issues/35)
As a User (Customer), I would like to be able to proceed to the checkout, so that I can purchase my items and place an order.

__Acceptance Criteria__
- Given that I am a user, when I have reviewed my shopping cart, then I have the option to proceed to the checkout.

__Implementation__
- Develop a checkout link on shopping basket page
- Develop a checkout link on shopping basket preview

---

#### Provide personal details needed in the checkout process

[User story #37:  ](https://github.com/Agnieszka-21/health-store/issues/37)
As a User (Customer), I would like to be able to provide my details, so that my order can be processed.

__Acceptance Criteria__
- Given that I am a user who is not logged in, when I proceed to checkout, then I am asked to enter my shipping and billing address
- Given that I am a user who is not logged in, when I enter my billing address, then I can use the same address as my shipping address without having to fill it out twice.
- Given that I am a logged in user,, when I enter my billing and shipping address details, then I have the option to save them to my account.
- Given that I am a logged in user and there are address details saved in my account, when I get to the enter billing and shipping address page, then I have the option to use previously saved details.
- Given that I am a registered user and I am not logged in, when I proceed to enter the address information, then I have the ability to log in to my account and then return to the same page and use previously saved address details.

__Implementation__
- Develop checkout page to collect billing and delivery address details
- Enable option to use billing address for delivery address
- Enable option for users to save address details to their account
- Enable link to login which redirects back to checkout page
- Enable logged in users to select previously saved addresses instead of manual completion of the form

---

#### Pay for the items in the shopping basket

[User story #38:  ](https://github.com/Agnieszka-21/health-store/issues/38)
As a User (Customer), I would like to be able to use my credit/debit card to make a purchase, so that I can pay for my items easily and I can receive my order.

__Acceptance Criteria__
- Given that I am a user, when checking out my shopping basket, then I have the ability to enter my credit/debit card details securely.
- Given that I am a user, when I enter my card details to pay for the transaction, then my payment will be processed.
- Given that I am a user, when I enter my card details and click/tap "buy", then I am kept informed as to the status of the transaction as it progresses.
- Given that I am a user, when my payment fails, then I am redirected back to the checkout page without losing all the inputted information so that I can try again or with a different card.
- Given that I am a user, when I check out and my payment is processed successfully, then I am taken to a confirmation page.

__Implementation__
- Develop secure form to capture credit card details
- Develop link to payment processor
- Develop message system to keep customer informed of processing status
- Develop redirect to appropriate page depending on payment outcome

---

#### Receive an order confirmation

[User story #39:  ](https://github.com/Agnieszka-21/health-store/issues/39)
As a User (Customer), I want to be shown a confirmation page when my payment is accepted and my order is placed, so that I can see that my order will be processed.

__Acceptance Criteria__
- Given that I am a user, when I complete the checkout process and my payment is accepted, then I can see a confirmation page with my order details.
- Given that I am a user, when I complete the checkout process and my payment is accepted, then I receive a confirmation email with my order details.
- Given that I am a registered user and I was logged in when I placed my order, when I have completed the checkout process and my payment was accepted, then my order appears in my user account.

__Implementation__
- Create an order confirmation page that is shown to the user when they successfully complete the checkout process
- Develop an automated order confirmation email containing all important order details
-  Link a new order to a user so that it is visible in the user's profile/account
- Ensure each order has a unique id number

---

#### View product reviews

[User story #73:  ](https://github.com/Agnieszka-21/health-store/issues/73)
As a User (Customer), I would like to be able to submit a review of a product, so that I feel that my opinion matters and is heard.

__Acceptance Criteria__
- Given that I am a user, when I go to a product detail page and scroll down, then I can see a list of existing reviews for that product.
- Given that I am a registered user who recently submitted a review of a product that contained text, when I go to that product's page and scroll down, then I can see my review with a badge "Review awaiting approval".
- Given that I am a registered user who recently submitted a review of a product that contained text, when I go to that product's page and scroll down after an admin approved my review, then I can see my review on the page.
- Given that I am a registered user who recently submitted a review of a product that did not contain text (star rating only), when I go to that product's page and scroll down to the Review section, then I can see my review (rating) on the page.

__Implementation__
- Display all reviews that are marked as "approved" on the relevant product page
- Ensure that reviews without text are automatically marked as "approved" to be displayed right away
- Do not display new reviews with text until they have been approved by an admin
- If a user is logged in and they have a review awaiting approval, display that review under "Reviews" with a suitable badge

---

#### Create a product review

[User story #74:  ](https://github.com/Agnieszka-21/health-store/issues/74)
As a User (Customer), I would like to be able to create a product review/rating, so that my opinion can be shared with other customers to help them make an informed decision.

__Acceptance Criteria__
- Given that I am an unauthenticated user, when I go to a product page and scroll down to "Reviews", then I can click a "Log in to leave a review" button that redirects me to the login page.
- Given that I am a logged in user, when I go to a product page and scroll down to "Reviews", then I can see a "Submit a review" form with a mandatory star rating and an optional text.
- Given that I am a logged in user who just filled the review form, when I click "Submit", then a message is displayed to confirm a successful review submission if the form was valid.
- Given that I am a logged in user who just filled the review form, when I click "Submit", then a suitable warning/information is shown if the form was not valid (star rating missing)

__Implementation__
- Display a "log in to leave a review" button to unauthenticated users
-  Display a review form to logged in users
- Show a confirmation of review submission on success
- Validate form to ensure that a star rating is present in the submitted form (required field)

---

#### Edit a review

[User story #75:  ](https://github.com/Agnieszka-21/health-store/issues/75)
As a User (Customer), I would like to be able to edit my own product review, so that it reflects my current opinion on the product.

__Acceptance Criteria__
- Given that I am a logged in user, when I go to a product page and scroll down to "Reviews", then I can see any reviews I submitted for that product
- Given that I am a logged in user, when I go to a product page and scroll down to "Reviews", then I am shown an "Edit" button next to each of my reviews.
- Given that I am a logged in user, when I click "Edit" next to one of my reviews, then my review is displayed in the review form and I can update it there.
- Given that I am a logged in user who just edited a review, when I click "Submit", then a suitable message is shown to let me know whether my submission was successful or whether I need to add any missing information in the form.

__Implementation__
- Display an "Edit" button next to each product review whose author is the authenticated user
- Make the review populate the review form once user clicked "Edit"
- Show a confirmation of review submission on success
- Validate form to ensure that a star rating is present in the submitted form (required field)
- Ensure that for any reviews with text, they are shown as "awaiting approval" and are displayed only to their logged-in author until they have been approved by an admin.

---

#### Delete a review

[User story #76:  ](https://github.com/Agnieszka-21/health-store/issues/76)
As a User (Customer), I would like to be able to delete my own product review, so that it is not displayed on the page if I change my mind.

__Acceptance Criteria__
- Given that I am a logged in user, when I go to a product page and scroll down to "Reviews", then I can see any reviews I submitted for that product
- Given that I am a logged in user, when I go to a product page and scroll down to "Reviews", then I am shown an "Delete" button next to each of my reviews.
- Given that I am a logged in user, when I click "Delete" next to one of my reviews, then I am asked warned about the action being irreversible and asked for confirmation, or I can cancel the process.
- Given that I am a logged in user who just confirmed they want to delete their review, when I check the list of reviews of the product, then |I can see that the review I deleted is not displayed anymore.

__Implementation__
- Display a "Delete" button next to each product review whose author is the authenticated user
- Display a modal to sk for confirmation to avoid accidental deletions
- Show a message confirming successful review deletion if the user decided to click "Delete"
- If user cancels the deletion process, simply close the modal.

---

#### Mark and save a product as "favourite"

[User story #27:  ](https://github.com/Agnieszka-21/health-store/issues/27)
As a User (Customer), I would like to be able to save my favourite products to a wishlist in my profile/account, so that I can find them easily when I am ready to buy them.

__Acceptance Criteria__
- Given that I am a user, when I navigate to the shop page, then I can tap/click/select a heart icon next to any product.
- Given that I am a logged in user, when I tap the heart icon next to a specific product, then that product is automatically saved to the wishlist in my profile/account.
- Given that I am a user who is not logged in, when I tap the heart icon next to a specific product, then a notification telling me to log in pops up.

__Implementation__
- Add a heart icon next to each product, both on the shop page, and on a product detail page
- Create a functionality that saves the product to a list of favourites" if the user is logged in
- Show a message prompting a user to log in in order to mark a product as "favourite" if they are not logged in
- Make the heart icon accessible to keyboard users as well

---

#### View your wishlist/"favourites"

[User story #28:  ](https://github.com/Agnieszka-21/health-store/issues/28)
As a User (Customer), I would like to be able to view a list of all products I have marked as "favourite" in my profile/account, so that I can access them easily.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to my profile/account, then I can view a list of products I have marked as "favourite".

__Implementation__
- Add the wishlist/"favourites" to a user profile/account
- Make it easily accessible through the profile/account navigation

---

#### Remove a product/products from your wishlist

[User story #29:  ](https://github.com/Agnieszka-21/health-store/issues/29)
As a User (Customer), I would like to be able to remove from my wishlist any products previously marked as "favourite", so that the list stays clean and up to date.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to the wishlist in my profile/account, then I can remove any product from the wishlist.

__Implementation__
- Add a heart icon (filled in/coloured) next to each product listed in the whislist
- Create a functionality that removes a product from the wishlist if the user taps the heart

---

#### View/read a blog with articles and healthy recipes

[User story #48:  ](https://github.com/Agnieszka-21/health-store/issues/48)
As a User (Customer), I would like to have easy access to the stores's blog, so that I can be learn more about a healthy lifestyle.

__Acceptance Criteria__
- Given that I am a user, when I visit the store's website, then I can easily navigate to the blog and read any articles/recipes.

__Implementation__
- Add a blog to the website which contains health and wellness-related articles and healthy recipes
- Add a link to the blog in the nav bar

---

#### Save an article/recipe to a user profile

[User story #49:  ](https://github.com/Agnieszka-21/health-store/issues/49)
As a User (Customer), I would like to be able to save my favourite blog articles and recipes to my profile so that I can access them easily in the future.

__Acceptance Criteria__
- Given that I am a logged in user, when I navigate to any blog post (article/recipe), then I can save the post to my account to easily find it in the future.
- Given that I am a logged in user, when I navigate to my user profile/account, then I can see and easily access all my saved blog posts.

__Implementation__
- Add a "save/bookmark" icon to the blog article/recipe detail template
- Create the functionality to save an article/recipe to the profile for any logged-in user when they click the icon
- Ensure there is a section of the user account where each user can see their saved articles/recipes

---

#### Sign up to a webinar on health- an wellness-related topics

[User story #50:  ](https://github.com/Agnieszka-21/health-store/issues/50)
As a User (Customer), I would like to be able to attend online events organised by the store so that I can be a part of a community of like-minded people who are interested in health and wellness.

__Acceptance Criteria__
- Given that I am a user, when I go to the main navigation, then I can access a page with details of upcoming webinars.
- Given that I am a registered user, when I navigate to the page with upcoming webinars, then I can sign up for any of them.
- Given that I am a user, when I go to my mailbx, then I can see the confirmation email with event details.

__Implementation__
- Add a page for upcoming webinars/online events
- Add a link to this page in the main navigation
- Develop the correct webinar sign-up functionality depending on the user's status (logged-in/logged-out/unregistered)
- Send a registration confirmation email

---

#### Copy the URL of an article/recipe with one click for easy sharing 

[User story #51:  ](https://github.com/Agnieszka-21/health-store/issues/51)


__Acceptance Criteria__
- Given that I am a user, when I visit any article or recipe in the store's blog, then I can click the "copy" icon to copy the page's URL with one click.

__Implementation__
- Add a "copy" icon in the template for every blog article/recipe
- Develop the functionality to copy the URL of that article's/recipe's page just by clicking on that icon
- Display a message "Link copied" so that the user knows what just happened

---

#### Sign up to the newsletter

[User story #40:  ](https://github.com/Agnieszka-21/health-store/issues/40)
As a User (Customer), I want to be able to sign up to the health store's newsletter, so that I can receive special offers, information on exclusive online events, as well as health and wellness-related content.

__Acceptance Criteria__
- Given that I am a user, when I fill the newsletter signup form, then I am added to the list of recepients of the store's newsletter.
- Given that I am a user, when I am considering filling the newsletter signup form, then I can read the store's privacy policy to have a better understanding of what happens to my data.

__Implementation__
- Create a newsletter signup form and place it in the footer so that it is easily accessible on multiple pages
- Create a Privacy Policy and a link to it right below/next to the newsletter signup form for easy access

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

Wireframes were produced for each major page for mobile devices since the intention was to make the site fully responsive so that it displays correctly regardless of the user's screen size. These wireframes were created in the initial stages of work on this project because of the mobile-first approach. This is why they show an earlier version of the project, which kept evolving with time as the development process was progressing.

See the mobile wireframes below:

| Homepage | Shop page | Product detail page |
| :------------------- | :--------------- | :------------- |
| ![Homepage mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_home.png) | ![Shop page mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_shop.png) | ![Product detail mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_product_detail.png) |

| Blog | Recipe detail | Article detail |
| :------------------- | :--------------- | :--------------- |
| ![Blog mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_discover.png) | ![Recipe detail mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_recipe.png) | ![Article detail mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_blog_article.png) |

| Basket | Account | Events |
| :------------------- | :--------------- | :--------------- |
| ![Basket mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_basket.png) | ![Account mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_user_account.png) | ![Events mobile wireframe](https://github.com/Agnieszka-21/health-store/blob/main/assets/wireframes/health_events.png) |


#### Desktop version

__Home page__

The home page provides the user with a clear picture as to the purpose of the site. Under the hero carousel of images showcasing typical products that Health Store sells, there is a clear call to action for the user to go to the shop, with a large button in the center of the page that links directly to the Shop page. At the very top, there is a mimimalistic banner that encourages users to sign up to the newsletter in order to get a discount code for their first purchase - the words "sign up" are a link to the form, present in the footer. There is also a navigation bar at the top of the page with the menu and a search bar, and a footer including social media links, a link to the Privacy Policy page, and a newsletter sign-up form - these elements are visible on all pages.

__Shop page__

The Shop page contains the title ("Products"), 2 dropdowns ("Filter", "Sort"), and a list of all products offered by the store. Each listed product is shown as a card, presenting the most important information like product image, its name, price, category, and average rating. Both the image and the title of each product are clickable links that lead to a detail page for that specific product, should the user be interested in checking out more details. At the bottom of each card, there is also an "Add" button (or "Add to basket" on larger screens) for users who do not need any additional information. The Shop page uses pagination to display 8 products at a time.

__Product Detail pages__

Each product listed on the Shop page leads to its own page where user can find the product's name and price, a detailed description, its ingredients (if applicable), its category, and brand. There is also an average product rating shown, if present, and a field where user can choose the quantity of the product, should they choose to add it to their basket by clicking the "Add to basket" button below. Underneath all that, there is a section displaying any existing reviews for the product, and a button with a call to action: "Log in to leave a review". For logged in users, instead of the button there is a review form they can fill to submit their rating and an optional comment.

__Basket__

This page is accessible to all users. It lists all items currently present in a user's basket (if there are any), including each product's basic information and details regarding quantities, which can be adjusted and updated. Any of the listed products can also be removed completely. Underneath, the basket total, delivery fee, and grand total payable amount are displayed, alongside with the information on how much more one needs to spend to qualify for free delivery. 2 buttons at the bottom of the page let the user decide whether they want to keep shopping, or proceed to checkout.

__Checkout__

This page is also accessible to all users. It displays a checkout form that has to be filled with personal details (name and email), delivery details (address) and payment details that are processed by Stripe. There is also a list of all items that the user is about to buy and a summary of the order (order total, delivery feel, grand total).

For logged in users, there is also a checkbox under the delivery section of the form that can be checked if the user wishes to save their information to the profile. If they saved their personal and address data in the past, the checkout form is pre-filled.

__Checkout Success page__

This page, visible to any user upon placing their order successfully, displays any order details, including order number, basket items, and payment information. This is a confirmation that the order has been processed. Below all the order details, there is a button leading the customer back to the store.

__Account__

This page can be accessed only if user is logged in. Each user can see here a form for their personal and address details, which are used to simplify and speed up the checkout process. If any data has already been saved during a previous checkout (customer can choose this option), the form is pre-filled with the saved data. The data in the form can be updated anytime by changing the desired details in the form and clicking the "Update information" button below.

There are also 3 cards on this page: one for "Order history", one for "Wishlist", and one for "Bookmarked articles/recipes". These cards link user to further pages where they can see a table with their past orders, further leading them to each order's confirmation details, access and manage the list of their favourite items, as well as access and manage their lists of saved articles and recipes.

__Blog__

This page can be accessed by all users and shows 2 options to choose from: one is a link leading to the page listing all blog articles, and the other is a link leading to the page listing recipes. 2 large images are used as backgrounds for these 2 options.

__Articles page, Recipes page__

These 2 pages are very similar to one another and they display a list of all published articles/recipes, with a thumbnail image and a title as a link to the detail page for each blog post.

__Article Detail, Recipe Detail__

These 2 pages display a particular article or recipe. 

For an __article__, there is a title (heading), information on when the post was published, a link icon for copying the URL with one click, and - for loged in users - a bookmark icon that allows user to save the article to their account. Underneath, a banner image for the post is displayed, followed by the article's content. At the bottom of the page, there is a section showcasing related products from the store, if such information has been added to the article. Each product is displayed as an image and a name, both of which are clickable links leading user to this product's detail page. In the bottom right corner, there is also a button that can take user back to the page listing all published articles.

For a __recipe__, the structure of the detail page is only slightly different. Instead of one block of content, the text for each recipe is divided up into an intro, an ingredients section, and a method section. Apart from that, everything else is the same.

__Events__

This page can be accessed by all users and shows a list of all upcoming events. Past events are not shown by default. Each event is a card displaying the event's title, information on when it takes place, who the guest speaker is, and a short description. For unauthenticated users, a "Log in to register" button is shown for each event, and for logged-in users, a "Register" button. By clicking the "Register" button, user is taken to a new page with the particular event's details where they are asked to either confirm their decision with "Register" or to cancel, which sends them back to the Events page. If the user registers for an event, a confirmation email is sent to them.


#### Database schema

Multiple custom models were predicted to be required when building this application.

Built-in Django AllAuth with its User model was applied for the user authentication system, removing the need to build a custom User model. However, a custom UserProfile model was required in order to obtain and store additional information like user's full name, email, and delivery address - should they choose to save these in their account for a faster checkout. The __UserProfile__ model has been copied from Code Instute's walkthrough project, Boutique Ado, and it is present in the Profiles app.

In the Products app, there are further custom models: __Category, Brand, Product, Image, Wishlist,__ and __Review.__ Category and Product have been copied from the walkthrough project Boutique Ado and adapted. The Brand model is very similar to Category. Image is a model for storing product images. Review was based on Code Institute's walkthrough project I Think Therefore I Blog (originally a Comment model).

There are no models in the Basket app.

In the Checkout app, there are 2 models: __Order,__ and __OrderLineItem,__ both copied and adapted from the walkthrough project Boutique Ado. You can find a link to this project under [Credits](#code) in the Credits section.

In the Blog app, further models were created: __Article, Recipe, Reading,__ and __FavouriteRecipe__. The last two models are connected to the UserProfile model and are created/updated with signals, ensuring that each user has automatically one reading list (a list of bookmarked articles), and one list of favourite recipes in their account that they can interact with.

There is just one custom models in the Events app, called __Events__, utilized to store data in relation to monthly online events (webinars) on topics related to health and well-being.

In the home app, there is the __Carousel__ model which allows admin users to manage homepage appearance through carousels of images displayed in the hero section.

Extended CRUD functionalities are possible thanks to these models' interactions with one another through field types like one to one, foreign key, and many to many. Thank to the use of signals certain models automatically create an object as soon as a User or UserProfile object is created (e.g. Wishlist, ReadingList, FavouriteRecipes). 

What is more, I tried to ensure that any admin functionalities related to data manipulation can be handled in the front-end rather than in the built-in Django admin. This reflects the fact that most store admins are not developers, so they need these options for optimal user experience while using the application. Some examples of this are full CRUD for blog articles, recipes, events, carousel, and products.

You can see the models and the relationships between the models in the following database schemas, created using the [drawSQL app](https://drawsql.app/).

The first schema showcases how different models revolve around the User or UserProfile model, using one of these two either in a one-to-one, foreign key, or many-to-many relationship.

![Database schema - models connected with one another through User or UserProfile](https://github.com/Agnieszka-21/health-store/blob/main/assets/database_schema/drawSQL-user.png)

The second schema (see below) depicts product-related database models.

![Database schema - models connected with one another through Product model](https://github.com/Agnieszka-21/health-store/blob/main/assets/database_schema/drawSQL-product.png)

The Carousel model has no connection with any of the other models.


### The Surface Plane

#### Design
The design of the website is supposed to convey ease, simplicity, and naturalness. This communicates on a deeper level the store's commitment to selling products which are close to nature, environmentally friendly, and which support one's health and well-being.

The color palatte is based on colors associated with nature and simplicity.

The main color - dark green #013a20 - has been used throughout the page in the header and footer, and also for most elements that the end-user might interact with like buttons and links to keep the website's design coherent and simple. It is a deep shade of green, bringing to mind nature, especially the plant world. This color reinforces the store's goals: we are here to support your health and to provide products that are close to nature.

The main background color of the page is a pure white color #fff. Since most of the text is liquorice black #1C0F13 or pure black #000, white provides excellent contrast, ensuring the website's optimal accessibility. It also works well for both dark green (e.g. used in links) and light sage #cdd193 used for the "Shop now" button on the homepage as well as while hovering over or focusing on any other buttons.

Most elements that are links use the dark green color, are underlined, and the font-weight is bold to ensure plenty of contrast with the background since these are elements that the end-user will interact with. On hover/focus, the text decoration (underline) disappears for both better readability and to ensure that the user knows the link is active. An exception from that would be product names on the Shop page that are black and not underlined since the convention is that these are links to each product's detail page. On hover/focus, each product name becomes underlined to indicate that it is an active link.

All buttons that are shown only to authenticated staff and admin users have a pale yellow color #FCFFD9 so that they are clearly discernible. This ensures easier website navigation for any staff members and visual clarity as to what is shown to the end-user, and what is hidden from them.

The following table created with [Contrast Grid](https://contrast-grid.eightshapes.com/) shows the color palette utilised in this project.

![Contrast Grid color palette](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/contrast_grid.png)


#### Typography
Two types of Google fonts have been used in this project.
For the brand name "Health Store", shown at the top of each page in the center of the header, the Orelega One font was used to provide an eye-catching yet classic and simple design. Since this is a serif font, serif was also declared as a fallback font-family in the base.css file. To reinforce the business's dedication to natural and eco-friendly products, a herb emoji was inserted in between "Health" and "Store", tying it also to the herb emoji in the favicon.

Montserrat font-family was used for all remaining text, in various weights ranging from 100 to 900. This is a sans-serif font, easily readable, light and easy on the eyes, which matches the website's overall feel of ease, simplicity, and naturalness.


#### Images
Images used in the homepage carousel as well as on the main blog page are free-licence images from Pexels. 

Product images have been copied from each product's brand's or main vendor's websites to allow for using high-quality, multiple images for each product as would be the industry standard - [you can find exact sources here](#content).

Images used as thumbnails on the Articles page, and as banners on each article's detail page, were copied from Holland & Barrett's blog posts. Images used as thumbnails on the Recipes page, and then in a larger size on each recipe's detail page, were copied from BBC Good Food's recipe pages. You can find more information on sources of any images used throughout the application under [Content](#content).


## Features

### Homepage

__Promo banner linked to newsletter form__

The promo banner at the very top of the page informs users that they can get a discount code if they sign up to the store's newsletter. When clicked, the "sign up" link sends the user to the newsletter form in the footer.

![Promo banner](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_promo_banner.png)

__Header - the logo, navigation bar, search bar__

The store's logo is shown in the center of the navigation bar and it acts as a link to the homepage.

The navigation bar is shown in 3 versions, depending on whether the user is logged in, user is not logged in, or user is an authenticated admin. In these 3 versions the main navbar stays the same, displaying the following options: Shop, Blog, Events, a Profile icon, and a Basket icon (screenshot below).

![Header - navbar](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_header.png)

What changes is the dropdown under the profile icon. For an unauthenticated user it looks like this:

![Navbar profile menu](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_navigation_profile.png)

For a logged in end-user or staff user, it shows the following options: Account and Log out.

![Navbar profile menu - end-user logged in](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_navigation_profile_loggedin.png)

For a logged in admin, it shows the following options: Admin Panel, Account and Log out.

![Navbar profile menu - admin user logged in](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_navigation_profile_admin.png)

__Hero section carousel__

The hero section consists of a responsive full-width carousel with 4 images that slide left at regular intervals. User can also control the carousel by clicking a right/left arrow or one of the 4 thin rectangles at the bottom of the carousel where each rectangle stands for a specific image.

![Carousel](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_carousel.png)

__Shop now button__

Underneath the carousel, there is a large "Shop now" button, which redirects the user to the Shop page when clicked. Because of its central placement on the page, it reinforces the application's aim to sell products to customers.

![Shop now button](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_button.png)

__Footer - newsletter signup form, social icons, privacy policy link__

The footer includes a newsletter signup form embedded from MailChimp, as well as links to social media pages, which open in a new tab each. It also has a link to the store's Privacy Policy which opens in a new tab, and copyright information.

![Footer](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_footer.png)


### Shop page

__Title, filtering, sorting__

At the top of the shop page, there is a title "Products" and 2 dropdowns: one for filtering products by category, and one for sorting products according to their price/name/average rating.

If filtering by a category is active, the chosen category is shown under the title, and a link to all products is visible on the left side. The same link is displayed when sorting is active, and when clicked any sorting/filtering is removed.

![Shop page - category filter active](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/products_filtered.png)

![Shop page - sorting active](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/products_sorted.png)

__Main section - list of products__

Each product is shown as a card, and there are up to 8 products per page. For any authenticated users, a heart icon is shown next to each product, adding a wishlist functionality. For admin users, there are additionally 2 buttons for each product - Edit and Delete. See the screenshot below.

If the user is logged in, the page looks like this:
![Shop page - view for logged-in users](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/products_loggedin.png)

For unauthenticated users, heart icons next to each product are not shown:

![Shop page - unauthenticated user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/products_customer.png)

__Pagination__

The shop page is paginated, so that there are only 8 products on each page - or less on the last page.

![Pagination](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/products_pagination.png)


### Product detail page

__Product images__

For added visual interest, on each product's detail page, there are up to 3 images of the product. The main image is shown as larger, the other 2 as thumbnails.

![Product detail page - images and product information](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail.png)

These images switch places when clicked so that any of the available product images can be shown in the larger size.

![Product images - switched](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail_img_switch.png)

Additionally, the user can open any image in a new tab with a click on the larger image.

__Product information__

The following details are shown to all users: product name, its price, average rating, a link to product's category, a link to product's brand (which opens in a new tab since it is an external link), description, and ingredients. Additionally, logged-in users can see a heart icon next to the product name which allows them to add product to their wishlist.

__Quantity input and "Add to basket" button__

Under product information, there is an input field for the user to choose quantity (from 1 to 9) of the product, and an "Add to basket" button which adds the product to the shopping basket in the quantity specified in the input field. 

A success message is shown upon successful addition of the product to the basket. The message can be closed on the close (x) button. It also includes a "Go to checkout" button which redirects the user to the basket page.

![Success message - product added to basket](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/msg_addtobasket.png)

Similar messages are displayed for any user interactions with the application, letting them know whether their operation has been successful or not, and what the recommended solution is.

__Product reviews__

At the bottom of the page, there is a Reviews section for that particular product. It displayes any existing and approved by admin reviews. For an unauthenticated user, there is also a "Log in to leave a review" button, redirecting them to the Log in page.

![Reviews as displayed to an unauthenticated user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail_reviews.png)

For a logged-in user, instead of the button, there is a review form which they can fill and submit. A star rating required while the text field can be left empty. If the user submits only a star rating, their review is displayed under "Reviews" right away. If they decided to add text, they can see their review with a badge "Review waiting for admin's approval". The review is not visible to any other users until it has been approved by an admin.

![Reviews as displayed to a logged-in user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail_reviews_loggedin.png)

For any existing reviews submitted by this particular user, there are also 2 buttons shown for each review: "Edit" and "Delete". If the user clicks "Edit", their review populates the review form and can be updated and submitted. Should the edited review contain text, it is again not displayed to the general public until it has been approved by an admin.

![Edit review](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail_reviews_loggedin_edit.png)

The "Delete" button opens a modal where the user can choose either "Cancel" or "Delete". The modal warns the user that their action is irreversible, and if the user chooses "Delete", the review disappears from the website, and the database.

![Delete review modal](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/product_detail_reviews_loggedin_delete.png)

### Basket page

__List of basket items__

The page displays a list of all items present in the user's basket. Each product is shown inside a card, which includes basic product information: product's primary image, its name, SKU, and price. There is also the same quantity input as the one shown on a product detail page, as well as 2 links: "Update" and "Remove". The first link saves any product quantity adjustments, and the "Remove" link deletes the item from the user's basket. Under all products, there is a basket summary, stating basket total price, delivery fee, and the grand total. If the basket's value is under EUR 50.00, the user is also informed how much more they need to spend in order to avail of free delivery. At the bottom of the page, there are 2 buttons. The "Keep shopping" button redirects the user back to the shop page, while the "Go to checkout" button takes them to the checkout page.

![Basket page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/basket.png)

If there are no items in the user's basket, the page informs them that their basket is empty, and there is a "Keep shopping" button redirecting them to the shop page.


### Checkout page

__Checkout form__

The checkout form has 3 sections. The first, "Details", collects user's full name and email. The second, "Delivery", collects user's delivery address information. The third, "Payment", comes from Stripe and collects user's credit/debit card details. There are also 2 buttons: "Adjust basket" takes the user back to the basket page, and "Complete order" submits the form so that their payment can be processed and their order is placed. While the processing is happening (usually up to a few seconds), a green overlay with the animated loading icon is displayed.

![Checkout page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/checkout.png)

If the user is not authenticated, at the bottom of the form, they can click a link to the "Log in" or "Sign up" page if they wish to use an account.

![Checkout form - unauthenticated user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/checkout2.png)

Should the user be logged in, at the bottom of the delivery section of the form, there is a checkbox which they can check in order to save their personal and address details to their account for a faster checkout in the future.

If the logged-in user already saved their data in the past, the checkout form will be populated with those details.

__Order summary__

On the checkout page, there is also an order summary showing all basket items with their most important details, and the basket total, delivery fee, and grand total amount to ensure the customer is clear on what they are buying and how much they are going to be charged.


### Checkout success page

Once the payment has been processed, the customer is redirected to the page where they can see a thank you message and exact details of their order. They are also informed that a confirmation email has been sent and should be able to find the email in their mailbox within a few minutes.

![Checkout success page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/checkout_success.png)

### Account page

__Profile form__

The form can be filled with the user's personal and address details, which are then used to speed up the checkout process, as long as the user is logged into their account. These details can be updated at any point and the changes are saved by the user clicking the "Update information" button below.

__Links to order history, wishlist, and boomarked articles/recipes__

Furthermore, there are 3 cards with distinct titles, letting the user know which page they can redirect them to.

![Account page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/account.png)

__Order history__

This page lists user's past orders. Each order number on the list is a link to a separate page, where the user can check this particular order's details.

![Order history](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/account_orders.png)

By clicking the order number link, the user is redirected to the order confirmation page.
![Specific order from history](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/account_order.png)

__Wishlist__

The wishlist is where any products "liked" by the user are shown. Each product's image is a link to this product's detail page. The user can remove any of these items from the wishlist simply by clicking the heart icon. Lastly, there is also a button which redirects the user back to their account page.

![Wishlist](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/account_wishlist.png)

If there are no items on the wishlist, the user is informed about it.

![Empty wishlist](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/wishlist_empty.png)

__Bookmarked articles/recipes__

This page lists any articles and recipes that the user has saved by clicking the bookmark icon on their respective detail pages. Bookmarked recipes are shown separately from bookmarked articles for increased clarity and better user experience. For each item on the list, the thumbnail image and the title are shown, together with a solid bookmark icon. By clicking this icon, the user can remove the item from the page. If the user clicks the title, it redirects them to the item's detail page. If the user has not saved any articles or recipes, the "Check out articles" or "Check out recipes" button is shown. At the bottom of the page, there is also a "Back to profile" button redirecting the user to their account page.

![Bookmarked articles/recipes](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/account_bookmarked.png)

### Blog

__Blog page__
This is a page showing simply 2 options to choose from: articles, and recipes. This is where the user chooses which ones they would like to check out by clicking one of the 2 links. For each option, an image is used as background for added visual interest.

![Blog page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/blog.png)

__Articles__

This page lists all published articles, and for each of them the user can see a thumbnail image and their title, which is a clickable link redirecting the user to this article's detail page.

![Articles page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/articles.png)

For logged-in staff users, further options are visible: the "Create a new article" button, and an "Edit" button for each of the articles. The list is shown in 3 segments: approved and scheduled for publishing, waiting for admin's approval, and all published articles.

For logged-in admins, in addition to the options visible to the staff, there are "Delete" buttons next to any articles that have not been published yet, and "Unpublish" buttons next to each article that has already been published. 

![Articles page - admin user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/admin_articles.png)

__Create article page__

This page, accessible to any staff users, shows an article form where all required details can be added. Any articles submitted successfully through this form are shown on the articles page, under "Waiting for admin's approval". 

![Create article page - part 1](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/admin_create_article.png)
![Create article page - part 2](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/admin_create_article2.png)

__Edit article page__

This page dispalys an article form identical to the one on the article creation page, but populated with relevant article data. For admins, this form includes one additional field, "approved", which can be checked to indicate that the article is ready to be shown on the website to the general public. If "approved" is checked, the "publication date" field is required for submitting the form - in case the user forgets about it, they are shown a suitable reminder.

__Unpublish article__

This page is accessible only to admins and it asks the user to choose either "Cancel" or "Unpublish" - using defensive design here and for any deletions reduces the risk of mistakes.

![Unpublish article page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/admin_unpublish_article.png)

__Delete article__

This page, accessible only to admins, warns the user that should they choose to delete an article, their decision is irreversible. They can choose to cancel or proceed with their request, which results in the article being deleted.

![Delete article](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/admin_delete_article.png)

__Article detail__

A specific article is displayed here with the following details: a title, publication date, the link icon for copying the URL with one click and easy sharing, a banner image, and the article's content. If any products have been marked as related to this article, the "Recommended products" section is shown at the bottom of the page. There is also a button redirecting the user back to the main page listing articles.

![Article detail](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/article_detail.png)

![Article detail - recommended products](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/article_detail_recommended.png)

For any authenticated users, there is a bookmark icon next to the link icon, which allows the user to save that article to their profile (bookmark it) with one click.

![Bookmark article icon](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/article_detail_bookmark.png)

For staff users and admins, further options are visible (buttons like "Edit", "Unpublish", or "Delete", depending on the user's permissions and the article's status).

__Recipes__

This page lists all published recipes, and it is nearly identical to the artiles page regarding its layout, and exactly identical when it comes to access permissions and available funcitonalities.

__Staff/admin pages for recipes__

These are shaped in a very similar way to the staff/admin articles pages, so a detailed description is unneccessary. 

__Recipe detail__
A specific recipe is displayed here with the following details: an image, title, publication date, the link icon for copying the URL with one click and easy sharing, a description, a list of ingredients, and numbered list of preparation steps (method). If any products have been marked as related to this recipe, the "Recommended products" section is shown at the bottom of the page. There is also a button redirecting the user back to the main page listing recipes.

![Recipe detail - part 1](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/recipe_detail.png)
![Recipe detail - part 2](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/recipe_detail2.png)

Any other functionalities that are available to logged-in users, staff users, and admin users on an article detail page, are available for recipes as well.


### Events

The user can see here a list of upcoming online events (webinars), each of them shown as a card with the following details in the header: event title, guest speaker, and when it takes place. The body of each card contains a short description of the event and the "Log in to register" button if the event has not been cancelled.

![Events page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/events.png)

If the event is cancelled, a badge with this information is shown instead of the button.

![Events page - cancelled event](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/events_cancelled.png)

For a logged-in user, there is a "Register" button shown instead of the "Log in to register" option, redirecting them to the registration page.

![Events page - authenticated user](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/events_loggedin.png)

For admins, this page is shown with additional buttons: "Create a new event" at the top of the page, as well as "Edit" and "Delete" for each existing event in the footer of its card.

__Event registration page__

If an authenticated user chose to click the "Register" button, they are redirected to this event's registration page that summarizes the most important details and lets them either "Register" or "Cancel" if they changed their mind. The page also informs them that a confirmation email has been sent, and it should appear in the user's mailbox within a few minutes.

![Event registration page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/event_register.png)

__Admin pages for events__
These pages designed very similarly to the recipe and article management pages. What might be worth mentioning for clarity is that an admin can cancel an event by clicking "Edit" next to an event and checking the "Cancelled" box.


### Sign up page
The Sign Up option in the navigation menu is shown when user is not logged in. This page presents a sign up form, allowing the user to create an account and therefore access further features.

![Sign up page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/sign_up.png)


### Log in page
The Log In option in the navigation menu is shown when user is not logged in. This page presents a log-in form, allowing the user to log into their account and access further features.

![Log in page](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/log_in.png)


### Log out page
The Log Out option in the navigation menu is shown when user is logged in. This page asks for a log-out confirmation, allowing the user to log out of their account and keep their personal data safe. Just like the two previous pages, it is based on an AllAuth template with custom styling.

### Additional screenshots
Additional screenshots (mainly for pages accessed only by admins) are available in [this folder](https://github.com/Agnieszka-21/health-store/tree/main/assets/screenshots).


## Future Enhancements

While the following User Stories have not been completed as they have been deemed unnecessary for an MVP, they present a wide range of potential enhancements that could be added to the project in the future.

- [#20 Delete a user profile/account](https://github.com/Agnieszka-21/health-store/issues/20) - so that User (Customer) can remove their account if they think they are not going to need it anymore
- [#21 Sign in to the user profile/account using a social media login](https://github.com/Agnieszka-21/health-store/issues/21) - so that users can utilise their existing login credentials for easy authentication
- [#34 Save the shopping basket for later](https://github.com/Agnieszka-21/health-store/issues/34) - so that the basket does not get lost the moment the user closes the tab with their basket
- [#36 Create a user account during checkout](https://github.com/Agnieszka-21/health-store/issues/36) - so that new user can easily and quickly create an account
- [#63 Keep the existing basket when logging in](https://github.com/Agnieszka-21/health-store/issues/63) - so that users with an existing account can log in and benefit from a pre-filled checkout form for convenience
- [#41 Unsubscribe from the newsletter](https://github.com/Agnieszka-21/health-store/issues/63) - so that the email campaign is GDPR compliant (this requires actually creating a newsletter campaign though)
- [#42 Re-subscribe to the newsletter](https://github.com/Agnieszka-21/health-store/issues/63) - similar to the above.

Another possible enhancement could be handling stock data and using that information to automatically update the maximum quantity of a product available for purchase for a customer.


## Testing

### Testing Overview

Continuous testing was an integral part of the development process. I used numerous print and cosole.log statements, which were removed as specific features reached their desired shape and functionality. The statements helped me follow what is happening, especially in the more complex scenarios where multiple things were affected by just one change and where multiple functions worked together, calling one another and handling a wide range of scenarios.

While there is still a significant potential for further enhancements in a project as complex as this one, I ensured to handle all errors that I encountered, and took great care to minimise the risk of any errors occurring on submission of forms. Multiple success/error messages are shown to users to confirm their actions, or inform them about any issues and recommended solutions. Validation was also handled at the earliest stages while developing the forms, limiting the users' access to information that can be handled in the backend in a more secure way where possible.

Manual tests were conducted mainly in my development environment, and once results were positive, they were re-checked within the live application after it was deployed to Heroku. 

Automated tests were also written to confirm that each view renders the correct template, to ensure correct access permissions to different pages for various users (customers, staff, admin), and many more.


### Manual Testing

While testing every single functionality as I was creating and refining it was essential to progressing with this project, I also applied a more structured approach to testing once everything seemed to work correctly in order to double-check the code's behavior and ensure that I handled any possible scenarios to avoid any issues. The table below documents this more structured approach, where I tested all possible functionalities as well as likely user inputs in [the live version of the app](https://health-store-ff0f909bba3d.herokuapp.com/).


| Functionality being tested | Expected Outcome | Actual Outcome | Result (pass/fail) |
| :------------------------- | :--------------- | :------------- | :-------------------- |
| "Sign up" link in the promo banner | takes the user to the newsletter signup form in the footer | as expected | pass |
| Logo "Health Store" | takes the user to the homepage when selected on any page | as expected | pass |
| Navbar profile icon | opens/closes a dropdown when selected | as expected | pass |
| Navbar link "Sign up" under the profile icon | takes the user to the Sign up page | as expected | pass |
| Navbar link "Log in" under the profile icon | takes the user to the Log in page | as expected | pass |
| Navbar link "Shop" | takes the user to the Shop page | as expected | pass |
| Navbar link "Blog" | takes a logged-in user to the blog page | as expected | pass |
| Navbar link "Events" | takes a logged-in user to the Events page | as expected | pass |
| Navbar link "Admin Panel" under the profile icon | takes a logged-in admin to the Admin Panel page | as expected | pass |
| Navbar link "Account" under the profile icon | takes a logged-in user to their account/profile | as expected | pass |
| Navbar link "Log out" under the profile icon | takes a logged-in user to the log out page | as expected | pass |
| Header: Search bar | lets the user type a keyword and search for a product | as expected | pass |
| Footer: Facebook icon | opens Facebook in a new tab | as expected | pass |
| Footer: Instagram icon | opens Instagram in a new tab| as expected | pass |
| Footer: YouTube icon | opens YouTube in a new tab | as expected | pass |
| Footer: Privacy Policy link | opens Privacy Policy page in a new tab | as expected | pass |
| Footer: Newsletter form | submits datails entered by user to the MailChimp account | as expected | pass 
| Sign up page: "Sign up" button | creates a user account & profile, sends a verification email, redirects the user to the homepage and shows a suitable message | as expected | pass |
| Sign up page: "log in" link | redirects the user to the Log in page | as expected | pass |
| Log in page: "sign up" link | redirects the user to the Sign up page | as expected | pass |
| Log in page: "Log in" button | logs the user into their account, redirects them to the homepage, shows a success message | as expected | pass |
| Log in page: "Forgot password" link | redirects the user to the Password Reset page | as expected | pass |
| Log out page: "Log out" button | logs the user out of their account, redirects them to the homepage, shows a success message | as expected | pass |
| Home: "Shop now" button | redirects user to the Shop page | as expected | pass |
| Shop: Sort dropdown | lets the user choose how to sort the products | as expected | pass |
| Shop: Filter dropdown | lets the user choose a product category | as expected | pass |
| Shop: Filter dropdown | lets the user choose a product category, displays a category badge | as expected | pass |
| Shop: "Back to all products" link | resets any filters/sorting | as expected | pass |
| Shop: "Add" or "Add to basket" button | adds a product to the basket with quantity equal to 1 | as expected | pass |
| Shop: heart icon (logged-in users only) | updates the wishlist, changes the icon's color | as expected | pass |
| Shop: product name/image links | redirect the user to a product detail page for the chosen product | as expected | pass |
| Shop: "Edit" button (logged-in admins only) | redirect admin to the edit product page | as expected | pass |
| Shop: "Delete" button (logged-in admins only) | redirect admin to the delete product page | as expected | pass |
| Edit product page (logged-in admins only): "Cancel" button | redirect admin to the shop page | as expected | pass |
| Edit product page (logged-in admins only): "Update Product" button | save changes, redirect admin to product detail page | as expected | pass |
| Delete product page (logged-in admins only): "Cancel" button | redirect admin to the shop page | as expected | pass |
| Delete product page (logged-in admins only): "Delete" button | delete product, redirect admin to the shop page | as expected | pass |
| Product detail: product images | thumbnail images and main image switch places when clicked | as expected | pass |
| Product detail: category link | redirects user back to the Shop page filtered by the category | as expected | pass |
| Product detail: brand link | opens the website of a product's brand in a new tab | as expected | pass |
| Product detail: quantity input | lets the user choose product quantity between 1-9 | as expected | pass |
| Product detail: "Add to basket" button | adds the product to basket | as expected | pass |
| Product detail: "Log in to leave a review" button | redirects user to the Log in page | as expected | pass |
| Product detail: "Leave a review" form and submit button (logged-in users only) | allows the user to submit a product review | as expected | pass |
| Product detail: "Edit" under the user's review (logged-in users only) | displays the review in the review form ready for editing | as expected | pass |
| Product detail: "Delete" under the user's review (logged-in users only) | opens a modal with 2 options: Close (closes the modal) or Delete (deletes the review) | as expected | pass |
| Product detail: "Edit" button (logged-in admins only) | redirect admin to the edit product page | as expected | pass |
| Product detail: "Delete" button (logged-in admins only) | redirect admin to the delete product page | as expected | pass |
| Basket - empty: "Keep shopping" button | redirects user back to the shop page | as expected | pass |
| Basket - full: quantity input | lets the user choose product quantity from 1-9 | as expected | pass |
| Basket - full: "Update" link | applies any changes in product quantity | as expected | pass |
| Basket - full: "Remove" link | removes a product from basket | as expected | pass |
| Basket - full: "Go to checkout" button | redirects user to the checkout page | as expected | pass |
| Basket - full: "Keep shopping" button | redirects user back to the shop page | as expected | pass |
| Checkout: form | user can fill it with their data needed to check out | as expected | pass |
| Checkout: form - "Save to profile" checkbox (logged-in users only) | lets user save their delivery data for | as expected | pass |
| Checkout: "Adjust basket" button | redirects user back to their basket | as expected | pass |
| Checkout: "Complete order" button | submits the order, processes the payment, and redirects user to success page or back to checkout if the form is not valid (any errors are displayed) | as expected | pass |
| Checkout success: button | redirects user to the shop page | as expected | pass |
| Blog page: "Articles" link/button | takes user to the page listing articles | as expected | pass |
| Blog page: "Recipes" link/button | takes user to the page listing recipes | as expected | pass |
| Articles page: article title link | takes user to the article detail page | as expected | pass |
| Articles page: "Create a new article" button (logged-in staff users only) | takes user to the create article page | as expected | pass |
| Articles page: "Edit article" button (logged-in staff users only) | takes user to the edit article page | as expected | pass |
| Articles page: "Delete article" button (logged-in admins only) | takes user to the delete article page to confirm/cancel | as expected | pass |
| Articles page: "Unpublish article" button (logged-in admins only) | takes user to the unpublish article page to confirm/cancel | as expected | pass |
| Unpublish article page (logged-in admins only): "Cancel" button | takes user to the articles page | as expected | pass |
| Unpublish article page (logged-in admins only): "Unpublish" button | redirects user to the articles page, the unpublished article is listed under "Waiting for admin's approval" | as expected | pass |
| Delete article page (logged-in admins only): "Cancel" button | takes user to the articles page | as expected | pass |
| Delete article page (logged-in admins only): "Delete" button | deletes article and takes user to the articles page | as expected | pass |
| Recipes page: recipe title link | takes user to the recipe detail page | as expected | pass |
| Recipes page: "Create a new recipe" button (logged-in staff users only) | takes user to the create recipe page | as expected | pass |
| Recipes page: "Edit recipe" button (logged-in staff users only) | takes user to the edit recipe page | as expected | pass |
| Recipes page: "Delete recipe" button (logged-in admins only) | takes user to the delete recipe page to confirm/cancel | as expected | pass |
| Recipes page: "Unpublish recipe" button (logged-in admins only) | takes user to the unpublish recipe page to confirm/cancel | as expected | pass |
| Unpublish recipe page (logged-in admins only): "Cancel" button | takes user to the recipes page | as expected | pass |
| Unpublish recipe page (logged-in admins only): "Unpublish" button | redirects user to the recipes page, the unpublished recipe is listed under "Waiting for admin's approval" | as expected | pass |
| Delete recipe page (logged-in admins only): "Cancel" button | takes user to the recipes page | as expected | pass |
| Delete recipe page (logged-in admins only): "Delete" button | deletes recipe and takes user to the recipes page | as expected | pass |
| Article detail: link icon | copies the article's URL with one click, show "Link copied" notification | as expected | pass |
| Article detail: bookmark icon (logged-in users only) | saves the article to user's profile | as expected | pass |
| Article detail - recommended products: product image/name link | redirects user to product detail page | as expected | pass | 
| Article detail: "Back to articles" button | redirects user to the artilcles page | as expected | pass |
| Article detail: "Edit" button (logged-in staff users only) | redirects user to the edit artilcle page | as expected | pass |
| Article detail: "Unpublish" button (logged-in admins only) | redirects user to the unpublish artilcle page | as expected | pass |
| Recipe detail: link icon | copies the recipe's URL with one click, show "Link copied" notification | as expected | pass | 
| Recipe detail: bookmark icon (logged-in users only) | saves the recipe to user's profile | as expected | pass | 
| Recipe detail - recommended products: product image/name link | redirects user to product detail page | as expected | pass | 
| Recipe detail: "Back to recipes" button | redirects user to the recipes page | as expected | pass |
| Recipe detail: "Edit" button (logged-in staff users only) | redirects user to the edit recipe page | as expected | pass |
| Recipe detail: "Unpublish" button (logged-in admins only) | redirects user to the unpublish recipe page | as expected | pass |
| Events: "Log in to register" button | redirects user to the Log in page | as expected | pass |
| Events: "Register" button (logged-in users only) | redirects user to the even registration page | as expected | pass |
| Events: "Create a new event" button (logged-in admins only) | redirects admin to the create event page | as expected | pass |
| Events: "Edit event" button (logged-in admins only) | redirects admin to the edit event page | as expected | pass |
| Events: "Delete event" button (logged-in admins only) | redirects admin to the delete event page | as expected | pass |
| Edit event (logged-in admins only): "Cancelled" checkmark in the form | once the form is submitted successfully, the event on events page has a badge "Event cancelled" instead of the registration button (shown to all users) | as expected | pass |
| Edit event (logged-in admins only): "Cancel" button | redirects admin to the events page | as expected | pass |
| Edit event (logged-in admins only): "Update Event" button | saves changes, redirects admin to the events page | as expected | pass |
| Delete event (logged-in admins only): "Cancel" button | redirects admin to the events page | as expected | pass |
| Delete event (logged-in admins only): "Delete" button | deletes event, redirects admin to the events page | as expected | pass |
| Event registration page: "Register" button | sends a registration confirmation email, shows a success message | as expected | pass |
| Event registration page: "Cancel" button | redirects user to the events page | as expected | pass |
| Account: "Update information" button | submits the profile form, saving user's data | as expected | pass |
| Account: "Order history" | redirects the user to the order history page | as expected | pass |
| Account: "Wishlist" | redirects the user to the wishlist page | as expected | pass |
| Account: "Bookmarked articles/recipes" | redirects the user to the page with their saved articles/recipes | as expected | pass |
| Order history page: order link | redirects the user to order confirmation page | as expected | pass |
| Order history page: "Back to profile" button | redirects user back to their account page | as expected | pass |
| Order detail page: "Back to orders" button | redirects user back to their order history page | as expected | pass |
| Wishlist page: heart icon | when clicked, removes a product from wishlist | as expected | pass |
| Wishlist page: "Back to profile" button | redirects user back to their account page | as expected | pass |
| Bookmarked articles/recipes page: bookmark icon | when clicked, removes an article/recipe from the list | as expected | pass |
| Bookmarked articles/recipes page: "Back to profile" button | redirects user back to their account page | as expected | pass |
| Admin Panel page (logged-in admins only): "Add a new product" card | redirects admin to the create product page | as expected | pass |
| Admin Panel page (logged-in admins only): "Manage reviews waiting for approval" card | redirects admin to the review management page | as expected | pass |
| Admin Panel page (logged-in admins only): "Create a new carousel" card | redirects admin to the create carousel page | as expected | pass |
| Admin Panel page (logged-in admins only): "Choose carousel" card | redirects admin to the create product page | as expected | pass |
| Review management page (logged-in admins only): "Cancel" button | redirects admin back to the Admin Panel | as expected | pass |
| Review management page (logged-in admins only): "Save Updates" button | saves changes as marked (approve/delete) and redirects admin to the shop page | as expected | pass |
| Create carousel page (logged-in admins only): "Cancel" button | redirects admin back to the Admin Panel | as expected | pass |
| Create carousel page (logged-in admins only): "Add carousel" button | creates carousel, redirects admin back to the Admin Panel | as expected | pass |
| Choose carousel page (logged-in admins only): "Cancel" button | redirects admin back to the Admin Panel | as expected | pass |
| Choose carousel page (logged-in admins only): "Activate carousel" button | makes the carousel chosen from the dropdown appear on the homepage, redirects admin to the homepage | as expected | pass |
| Choose carousel page (logged-in admins only): "Edit" button | redirects admin to the edit carousel page | as expected | pass |
| Choose carousel page (logged-in admins only): "Delete" button | redirects admin back to the delete carousel page | as expected | pass |
| Edit carousel page (logged-in admins only): "Cancel" button | redirects admin to the Admin Panel | as expected | pass |
| Edit carousel page (logged-in admins only): "Edit carousel" button | saves changes, redirects admin to the Admin Panel | as expected | pass |
| Delete carousel page (logged-in admins only): "Cancel" button | redirects admin to the Admin Panel | as expected | pass |
| Delete carousel page (logged-in admins only): "Cancel" button | deletes carousel, redirects admin to the Admin Panel | as expected | pass |


### Validator Testing

__HTML__

The [W3C Markup Validation Service](https://validator.w3.org/) was used to check any html files containing custom code. All files are passed the validation test without errors - you can see relevant screenshots [here](https://github.com/Agnieszka-21/health-store/tree/main/assets/validators/html).

__CSS__

All css files containing custom styling for the application has been checked in the [W3C CSS Validation Service Jigsaw](https://jigsaw.w3.org/css-validator/) and have no errors - you can find relevant screenshot in [this folder](https://github.com/Agnieszka-21/health-store/tree/main/assets/validators/css).

__JavaScript__

[JSHint](https://jshint.com/) has been used to validate all JavaScript files in the application. The files returned no errors and any related screenshots can be found [here](https://github.com/Agnieszka-21/health-store/tree/main/assets/validators/jshint).

__Python__

All Python files containing custom code have been run through the [Code Institute's Python linter](https://pep8ci.herokuapp.com/#) in order to ensure that they meet the PEP8 requirements/recommendations. No errors were found - you can find relevenat screenshots in [this folder](https://github.com/Agnieszka-21/health-store/tree/main/assets/validators/python).


### Lighthouse and Webaim Wave Testing

The deployed website has been tested using both Lighthouse and WebaAim WAVE in order to ensure that it performs well and meets accessibility criteria. 

Lighthouse accessibility and SEO scores are within the optimal green range on all tested pages. However, it is worth noting that using Stripe, MailChimp, AWS, as well as applying Bootstrap, Google Fonts, and Font Awesome has led to Best Practices and Performance scores being slightly lower - some of them in the green range, some in the yellow range. From the perspective of a business using this web application, it made more sense to keep these external resources. The mobile view scores are usually slightly lower, especially when any images are involved, despite all media files having been compressed and optimized. This would indicate that for optimal performance, each image should be available in at least two sizes, so that the mobile version does not have to load any images meant for larger screens.

When it comes to WebAim WAVE, a few errors were indicated. There is a missing label error coming from the embedded newsletter form from MailChimp. There is a contrast issue indicated in the homepage carousel (which was copied from Bootstrap documentation), even though the element it applies to is visually hidden. There are also missing labels on the Shop page for the invisible input field for each product's quantity, and on the product detail page empty buttons were found (again, related to the quantity input field - which in this case is visible). Since the code for product quantity input has been copied from the Boutique Ado walkthrough project, I decided to leave it as it is for the moment. These errors can certainly be eliminated, so this has been added to the list of potential future enhancements.

You can find screenshots with relevant results here for [Lighthouse](https://github.com/Agnieszka-21/health-store/tree/main/assets/lighthouse), and here for [WebAim WAVE](https://github.com/Agnieszka-21/health-store/tree/main/assets/wave_webaim).


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


## Business considerations

### Business model

The Health Store project was set up as an example of a B2C business, so interacting direcly with customers. It is an online retail store selling products internationally and 24/7. 

__Who is the customer__

The store's customers are likely to be impulse buyers who make the choice to buy on their own. Therefore it was crucial to make the checkout and payment process as easy and streamlined as possible.

__What is being sold__

Health Store sells physical products, therefore it was important to develop the following functionalities:
- searching, filtering, and sorting results
- order notifications.
A possible future enhancement would be adding stock management options so that users are notified when a product is sold out, and product quantity in the quantity input field is dynamically updated to reflect product stock levels.

__How is the payment made__

In this application, each transaction is finished after a single payment is made, which is typical for businesses selling physical products.


### SEO

__Keywords__
Keywords included in the relevant meta tag of the application have been chosen by following these steps:
1. Brainstorming general types of topics that Health Store's customers are likely to search for
2. Filling in the general topics with some possible keyword ideas (long and short keywords)
3. Trying these ideas out on Google and using the auto-complete feature as well as "People also ask"
4. Selecting from the list the best keywords, considering their relevance, authority, and volume

Here is the list of keywords selected in this process:
"health store, shop online, well-being, healthy food, vegan food, organic food, vegan recipes, healthy cooking, supplements for better sleep, vitamins for tiredness, natural skincare, natural beauty products, soy candles, non-toxic candles, soy wax candles, aromatherapy, essential oils, alternative health"

Further keywords are added to this list (to the meta tag) for blog articles and recipes for more accourate search results for users interested in content on a healthy lifestyle and healthy cooking. The keywords can be set in a suitable form (create article/recipe, edit article/recipe) by a staff user or admin, and if they are present, they are automatically appended to the list shown above for any published article or recipe.

__SEO implementation in HTML__
- Semantic HTML elements (header, footer, nav, article, section, etc.) have been utilized throughout the application with SEO in mind
- Any external links have been given been given the rel attribute "noopener nofollow"
- External links include social media sites (in the footer) and product brand's sites (on product detail pages)
- Internal links connect the pages with one another, making navigation easy and intuitive, and helping users to explore the website
- Relevant words and keywords have been used to describe any images (the alt attribute)
- Image file names have been checked to indicate what they depict
- Apart from keywords, meta tags were used for the website's title and description

__Other SEO implementations__

Two files have been create and added in the root folder of the project with the specific goal of improving the website's SEO: 
- sitemap.xml,
- and robots.txt.

[xml-sitemaps.com](https://www.xml-sitemaps.com/) was utilised to generate a sitemap file for the deployed webiste.
As for the robots.txt file, the following parts of the website have been excluded from crawling to protect user's data: accounts, basket, checkout, and profile.

### Web marketing

__Content marketing__
Blog articles and recipes as well as online events have been created as examples of content marketing, used for driving traffic to the store's website by handling topics that the store's potential customers are interested in. What is more, for each article/recipe, any additional keywords saved the relevant forms (create article/recipe, edit article/recipe) are automatically appended to the meta tag with keywords in the base template, making each specific article or recipe easier to find for search engines.

__Organic social media marketing__
A business Facebook page has been set up for Health Store to provide an example of unpaid social media marketing. It could also be used for paid social media marketing, if the store owner were to boost posts or create ads. Please see screenshots of the page below.

![Facebook page - part 1](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/fb_1.png)
![Facebook page - part 2](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/fb_2.png)

And here is the page as seen by an external user.

![Facebook page - part 1](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/fb_customer.png)

Since the action button "Buy now" required an external shopping platform, I decided to go with the classic "Learn more" which opens Health Store's website in a new tab.

__Email marketing__

A MailChimp account was created in order to add to the website a newsletter signup form. The form can be found in the footer and is fully functioning. It has been customized to match the styling of the Health Store application. There is also a link to the newsletter in the promotional banner at the very top of each page, guiding users' attention toward in a subtle way and encouraging them to sign up. No email campaign has been connected to the form at the moment but it is something that could be done in the future.

![Newsletter signup form](https://github.com/Agnieszka-21/health-store/blob/main/assets/screenshots/home_footer.png)

__GDPR considerations__

A Privacy Policy has been created for Health Store with the help of [this free privacy policy generator](https://www.privacypolicygenerator.info/). A link to a hosted page displaying the document has been added to the footer, near the newsletter sign-up form, to ensure that users can find it easily. The policy informs users about how their data is collected and processed by Health Store. You can see the Privacy Policy link in the previous screenshot.


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

