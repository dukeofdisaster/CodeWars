def delete_nth(order, max_e):
    order.sort()
    first = order[0]
    count = 1
    for _ in order:
        if not order[_+1]:
            break
        if (order[_+1] == order[_]):
            count += 1
        else:
            count = 0
    print(count)
delete_nth([1,3,4,1,4], 3)
