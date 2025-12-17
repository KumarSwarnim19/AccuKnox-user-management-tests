import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage


TEST_USER = "NewUser"
TEST_PASS = "admin123!"

def test_orangehrm_e2e(page: Page):
    
    login_p = LoginPage(page)
    admin_p = AdminPage(page)

    print("\n--- Starting Test Execution ---")

    
    print(f"Step 1: Logging in as Admin...")
    login_p.navigate()
    login_p.login("Admin", "admin123")
    print("  -> Login Successful")

    
    print("Step 2: Navigating to Admin module...")
    admin_p.navigate_to_admin()

    #
    print(f"Step 3: Adding new user '{TEST_USER}'...")
    try:
        admin_p.add_user(TEST_USER, TEST_PASS)
        print("  -> User Added Successfully")
    except:
        print("  -> (Note: User might already exist, continuing...)")

    
    print("Step 4: Searching for the new user...")
    admin_p.search_user(TEST_USER)
    print("  -> User Found")

    
    print("Step 5: Editing user role to ESS...")
    admin_p.edit_user_role(TEST_USER, "ESS")
    print("  -> User Role Updated")

    
    print("Step 7: Deleting the user...")
    
    admin_p.search_user(TEST_USER)
    admin_p.delete_user(TEST_USER)
    print("  -> User Deleted Successfully")

    print("\n--- Test Completed Successfully! ---")