from ca_main import generate_ruleset, new_gen

# TODO recognize and output number of interesting case happening

start_rule = 89
finish_rule = 255

for rule in range(start_rule, finish_rule):
    ruleset = generate_ruleset(rule)
    data = [int(n) for n in '{0:020b}'.format(1)]  # Reset data

    print(data[-5:])

    dataset = []
    for _ in range(50):
        dataset.append(data)

        if len(dataset) > 20:
            last_5 = dataset[-5:]
            # if all of the last_5 are the same - constant
            # if every other from last_5 is the same - repetition
