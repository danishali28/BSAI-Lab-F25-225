import math

count = 0

def minimax(depth,index,is_max,score,target):
    global count

    if depth == target:
        count += 1
        return score[index]

    if is_max:
        return max(
            minimax(depth+1,index*2,False,score,target),
            minimax(depth +1,index*2+1,False,score,target)
        )

    return min(
        minimax(depth+1,index*2,True,score,target),
        minimax(depth+1,index*2+1,True,score,target)
    )

score=   [3,5,2,9,3,5,2,9]

target=  int (math.log2 (len  (score)))
result=minimax(0,0,True,score,target)

print("Minimax value :",result)
print("Leave Eliminated:",count)


#alpha beta pruning

import math

count= 0

def alphabeta(depth,  index, is_max,score,  target,alpha,beta):
    global count

    if depth == target:
        count += 1
        return score[index]

    if is_max:
        value = float("-inf")

        for i in range(2):
            value = max(value,alphabeta(
                depth + 1,index*2+i,False,
                score,target,alpha,beta
            ))

            alpha = max(alpha,value)

            if alpha >= beta:
                break

        return value

    value = float("inf")

    for i in range(2):
        value = min(value,alphabeta(
            depth+1,index*2+i,True,
            score,target,alpha,beta
        ))

        beta = min(beta, value)

        if alpha >= beta:
            break

    return value

score=   [3,5,2,9,3,5,2,9]

target=int(math.log2(len(score)))

result=alphabeta(
    0,0,True,score,target,
    float("-inf"),float("inf")
)

print("Alpha-beta values:",result)
print("Leave evaluted",count)