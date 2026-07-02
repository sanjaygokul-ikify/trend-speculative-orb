from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    service_name: str
    ingestion_url: str
    processing_url: str
    visualization_url: str

    def __post_init__(self):
        if not self.service_name:
            raise ValueError('Service name must be provided')
        if not self.ingestion_url:
            raise ValueError('Ingestion URL must be provided')
        if not self.processing_url:
            raise ValueError('Processing URL must be provided')
        if not self.visualization_url:
            raise ValueError('Visualization URL must be provided')
