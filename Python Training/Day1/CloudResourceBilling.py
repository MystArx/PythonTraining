def billing(compute_hours,storage,plan):

    if plan=="Basic":
        discount=0
        basic(compute_hours,storage)
    if plan=="Premium":
        discount=0.1
        premium(compute_hours,storage,discount)
    if plan=="Enterprise":
        discount=0.2
        enterprise(compute_hours,storage,discount)



def basic(compute_hours,storage):
    support=1000
    compute_cost=compute_hours*5
    storage_cost=storage*2


def premium(compute_hours,storage,discount):
    support=1500
    compute_cost=compute_hours*5*discount
    storage_cost=storage*2

def enterprise(compute_hours,storage,discount):
    compute_cost=compute_hours*4
    storage_cost=storage*2*discount