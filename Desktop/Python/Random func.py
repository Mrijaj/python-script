import random
first_name=[" Viv" ," Sumit", " Karl ", " Sammy ", "Logan ", "Haris ", "Soria ", "Pitbull ", "Ronald ", "Corey ", " Logan"]
last_name=[" paul" ," Moris ", " sora ", "Loxa ", "Begu ", " point", " Gay", " andre", "gowda ", "chaman ", " anime"]
street_names=[" Main" ," Low", " straight", " curved", " bend", " high", " u turn", " pine ", " cedar", "Main pine ", "Killer "]
fake_cities=[" pune" ,"Mumbai ", " aurangabad", " latur ", " kolkata ", " nanded", " patna", " jamshedpur", "ranchi ", " Gondia", " Wasim "]
states=[" Maharashtra" ," jharkhand ", " Bihar", " uttar pradesh ", " Madhya pradesh", "West bengal ", "Andaman ", "Goa ", " Chattisgarh", "Kerala ", "Bengaluru "]
email_add=["@ymail" ,"@gmail ", "@google ", "@hpe ", "@cognizant ", " @microsoft", "@yahoo ", "@hemms ", "@swissbank ", " @dope", " @mahipal"]
    first=random.choice(first_name)
    first=random.choice(first_name)ast=random.choice(last_name)
    phone=f"{random.randint(621,1000)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    street_num=random.randint(10,99)
    street=random.choice(street_names)
    city=random.choice(fake_cities)
    state=random.choice(states)
    zip_code=random.randint(400000,999999)
    Address=f"{street_num} {street} {city} {state} {zip_code}"
    email=random.choice(email_add)
    
    email=first.lower().strip() + last.lower().strip() + email+".com"
    print(f" {first} {last} \n {phone}\n {Address}\n {email}\n")
    #Hello
