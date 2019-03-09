"""This program has been created to help understand which of 2 methods:
  Simple - if a six-digit number is printed on the ticket, and the sum
  of the first three digits is equal to the sum of the last three.
  Complicated - if the sum of the even numbers of the ticket is equal
  to the sum of the odd numbers of the ticket.
  Which of this two methods can fond more happy tickets in range which
  is chosen by user."""


def happy_ticket_list(start_ticket: int, stop_ticket: int) -> list:
    tickets_output = [str(_).zfill(6) for _ in range(start_ticket, stop_ticket)]
    return tickets_output


def method_easy(tickets_list: list) -> int:
    happy_tickets_amount1 = 0
    for digit in tickets_list:
        first_half = int(digit[0]) + int(digit[1]) + int(digit[2])
        second_half = int(digit[3]) + int(digit[4]) + int(digit[5])
        if first_half == second_half:
            happy_tickets_amount1 += 1
    return happy_tickets_amount1


def method_hard(tickets_list: list) -> int:
    happy_tickets_amount2 = 0
    for digit in tickets_list:
        even = int(digit[0]) + int(digit[2]) + int(digit[4])
        odd = int(digit[1]) + int(digit[3]) + int(digit[5])
        if even == odd:
            happy_tickets_amount2 += 1
    return happy_tickets_amount2


def is_valid(input_value: str) -> int:
    while True:
        try:
            entered_value = int(
                input(f"Please, enter {input_value} between 0 to 1000000: ")
            )
            if 0 <= entered_value <= 1_000_000:
                break
        except ValueError:
            print("Please, enter integer between 0 to 1000000")
    return entered_value


def result(res_first: int, res_second: int) -> str:
    if res_first > res_second:
        return "Easy"
    if res_second > res_first:
        return "Hard"
    return "Both"


def main():
    tickets = happy_ticket_list(is_valid("start value"), is_valid("stop value"))

    first_variant = method_easy(tickets)

    second_variant = method_hard(tickets)

    result_methods = result(first_variant, second_variant)

    print(
        f"{result_methods} method won!\n"
        f"Easy has {first_variant} happy tickets!\n"
        f"Hard has {second_variant} happy tickets!"
    )


if __name__ == "__main__":
    main()
