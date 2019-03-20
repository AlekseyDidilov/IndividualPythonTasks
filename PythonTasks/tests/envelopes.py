from models.envelopes_algorithm import Envelope


class TestEnvelope:
    def test_first_envelope_bigger(self):
        output = True
        first_envelope = Envelope(1.3, 2.4)
        second_envelope = Envelope(1.2, 2.1).__lt__(first_envelope)
        assert output == second_envelope

    def test_second_envelope_bigger(self):
        output = True
        first_envelope = Envelope(1.3, 2.4)
        second_envelope = Envelope(1.3, 2.4).__lt__(first_envelope)
        assert output != second_envelope

    def test_equal_sizes(self):
        output = False
        first_envelope = Envelope(1.3, 1.4)
        second_envelope = Envelope(1.3, 1.4).__lt__(first_envelope)
        assert output == second_envelope
