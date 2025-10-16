# 1. Constant o(1)

# def get_first_friend(friends_ids):
#  """
#  o(1) - Constant time
#  Returns the first friend ID from the list.
#  """   
#  return friends_ids[0]  #always returns the first elemets


# 2. Logarithmic o(log n)
# def find_friend_with_id_starting_with( start_digit):
#     """
#     o(log n) - Logarithmic Time 
#     performs a binary search to find a friend ID starting with the given digit.
    
#     """
#     sorted_friends_ids = [0,1,2,3,4,5,6]
#     left, right = 0, len(sorted_friends_ids) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if sorted_friends_ids[mid]: #.startswith(start_digit):
#             return sorted_friends_ids[mid]
#         elif sorted_friends_ids[mid] < int(start_digit + '0' * (len(str(sorted_friends_ids)))):
#             left = mid + 1
#         else:
#             right = mid - 1
#             return None
        
        
# find_friend_with_id_starting_with(5)




# 3. Linear o(n)

# def find_friend_with_max_id(friends_ids):
#     """
#     o(n) - Linear Time
#     Finds the friends with the maximum ID from the list.
#     """
    
#     max_id = friends_ids[0] #initialize the max ID  with the first ID
#     for friend_id in friends_ids: # Iterate through each friend ID
#         if friend_id > max_id: # Compare with the current max id
#             max_id - friend_id # Update the max id if current id is greater
#     print(max_id)
# find_friend_with_max_id([1,2,3,4,5])
        
    
 
#  4. Linearithmic o(n log n)

# def rank_friends_by_id(friends_ids):
#     """
#     o(n log n) - Linearithmic Time
#     Sorts a list of friends IDs in ascending order.
#     """
#     print(sorted(friends_ids))
# rank_friends_by_id([0,1,2,3,4,5])



# 5. Quadratic o(n^2)

# def find_common_friends(friend_list1, friend_list2):
#     """
#     o(n^2) - Quadratic Time
#     Finds common friends between two lists of friends IDs.
#     """
#     common_friends = [] #Iinitialize any empty list to store common friends
#     for friend1 in friend_list1: # Iterare through each friend in the firts list
#         for friend2 in friend_list2: # Iterate thriugh each friend in the second list
#             if friend1 == friend2: #check if the friends are same
#                 common_friends.append(friend1) # Add the friend to the list
#     print(common_friends)
    
# find_common_friends([0,1,2,3,4],[5,6,7,0,3]) 



# 6. Cubic o(n^3)        

def find_common_friends_among_three_lists(friends_list1, friends_list2, friends_list3):
    """
    0(n^3) Cubic Time
    Finds common friends among three lists of friends IDs.
    """        
    common_friends = [] #Iinitialize any empty list to store common friends
    for friend1 in friends_list1: # Iterare through each friend in the firts list
        for friend2 in friends_list2: # Iterate through each friend in the second list
            for friend3 in friends_list3: #Iterate through each friend in the third list
             if friend1 == friend2 == friend3: #check if the friends are same
                 common_friends.append(friend1) # Add the friend to the list
    print(common_friends)
    
find_common_friends_among_three_lists([0,1,2,3,4],[5,6,4,0,3],[0,1,2,3,4])
    
                                           
   