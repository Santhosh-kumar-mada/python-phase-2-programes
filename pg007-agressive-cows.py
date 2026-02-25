#geeks for geeks - agressive cows
def aggressive_cows_linear(stalls, cows):
    stalls.sort()
    max_distance = stalls[-1]-stalls[0]
    answer = 0
    for distance in range(1,max_distance+1):
        count = 1
        last_position = stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last_position >= distance:
                count += 1
                last_position = stalls[i]
            if count == cows:
                answer = distance
            else:
                break
    return answer

a = [10,1,2,7,5]
print(aggressive_cows_linear(a,3))