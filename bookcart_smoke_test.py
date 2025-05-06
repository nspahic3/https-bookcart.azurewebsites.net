from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bookcart.azurewebsites.net/")


# Smoke Test 1: Login 
try:
    wait = WebDriverWait(driver, 10)

    # Open Login form
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Login')]")))
    login_link.click()

    # Enter credentials
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='username']")))
    password_input = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")

    username_input.send_keys("nspahic")
    password_input.send_keys("hrXUB@8EgAyUP")

    # Click Login button
    login_button = driver.find_element(By.XPATH, "//button//span[text()='Login']")
    login_button.click()

    # Click on the menu (avatar)
    menu_trigger = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'mat-mdc-menu-trigger')]")))
    menu_trigger.click()

    # Click Logout
    try:
        logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Logout']")))
        print("✅ Logout button found. Test passed!")

    except Exception as e:
        print("❌ Test failed:", e)

    close_menu_button = driver.find_element(By.XPATH, "//div[contains(@class, 'cdk-overlay-backdrop')]")
    driver.execute_script("arguments[0].click();", close_menu_button)

except Exception as e:
    print("❌ Test failed:", e)



# Smoke test 2: Add 2 books to cart, checkout and order
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cdk-overlay-backdrop")))

    first_product_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//app-addtocart/button)[1]")))
    first_product_button.click()

    time.sleep(3)

    second_product_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//app-addtocart/button)[2]")))
    second_product_button.click()
    time.sleep(3)

    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//mat-icon[text()='shopping_cart']]")))


    driver.execute_script("arguments[0].click();", cart_button)

    checkout_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'mat-column-action')]//button[.//span[contains(text(), 'CheckOut')]]")))

    print("Checkout dugme je prisutno!")


    if checkout_btn.is_displayed() and checkout_btn.is_enabled():
        driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)
        driver.execute_script("arguments[0].click();", checkout_btn)
      
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.ID, "mat-input-2"))).send_keys("Ime Prezime")
    driver.find_element(By.ID, "mat-input-3").send_keys("Adresa 123")
    driver.find_element(By.ID, "mat-input-4").send_keys("Adresa 2")
    driver.find_element(By.ID, "mat-input-5").send_keys("123456")
    driver.find_element(By.ID, "mat-input-6").send_keys("Država")


    place_order_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[span[contains(text(), 'Place Order')]]")))


    if place_order_btn.is_displayed() and place_order_btn.is_enabled():
        driver.execute_script("arguments[0].scrollIntoView(true);", place_order_btn)
        driver.execute_script("arguments[0].click();", place_order_btn)
    


    print("✅ Smoke test passed: Order placed successfully!")

except Exception as e:
    print("❌ Smoke test failed:", e)

time.sleep(3)



# Smoke Test 3: Logout 
try:
    wait = WebDriverWait(driver, 10)

    menu_trigger = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'mat-mdc-menu-trigger')]")))

    driver.execute_script("arguments[0].scrollIntoView(true);", menu_trigger)

    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cdk-overlay-backdrop")))

    driver.execute_script("arguments[0].click();", menu_trigger)

    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Logout']")))

    driver.execute_script("arguments[0].scrollIntoView(true);", logout_btn)

    driver.execute_script("arguments[0].click();", logout_btn)

    print("✅ Logout test passed!")

except Exception as e:
    print("❌ Logout test failed:", e)

# Cleanup
driver.quit()
