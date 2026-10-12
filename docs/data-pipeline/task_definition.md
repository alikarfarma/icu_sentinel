\# Clinical Prediction Task Definition



\## Goal



ICU Sentinel predicts whether an ICU patient will develop sepsis within a future prediction horizon using historical ICU data from a fixed observation window.



Default task:



Given patient data from ICU hour 0 through hour 24,

predict whether sepsis onset occurs in the next 6 hours.



The model output is:

P(Sepsis | Patient History)



Default Window Setup

\- Observation window: 24 hours

\- Prediction horizon: 6 hours

\- Gap window: 0 hours

\- Prediction target: sepsis onset inside the prediction horizon

\- Output type: probability



Label Definition

A patient window is labeled positive if sepsis onset occurs after the observation window and within the prediction horizon.

For the default setup:

\- Positive example: sepsis onset occurs after hour 24 and at or before hour 30.

\- Negative example: no sepsis onset occurs inside that future horizon.

Patients who develop sepsis before or during the observation window should be excluded from early prediction experiments unless a later experiment explicitly studies already-deteriorating patients.



Data Modalities

The task supports four modality groups.

Vital Signs

Examples:

\- Heart rate

\- Systolic blood pressure

\- Diastolic blood pressure

\- Mean arterial pressure

\- Respiratory rate

\- Oxygen saturation

\- Body temperature



Laboratory Measurements

Examples:

\- White blood cell count

\- Platelet count

\- Creatinine

\- Bilirubin

\- Lactate

\- Hemoglobin

\- Glucose



Demographics

Examples:

\- Age

\- Sex

\- Weight

\- Height



Derived Clinical Features

Examples:

\- Shock index

\- Rolling means

\- Rolling standard deviations

\- Trend features

\- Missingness indicators

\- Time since last measurement



Split Strategy

Splits must happen at the patient level.

The same patient must never appear in more than one of:

\- Training set

\- Validation set

\- Test set



This prevents the model from seeing one window from a patient during training and another window from the same patient during evaluation.

Leakage Controls

The pipeline must enforce these rules:

\- No measurements after the observation window can be used as input features.

\- Labels must be generated only from events after the observation window.

\- Patient-level splitting is required before model evaluation.

\- Events before or during the observation window must be handled explicitly.

\- The observation window, gap window, and prediction horizon must be recorded with every experiment.

