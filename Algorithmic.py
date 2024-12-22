
#########################O(n^2)########
def FindCommomElements1(arr1,arr2):
    
    common_elements=[]
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2 and elem1 not in common_elements:
                common_elements.append(elem1)
    return(common_elements)            

#########################O(n)########

def FindCommonElements2(arr1,arr2):
    common_elements=[]
    all_elements={}

    for elem1 in arr1:
        if elem1 in all_elements:
           all_elements[elem1]+=1
        else:
            all_elements[elem1]=0   

    for elem2 in arr2:
        if  elem2 in all_elements:
            all_elements[elem2]+=1
        else:
            all_elements[elem2]=0  

    for elem, count in all_elements.items():
        if count > 0:
            common_elements.append(elem)     

    return(common_elements) 



################################

def FindCommonElements_between_three_arrays(arr1,arr2,arr3):
    instriction=[]
    common_elements=[]

    my_set1=set(arr1)
    my_set2= set(arr2)
    my_set3= set(arr3)

    for elem2 in my_set2:
        if elem2 in my_set1:
            instriction.append(elem2)

    for elem3 in my_set3:
        if elem3 in instriction:
            common_elements.append(elem3)

    return(common_elements) 




################################

def count_vowels(str):
   
   num_vowels=0
   num_consonants=0
   vowels=["a","i","e","o","u","A","I","E","O","U"]
   for char in str:
       if char in vowels:
           num_vowels+=1
       elif char.isalpha():
           num_consonants +=1    

   return num_vowels, num_consonants
       



def find_median_char(str):
    sorted_string = sorted(str)
    n = len(sorted_string)
    if n % 2 == 1:  
        median_char = sorted_string[n // 2]
    else:  
        median_char = sorted_string[(n // 2) - 1]
    
    return median_char



def highest_scoring_word(sentance):

    words=sentance.split()
    max_score=0
    best_word=""


    for word in words:
        score=0
        for char in word:
            print(ord(char) - ord('a') + 1)
            score +=  ord(char) - ord('a') + 1
        if score>max_score:
            max_score=score
            best_word=word

    return best_word


def biggest_number(num1,num2,num3):

    if num1>num2:
        largest= num1
    else:
        largest = num2

    if num3>largest:
        largest=num3

    return largest        


print(biggest_number(3, 7, 5))  
print(biggest_number(10, 2, 10))  
print(biggest_number(-1, -5, -3))  