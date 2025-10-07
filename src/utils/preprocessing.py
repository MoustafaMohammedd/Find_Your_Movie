

def preprocess_data(df):
    
    df=df[["title","description"]] 
       
    df["description"]=df["description"].astype("string")
    df["title"]=df["title"].astype("string")
    
    return df