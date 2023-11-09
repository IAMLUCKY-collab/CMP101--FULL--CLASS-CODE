
print("MR YUSUF AND SONS")
print("Enter the required information to calculate simple and compound interest respectively")
i_p = float(input("Enter your initial principal:   "))
i_r = float(input("Enter your initial rate:   "))
no_of_times_interests_per_time_period = float(input("Enter number of times interests per time period:   "))
no_of_time_period_elapsed = float(input("Enter number of time period elapsed:   "))

simple_interest = i_p * (1 + i_r * no_of_times_interests_per_time_period)
compound_interest = (i_p * (1+(i_r/no_of_time_period_elapsed))
                     ** no_of_time_period_elapsed*no_of_times_interests_per_time_period)

print("YUSUF AND SONS COMPANY")
print(f'Simple interest : {simple_interest}')
print(f'Compound interest : {compound_interest}')

#i am lucky