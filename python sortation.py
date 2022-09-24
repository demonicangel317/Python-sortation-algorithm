"""
FIT2004 Assignment 1
Ravindu Santhush Ratnayake, 32634269, rrat0006@student.monash.edu
"""

def max_item(myList):
    """
    This function takes in a list as an argument and returns its maximum value.
    First it iterates through the entire list adjusts the maximum value by comparing
    the current maximum value to the current list item in the iteration
    :Input:
        argv1:myList The list that is used to get the maximum value from
    :Output:
        returns maximum value of the list
    Time Complexity:
        Best :O(N) N = length of the list
        Worst:O(N) N = length of the list
    Space complexity:
        Aux: O(1)
        Input:O(N) N = number of elements in list
    """
    maxItem = myList[0]
    for item in myList:
        if item < maxItem:
            maxItem = item
    return maxItem


def empty_array(space_allocate):
    """
    Returns a list containing n number of lists
    Takes in the amount of space to allocate then returns a list of list depending on the value entered
    :Input:
        argv1:space_allocate amount of space to allocate to the list
    :Output:
        returns list containing n number of lists
    Time Complexity:
        Best: O(N) N = number of lists to append to list
        Worst: O(N) N = number of lists to append to list
    Space complexity:
        AUX: O(N) N = Size of the list to be created
        Input: O(1)
    """
    count_array = [None] * (space_allocate)
    for i in range(len(count_array)):
        count_array[i] = []
    return count_array

def radix_sort_string_word(myList, index, roster=27):
    """
    Sightly modified radix sort which is used to change the results list according to the order of the words.
    This takes in an index to indicated which sublist element needs to be taken.
    Input:
        :param myList:The list that needs to be sorted
        :param index: which index of the sublist must be taken
        :param roster: the number of letters the team has been constructed in
        :return: the sorted list

    Time Complexity:
        K = length of team string
        M = roster size
        N = Number of elements in results
        O(KM + KN)
        ~O(KM)
        Best: O(KN)
        Worst: O(KN)

    Auxillary Space:
        The creation of empty array take O(M) space M = roster size
        Then we will append all the elements into this therefore an additional N space will be taken.
        therefore, the auxiliary space is,
        =O(M + N) N = number of elements inside the array(myList)
    Input Space:
        =O(N) N = N = number of elements inside the array(myList)
    Post Condition:
        The list is sorted on based on the words in the specific index of the sublist
    """

    numColoums = len(myList[0][1])                                                                                      #O(1)
    # creating the count array
    count_array = empty_array(roster)                                                                                   #O(M) M = size of roster
    # iterate through the main list
    for column in range(-1, -(numColoums + 1), -1):                                                                     #O(K) M = length of team string
        # chekcs if the coloumn length is greater than item length
        for item in myList:                                                                                             #K*N =O(KN) N = length of list
            listItem = item[index]
            index2 = ord(listItem[column]) - 65                                                                         #K*N =O(KN)
            count_array[index2].append(item)                                                                            #K*N =O(KN)
        # rearrange the semi sorted list back into the original list
        rearrangeList(myList, count_array)                                                                              #K*(N + M)=O(KN + KM)
        # reset count array
        count_array = empty_array(roster)                                                                               #K*M = O(KM)
    return myList



def rearrangeList(mainList, suppList):
    """
    This function is a part of radix sort. It takes in a supplementary list of lists
    which contains the elements in the main list.
    It then iterates through the supplementary list and replaces the elements of the mainlist
    with a new ordering by the supplementary list while maintaining stability
    :Input:
        argv1:mainlist the list where the ordering is to be changed
        argv2:suppList the list which contains the elements of the main list
    :Postcondition:
        mainlist input has a new ordering of its elements
    Time Complexity:
        The outer loop will run M times and the inner loop will run a total of N times
        Best: O(N + M) N = Length of mainList M = length of supplementary list
        Worst: O(N + M) N = Length of mainList M = length of supplementary list
    Space Complexity:
        Aux : O(1)
        Input : O(M + N) M = number of elements in mainList N = number of elements in supplementary list
    PostCondition = the mainList will now have the supplementary list ordering

    """
    index = 0
    for i in range(len(suppList)):
        itemList = suppList[i]
        if (len(itemList) == 0):
            continue
        else:
            frequency = len(itemList)
            for j in range(frequency):
                mainList[index] = itemList[j]
                index += 1

