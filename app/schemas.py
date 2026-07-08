from pydantic import BaseModel, Field, field_validator

class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=130)
    amount: float
    description: str | None = Field(None, max_length=255)

    @field_validator('amount')
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")

        return v
    
    @field_validator("wallet_name")
    def wallet_name_not_empty(cls, v: str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Wallet name can not be empty")

        return v
    
class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=130)
    initial_balance: float = 0

    @field_validator("name")
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Wallet name can not be empty")

        return v
    
    @field_validator('initial_balance')
    def balance_not_negetive(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Initial_balance must be positive")

        return v




