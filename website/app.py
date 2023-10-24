import json
import sys
import os
with open('config.json','w') as f:
    json.dump({"bool":True,"old_prompt":""},f)

os.system("streamlit run trial.py")

