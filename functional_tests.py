from selenium import webdriver
import pretty_errors

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Congratulations" in browser.title
