prompt_template_dict = {"mixtral-8x7b-32768" : """[Case note]:
{note}
[Example]:
<code descriptions>
* Gastro-esophageal reflux disease
* Enteroptosis
* Acute Nasopharyngitis [Common Cold]
</code descriptions>

<response>
* Gastro-esophageal reflux disease: Yes,Patient was prescribed omeprazole. 
* Enteroptosis: No.
* Acute Nasopharyngitis [Common Cold]: No.
</response>

[Task]:
Follow the format in the example response exactly, including the entire description   after your (Yes|No) judgement , followed by a newline. 
Consider each of the following ICD-10 code descriptions and evaluate if there are any related mentions in the Case note.
{code_descriptions}""",

"llama3-70b-8192": """[Case note]:
{note}

[Example]:
<code descriptions>
* Gastro-esophageal reflux disease
* Enteroptosis
* Acute Nasopharyngitis [Common Cold]
</code descriptions>

<response>
* Gastro-esophageal reflux disease: Yes,Patient was prescribed omeprazole. 
* Enteroptosis: No.
* Acute Nasopharyngitis [Common Cold]: No.
</response>

[Task]:
Follow the format in the example response exactly, including the entire description   after your (Yes|No) judgement , followed by a newline. 
Consider each of the following ICD-10 code descriptions and evaluate if there are any related mentions in the Case note.
{code_descriptions}"""
}                   
   