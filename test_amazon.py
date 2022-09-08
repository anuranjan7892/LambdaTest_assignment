from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAmazon:

    def test_amazon_searchbar(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("https://amazon.in")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("lg soundbar")
        driver.find_element(By.ID, "nav-search-submit-button").click()

        search_results = driver.find_elements(By.XPATH, "//div[contains(@class,'card-container')]")
        print("-------------------------------------------")

        for i in range(1, len(search_results) + 1):

            name = driver.find_element(By.XPATH, f"(//div[contains(@class,'card-container')]//h2//span)[{i}]").text

            try:
                cost = driver.find_element(By.XPATH,
                                           f"(//div[contains(@class,'card-container')]//h2//span)[{i}]//ancestor::h2//parent::div//following-sibling::div[@class='sg-row']//span[@class='a-price-whole']").text
            except NoSuchElementException:
                cost = "0"

            print(cost, " : ", name)

        driver.close()
