import os
import math


# Example variable assignment and comparison
x = 12
y = 1
print(x == y)

# Test dict
label_map = {"happy": 0, "sad": 1, "angry": 2, "neutral": 3}
# Example SQL queries
selection_query = (
    "SELECT JID, Journal FROM `journal` " "WHERE status = %(unique_timestamp)s "
)

# Example SQL queries
insertion_query = "INSERT IGNORE INTO `journal_analysis` (JID, AnalysisValue, Flag, Indicators) VALUES (%(JID)s, %(AnalysisValue)s, %(Flag)s, %(Indicators)s) "
# Test format
a = 1
b = 2
print(a == b)

c = math.pi * 2

print(f"2pi = {c:.5f}")

print(os.getcwd())