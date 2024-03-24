  
1. Specify the characters speaking (Claude is generally accurate at automatically distinguishing speakers)  
2. Request the content be divided into chapters by topic (important for readability and summarization)  
3. Request that no content be omitted (or it may summarize without including everything)  
  
prompt example: "The following is a transcript of an interview with XXX by YYY that I have organized. Please reformat it as a more readable dialogue, divided into chapters by topic. Include speaker names, and make appropriate stylistic edits while preserving the original meaning. Start from the beginning and omit no content."   
  
If it returns part of output , you have to keep entering "continue" until it finishes. For summarizing, it's best to wait until the full formatted transcript is output, then request a chapter-based summary to avoid omitting key points.  
  
prompt for summarizing is: "Please summarize the above transcript based on the chapters, providing a thorough summary without omitting important points.  
