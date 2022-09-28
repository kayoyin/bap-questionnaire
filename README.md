# The Online Broad Autism Phenotype Questionnaire

This toolkit allows you to complete [The Broad Autism Phenotype Questionnaire](https://pubmed.ncbi.nlm.nih.gov/17146701/) and compare your scores to the cutoff scores provided by [The Broad Autism Phenotype Questionnaire: Prevalence and Diagnostic Classification](https://pubmed.ncbi.nlm.nih.gov/23427091/).

To use this toolkit:
```bash
python questionnaire.py --gender (m | f) --answerer (self | informant)
```

Upon completion of the questionnaire, the script will print your scores for each BAP category and their average, as well as your cutoff scores. The cutoff scores reported are designed to increase specificity at the cost of sensitivity, therefore it is highly likely that "positive" cases identified by the questionnaire do exhibit clinically identifiable BAP traits, but it is also somewhat likely that invididuals who would be clinically diagnosed with BAP are not identified by this questionnaire.

Please note that this questionnaire does not constitute an official diagnosis but gives a mere indication of people who may likely have clinically identifiable BAP traits.