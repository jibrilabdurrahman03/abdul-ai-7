abdul-ai-7
Repository navigation
Code
Issues
Pull requests
abdul-ai-7
/
main.py
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

No wrap
Editing main.py file contents
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
main.pyfrom kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.utils import escape_markup
from datetime import datetime
import os
import threading
import urllib.request
import json

APP_CODE = """
BoxLayout:
    orientation: "vertical"
    padding: "12dp"
    spacing: "10dp"

    canvas.before:
        Color:
            rgba: 0.035, 0.055, 0.10, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        size_hint_y: None
        height: "65dp"
        Label:
            text: "[b]ABDUL AI 7.0[/b]\\n[color=66D9EF]Your personal AI assistant[/color]"
            markup: True
            halign: "left"
            valign: "middle"
            text_size: self.size
            font_size: "20sp"

    ScrollView:
        do_scroll_x: False
        Label:
            id: chat
            text: "[b]ABDUL AI:[/b] Welcome! I am ready to chat."
            markup: True
            size_hint_y: None
            height: self.texture_size[1] + dp(30)
            text_size: self.width, None
            halign: "left"
            valign: "top"
            padding: "8dp"
            color: 0.94, 0.96, 1, 1

    BoxLayout:
        size_hint_y: None
        height: "55dp"
        spacing: "8dp"
        TextInput:
            id: message
            hint_text: "Type your message..."
            multiline: False
            on_text_validate: app.send_message()
        Button:
            text: "SEND"
            size_hint_x: None
            width: "85dp"
            on_release: app.send_message()

    Label:
        text: "ABDUL AI • Created by Abdurrahman Jibril"
        size_hint_y: None
        height: "25dp"
        font_size: "11sp"
        color: 0.55, 0.65, 0.78, 1
"""

class AbdulAI(App):
    def build(self):
        from kivy.metrics import dp
        Builder.load_string("from kivy.metrics import dp")
        root = Builder.load_string(APP_CODE)
        self.chat = root.ids.chat
        self.message = root.ids.message
        self.history = []
        return root

    def send_message(self):
        question = self.message.text.strip()
        if not question:
            return

        self.message.text = ""
        self.add_chat("YOU", question)
        self.add_chat("ABDUL AI", "Thinking...")

        threading.Thread(
            target=self.answer_question,
            args=(question,),
            daemon=True
        ).start()

    def add_chat(self, speaker, text):
        safe = escape_markup(text)
        self.chat.text += f"\\n\\n[b]{speaker}:[/b] {safe}"

    def answer_question(self, question):
        answer = (
            "Your app interface is working! To enable powerful online AI "
            "responses, we must connect a securely deployed backend. "
            "This starter version does not yet connect to an online AI model."
        )

        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.add_chat("ABDUL AI", answer))

if __name__ == "__main__":
    AbdulAI().run()
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Commit changes
Commit message
Create main.pyAdd ABDUL AI Android app
Extended description
Add an optional extended description...
Direct commit or PR

Commit directly to the main branch

Create a new branch for this commit and start a pull request Learn more about pull requests
