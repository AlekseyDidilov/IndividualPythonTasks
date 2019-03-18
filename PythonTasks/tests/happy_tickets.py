from models.happy_tickets_algorithm import HappyTickets


class TestHappyTickets:
    def test_happy_ticket_list_valid_output(self):
        output_list = ["000000", "000001"]
        happy_ticket_instance = HappyTickets(0, 2).happy_ticket_list()
        assert output_list == happy_ticket_instance

    def test_happy_ticket_list_without_zero(self):
        output_list = ["0", "1"]
        happy_ticket_instance = HappyTickets(0, 2).happy_ticket_list()
        assert output_list != happy_ticket_instance

    def test_happy_ticket_list_invalid_output(self):
        output_list = ["000000", "000001"]
        happy_ticket_instance = HappyTickets(0, 3).happy_ticket_list()
        assert output_list != happy_ticket_instance

    def test_get_happy_tickets_valid_output(self):
        output_value = (1, 10)
        happy_ticket_instance = HappyTickets(0, 100).get_happy_tickets()
        assert output_value == happy_ticket_instance

    def test_get_happy_tickets_invalid_output(self):
        output_value = (1, 10)
        happy_ticket_instance = HappyTickets(100, 100).get_happy_tickets()
        assert output_value != happy_ticket_instance