def counting_sort_string(myString, roster):
    """
        A countring sort which takes a string and orders the characters lexicographically
        Input:
            :param myString the string used to be sorted
            :param size of the roster
        Output:
            :return: return a sorted string
        Time Complexity:
            Best : O(N + M) ~ O(N) N = number of characters in string M = size of roster
            Worst : O(N + M) ~O(N) N = number of characters in string list M = size of roster
        Auxillary Space:
            O(N+M) N = Number of elements in the list created from string  M = number of elements created in the
                                                                               supplementary list
        Input Space:
            O(N) N = String length
        Output:
            a sorted string is returned
        """

    """
    list() function
    Time Complxity: O(N) N = length of string
    AUX Space: O(N) N = length of string
    """
    myList = list(myString)
    """
    Creating the Empty array in the list
    Time Complexity:
        O(M) M = size of Roster
    Auxiliary Space:
        O(M) M = Size of the list due to size of roster
    """
    count_array = empty_array(roster + 1)
    # update count array
    """
    Appending items in Main list to the supplementary list
    Time Complexity:
        O(N) N = number of lements in the list
    Auxillary Space: 
        O(N) N = number of list items appended into supplementary list
    """
    for item in myList:
        count_array[ord(item) - 65].append(item);
    index = 0
    """
    Rearranges the elements of the main list based on supplementary list length
    Time Complexity:
        O(N + M) N = number of elements in the list M = number of elements in supplementary list
    Auxillary Space: 
        O(1)
    """
    for i in range(len(count_array)):
        item = count_array[i]
        frequency = len(item)
        for j in range(frequency):
            if frequency == 0:
                continue
            myList[index] = item[j]
            index += 1
    """
    .join() time complexity is O(N) N = number of elements in the list
    """
    return "".join(myList)

def counting_sort(myList, listIndex):
    """
    A stable counting sort sued to sort the results list this takes in an additional argument which indicated the index
    of the element within the list used to
    Input:
        :param myList the list that s=is used to sort
        :param listIndex: the index of the element of the results table
    Output:
        :return: return a sorted results based on the score
    Time Complexity:
        Best : O(N + M) N = number of elements in input list M = size of maximum element
        Worst : O(N + M) N = number of elements in input list M = size of maximum element
    Auxillary Space:
        O(N+M) N = Number of elements in the input list M = number of elements created in the supplementary list
                                                            due to maximum item
    Input Space:
        O(N) N = Number of elements in the input list
    Post Condition:
        The list is now ordered according to the value from the index provided in the sublists
    """

    # finding maximum
    maxItem = myList[0]
    """
    Finding Maximum value
    Time Complexity:
        O(M)
    Aux Space Complexity:
        O(1)
    """
    for item in myList:                                                                                                 #O(N) N = length of lsit
        if item[listIndex] > maxItem[listIndex]:
            maxItem = item
    # initialize count array

    """
    Creating the Empty array in the list
    Time Complexity: 
        O(M) M = size of maximum element in the array
    Auxiliary Space: 
        O(M) M = Size of the list due to size of max element
    """
    count_array = empty_array(maxItem[listIndex] + 1)
    # update count array
    """
    Appending items in Main list to the supplementary list
    Time Complexity:
        O(N) N = number of lements in the list
    Auxillary Space: 
        O(N) N = number of list items appended into supplementary list
    """

    for item in myList:
        count_array[(maxItem[listIndex] - item[listIndex])].append(item);
    index = 0
    """
    Rearranges the elements of the main list based on supplementary list length
    Time Complexity:
        O(N + M) N = number of elements in the list M = number of elements in supplementary list
    Auxillary Space: 
        O(1)
    """
    for i in range(len(count_array)):
        item = count_array[i]
        frequency = len(item)
        for j in range(frequency):
            if frequency == 0:
                continue
            myList[index] = item[j]
            index += 1
    return myList


def return_sub_list(list, index):
    """
    This function takes in a list and a value called index which indicates upto which point the sublist must be copied
    Input:
        :param list: the list in which the sublist must be created
        :param index: the index value upto which the sublist must be brought onto
    Output:
        :return:returns a sublist up to the index provided
    Time Cmplexity:
        Worst:O(N) N = length of list
        Best:O(N) N = length of list
    Space Complexity:
        Aux:O(N) N = size of input list
        Input:O(N) N = size of input list

    """

    if (index >= len(list)):
        return list
    else:
        subList = [None] * (index)
        for element in range(index):
            subList[element] = list[element]
        return subList


def searchedmatches(results, searchScore):
    """
    This function takes in a sorted list and then it returns another list which will have the searched values.
    If the searched values are not present then the elements with the next greatest value will be returned in a new list.
    IF no greater elements are found then this will return a null list
    :param results: the list of results used to find the search values
    :param searchScore:the integer input that is used to find the search value
    :return: a list which may contain the search results
    Time Complexity:
        Worst:
        O(2N) = O(N) N = length of the input list
        Best:
        O(N) =  N = length of the input list

    Auxillary Time Complexity:
        In a case where this list has all equal values for the score and it is all greater than this the seacrh value
        then we will place all the items of the list in the list we return
        therefore this will take,
        O(N) space N = number of elements in the input list
    Input Time Complexity:
        O(N) space N = number of elements in the input list
    Precondtion:
        Results List must be fully sorted

    """
    searchList = []
    index = 0
    while (index < len(results) and results[index][2] >= searchScore):
        temp = results[index]
        if (results[index][2] == searchScore):

            searchList.append(results[index])
        index += 1

    higherScore = 0
    if (len(searchList) == 0):
        index -= 1
        higherScore = 0
        if (index >= 0):
            higherScore = results[index][2]
            index = 0
            while (index < len(results) and results[index][2] >= searchScore):
                temp = results[index]
                if (results[index][2] == higherScore):
                    searchList.append(results[index])
                index += 1
    return searchList


