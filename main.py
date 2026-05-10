from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager

class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        
        logo_label = MDLabel(
            text="REVISION APP",
            halign="center",
            font_style="H3",
            theme_text_color="Primary"
        )
        
        welcome_text = MDLabel(
            text="Exam Revision Hub",
            halign="center",
            theme_text_color="Secondary"
        )

        login_btn = MDRaisedButton(
            text="START A FREE TEST",
            pos_hint={"center_x": .5},
            on_release=self.go_to_login
        )

        layout.add_widget(logo_label)
        layout.add_widget(welcome_text)
        layout.add_widget(login_btn)
        self.add_widget(layout)

    def go_to_login(self, instance):
        # This switches the "current" screen in the manager
        self.manager.current = 'quiz_screen'

# 2. Define the Quiz Screen (the screen we go to after clicking)
class QuizScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        
        label = MDLabel(text="You are now logged in!", halign="center")
        back_btn = MDFlatButton(
            text="Back to Welcome", 
            pos_hint={"center_x": .5},
            on_release=self.go_back
        )
        
        layout.add_widget(label)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'welcome_screen'

# 3. The Main App Class
class ExamApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        
        # Create the Screen Manager
        sm = MDScreenManager()
        
        # Add screens to the manager
        sm.add_widget(WelcomeScreen(name='welcome_screen'))
        sm.add_widget(QuizScreen(name='quiz_screen'))
        
        return sm

if __name__ == "__main__":
    ExamApp().run()
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        # Layout
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Question
        self.question_label = MDLabel(
            text="What is the chemical symbol for Water?",
            halign="center",
            theme_text_color="Primary",
            font_style="H5"
        )
        
        # Options
        btn1 = MDRaisedButton(text="H2O", pos_hint={'center_x': .5}, on_release=self.check_answer)
        btn2 = MDRaisedButton(text="CO2", pos_hint={'center_x': .5}, on_release=self.check_answer)
        
        layout.add_widget(self.question_label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        
        return layout

    def check_answer(self, instance):
        if instance.text == "H2O":
            self.question_label.text = "Correct! ✅"
        else:
            self.question_label.text = "Try Again! ❌"

if __name__ == "__main__":
    ExamApp().run()