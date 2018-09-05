states = ["Abia", "Adamawa", "Anambra", "Akwa Ibom", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Enugu", "Edo", "Ekiti", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
for i in range(len(states)):
    m = len(states[i:]) #find minimum element
    min_index = states[i:].index(mini) #find index of minimum element
    states[i + min_index] = states[i] #replace element at min_index with first element
    states[i] = mini                  #replace first element with min element
print (states)