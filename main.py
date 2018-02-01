import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

temp_x= "temp"
temp_y= "temp"

class PlantListButton(ListItemButton):
    pass

class PlantDB(BoxLayout, Screen):
    plant_name_text_input = ObjectProperty()
    date_text_input = ObjectProperty()
    plant_list = ObjectProperty()
    app= App.get_running_app()
    
    def load_list(self):
        try:
            with open("plants.txt", "r") as f:
                x=f.readline()
                while x:
                    plant_name= x.rstrip()
                    #add tp plant vview
                    self.plant_list.adapter.data.extend([plant_name])
                    #reset the pplant view
                    self.plant_list._trigger_reset_populate()
                    x = f.readline()
        except:
            pass
    def plant_plant(self):
     
        #get plant name from text
        plant_name = self.plant_name_text_input.text+"_" +self.date_text_input.text
        #write to plant database file
        with open("plants.txt", "a") as f:
            f.write(plant_name+"\n")
        #create fle for plant
        with open(plant_name+".txt", "a") as f:
            f.write(self.plant_name_text_input.text+" was planted on "+self.date_text_input.text+"\n")
        
        #add tp plant vview
        self.plant_list.adapter.data.extend([plant_name])
        #reset the pplant iew
        self.plant_list._trigger_reset_populate()
        
    def plant_edit(self):
         #if a list item is selected
        if self.plant_list.adapter.selection:
            #get the text from item selected 
            self.app.tempx = self.plant_list.adapter.selection[0].text
            self.manager.get_screen('Plant_Edit').tempx = self.app.tempx
         
         
                
     
         
    def plant_view(self):
         #if a list item is selected
        if self.plant_list.adapter.selection:
            #get the text from item selected and save outside class
            self.app.tempx = self.plant_list.adapter.selection[0].text 
         
            #read plant info into variable for display 
            with open(self.app.tempx+".txt", "r") as f:
                self.app.tempy=f.read()
            self.manager.get_screen('Plant_View').tempx = self.app.tempx
            self.manager.get_screen('Plant_View').tempy = self.app.tempy
    
class PlantEdit(BoxLayout, Screen):
    plant_info_text_input = ObjectProperty()
    app= App.get_running_app()
    tempx= StringProperty()
    def plant_update(self):
        #get plant update information from text
        plant_update = self.plant_info_text_input.text
        #write to plant file
        with open(self.tempx+".txt", "a") as f:
            f.write(plant_update+"\n")
    
class PlantView(BoxLayout, Screen):
    app= App.get_running_app()
    tempx= StringProperty()
    tempy= StringProperty()
 
     
 
 
        




class PlantDBApp(App):
    tempx = StringProperty()
    tempy = StringProperty()
    def build(self):
        screen_manager= ScreenManager()
        screen_manager.add_widget(PlantDB(name="Plant_DB"))
        screen_manager.add_widget(PlantEdit(name="Plant_Edit"))
        screen_manager.add_widget(PlantView(name="Plant_View"))
        return screen_manager

dbapp = PlantDBApp()


dbapp.run()
