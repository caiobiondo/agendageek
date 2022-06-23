from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior


class ContentNavigationDrawer(BoxLayout):
    pass


class HomeScreen(Screen):
    pass


class MainWidget(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        return MainWidget()


MainApp().run()