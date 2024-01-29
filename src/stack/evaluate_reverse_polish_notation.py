"""
2024-01-28

150. Evaluate Reverse Polish Notation 
(https://leetcode.com/problems/evaluate-reverse-polish-notation)
"""
import math

from src.utils import timer


class EvaluateReversePolishNotationSolution:
    @timer
    def eval_rpn(self, tokens: list[str]) -> int:
        """
        stack 활용, operator 만날 때까지 push 하다가, operator 만나면 int pop(), pop().
        계산 결과 push().

        O(N)
        0.0250ms
        """
        operator = "+-*/"

        stack: list[str] = []
        for n in tokens:
            if not n in operator:  # numbers
                stack.append(n)

            if n in operator:  # operators
                right_n = int(stack.pop())
                left_n = int(stack.pop())
                if n == "+":
                    calc_n = left_n + right_n
                elif n == "-":
                    calc_n = left_n - right_n
                elif n == "*":
                    calc_n = left_n * right_n
                else:
                    calc_n = math.trunc(left_n / right_n)

                stack.append(str(calc_n))

        return int(stack[0])
