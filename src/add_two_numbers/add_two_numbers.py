def add_two_numbers(l1: list, l2: list) -> list:
    try:
        if len(l1) != len(l2):
            return None
        answer = []
        carry = 0
        for i in range(len(l1)-1, -1, -1):
            result = l1[i] + l2[i] + carry
            carry = int(result / 10) if (result / 10) >= 1 else 0
            answer.insert(0, result % 10)
        return answer
    except (IndexError, TypeError):
        return None
