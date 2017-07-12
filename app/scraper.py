import json
#from pyvirtualdisplay import Display
from selenium import webdriver

def run_scraper(id):
	display = Display(visible=0, size=(1024, 768))
	display.start()

	browser = webdriver.Chrome()

	url = "https://www.youtube.com/live_chat?v=" + str(id)
	browser.get(url)

	#innerHTML = browser.execute_script("return document.body.innerHTML")
	chats = []
	for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):
		message = chat.find_element_by_css_selector("#message").get_attribute('innerHTML')
		chats.append(("{ message: '" + message.encode('utf-8').strip() +"' },"))

	browser.quit()
	display.stop()
	return chats