from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

try:
    
    driver.get("https://www.imdb.com/search/name/")
    
   
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    
   
    name_input.send_keys("Tom Hanks")
    
   
    birth_month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birth_month"))
    )
    select_birth_month = Select(birth_month_dropdown)
    select_birth_month.select_by_visible_text("July")
    
    
    birth_year_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birth_year"))
    )
    birth_year_input.send_keys("1956")
    
   
    birth_place_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birth_place"))
    )
    birth_place_input.send_keys("Concord, California, USA")
    
    
    role_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "roles"))
    )
    select_role = Select(role_dropdown)
    select_role.select_by_visible_text("Actor")
    
   
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Search']"))
    )
    search_button.click()
    
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".lister-list"))
    )
    print("Search performed successfully and results loaded.")
    
finally:
    # Step 4: Close the driver
    driver.quit()