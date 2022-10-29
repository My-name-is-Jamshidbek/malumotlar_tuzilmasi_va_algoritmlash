"""
 Convert the Temperature
User Accepted:11445
User Tried:11583
Total Accepted:11778
Total Submissions:12766
Difficulty:Easy
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.
"""
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [float("%.5f"%(celsius + 273.15)),float("%.5f"%(celsius * 1.80 + 32.00))]
a =Solution()
print(a.convertTemperature(36.50))