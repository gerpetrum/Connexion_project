import base64

s = 'Nameless king - is one of the most fascinating boss in Dark Souls 3. He has great power and fast combos'
print(s)
s_encoded = s.encode('utf-8')
print(s_encoded)
s_bytes = base64.b64encode(s_encoded)
print(s_bytes)
decoded = base64.b64decode(s_bytes)
print(decoded)
