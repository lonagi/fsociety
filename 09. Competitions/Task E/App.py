# НЕДОДЕЛАНА

N = int(input())
result = []

for test in range(N):
    E, N, K = list(map(int, input().split()))
    K = K*60

    users = dict()
    rides = dict()
    for i in range(E):
        event = input().split()
        if event[1] not in rides:
            rides[event[1]] = dict()
            
        if event[0] == 'ordered':
            rides[event[1]]['oredered'] = int(event[3])
            rides[event[1]]['to_arrive'] = int(event[4])*60
            rides[event[1]]['to_end'] = int(event[5])*60
            if event[2] in users:
                users[event[2]].append(event[1])
            else:
                users[event[2]] = [event[1]]

        if event[0] == 'arrived':
            rides[event[1]]['arrived']=int(event[2])

        if event[0] == 'started':
            rides[event[1]]['started']=int(event[2])


        if event[0] == 'finished':
            rides[event[1]]['finished']=int(event[2])

    # print(users)
    # print(rides)

    user_wait = dict([(user, 0) for user in users.keys()])
    for user in users:
        for user_ride in users[user]:
            # если пользователь не проебался сам
            if rides[user_ride]['started'] - rides[user_ride]['arrived'] <= K:
                proeb = -(rides[user_ride]['oredered'] + \
                    rides[user_ride]['to_arrive'] + \
                    K + rides[user_ride]['to_end'] - rides[user_ride]['finished'])
                if proeb > 0:
                    if user in user_wait:
                        user_wait[user] += proeb
                    else:
                        user_wait[user] = proeb
    print(user_wait)
    user_wait = sorted(user_wait.items(),
                       key=lambda x: (-x[1], x[0]), reverse=True)
    print(user_wait)

