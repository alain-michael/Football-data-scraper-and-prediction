import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def configure_edge_driver(log_file_path):
    # Configure Edge WebDriver options
    edge_options = Options()
    
    # Specify the path for the EdgeDriver executable
    edge_driver_path = 'msedgedriver.exe'

    # Initialize the Edge WebDriver with custom logging
    edge_service = Service(edge_driver_path)
    edge_service.log_path = log_file_path  # Set the log file path

    # Create the Edge WebDriver instance with custom service
    driver = webdriver.Edge(service=edge_service, options=edge_options)
    
    return driver

if __name__ == "__main__":
    log_file_path = "webdriver.log"  # Path to your log file
    driver = configure_edge_driver(log_file_path)
    
    # Your Selenium automation code goes here...

    driver.quit()  # Make sure to quit the WebDriver when done
