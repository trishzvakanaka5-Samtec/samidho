from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = 400,600

helper_text = """
Screen:
   MDNavigationLayout:
      MDScreenManager:
         Screen:
            MDBoxLayout:
               orientation:"vertical"
      
               MDTopAppBar:
                  id:Bar
                  title:'Tagtel'
                  left_action_items:[['menu',lambda x: nav_drawer.set_state("open")]]
                  right_action_items:[['clock']]
                
         
               MDLabel:
                  text:'Samuel'
                  
               Accordion:
                  orientation:'vertical'
                  
                  AccordionItem:
                     title:'Item 1'
                     MDLabel:
                        id: label
                        text:'Samuel'
                     MDTextButton:
                        text: 'Start'
                        on_press: app.Start_Count()
                        
                  AccordionItem:
                     title:'Item 2'
                     MDLabel:
                        text:'Zvakanaka'
                        
                  AccordionItem:
                     title:'Item 3'
                     size_hint:280, 300
                     Image:
                        source:"samuel.jpg"
                     OneLineListItem:
                        text:'Samuel Zvakanaka'
                        
                  AccordionItem:
                     title:'Item 4'
                     MDLabel:
                        text:'Email'
                        
                  AccordionItem:
                 
                  
      MDNavigationDrawer:
         id: nav_drawer
         navigationLabel:'User'
         
         MDBoxLayout:
            orientation:'vertical'
            Image:
               source:'Sekuru nevazukuru.jpg'
            MDLabel:
               text:'Samuel Zvakanaka'
               font_style:'H6'
               font_color:'Custom'
               color:'green'
               size_hint_y:None
               height:self.texture_size[1]
               
            MDLabel:
               text:'trishzvakanaka5@gmail.com'
               font_family:'custom'
               size_hint_y:None
               height:self.texture_size[1]
            
            MDNavigationDrawerDivider:
               
            MDScrollView:
               MDList:
               
                  
               
                  OneLineIconListItem:
                     text:'My Files'
                     divider_color:'white'
                     IconLeftWidget:
                        icon:'file'
                        
                  OneLineIconListItem:
                     text:'Upload'
                     divider_color:'white'
                     IconLeftWidget:
                        icon:'upload'
                     
                  OneLineIconListItem:
                     text:'Logout'
                     divider_color:'white'
                     IconLeftWidget:
                        icon:'logout'
                              
"""
class MyApp(MDApp):
    def build(self):
        app = Builder.load_string(helper_text)
        return app

    def Start_Count(self):
        Counter = 0
        for i in range(20):
           Counter += 1
           self.root.ids.label.text = str(Counter)




if __name__ == "__main__":
    MyApp().run()




