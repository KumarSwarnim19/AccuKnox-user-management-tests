from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

    def navigate(self):
        
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()