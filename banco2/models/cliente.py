from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    saldo: float
    score: int