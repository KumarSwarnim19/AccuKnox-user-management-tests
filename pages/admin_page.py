import re
from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.admin_menu_link = page.locator("text=Admin")
        self.add_button = page.locator("button:has-text(' Add ')")
        self.save_button = page.locator("button[type='submit']")
        self.success_toast = page.locator(".oxd-toast")
        
        
        self.search_username_input = page.locator("form input.oxd-input").nth(0)
        self.search_button = page.locator("button[type='submit']")
        self.reset_button = page.locator("button:has-text(' Reset ')")

    def navigate_to_admin(self):
        self.admin_menu_link.click()
        
        expect(self.page).to_have_url(re.compile("viewSystemUsers"))

    def add_user(self, username, password, employee_hint="a"):
        
        if "viewSystemUsers" not in self.page.url:
            self.navigate_to_admin()
            
        self.add_button.click()
        
        
        self.page.locator(".oxd-select-text").nth(0).click()
        self.page.locator("role=option[name='Admin']").click()
        
        
        self.page.locator(".oxd-select-text").nth(1).click()
        self.page.locator("role=option[name='Enabled']").click()
        
        
        print("    -> Selecting Employee Name...")
        type_hint = self.page.locator("input[placeholder='Type for hints...']")
        type_hint.click()
        type_hint.fill(employee_hint)
        
        
        self.page.wait_for_selector("div[role='listbox']", state="visible")
        self.page.wait_for_timeout(1000) 
        
        
        self.page.locator("div[role='listbox'] div[role='option']").first.click()
        
        
        self.page.get_by_role("textbox").nth(2).fill(username) 
        self.page.locator("input[type='password']").nth(0).fill(password)
        self.page.locator("input[type='password']").nth(1).fill(password)
        
        
        self.save_button.click()
        
        
        self.page.wait_for_url(re.compile("viewSystemUsers"), timeout=10000)

    def search_user(self, username):
        
        if "viewSystemUsers" not in self.page.url:
            self.navigate_to_admin()

        self.page.wait_for_timeout(2000) 
        
        
        self.reset_button.click()
        self.page.wait_for_timeout(1000)

        
        self.page.get_by_role("textbox").nth(1).fill(username)
        self.search_button.click()
        
        
        
        self.page.wait_for_selector(f"div.oxd-table-card:has-text('{username}')", timeout=10000)

    def edit_user_role(self, username, new_role="ESS"):
        
        self.page.locator(f"div.oxd-table-card:has-text('{username}') .bi-pencil-fill").click()
        
        self.page.wait_for_timeout(1000)
        
        
        self.page.locator(".oxd-select-text").nth(0).click()
        self.page.locator(f"role=option[name='{new_role}']").click()
        
        self.save_button.click()
        self.page.wait_for_url(re.compile("viewSystemUsers"))

    def delete_user(self, username):
        
        self.page.locator(f"div.oxd-table-card:has-text('{username}') .bi-trash").click()
        
        
        self.page.locator("button:has-text(' Yes, Delete ')").click()
        
        
        expect(self.success_toast).to_be_visible()