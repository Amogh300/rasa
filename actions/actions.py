# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"))

from SkinCare import skinCare

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_skin_care"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        skinDescription= next(tracker.get_latest_entity_values("skinkind"),None)
        # skinDescription=tracker.latest_message['text']
        if not skinDescription:
            msg = f"Please give me a skin type"
            dispatcher.utter_message(text=msg)
        urls=skinCare(skinDescription)
        length = len(urls)
        if(length>5):
            length = 5
        if(length!=0):
            for i in range(0,length):
                # msg = f"[{urls[i]['Name']}](http://localhost:3000/product/{urls[i]['_id']})"
                # dispatcher.utter_message(msg)
                dispatcher.utter_message(response = "utter_skin_url", name = urls[i]['name'],domain="https://j3c5e.csb.app/product/",url=urls[i]['_id'])
        else:
            dispatcher.utter_message("Invalid Skin Type")
        return []