def uniqueList(results):
    """
    The purpose of this function is to remove the duplicated elements from a fully sorted list
    It first  goes through the list upto the n-1th position and compares every element with the next adjacent element
    and then appends it to the new sublist created.
    Then finally it checks if the nth element exists in the unique list created and if it exists then appends the final
    element into the unique list
    Input:
        :param results: The list used to derive the list with non duplictaed elements
    Output:
        :return: a list with non duplicataed items.
    Time Complexity:
        Worst:
        Goes throught he results list provided which Takes O(N) N = list length time and the string comparison of two
        teams is 2*O(M) M = length of string of team ,Therefore totoal time is,
        =O(M*N)
        Best:
        =O(M*N)
    Auxillary Time Complexity:
        =O(N) N = length of original list
    Input Space Complexity:
        =O(N) N = length of original list
    Precondtion:
        List must be fully sorted

    """
    nonDuplicatedList = []
    for index in range(len(results) - 1):
        if (results[index][2] == results[index + 1][2]):
            if ((results[index][0] == results[index + 1][0]) and (results[index][1] == results[index + 1][1])):
                continue
        nonDuplicatedList.append(results[index])

    if(len(nonDuplicatedList) == 0):
        nonDuplicatedList.append(results[0])

    elif(not((nonDuplicatedList[len(nonDuplicatedList) - 1][2] == results[len(results) - 1][2]) and (nonDuplicatedList[len(nonDuplicatedList) - 1][1] == results[len(results) - 1][1]) and (nonDuplicatedList[len(nonDuplicatedList) - 1][0] == results[len(results) - 1][0]))):
        nonDuplicatedList.append(results[len(results) - 1])

    return nonDuplicatedList;


def analyze(results, roster, score):

    """
    Input:
        :param results: the results list used to do the analysis
        :param score: the score that we need to seek within the results list
        :param roster:the roster that makes up the teams in the results list
    Output:
        :return: returns the top 10 search results and a list with the search items
    Time Complexity:
        Best: O(N*M) M = length of string in team N = number of elements in the list
        Worst: O(N*M) M = length of string in team N = number of elements in the list
    Auxillary Space Complexity:
        O(N + M) M = length of string in team N = number of elements in the list
    Input Space Complexity:
        O(N) N = length of results
    """

    """
    loops through the whole results and sorts the characters in each and every team in results
    Time Complexity:
        2*O(M*N)
        ~O(M*N) M = length of string in team N = number of elements in the list
    Auxillary Time Complexity:
        O(M) M = length of string in team 
    """
    for result in results:
        result[1] = counting_sort_string(result[1], roster)                                                                #O(M*N)
        result[0] = counting_sort_string(result[0], roster)                                                                #O(M*N)

    """
    reverses the values of the list and appends everthing to the existing list
    Time Complexity:
        O(N) N = number of elements in the list
    Auxillary Space:
        O(N) N = number of elements in the list
    """
    for index in range(len(results)):
        reveredResult = []
        reveredResult.append(results[index][1])
        reveredResult.append(results[index][0])
        reveredResult.append(100 - results[index][2])
        results.append(reveredResult)

    """
    radix sort the results list based on team 2 values first
    radix sorts the results list based on team 1 values second
        
    Time Complexity:
        O(NM) N = number of elements in the list M = length of the string of team 
    Auxillary Space:
        O(N + M) N = number of elements in the list M = roster length / length of string in team
    """
    radix_sort_string_word(results, 1, roster)
    radix_sort_string_word(results, 0, roster)

    """
    finally uses counting sort to sort list by the score
    Time Complexity:
        O(N + K) N = number of elements in input list K = size of maximum element
    Auxillary Space:
        O(N + J) N = Number of elements in the input list J = number of elements created in the supplementary list
                                                            due to maximum item
        
    """
    counting_sort(results, 2)

    """
    removes duplicates from a string
    Time Complexity:       
        =O(M*N) N = length of string of team, M = list teams string length 
    Auxillary Time Complexity:s
        =O(N) N = length of results
    """
    nonDuplicatedList = uniqueList(results)

    """
    Returns a list with the search item
    Time Complexity:
        O(N) = O(N) N = length of the results
    Auxillary TIme Complexity:
        O(N) space N = number of elements in the results list
    """
    searchList = searchedmatches(nonDuplicatedList, score)

    """
    Returns the top ten sub results
    Time Cmplexity:
        O(N) N = length of list
    Auxillary Space Complexity:
        O(N) N = size of input list
    """
    subList = return_sub_list(nonDuplicatedList, 10)

    returnList = []
    returnList.append(subList)
    returnList.append(searchList)
    return (returnList)

"""
This the driver, where you can have your programming codes here.
No other codes should be outside function or the driver; as I saw a lot in the code review.
"""
if __name__ == "__main__":
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
        ]
    # looking for a score of 64
    score = 64
    # running the function
    analyze(results, roster, score)