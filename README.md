# playwright-learning
I'm learning Playwright (python + pytest) by testing the Sauce Labs demo website.

## Progress log
## 15/11/2026
*Extracted the login function.* Username and password are now the parameters of the login function. 
I can call the function in one of the ways:
- `login(page)` => username and password are default
- `login(page, "alternative_username")` => different username, standard password
- `login(page, password="alternative_password")` => standard user, different password

*Tested the product pictures.* 
1. find the picture on the page by its alt attribute, which in case of this website is unique for every pic
2. compare the src attribute on the page with the expected one in the code
