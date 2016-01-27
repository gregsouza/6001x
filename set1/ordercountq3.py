def item_order(order):
    order = order.lower()
    ham_count = 0
    salad_count = 0
    water_count = 0
    size = len(order)
    counter = 0
    for char in order:
        if counter >= (size-4):
            break
        if char == 'h':
            if counter < (size-8):
                comp = order[counter: counter+9]
                if comp == 'hamburger':
                    ham_count+=1
        elif char == 'w':
            comp = order[counter: counter+5]
            if comp == 'water':
                water_count+=1
        elif char == 's':
            comp = order[counter: counter+5]
            if comp == 'salad':
                salad_count +=1
        counter+=1
    ret = 'salad:['+str(salad_count)+' salad] hamburger:['+str(ham_count)+' hambruger] water:['+str(water_count)+' water]'
    return ret


