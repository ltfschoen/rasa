from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateExchangeForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_exchange_form"

    @staticmethod
    def pair_db() -> List[Text]:
        """Database of supported pairs."""

        return [
            "ausd",
            "usd",
            "btc",
            "dot",
            "dot",
            "aca",
            "kusd",
            "ksm",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_pair(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate pair value."""

        if value.lower() in self.pair_db():
            # validation succeeded, set the value of the "pair" slot to value
            return {"pair": value}
        else:
            dispatcher.utter_message(response="utter_wrong_pair")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"pair": None}

    def validate_num_tokens(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_tokens value."""

        if self.is_int(value) and int(value) > 0:
            return {"num_tokens": value}
        else:
            dispatcher.utter_message(response="utter_wrong_num_tokens")
            # validation failed, set slot to None
            return {"num_tokens": None}

    def validate_high_liquidation_risk(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate high_liquidation_risk value."""

        if isinstance(value, str):
            if "high" in value:
                # convert "high..." to True
                return {"high_liquidation_risk": True}
            elif "low" in value:
                # convert "low..." to False
                return {"high_liquidation_risk": False}
            else:
                dispatcher.utter_message(response="utter_wrong_high_liquidation_risk")
                # validation failed, set slot to None
                return {"high_liquidation_risk": None}

        else:
            # affirm/deny was picked up as True/False by the from_intent mapping
            return {"high_liquidation_risk": value}
