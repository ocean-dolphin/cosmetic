# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])


def clean_phone(phone):
    return "".join([c for c in phone if c.isalpha()])


def clean_address(address):
    return "".join([c for c in address if c.isalpha()])


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_name_guest(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name_guest` value."""

        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="Tên của quý khách quá ngắn. Mời quý khách nhập lại tên!")
            return {"name_guest": None}
        return {"name_guest": name}

    def validate_phone(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phone` value."""

        phone = clean_phone(slot_value)
        if len(phone) == 0:
            dispatcher.utter_message(text="Số điện thoại của quý khách không hợp lệ. Mời quý khách nhập lại số điện thoại!")
            return {"phone": None}
        return {"phone": phone}

    def validate_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        address = clean_address(slot_value)
        if len(address) == 0:
            dispatcher.utter_message(text="Địa chỉ của quý khách quá ngắn. Mời quý khách nhập lại địa chỉ!")
            return {"address": None}
        return {"address": address}


