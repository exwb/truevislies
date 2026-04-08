TEMPLATE_PROMPT_2A = """
You are given an image that contains a data visualization and an accompanying caption.

The caption is:
<CAPTION_START>
<<<CAPTION>>>
<CAPTION_END>

The visualization may or may not be misleading, either intentionally or unintentionally.
It may contain distortions, manipulations, or design choices that misrepresent the data.

Your task is to:
1. Analyze the content of the image and its caption.
 - Describe in detail what the visualization represents.
 - Interpret the visualization: What insights can be drawn? What is the likely message or conclusion the visualization is communicating?
 - Provide your own conclusion based on your analysis. 

2. Determine if you believe the visualization is misleading. 
 - Justify in detail your judgment with specific references to elements in the visualization and the caption.
 - If you rate the visualization as not misleading, do not provide a justification.

3. Only if you believe the visualization is misleading, specify which author intents and factors may have contributed to making this visualization misleading.
 - Use the following definitions author intent and factors behind the misleading effect of a visualization to guide your analysis. These categories describe possible author intents when creating or sharing the visualization that may explain why it is misleading.
	- aesthetic_driven_misrepresentation: The author prioritizes the visual appeal of the visualizations, giving them precedence over accuracy. These stylistic preferences, such as decorative choices, lead to misinterpretation, despite the author's intention not to mislead.
	- bias_exploitation: The visualization is crafted to take advantage of known human visual perceptual or cognitive biases in order to push the reader to a particular interpretation.
	- claim_supporting_manipulation: The author shapes the visualization and its caption to highlight a desired pattern or hide counter-evidence. The goal is to persuade the reader to adopt a particular perspective, for example, by spreading disinformation about COVID-19.
	- context_distortion: The author removes (or hides/omits) relevant context that is essential for accurate interpretation of the visualization (missing labels, explanations, legends). The goal is to persuade the reader towards a particular perspective.
	- deliberate_reader_confusion: The author introduces unnecessary complexity, such as ambiguous encodings, to create confusion and make the reader more receptive to the author's narrative.
	- lack_of_visualization_literacy: The author is unfamiliar with best practices in visualization and inadvertently introduces misleading elements. For example, the author may choose inappropriate chart types or a design that inadvertently leads to misleading conclusions.
	- selective_reporting: The author reports only partial information, such as, reporting partial data, focusing/highlighting on a data subset. The goal is to provide a skewed representation of the information, aiming at persuading the reader towards a particular perspective.
	- space_and_format_constraints: Constraints (such as, space constraints, image size/format) limit the design or presentation of the visualization. The author, to cope with these constraints, may incur information loss, which can lead to misrepresentation.
	- unintentional_context_omission: Accidental omissions of relevant context that are essential for accurate interpretation of the visualization (missing labels, explanations, legends). The misleading purpose is not deliberate. 
 - For each intent you identify, explain in detail how it contributes to the misleading nature of the visualization. 
 - For each intent you identify, rate how much it contributes to the misleading nature of the visualization on a scale from -1 to 6 with the following meaning: [-1: "I don't know", 0: "None", 1: "Minimal", 2: "Limited", 3: "Moderate", 4: "Considerable", 5: "Strong", 6: "Very Strong"]. If you are unsure about the contribution, rate it as -1.
 - It is possible that multiple intents contribute to the misleading nature of the visualization, or that none do.
 - If the visualization is not misleading, set all misleading_contribution_score to 0.
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
  "is_misleading": true | false, // Boolean from task point 2 goes here.
  "why_misleading": "", // Detailed explanation from task point 2 goes here. If is_misleading is false, why_misleading MUST be an empty string "" (not null). Do not include any explanation in that field
  "author_intents": { // This object contains entries for each of the nine author intent types.
    "aesthetic_driven_misrepresentation": {
	  "misleading_contribution_score": 0, // Numerical score from task point 3 goes here. If the visualization is not misleading, set to 0.
	  "why_contribute_to_misleading": "", // Explanation of how this intent supports the misleading aspects, if misleading_contribution_score > 0, else empty string (not null).
	},
	"bias_exploitation": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "claim_supporting_manipulation": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "context_distortion": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "deliberate_reader_confusion": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "lack_of_visualization_literacy": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "selective_reporting": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "space_and_format_constraints": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    },
    "unintentional_context_omission": {
        "misleading_contribution_score": 0,
        "why_contribute_to_misleading": ""
    }
  }
}
"""