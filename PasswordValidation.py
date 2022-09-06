'''
Just a sample regex to validate passwords from a kata
Uses "Positive lookahead" group construct
(1)Capital + (2)non-capital letters + (3)numbers, (4)No special characters(!), (5)6+ characters long.
'''
#               1           2        3         4         5
regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?!.*[\s\W_]).{6,}$"