MultiArmed Bandit app

This application randomly displays landing pages and grabs information of registered users. For now I am just using a mockup shopify landing page for learning purposes.
My database records the users email and the random landing page were the user registers (fx: Landing Page # 1).
The Multiarmed Bandit Module is determines the probability of a landing page being displayed based on the conversion rate for each fo the landing pages.

It is still a work in progress!

How to use it:
____________________________________________________

1. Erase __pycahe__ files
2. Erase migration folder
3. Erase data.sqlite
____________________________________________________

4. Open the console:
5. Create the database by typing: flask db init
6. Create migrations by typing: flask db migrate -m "First Database"
7. Upgrade : flask db Upgrade
____________________________________________________

8. Run the applications :  python app.py
