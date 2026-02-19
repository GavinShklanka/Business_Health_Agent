from pydantic import BaseModel
from typing import Dict, Optional

class AgentRunRequest(BaseModel):
    user_input: str
    parameters: Optional[Dict] = None
