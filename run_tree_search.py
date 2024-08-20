import argparse
import os
import pandas as pd
import json
from tree_search_icd import get_icd_codes
from tqdm import tqdm
import csv
import streamlit as st
import tempfile
from pathlib import Path
from io import StringIO

# def process_medical_notes(file_path,model_name):
# def process_medical_notes(input_dir, output_file, model_name):
    
#     code_map = {}
    
#     if not os.path.isdir(input_dir):
#         raise ValueError("The specified input directory does not exist.")

#     # Process each file in the input directory
#     for files in tqdm(os.listdir(input_dir)):
#         file_path = os.path.join(input_dir, files)
#         print(file_path)
#         with open(file_path, "r", encoding="utf-8") as file:
#             medical_note = file.read()
    
#     if not os.path.isfile(file_path):
#         print(f"File does not exist: {file_path}")
#         return None
    
  
#     # if os.path.isfile(file_path):
#     #     st.write(f"File exists: {file_path}")
    
#     # try:
        
#     #     with open(file_path, "r",encoding="utf-8") as txtfile:
#     #         st.write(file_path)
#     #         medical_note = txtfile.read()
            
#     #         st.write(f"Content of the file: {medical_note[:1000]}")  # Print the first 1000 characters
#     # except Exception as e:
#     #     print(f"Error reading file: {e}")
#     #     return None
    
#     # print(f"File read successfully. Content length: {len(medical_note)}")

#     #print(medical_note)   
#     icd_codes = get_icd_codes(medical_note, model_name)
#     print(icd_codes)
#     # return icd_codes
# #     print(icd_codes)
# #     code_map[files] = icd_codes

#     with open(output_file, "w") as f:
#         json.dump(code_map, f, indent=4)
   

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Process medical notes to extract ICD codes using a specified model.")
#     parser.add_argument("--input_dir", help="Directory containing the medical text files")
#     parser.add_argument("--output_file", help="File to save the extracted ICD codes in JSON format")
#     parser.add_argument("--model_name", default="llama3-70b-8192", help="Model name to use for ICD code extraction")

#     args = parser.parse_args()
#     process_medical_notes(args.input_dir, args.output_file, args.model_name)

def process_medical_notes(filepath, model_name):
    
    
    try:
        for txtfile in filepath:
           with open(filepath, "r",encoding="utf-8") as txtfile:
               medical_note = txtfile.read()
            
          
    except Exception as e:
        # print(f"Error reading file: {e}")
        return None
    
   
    icd_codes = get_icd_codes(medical_note, model_name)
    return icd_codes



def add_custom_css():
    st.markdown(
        """
        <style>
        /* Remove padding around the main block */
        .block-container {
            padding: 1rem;
        }
        /* Remove padding around the top */
        header, footer, .reportview-container .main .block-container {
            padding: 5;
        }
        /* Fullscreen layout adjustments */
        .css-1d391kg { 
            padding: 5; 
        }

        h1 {
            text-align: center;
        }
         .table-wrapper {
            text-align: center;
        }




        </style>
        """,
        unsafe_allow_html=True,
    )
def main():
    st.set_page_config(layout="wide",page_icon='🔎',page_title='ICD Identifier') 
    add_custom_css()
    st.title("ICD Code Extractor From Medical Notes")
  
    col1, col2 = st.columns([1, 5])
    with col2:
        
        file_uploads=st.file_uploader('Choose Medical Note File',type='txt', accept_multiple_files=True)
     
        submit = st.button("Submit")
       
    
    with col1:
         model_name = st.selectbox(
            "Select Model",
            ["llama3-70b-8192", "mixtral-8x7b-32768"],
            index=0  # Default model selected
        )

    if submit :
        
        for file_input in file_uploads:
            file_name = Path(file_input.name).name
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        
                temp_file.write(file_input.getbuffer())
                temp_file.flush()
                file_paths = temp_file.name
                response=process_medical_notes(file_paths, model_name)
                res_data=pd.DataFrame(response,columns=['ICD Code','Code Description','Evidence From Notes'])
                with col2:
                    

                #     st.markdown(f"""
                    
                         
                #     <div class="custom-table-container" >
                #         <h4>Case Id: {file_name}</h4>
                 
                #         <div class="table-wrapper"  >
                #             {res_data.to_html(classes='table-wrapper', index=False)}
                #         </div>
                #     </div>
                  
                   
                # """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <h5>Case Id: {file_name}</h5>
                    """, unsafe_allow_html=True)
                    st.markdown(res_data.style.hide(axis="index").to_html(), unsafe_allow_html=True)

                # st.write(response)

if __name__=="__main__":
    main()