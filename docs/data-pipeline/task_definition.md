\# Clinical Prediction Task Definition



Goal:



ICU Sentinel predicts whether an ICU patient will develop sepsis within a future prediction horizon using historical ICU data from a fixed observation window.



Default task:



Given patient data from ICU hour 0 through hour 24,

predict whether sepsis onset occurs in the next 6 hours.



The model output is:

P(Sepsis | Patient History)

\- Patient-level splitting is required before model evaluation.

\- Events before or during the observation window must be handled explicitly.

\- The observation window, gap window, and prediction horizon must be recorded with every experiment.

