import re
import string

trigger_words = ["waiter", "waiters", "waitstaff", "waitstaffs", "all-rounder","all-rounders", "runner", "runners", "floor staff", "rsa", "join our team", "requirements","hiring", "tuyển dụng", "tuyển nhân viên", "tuyển nam", "tuyển người"]
exclude_words = ["i'm looking for"]

def preprocess_text(text):
    # Step 1: Trim leading and trailing spaces
    text = text.strip()
    
    # Step 2: Remove emojis and other characters that could prevent further processing
    # This regex pattern matches most common emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    text = emoji_pattern.sub(r'', text)
    
    # Step 3: Convert text to lowercase
    text = text.lower()

    # Step 4: Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 5: Remove numbers
    text = re.sub(r'\d+', '', text)

    # Step 6: Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def is_valid(post, trigger_words, exclude_words = []):
    post = preprocess_text(post)
    for word in trigger_words:
        if word in post:
            for ex_word in exclude_words:
                if ex_word in post:
                    return False
            return True
    return False
        
# Desired post
post = """|| CHEF / WAITSTAFF / KITCHEN HAND ||
Cronulla
We are a small, boutique restaurant in Cronulla serving modern Australian cuisine and we’re looking for a part time chef, casual waitstaff, and a kitchen-hand.
We are a close-knit, caring and friendly team who love a laugh. We take pride in offering our guests high quality food and great service, and are looking for someone to join us and share their talents with our customers, who are like family to us.
We are continually doing things to make our venue and workspaces better and better, and are open to creating opportunities for growth where we can.
If this place sounds like it’s for you please reach out and send your resume to info@littleparrot.com.au!
CHEF
Must be available minimum of 2 x shifts per week (we open wed-sat night and friday and Sunday lunches), and ideally available to cover the other chef when on holidays once per year.
Minimum 3 years experience as a chef and able to handle a busy kitchen / lots of orders coming in
Looking for a team-player who is willing to help more junior staff grow
COOK
Looking for someone who is available 2-3 shifts week (we open wed-sat night and friday and Sunday lunches),
Must have experience on the grill and fryer - we’re a small restaurant so you will be involved in a lot of parts! Even better if you can make desserts.
At least 2 years experience
WAITSTAFF
We are looking for someone friendly and personable, who is a natural at caring for others and providing great experiences.
We have availability for work 1-4 shifts per week (night or day). we can arrange set shifts but ideally you will be flexible. We are open wed - sat night and sunday / friday lunch
Must have experience as a waiter/waitress: taking orders, serving guests
Knowing how to make coffee is a bonus, otherwise we are happy to train teh right person
Must have RSA
KITCHEN HAND
Looking for someone to take on 2-3 shifts per week
We are open wed - sat night and friday and sunday lunches
Must be experienced in working in a busy kitchen
-
"""

# Data which should be excluded
not_a_job_1 = """
Hello peeps!! 
I’m looking for a job as an all rounder in a cafe Monday to Friday. 
I’m situated in Campbelltown, 4+ years in hospitality, diploma as a restaurant manager knowing how to make coffee, manage till and all regarding FOH and BOH. 
Pm me so I can forward to you my latest resume. 
Thank you 
Sarah
"""

# Data with emoji
not_a_job_2 = """
🛍️ HÀNG CÓ SẴN ORDER NOW OR CRY LATER 🛍️ 
🎀 Secret Labubu V2 1️⃣8️⃣ 
🎀 Combo Catch Me Pink S + Black 4️⃣0️⃣ 
🎀 LIMITED MERI LABUBU 2️⃣0️⃣ 
🎀 Catch Me Pink S 2️⃣0️⃣
🎀 Set Labubu V1 2️⃣0️⃣
🎀 Set Labubu V2 2️⃣6️⃣
🎀 Cheer Up Baby 5️⃣ 
🎀 Set Bé 3 1️⃣8️⃣
"""


print(is_valid(post, trigger_words, exclude_words))
print(is_valid(not_a_job_1, trigger_words, exclude_words))
print(is_valid(not_a_job_2, trigger_words, exclude_words))