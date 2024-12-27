from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define the URL
url = "https://nasscom.in/members-listing"

# Set up the Selenium WebDriver (update the path to your ChromeDriver)
service = Service("./chromedriver.exe")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get(url)

# Wait for the page to load (adjust timeout if necessary)
wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "views-row")))

# Scroll down to load more companies (if applicable)
for _ in range(5):  # Adjust range based on the number of rows
    driver.execute_script("window.scrollBy(0, 1000);")  # Scroll by 1000 pixels
    time.sleep(2)  # Wait for content to load

# Find all the company rows
companies = driver.find_elements(By.CLASS_NAME, "views-row")

# Extract company details
company_data = []
for company in companies:
    # Extract the company name
    name = company.find_element(By.TAG_NAME, "h2").text.strip()
    
    # Extract additional details (if available)
    description = company.find_element(By.CLASS_NAME, "field-content").text.strip() if company.find_elements(By.CLASS_NAME, "field-content") else "N/A"
    
    # Add to the list
    company_data.append({"Company Name": name, "Description": description})

# Close the browser
driver.quit()

# Convert the data into a DataFrame
df = pd.DataFrame(company_data)

# Export to an Excel file
output_file = "nasscom_members.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')
print(f"Data exported to {output_file} successfully!")
