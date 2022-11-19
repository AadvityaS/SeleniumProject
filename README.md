# SeleniumProject
Web Automation Using Selenium

Problem: To automate the following scenario on a demo website using selenium:
•	Click on any image link.
•	Select and Click any dropdown link on the website.
•	Add a product to your shopping cart.
•	Verify the product.

Solution:

I wrote a custom script of selenium using python which does the following steps in order to reach the solution:

1.	It opens the chrome browser and maximizes the windows.
2.	Then it searches for the given URL in the search box.
3.	After that the script searches for the interactable element on the webpage (in our case, an element with a drop-down menu).
4.	When that element gets located, the scripts opens it by sending a “click” command to the browser. Then the drop-down menu expands revealing other options (in our case the script clicks the “MARKETPLACE” option).
5.	Then the website gets onto the webpage from where we have to select a product. The script then selects a product (using the path of the element given to it).
6.	The browser then navigates to the product page and our scripts ads it to the cart by clicking on the ‘add to cart’ button and automatically entering the Username and the Email id.
7.	After adding to the cart, the scripts open’s the cart in order for us to verify that the product is added to the cart or not.

