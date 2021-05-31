# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

def get_my_data(query):
    print(query)
    mydata = open('mydata.txt')
    mydata = mydata.read()
    string =""
    my_data_list = mydata.split('.')
    for d in my_data_list:
        if(d.lower().find(query.lower())==-1):
            string = "Sorry what are you asking about"
        else:
            string = d
            break
    return string


class ActionUtterName(Action):
    def name(self) -> Text:
        return("action_utter_name")

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="My name is gagan")
        return []



class ActionUtterAge(Action):
    def name(self) -> Text:
        return("action_utter_age")

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("years old")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionSubmitname(Action):
    def name(self) -> Text:
        return "action_submitname"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        user_name = tracker.get_slot("registername")
        print("Name  is  : ",user_name) 
        dispatcher.utter_message(template="utter_details_thanks")

        return[]

class ActionUtterMyCity(Action):
    def name(self) -> Text:
        return "action_utter_my_city"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("belong to")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterMyQualification(Action):
    def name(self) -> Text:
        return "action_utter_my_qualification"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("highest qualification")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterMyCollege(Action):
    def name(self) -> Text:
        return "action_utter_my_college"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("college")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterCollegeCity(Action):
    def name(self) -> Text:
        return "action_utter_college_city"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("my college")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterCollegeYear(Action):
    def name(self) -> Text:
        return "action_utter_college_year"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("completed my college")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterSchoolName(Action):
    def name(self) -> Text:
        return "action_utter_school_name"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = ""
        for e in tracker.latest_message["entities"]:
            if e["entity"] == 'school':

                if e["value"] == "high school":
                    data = get_my_data(e["value"])
                    string = string+" "+data
                    print("h")

                elif e["value"] == "intermediate":
                    data = get_my_data(e["value"])
                    string = string+" "+data
                    print("i")

                elif e['value'] == "both":
                    h_data = get_my_data("high school")
                    i_data = get_my_data("intermediate")
                    string = h_data + " and " + i_data
                    print("b")

                else :
                    string = "for which class you are asking for the school\nHigh School\nIntermediate\nor both"
                    print("n")
            else:
                string = "for which class you are asking for the school\nHigh School\nIntermediate\nor both"
                print("n")


        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterCount(Action):
    def name(self) -> Text:
        return "action_utter_count"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = get_my_data("members in my family")
        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterFamilyMemberName(Action):
    def name(self) -> Text:
        return "action_utter_family_member_name"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = ""
        for e in tracker.latest_message['entities']:
            if e['entity'] == "relation":
                print(e["value"])
                if e['value'] == "grandfather":
                    string = string+"\n"+get_my_data("grandfather's name")
                
                elif e['value'] == "grandmother":
                    string = string+"\n"+get_my_data("grandmother's name")

                elif e['value'] == "father":
                    string = string+"\n"+get_my_data("my father's name")
                
                elif e['value'] == "mother":
                    string = string+"\n"+get_my_data("my mother's name")

                elif e['value'] == "uncle":
                    string = string+"\n"+get_my_data("uncle's name")

                elif e['value'] == "aunt":
                    string = string+"\n"+get_my_data("aunt's name")

                elif e['value'] == "parent":
                    string = get_my_data("my father's name")+ " \nand\n "+get_my_data("my mother's name")
                
                elif e['value'] == "grandparent":
                    string = get_my_data("grandfather's name")+ "\nand\n"+get_my_data("grandmother's name")

                else:
                    string = "Please be specific of what you are asking!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []
        

class ActionUtterSiblingsCount(Action):
    def name(self) -> Text:
        return "action_utter_siblings_count"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:

            if e['entity'] == "relation":

                if e['value'] == "siblings":
                    string = string+"\n"+get_my_data(e['value']) 

                elif e['value'] == "brothers":
                    string = string+"\n"+get_my_data(e['value'])

                elif e['value'] == "sister":
                    string = string+"\n"+get_my_data(e['value']+" "+"only")

                else:
                    string = "Please be specific of what you are asking!!!!"
            
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterSiblingsName(Action):
    def name(self) -> Text:
        return "action_utter_siblings_name"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:

            if e['entity'] == "brother_name":

                print(e['value'])
                if e['value'].lower() == "first" or e['value'].lower() == "second" or e['value'].lower() == "third":
                    string = string+"\n"+get_my_data(e['value']) 

                elif e['value'] == "all":
                    string = string+"\n"+get_my_data("first")+"\n"+get_my_data("second")+"\n"+get_my_data("third")

                elif e['value'].lower() == "kuldeepak" or e['value'].lower() == "aishwarya" or e['value'].lower() == "atulya":
                    print(e['value'])
                    string = "He is my brother lol!!!!"

                elif e['value'] == "":
                    string = "WHich brother your talking about\nFirst number brother\nSecond number brother\nThird number brother"

                else:
                    string = "I dont know!!!"

            elif e['entity'] == "sister_name":
                print("sister")
                if e['value'] == "sister's name":
                    string = string+"\n"+get_my_data(e['value'])

                elif e['value'] == "Ishika":
                    string = "She is my sister lol !!!!"

                else:
                    string = "I dont know"

            elif e['entity'] == "sibling_name":
                string = string+"\n"+get_my_data("first")+"\n"+get_my_data("second")+"\n"+get_my_data("third")+"\n"+get_my_data("sister's name")
            
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []
        


