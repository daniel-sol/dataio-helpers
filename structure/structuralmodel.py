from dataclasses import dataclass
from dataio.utils import _get_project, get_job_arguments


@dataclass
class RmsStructuralModel:
    project: str
    structural_model_name: str
    horizon_model_name: str
    job_name: str

    def __post_init__(self):
        self.project = _get_project(self.project, True)
        self.params = get_job_arguments(
            ["Structural models", self.structural_model_name, self.horizon_model_name],
            "Horizon Modeling",
            self.job_name,
        )
