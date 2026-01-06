data = {3: 30, 1: 10, 2: 20}

# Ascending order
asc = dict(sorted(data.items()))
print("Ascending order:", asc)

# Descending order
desc = dict(sorted(data.items(), reverse=True))
print("Descending order:", desc)
