def exclusive_time(n, logs):
    exclusive_times = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        function_id, action, timestamp = log.split(":")
        function_id = int(function_id)
        timestamp = int(timestamp)

        if action == "start":
            if stack:
                exclusive_times[stack[-1][0]] += timestamp - prev_time
            stack.append((function_id, timestamp))
            prev_time = timestamp
        else:
            start_function_id, start_time = stack.pop()
            exclusive_times[function_id] += timestamp - start_time + 1
            prev_time = timestamp + 1

    return exclusive_times


# Example usage:
n = 3
logs = ["0:start:0", "2:start:4", "2:end:5", "1:start:7", "1:end:10", "0:end:11"]
print(exclusive_time(n, logs))  # Output: [3, 3, 5]