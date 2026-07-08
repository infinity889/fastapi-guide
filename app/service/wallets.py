from app.repository import wallets as wallets_repository


def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return {"total_balance": sum(BALANCE.values())}

    if wallet_name not in BALANCE:
        raise HTTPException(status_code=404, detail=f"wallet {wallet_name} is not found")
    
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}


def create_wallet(wallet: CreateWalletRequest):
    if wallet.name in BALANCE:
        raise HTTPException(status_code=400, detail=f"wallet {wallet.name} already in exists")

    BALANCE[wallet.name] = wallet.initial_balance

    return {
        "message": f"wallet {wallet.name} created",
        "wallet": wallet.name,
        "balance": BALANCE[wallet.name]
    }
