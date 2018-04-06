import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
class qxf2move(unittest.TestCase):
 
    def setUp(self):
        self.driver=webdriver.Firefox()
 
    def testUserMove21Black(self):
        driver=self.driver
        driver.get("http://Team-bhp.com")
        self.assertIn("Home | Team-BHP - The Definitive Indian Car Website",driver.title)
 
        #Click on Black's 21st move
        #driver.find_element_by_id("fb-root").click()
        driver.find_element_by_xpath("//span[contains(text(),'News')]").click()
        
        #zgkjsjkbkjdbfkvbxdkjbfvkjxkjfvbxkj
 
                    #Verify the squares b6 and f2 ([2,1], [6,5]) have the right pieces
                #chess_square = driver.find_element_by_id("img_tcol5trow6")
                    #Verify that the square f2 has a black queen (bq.png)
                #self.assertEqual("http://www.chessgames.com/pgn4web-2.82/images/bq.png",chess_square.get_attribute('src'))
        title = self.assertEqual("News | Team-BHP",driver.title)


##        #Verify that the square b6 is empty (clear.png)
##        self.assertEqual("http://www.chessgames.com/pgn4web-2.82/images/clear.png",chess_square.get_attribute('src'))
 
    def tearDown(self):
        time.sleep(7)
        self.driver.quit()
 
if __name__=="__main__":
    unittest.main()
