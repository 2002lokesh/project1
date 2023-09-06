from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
import webbrowser
from kivy.core.window import Window
Window.size = (350, 500)
# Dictionary mapping batches to PDF URLs (replace with your actual URLs)
batch_to_pdf = {
    "2014-2018": "https://drive.google.com/file/d/1VbL4DxgMDWR-H3jkk4fQkZfnvvansP2F/view?usp=drive_link",
    "2015-2019": "https://drive.google.com/file/d/1sfc0FLH1ofmkjhh1dczZWQf-GM7li2rU/view?usp=drive_link",
    "2016-2020": "https://drive.google.com/file/d/1cSidHDndeXMiz--WiBsz2k7s2lokxOOX/view?usp=drive_link",
    "2017-2021": "https://example.com/batch4.pdf",
    "2018-2022": "https://example.com/batch5.pdf",
    "2019-2023": "https://example.com/batch6.pdf",
    "2020-2024": "https://example.com/batch7.pdf",
    "2021-2025": "https://example.com/batch8.pdf",
    "2022-2026": "https://drive.google.com/file/d/1VbL4DxgMDWR-H3jkk4fQkZfnvvansP2F/view",
}

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(16)
    spacing: dp(16)  # Add spacing between buttons

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: dp(48)
        pos_hint: {'center_x': .8}  # Center the button horizontally
        
        MDRaisedButton:
            text: "Select Batch"
            on_release: app.select_batch()
         

    BoxLayout:
        orientation: 'horizontal'
        MDBoxLayout:
            orientation: 'vertical'
            id: pdf_box
            size_hint: None, None
            size: self.minimum_size
            pos_hint: {'center_x': .9}  # Center the buttons horizontally
'''

class AlumniViewerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def select_batch(self):
        pdf_box = self.root.ids.pdf_box

        # Clear previous content
        pdf_box.clear_widgets()

        for batch, pdf_url in batch_to_pdf.items():
            # Create buttons for PDF (replace with actual functionality)
            pdf_button = MDRaisedButton(
                text=f"View PDF for {batch}",
                on_release=lambda batch=batch, url=pdf_url: self.open_pdf(batch, url)
            )

            pdf_box.add_widget(pdf_button)

    def open_pdf(self, batch, url):
        # Open the PDF URL in a web browser
        webbrowser.open(url)

if __name__ == '__main__':
    AlumniViewerApp().run()
