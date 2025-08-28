from kivymd.app import MDApp
from kivy.lang import Builder
from home import main_string
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from e import bill
from datetime import date

Window.keyboard_anim_args = {'d':.2,'t':'in_out_expo'}
Window.softinput_mode = "below_target"

class Home(Screen):
	pass
class Details(Screen):
	pass

#screen manager
sm= ScreenManager()
sm.add_widget(Home(name="mainpage"))
sm.add_widget(Details(name="result_scr"))

class Home(MDApp):
	def build(self):
		screen = Screen()
		self.source = Builder.load_string(main_string)
		screen.add_widget(self.source)
		return screen
	def details(self):
		self.productName = self.source.get_screen("mainpage").ids.Productname.text
		self.productQuantity = self.source.get_screen("mainpage").ids.Quantity.text
		self.productCost = self.source.get_screen("mainpage").ids.Cost.text
		self.productDiscount = self.source.get_screen("mainpage").ids.Discount.text
		self.a = bill(self.productQuantity,self.productCost,self.productDiscount)
	def erase(self, *args):
		self.source.get_screen("mainpage").ids.Productname.text= ""
		self.source.get_screen("mainpage").ids.Quantity.text= ""
		self.source.get_screen("mainpage").ids.Cost.text= ""
		self.source.get_screen("mainpage").ids.Discount.text = ""
	def change(self):
		self.source.get_screen("result_scr").ids.resPname.text = f"Product name:{self.productName}"
		self.source.get_screen("result_scr").ids.resPqunatity.text = f"Product quantity: {self.productQuantity}"
		self.source.get_screen("result_scr").ids.resCost.text = f"Total amount: {int(self.productCost)*float(self.productQuantity)}"
		self.source.get_screen("result_scr").ids.resDiscount.text = f"Discount: {self.productDiscount}%"
		self.source.get_screen("result_scr").ids.resTotal.text = f"Total amount to pay: {self.a}"
		with open("bill.txt","a+",encoding="utf-8") as f:
			f.write(f"""\nDate: {date.today()}\n
			--------☆ ☆ ☆ ☆ ☆ ☆ ☆------------\n
			Namaste user! Thankyou for shopping..\n
			Here is a copy of your bill:\n
			Product name:{self.productName}\n
			Product quantity: {self.productQuantity}\n
			Total amount: {int(self.productCost)*int(self.productQuantity)}\n
			Discount: {self.productDiscount}%\n
			YOU HAVE PAID:{self.a}\n
			--------☆ ☆ ☆ ☆ ☆ ☆ ☆------------\n""")
if __name__ == "__main__":
	Home().run()
