from dataclasses import dataclass, field


DEFAULT_MODALITIES = ("vitals", "labs", "demographics", "derived")


@dataclass(frozen=True)
class PredictionTask:
    name: str = "early_sepsis_risk_prediction"
    target_event: str = "sepsis_onset"
    observation_window_hours: int = 24
    prediction_horizon_hours: int = 6
    gap_window_hours: int = 0
    output_type: str = "probability"
    split_unit: str = "patient"
    modalities: tuple[str, ...] = field(default_factory=lambda: DEFAULT_MODALITIES)

    def __post_init__(self):
        if self.observation_window_hours <= 0:
            raise ValueError("observation_window_hours must be positive.")

        if self.prediction_horizon_hours <= 0:
            raise ValueError("prediction_horizon_hours must be positive.")

        if self.gap_window_hours < 0:
            raise ValueError("gap_window_hours must be non-negative.")

        if self.output_type != "probability":
            raise ValueError("output_type must be 'probability'.")

        if self.split_unit != "patient":
            raise ValueError("split_unit must be 'patient' to prevent leakage.")

        if not self.modalities:
            raise ValueError("At least one modality must be enabled.")

    @property
    def prediction_window_start_hour(self) -> int:
        return self.observation_window_hours + self.gap_window_hours

    @property
    def prediction_window_end_hour(self) -> int:
        return self.prediction_window_start_hour + self.prediction_horizon_hours

    def describe(self) -> str:
        return (
            f"Use ICU hour 0-{self.observation_window_hours} to predict "
            f"{self.target_event} during hours "
            f"{self.prediction_window_start_hour}-{self.prediction_window_end_hour}."
        )