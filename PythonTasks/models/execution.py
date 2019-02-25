class NewExecution:

    def __init__(self, question: str):
        self.question = question

    def choose_action(self) -> bool:
        enter_choice = input(f"{self.question} ")
        if enter_choice.lower() in ("yes", "y"):
            return True
        return False
