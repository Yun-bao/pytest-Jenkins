from testSelenium.base import Base


class TestWin(Base):
    def test_switchwidows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__regLink").click()
        # z找出所有窗口和当前窗口，打印出的窗口的list类型
        window1 = self.driver.current_window_handle
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("usernm677e")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("123dfghjkg")
        self.driver.switch_to_window(window1)
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("loginuser")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("oginpassword")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #跟进元素id或者index切换到对于frame
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        #切换到默认frame·
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").text

    def test_js(self):
        pass