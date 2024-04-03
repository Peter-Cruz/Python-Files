#peterOrderReceiptList.py

import MobilePlan

def main():
    plan1 = MobilePlan.MobilePlan( "32GB Plan", 32, 32, 19.99)
    plan2 = MobilePlan.MobilePlan( "45GB Plan", 45, 45, 25.99)
    plan3 = MobilePlan.MobilePlan( "18GB Plan", 18, 27, 11.29)
    plan4 = MobilePlan.MobilePlan( "100GB Plan", 100, 60, 40.00)

    plans = [plan1, plan2, plan3, plan4]

    plan2.set_rate_factor(3)
    plan3.set_rate_factor(2)

    total_cost = 0
    total_data = 0
    total_talk_time = 0

    for plan in plans:
        print(plan)
        total_cost += plan.get_order_cost()
        total_data += plan.get_order_data()
        total_talk_time += plan.get_order_talk_time()

    print(f"Total Cost of the plans picked are: ${total_cost:0.2f}")
    print(f"And total available data is {total_data} GB and total talk time is {total_talk_time:.2f} hours")

if __name__ == '__main__':
    main()