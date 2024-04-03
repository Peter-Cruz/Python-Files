#MobilePlan.py

class MobilePlan:
    def __init__(self, plan_name, data_gb, talk_time, cost, rate_factor=1):
        self.__plan_name = plan_name
        self.__data_gb = data_gb
        self.__talk_time = talk_time
        self.__cost = cost
        self.__rate_factor = rate_factor

    def get_plan_name(self):
        return self.__plan_name

    def get_order_data(self):
        return self.__data_gb * self.__rate_factor

    def get_order_talk_time(self):
        return self.__talk_time * self.__rate_factor

    def get_order_cost(self):
        return self.__cost * self.__rate_factor

    def set_rate_factor(self, rate_factor):
        self.__rate_factor = rate_factor

    def __str__(self):
        ret_str = f'{self.__plan_name} of ${self.__cost:.2f} provides {self.__data_gb} GB in data and {self.__talk_time} hours in talk time. \n'
        
        return ret_str
