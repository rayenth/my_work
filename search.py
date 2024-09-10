
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#this will find the search bar and inject a text in it
def searching_tunisianet(driver):
    x=""
    print("insert the gpu name or refernce or type in here : ")
    x=input()
    search_bar=driver.find_element(By.ID,"search_query_top")
    search_bar.send_keys(x)
    search_bar.send_keys(Keys.RETURN)


#this will find the commun html elements and make a list out of them 
def find_commun(e1,e2):
    li=[]
    for i in e1:
        for j in e2:
            if i==j:
                    li.append(i)
    if len(li)==1:
        return li[0]    
    else: 
        return li
    


#this will leave in the given list only the the items that start with a specified letter or text 
def filter_by(l,t):
    for i in l[:]:
          if not i.startswith(t):
               l.remove(i)



#this function will fill the dictionnary with the data scraped from the site
def collect_and_fill(listOfData,dic) : 
        dicc={}
        for spec in listOfData :
            for bglst in dic.values():
                    for pref in bglst[0]:
                        
                        if pref in spec:
                            bglst[1][len(bglst[1])-1]=spec
                            break    
        dicc=dic
        return dicc  


#this function will fill the lack of information from the site with "-"
def fill_t(dic):
    c={}
    for bglst in dic.values():
        bglst[1].append("-") 
    c=dic
    return c         
                               
                              
                    
                    
                    
                    






    