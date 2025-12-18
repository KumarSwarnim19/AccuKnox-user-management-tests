import requests

def check_app_status(url):
    print(f"--- Checking Application Status for: {url} ---")
    try:
        # Send a request to the URL (Wait up to 5 seconds)
        response = requests.get(url, timeout=5)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            print(f"✅ SUCCESS: Application is UP. (Status Code: {response.status_code})")
        else:
            print(f"⚠️  WARNING: Application is reachable but returned status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ CRITICAL: Application is DOWN. (Connection Failed)")
    except requests.exceptions.Timeout:
        print("❌ CRITICAL: Application is DOWN. (Request Timed Out)")
    except Exception as e:
        print(f"❌ ERROR: An unexpected error occurred: {e}")

if __name__ == "__main__":
    # We are checking the OrangeHRM demo site
    target_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" 
    check_app_status(target_url)