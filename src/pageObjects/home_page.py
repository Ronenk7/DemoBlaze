from selenium.webdriver.common.by import By


class HomePage:

    # ======== Carousel Locators ========#
    carousel_img_1 = By.XPATH, "//img[@alt='First slide']"
    carousel_img_2 = By.XPATH, "//img[@alt='Second slide']"
    carousel_img_3 = By.XPATH, "//img[@alt='Third slide']"
    btn_carousel_left_arrow = By.CLASS_NAME, "carousel-control-prev-icon"
    btn_carousel_right_arrow = By.CLASS_NAME, "carousel-control-next-icon"
    btn_carousel_mid_left = By.XPATH, "//li[@data-slide-to='0']"
    btn_carousel_mid_mid = By.XPATH, "//li[@data-slide-to='1']"
    btn_carousel_mid_right = By.XPATH, "//li[@data-slide-to='2']"

    # ======== Categories Menu Locators ========#
    categories_menu_header = By.ID, "cat"
    categories_phones = By.XPATH, "//a[@id='itemc' and text()='Phones']"
    categories_laptops = By.XPATH, "//a[@id='itemc' and text()='Laptops']"
    categories_monitors = By.XPATH, "//a[@id='itemc' and text()='Monitors']"

    # ======== Item Cards Locators ========#
    items_cards = By.XPATH, "//*[@class='card h-100']"  # all 9 cards
    cards_table = By.ID, "tbodyid"
    table_rows = By.XPATH, "//tr[@class='success']"
    cards_body = By.CLASS_NAME, "card-block"  # all 9 context
    cards_images = By.XPATH, "//img[@class='card-img-top img-fluid']"  # all 9 images
    cards_link = By.XPATH, "//h4[@class='card-title']"

    def __init__(self, driver):
        self.driver = driver

        # ======== Item Cards WebElements ========#
        self.get_carousel_img_1 = lambda: self.driver.find_element(*self.carousel_img_1)
        self.get_carousel_img_2 = lambda: self.driver.find_element(*self.carousel_img_2)
        self.get_carousel_img_3 = lambda: self.driver.find_element(*self.carousel_img_3)
        self.get_btn_carousel_left_arrow = lambda: self.driver.find_element(*self.btn_carousel_left_arrow)
        self.get_btn_carousel_right_arrow = lambda: self.driver.find_element(*self.btn_carousel_right_arrow)
        self.get_btn_carousel_mid_left = lambda: self.driver.find_element(*self.btn_carousel_mid_left)
        self.get_btn_carousel_mid_mid = lambda: self.driver.find_element(*self.btn_carousel_mid_mid)
        self.get_btn_carousel_mid_right = lambda: self.driver.find_element(*self.btn_carousel_mid_right)

        # ======== Item Cards WebElements ========#
        self.get_categories_menu_header = lambda: self.driver.find_element(*self.categories_menu_header)
        self.get_categories_phones = lambda: self.driver.find_element(*self.categories_phones)
        self.get_categories_laptops = lambda: self.driver.find_element(*self.categories_laptops)
        self.get_categories_monitors = lambda: self.driver.find_element(*self.categories_monitors)

        # ======== Item Cards WebElements ========#
        self.get_items_cards = lambda: self.driver.find_elements(*self.items_cards)
        self.get_cards_table = lambda: self.driver.find_element(*self.cards_table)
        self.get_table_rows = lambda: self.driver.find_elements(*self.table_rows)
        self.get_cards_body = lambda: self.driver.find_elements(*self.cards_body)
        self.get_cards_images = lambda: self.driver.find_elements(*self.cards_images)
        self.get_cards_link = lambda: self.driver.find_elements(*self.cards_link)