class ActionUtterSiblingsWork(Action):
    def name(self) -> Text:
        return "action_utter_siblings_work"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "siblings_work":

                print(e['value'])
                value = e['value'].lower()
                if value == 'ask':
                    string = string+"\n"+"I have many siblings whose work you are asking about\nSister's work\nBrother's work"
                elif value == 'brothers work':
                    string = string+"\n"+"I have many brothers which brother's work you are asking\nKuldeepak's work\nAishwarya's work\nAtulya's work"
                elif value == "kuldeepak's work":
                    string = string +"\n"+get_my_data("Kuldeepak is")
                elif value == "aishwarya's work":
                    string = string +"\n"+get_my_data("Aishwarya is")
                elif value == "atulya's work":
                    string = string +"\n"+get_my_data("Atulya is")
                elif value == "ishika's work" or value == "sisters work":
                    string = string +"\n"+get_my_data("Ishika is")
                else:
                    string = "Sorry its personal !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []


class ActionUtterFatherDetils(Action):
    def name(self) -> Text:
        return "action_utter_father_details"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "fathers_detail":

                print(e['value'])
                value = e['value'].lower()
                if value == 'yatendra kumar gupta':
                    string = string+"\n"+"He is my Father !!!!!"
                elif value == 'occupation':
                    string = string+"\n"+get_my_data('business') + "\n And "+ get_my_data("having business")
                elif value == "father's family":
                    string = string +"\n"+get_my_data("father's family live")
                elif value == "father lives":
                    string = string +"\n"+get_my_data(value)
                elif value == "members in father's family":
                    string = string +"\n"+get_my_data(value)
                elif value == "father works in" :
                    string = string +"\n"+get_my_data(value)
                else:
                    string = "Sorry its personal !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterUncleDetails(Action):
    def name(self) -> Text:
        return "action_utter_uncle_details"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "uncle_detail":

                print(e['value'])
                value = e['value'].lower()
                if value == 'gajendra kumar gupta':
                    string = string+"\n"+"He is my Uncle !!!!!"
                elif value == 'occupation':
                    string = string+"\n"+get_my_data('service')
                elif value == "uncle's family":
                    string = string +"\n"+get_my_data("uncle's family live")
                elif value == "uncle lives":
                    string = string +"\n"+get_my_data(value)
                elif value == "members in uncle's family":
                    string = string +"\n"+get_my_data(value)
                elif value == "uncle works in" :
                    string = string +"\n"+get_my_data(value)
                elif value == "designation" :
                    string = string +"\n"+get_my_data(value)
                else:
                    string = "Sorry its personal !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterGrandfatherDetails(Action):
    def name(self) -> Text:
        return "action_utter_grandfather_details"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "grandfather_detail":

                print(e['value'])
                value = e['value'].lower()
                if value == 'satya prakash gupta':
                    string = string+"\n"+"He is my Grandpa !!!!!"
                elif value == 'occupation':
                    string = string+"\n"+get_my_data('teacher')
                else:
                    string = "Sorry its personal !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterFamilyLadiesDetails(Action):
    def name(self) -> Text:
        return "action_utter_family_ladies_details"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "family_ladies":

                print(e['value'])
                value = e['value'].lower()
                if value == 'krishna bala gupta':
                    string = string+"\n"+"She is my Grandma !!!!!"

                elif value == 'shalini gupta':
                    string = string+"\n"+"She is my Mother !!!!!"

                elif value == 'lata gupta':
                    string = string+"\n"+"She is my Aunt !!!!!"
                else:
                    string = "I don't know !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []

class ActionUtterMyOccupation(Action):
    def name(self) -> Text:
        return "action_utter_my_occupation"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        string = ""
        for e in tracker.latest_message['entities']:
            print(e['entity'])
            if e['entity'] == "my_work":

                print(e['value'])
                value = e['value'].lower()
                if value == 'software':
                    string = string+"\n"+get_my_data(value)

                elif value == 'my designation':
                    string = string+"\n"+get_my_data(value)

                elif value == 'my work':
                    string = string+"\n"+get_my_data(value)
                else:
                    string = "Sorry its personal !!!!!"
            else:
                string = "Please be specific of what you are asking!!!!"

        print(string)
        dispatcher.utter_message(text=string)
        return []