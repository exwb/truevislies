TEMPLATE_PROMPT_1C = """
You are given an image that contains a data visualization and an accompanying caption.

The caption is:
<CAPTION_START>
<<<CAPTION>>>
<CAPTION_END>

Be aware: The provided visualization is misleading. 
It contains distortions, manipulations, or design choices that misrepresent the data.

The visualization contains the following error(s): 
<<<ERROR_LIST>>>

Your task is to:
1. Analyze the content of the image and its caption.
 - Describe in detail what the visualization represents.
 - Interpret the visualization: What insights can be drawn? What is the likely message or conclusion the visualization is communicating?
 - Provide your own conclusion based on your analysis. 

2. Explain in detail why the visualization is misleading.
 - Do not assess whether the visualization is misleading; assume it is misleading and focus on explanation.
 - Justify your explanation with specific references to elements in the visualization and the caption.
 - Set is_misleading to true.

3. Specify which visualization rhetoric techniques may have contributed to making this visualization misleading.
 - Use the following definitions of the five types of visualization rhetoric to guide your analysis:
   - information_access_rhetoric: Information Access Rhetoric refers to choices about what data to include, omit, filter, or aggregate. These choices shape what the viewer sees and which patterns or narratives are emphasized.
   - provenance_rhetoric: Provenance Rhetoric relates to how a visualization communicates trustworthiness, such as by citing sources, explaining methods, noting uncertainty, or including methodology or assumptions.
   - mapping_rhetoric: Mapping Rhetoric involves how data values are translated into visual features such as position, size, scale, metaphor, or color. This can create emphasis or shape perception beyond what the raw data conveys.
   - linguistic_based_rhetoric: Linguistic-Based Rhetoric uses language elements like titles, labels, annotations, or captions to guide interpretation. Often includes metaphor, irony, rhetorical questions, or other narrative framing.
   - procedural_rhetoric: Procedural Rhetoric relates to interaction and navigation design, such as default views, filters, or animations. These features guide how users explore the data and can influence which conclusions they reach.
 - For each rhetoric type you identify, explain in detail how it contributes to the misleading nature of the visualization. 
 - For each rhetoric type you identify, rate how much it contributes to the misleading nature of the visualization on a scale from -1 to 6 with the following meaning: [-1: "I don't know", 0: "None", 1: "Minimal", 2: "Limited", 3: "Moderate", 4: "Considerable", 5: "Strong", 6: "Very Strong"]. If you are unsure about the contribution, rate it as -1.
 - It is possible that multiple rhetoric types contribute to the misleading nature of the visualization, or that none do.
 - It is acceptable that all misleading_contribution_score values are 0 or -1.
 - If misleading_contribution_score is -1, set why_contribute_to_misleading to an empty string "".
 - If misleading_contribution_score is 0, set why_contribute_to_misleading to an empty string "".
 - If misleading_contribution_score > 0, provide a detailed explanation in why_contribute_to_misleading.

All your answers must be exclusively in English.
Answer in JSON format, like the example below.
Do not omit any fields. 
Do not change the field names.
Do not say '''json at the beginning.
Do not include any other text outside the JSON object. 

{
  "analysis": "", // Detailed analysis from task points 1 goes here.
  "is_misleading": true, // Boolean from task point 2 goes here.
  "why_misleading": "", // Detailed explanation from task point 2 goes here.
  "visualization_rhetoric": { // This object contains entries for each of the five rhetoric types.
    "information_access_rhetoric": {
	  "misleading_contribution_score": 0, // Numerical score from task point 3 goes here.
	  "why_contribute_to_misleading": "", // Explanation of how this rhetoric type supports the misleading aspects, if misleading_contribution_score > 0, else empty string (not null).
	},
	"provenance_rhetoric": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "mapping_rhetoric": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "linguistic_based_rhetoric": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "procedural_rhetoric": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    }
  }
}
"""