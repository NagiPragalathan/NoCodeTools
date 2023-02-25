from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.opera import OperaDriverManager


class SetupTools:
    def __init__(self) -> None:
        pass
    def install_selenium_tool(self,driver : str) -> webdriver :
        if driver == 'Chrome':
            test_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif driver == 'ChromeService':
            test_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif driver == 'Brave':
            test_driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
        elif driver == 'BraveService':
            test_driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        elif driver == 'Firefox':
            test_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif driver == 'FirefoxService':
            test_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif driver == 'IE':
            test_driver = webdriver.Ie(IEDriverManager().install())
        elif driver == 'IEService':
            test_driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        elif driver == 'Edge':
            test_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif driver == 'EdgeService':
            test_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif driver == 'Opera':
            test_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        return test_driver
