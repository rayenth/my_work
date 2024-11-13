from to_odf import make_ods
from to_exel import make_excel
from functions import create_driver,clean_by
#the job of this is to make the terminal prettier
from search import searching_tunisianet,find_commun,filter_by,collect_and_fill,fill_t
from selenium.webdriver.common.by import By
responce ="n"

#setting up the driver 
#sys.stdout = open(os.devnull, 'w')
#sys.stderr = open(os.devnull, 'w')
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
url="https://www.tunisianet.com.tn"
path="/usr/local/bin/chromedriver"

driver=create_driver(url,path)
print(driver.title)

print("_____________welcome to gpu_tunisianet searcher_______________")
while(responce=="n"):
    print("insert the gpu name or refernce or type in here : ")
    texti=input()
    searching_tunisianet(driver,texti)
    print (texti)

    #finding the div that contains the list of the products

    element_0 = driver.find_elements(By.CLASS_NAME, "products")
    element_1 = driver.find_elements(By.CLASS_NAME, "wb-product-list")
    l=[]
    l=find_commun(element_0,element_1)
           

    #filtring the div that we found leaving only the GPU's info as html element


    divs=driver.find_elements(By.TAG_NAME,"div")
    products=driver.find_elements(By.CLASS_NAME,"item-product")
    products_final=[]
    products_final=find_commun(divs,products)


    l=[]

    #the list that contains the gpu name and ram
    description=driver.find_elements(By.CLASS_NAME,'listds')


    #not all the gpu info are in the "product_final" list
    #as you  can see the price is elsewhere
    items_price=driver.find_elements(By.CLASS_NAME,"price")


    #there is a extrat empty item that is being added due to html structure in the list so we remove it 
    lp=[i.text for i in items_price if i.text!=""]


    #the actual element that contains the most of the description of the gpu
    item_name=driver.find_elements(By.CLASS_NAME,'product-title')
    item_name0=driver.find_elements(By.CLASS_NAME,'h3')
    l=find_commun(item_name,item_name0)


    li=[i.text for i in l]
    lps=[lp[i] for i in range(0,len(lp)) if li[i].startswith("C") ]


    #==========> name of the items


    lo=filter_by(li,"Carte Gra")
    l=[]

    #getting the ram data
    for i in li :
        x=clean_by(i,"/")
        l.append(x[1]) 
    # ram list
    ram_lst=[[],l]
    

    #more cleaning the info of description and turning it to a text
    as1=[]
    for i in description:
        x=i.find_element(By.XPATH,'.//a')
        as1.append(x.text)
    lis=[]

    lis=filter_by(as1,"C")

    print("there is ",len(li),"items in the list ")


    # dic[key][0] = the filters that will be applied to fetch the specs
    # dic[key][1] = where the specs will be stored
    dic={"name":[["Carte","carte"],[]],'Bus Memory':[['bits','bus'],[]],'Engine Boost Clock':[['MHz'],[]],'Interface (port)':[['HDMI'],[]],'Memory Clock':[['Gbit','Gbps'],[]],'Consumtion':[['CONSOMATION','Consomation'],[]],'Recomanded Power Supply':[['RECOMMAND','BLOC',"Puissance minimale requise pour le système",'recommandée'],[]],'Maximum Resolution':[['solution','SOLUTION'],[]],'Dimensions':[['Dimension','dimension','DIMENSION'],[]],'Weight':[['poids','Poids'],[]],"PCI    interface":[["PCI"],[]]}

    for i in as1:
        pre_list=clean_by(i," - ")
        dic=fill_t(dic)
        dic=collect_and_fill(pre_list,dic)
    dic["Memory"]=ram_lst
    dic["Price"]=[[],lps]

    #make_ods(dic)
    make_excel(dic,texti)






    print("We are done go check the excel file GPU_Data.xlsx that has been created in this directory !!!!")
    print("=====================================\n=====================================\n")
    print("are you satisfied with the answer [y/n]??")
    responce=input()

driver.close()




    
    





    
    






