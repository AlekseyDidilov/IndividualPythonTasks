from models.validation_value import GreaterThanZero, LessOneHundred, CheckRequirements
from models.input_value import AskInput, IntInput
from models.execution import NewExecution
from models.envelopes_algorithm import Envelope


class Side:
    def __init__(self, side: str):
        self._side = side

    def side_validation(self) -> int:
        envelope_side = IntInput(AskInput(self._side)).value()
        check_side = CheckRequirements(GreaterThanZero(), LessOneHundred())
        if check_side.passed(envelope_side):
            return envelope_side
        raise SystemExit


if __name__ == "__main__":
    while True:
        first_envelope = Envelope(
            Side("Please, enter length:").side_validation(),
            Side("Please, enter height:").side_validation(),
        )
        second_envelope = Envelope(
            Side("Please, enter length:").side_validation(),
            Side("Please, enter height:").side_validation(),
        )
        print(
            f"Second envelope can be nested it's - {first_envelope > second_envelope}\n"
            f"First envelope can be nested it's - {second_envelope > first_envelope}"
        )
        new_app_run = NewExecution(
            "Do you want to continue?\n" 
            "If yes, please type 'y' or 'yes'\n"
        ).choose_action()
        if not new_app_run:
            print("Run app has been stopped!")
            break
